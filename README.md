# AI i svenska myndigheter

Projekt för faktaboken **AI i svenska myndigheter – Regler, gränser och praktiska vägval för IT- och verksamhetsarkitekter**.

Författare: Erland Lindmark

## Projektstatus

Bokplan och källkarta är fastställda. Första manusutkast finns för inledning, kapitel 1–8 samt bilaga A–B, och den första helhetsrevisionen är genomförd. Se `docs/projektstatus.md` för aktuell status och nästa steg. Resultatet av första helhetsrevisionen finns i `docs/helhetsrevision-1.md`.

## Struktur

- `chapters/` – kanoniskt bokmanus
- `docs/` – bokspecifikation, kapitelplan, källmatris, canon och projektstatus
- `assets/cover/` – färdigt omslag när det genererats
- `assets/image-prompts/` – omslagsprompt
- `scripts/` och `styles/` – reproducerbar lokal exportpipeline
- `exports/` – genererade exportfiler

Se `docs/projektstatus.md` för nästa steg.


Version 0.17.0 innehåller första käll- och rättslägesrevisionen av hela manuset. Se `docs/kall-och-rattslagesrevision-1.md`.


## Omslag

Fastställt omslag finns i `assets/cover/cover.png` och används av EPUB-exporten.


Version 0.17.0 inför sidnummer i PDF-innehållsförteckningen och två-radiga centrerade kapitelöppningar för kapitel 1–8.

## GitHub Release

Projektet innehåller `.github/workflows/release.yml`. När en GitHub Release **publiceras** bygger GitHub Actions automatiskt PDF och EPUB och bifogar dem till releasen.

Release-taggen används som versionsnummer. En release med taggen `v1.0.0` ger exempelvis:

- `ai-i-svenska-myndigheter-v1.0.0.pdf`
- `ai-i-svenska-myndigheter-v1.0.0.epub`

Workflown använder projektets ordinarie `scripts/export-book.sh`, validerar att båda exporterna skapats och testar EPUB-arkivet innan filerna laddas upp till releasen.
