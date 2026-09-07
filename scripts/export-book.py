#!/usr/bin/env python3
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import zipfile
import re
import html as html_lib
import os
import yaml

ROOT = Path(__file__).resolve().parents[1]
META = ROOT / "docs" / "export-metadata.yaml"


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(1)


def postprocess_epub(epub_path: Path) -> None:
    """Keep EPUB navigation as reader index, but remove it from reading order.

    Also normalize chapter labels to `Kapitel N. Namn` in both EPUB3 nav
    and legacy NCX, since CSS generated punctuation is ignored by many readers.
    """
    with zipfile.ZipFile(epub_path, "r") as zin:
        entries = {name: zin.read(name) for name in zin.namelist()}

    nav_name = next((n for n in entries if n.endswith("nav.xhtml")), None)
    if nav_name:
        nav = entries[nav_name].decode("utf-8")
        nav = re.sub(
            r'<span class="chapter-number">(Kapitel\s+\d+)</span><span class="chapter-name">([^<]+)</span>',
            lambda m: f'{m.group(1)}. {m.group(2)}',
            nav,
        )
        entries[nav_name] = nav.encode("utf-8")

    ncx_name = next((n for n in entries if n.endswith("toc.ncx")), None)
    if ncx_name:
        ncx = entries[ncx_name].decode("utf-8")
        ncx = re.sub(r'(Kapitel\s+\d+)(?=[A-ZÅÄÖ])', r'\1. ', ncx)
        entries[ncx_name] = ncx.encode("utf-8")

    opf_name = next((n for n in entries if n.endswith(".opf")), None)
    if opf_name:
        opf = entries[opf_name].decode("utf-8")
        opf = re.sub(r'\s*<itemref\s+idref="nav"\s*/>', '', opf)
        entries[opf_name] = opf.encode("utf-8")

    tmp_path = epub_path.with_suffix(".tmp.epub")
    with zipfile.ZipFile(tmp_path, "w") as zout:
        if "mimetype" in entries:
            zout.writestr("mimetype", entries.pop("mimetype"), compress_type=zipfile.ZIP_STORED)
        for name, payload in entries.items():
            zout.writestr(name, payload, compress_type=zipfile.ZIP_DEFLATED)
    tmp_path.replace(epub_path)


def main() -> None:
    if not META.exists():
        fail("Saknar docs/export-metadata.yaml")
    data = yaml.safe_load(META.read_text(encoding="utf-8"))
    release_version = os.environ.get("BOOK_VERSION", "").strip()
    if release_version:
        data["version"] = release_version.removeprefix("v")
    chapters = [ROOT / p for p in data.get("chapters", [])]
    cover_rel = data.get("export", {}).get("cover") or data.get("cover-image")
    cover = ROOT / cover_rel if cover_rel else None
    missing = [str(p.relative_to(ROOT)) for p in chapters if not p.exists()]
    if missing:
        fail("Saknade kapitel: " + ", ".join(missing))
    if cover is not None and not cover.exists():
        fail(f"Saknar omslagsbild: {cover.relative_to(ROOT)}")
    for p in chapters:
        text = p.read_text(encoding="utf-8")
        if "####" in text:
            fail(f"H4 eller djupare rubrik hittad i {p.name}")

    pandoc = shutil.which("pandoc")
    if not pandoc:
        fail("Pandoc finns inte installerat")

    out = ROOT / "exports"
    out.mkdir(exist_ok=True)

    metadata_path = META
    metadata_tmp = None
    if release_version:
        metadata_tmp = tempfile.NamedTemporaryFile(
            mode="w", suffix=".yaml", encoding="utf-8", delete=False
        )
        yaml.safe_dump(data, metadata_tmp, allow_unicode=True, sort_keys=False)
        metadata_tmp.close()
        metadata_path = Path(metadata_tmp.name)

    common = [pandoc, *map(str, chapters), "--metadata-file", str(metadata_path)]

    epub_args = common + ["--toc", "--toc-depth=1", "--css", str(ROOT / "styles" / "epub.css")]
    if cover is not None:
        epub_args += ["--epub-cover-image", str(cover)]
    epub_args += ["-o", str(out / "ai-i-svenska-myndigheter.epub")]
    subprocess.run(epub_args, check=True)
    postprocess_epub(out / "ai-i-svenska-myndigheter.epub")
    print("EPUB skapad.")

    weasy = shutil.which("weasyprint")
    if not weasy:
        fail("WeasyPrint finns inte installerat; PDF kunde inte skapas")

    with tempfile.TemporaryDirectory(prefix="ai-book-export-") as tmpdir:
        tmp = Path(tmpdir)
        html = tmp / "book.html"
        pandoc_html = common + [
            "--standalone",
            "--toc",
            f"--toc-depth={data.get('export', {}).get('pdf_toc_depth', 3)}",
            "--css", str(ROOT / "styles" / "pdf.css"),
            "--metadata", "lang=sv-SE",
            "-o", str(html),
        ]
        subprocess.run(pandoc_html, check=True)
        text = html.read_text(encoding="utf-8")
        frontmatter = []
        if cover is not None:
            cover_uri = cover.resolve().as_uri()
            frontmatter.append(f'<div class="cover-page"><img src="{cover_uri}" alt="Omslag"></div>')
        title = html_lib.escape(str(data.get("title", "")))
        subtitle = html_lib.escape(str(data.get("subtitle", "")))
        author = html_lib.escape(str(data.get("author", "")))
        title_html = (
            '<section class="title-page" aria-label="Titelsida">'
            f'<h1>{title}</h1>'
            f'<p class="subtitle">{subtitle}</p>'
            f'<p class="author">{author}</p>'
            '</section>'
        )
        frontmatter.append(title_html)
        text = text.replace("<body>", "<body>\n" + "\n".join(frontmatter), 1)
        html.write_text(text, encoding="utf-8")
        pdf = out / "ai-i-svenska-myndigheter.pdf"
        subprocess.run([weasy, str(html), str(pdf)], check=True)
        print("PDF skapad.")

    if metadata_tmp is not None:
        Path(metadata_tmp.name).unlink(missing_ok=True)


if __name__ == "__main__":
    main()
