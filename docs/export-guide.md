# Exportguide

Projektets manus är canonical Markdown. EPUB/PDF-export görs reproducerbart utan AI.

## Pipeline

- EPUB: Pandoc, navigerbar TOC med huvudkapitel och bilagor, omslag från `assets/cover/cover.png`.
- PDF: Pandoc till HTML och därefter WeasyPrint, A4, omslag som första sida och en kort innehållsförteckning med huvudkapitel och bilagor.
- Före export valideras kapitelordning, rubriknivåer och omslagsfil.

Kör:

```bash
./scripts/export-book.sh
```

Färdiga filer skapas i `exports/`.

## Automatisk export vid GitHub Release

`.github/workflows/release.yml` triggas när en GitHub Release publiceras. Workflown installerar Pandoc, WeasyPrint och PyYAML, kör samma exportpipeline som lokalt och bifogar PDF och EPUB som release-assets.

Release-taggen styr versionsnumret i bygget. Taggen `v1.0.0` ger filnamnen `ai-i-svenska-myndigheter-v1.0.0.pdf` och `ai-i-svenska-myndigheter-v1.0.0.epub`.
