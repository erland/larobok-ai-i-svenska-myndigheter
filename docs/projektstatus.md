# Projektstatus

## Bok

Titel: AI i svenska myndigheter

Språk: Svenska

Författare: Erland Lindmark

Version: 0.17.0

## Nuvarande fas

**Första kompletta exporten granskad – typografisk finjustering genomförd**

## Kapitelstatus

| Kapitel | Titel | Status | Kommentar |
|---|---|---|---|
| 00 | Inledning | Första utkast klart | Källor verifierade 2026-09-07 |
| 01 | Kartan över styrningen | Första utkast klart | Källor fördjupade och verifierade 2026-09-07 |
| 02 | AI-förordningen – vilken sorts användning har vi framför oss? | Första utkast klart | Rättsläge och tillämpningsdatum verifierade 2026-09-07 |
| 03 | Informationen – vad matar vi AI:n med? | Första utkast klart | GDPR, sekretess och säkerhetsskydd verifierade 2026-09-07 |
| 04 | När AI påverkar människor och myndighetsbeslut | Första utkast klart | Förvaltningsrätt, GDPR artikel 22, AI-förordningen och diskrimineringsrisk verifierade 2026-09-07 |
| 05 | När någon annan tillhandahåller AI:n | Första utkast klart | LOU, dataskyddsroller, sekretess, AI-förordningen, molnpolicy och exit verifierade 2026-09-07 |
| 06 | Offentlighet, dokumentation och spårbarhet | Första utkast klart | TF, OSL, arkivlag, RA-FS och aktuell AI/offentlighetsutredning verifierade 2026-09-07 |
| 07 | Från idé till arkitekturbeslut | Första utkast klart | AI-kontroll i tio frågor, grönt–gult–rött och eskaleringsmodell sammanför kapitel 1–6 |
| 08 | Praktiska scenarier | Första utkast klart | Åtta scenarier testar grönt–gult–rött-modellen mot konkreta användningsfall |
| Bilaga A | Regelverkskarta och källor | Första utkast klart | Generell regelverkskarta och primärkällor verifierade 2026-09-07 |
| Bilaga B | Exempel på sektorsspecifik reglering | Första utkast klart | Tullverket, Polismyndigheten och Skatteverket med kort AI-påverkan och primärkällor verifierade 2026-09-07 |

## Introducerade begrepp

| Begrepp | Kapitel | Kort definition |
|---|---|---|
| Grönt–gult–rött | Inledning | Modell för tidig bedömning av AI-användning |
| Sektorsspecifik reglering | Kapitel 1 | Verksamhets- eller myndighetsspecifika regler utöver generella regelverk |

## Öppna beslut

- Exakt slutlig titel kan omprövas efter första manuspasset.
- Omslagsbild är skapad och införd som `assets/cover/cover.png`.
- Inre illustrationer är avstängda tills användaren uttryckligen väljer annat.
- Upphovsrätt, digital tillgänglighet och cybersäkerhetslagen är verifierade i första källrevisionen; kompletterande föreskrifter bör slutkontrolleras inför publicering.
- Molnpolicy för offentlig förvaltning (2026) är nu införd som vägledande policykälla i kapitel 5.

## Nästa rekommenderade steg

1. Kör den första fullständiga **PDF/EPUB-exporten** med det fastställda omslaget.
2. Gör en **visuell kvalitetskontroll** av titel-/omslagssidor, innehållsförteckning, sidbrytningar, tabeller och källhänvisningar.
3. Före slutpublicering görs en kort aktualitetskontroll, särskilt av AI-förordningens kommissionsriktlinjer om högriskklassificering.


## Export och visuell QA - v0.15.0

- Komplett PDF och EPUB exporterade.
- PDF renderad sida för sida och visuellt granskad.
- Innehållsförteckningen förenklad till huvudkapitel och bilagor för bättre läsbarhet.
- Omslaget används som första PDF-sida och som EPUB-omslag.
- PDF-pipelinen använder Pandoc + WeasyPrint.
- Nästa steg: slutlig publiceringskontroll och eventuell finjustering efter läsprov.


## Typografisk finjustering - v0.17.0

- PDF-innehållsförteckningen visar nu sidnummer med punktledare.
- Kapitel 1–8 börjar med två centrerade rader: `Kapitel N` och därefter kapitelnamnet.
- Samma två-radiga kapitelöppning används i EPUB.
- PDF har byggts om och samtliga 96 sidor har renderats utan exportfel.
- Innehållsförteckning samt kort och långt kapitelrubriksexempel har visuellt kontrollerats.


## Exportjustering v0.17.0

- PDF har fått en separat titelsida direkt efter omslaget med titel, undertitel och författare.
- EPUB:s navigations-TOC finns kvar som läsarindex men är borttagen ur dokumentets läsordning.
- Kapitelposter i EPUB-index/NCX använder formatet `Kapitel N. Kapitelnamn`.

## GitHub Release-export - v0.18.0

- `.github/workflows/release.yml` tillagd.
- Workflown triggas när en GitHub Release publiceras.
- PDF och EPUB byggs med projektets ordinarie exportpipeline.
- Release-taggen används som byggversion och i filnamnen.
- EPUB-arkivet valideras före uppladdning.
- Båda filerna bifogas automatiskt till den publicerade GitHub-releasen.
