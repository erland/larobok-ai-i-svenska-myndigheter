# Bilaga B. Exempel på sektorsspecifik reglering

Den här bilagan visar varför den generella AI-regleringen inte alltid räcker. Tullverket, Polismyndigheten och Skatteverket används som exempel eftersom de har tydliga specialregler om personuppgiftsbehandling och analys.

Bilagan är **inte uttömmande** och ersätter inte en rättslig analys av ett konkret användningsfall. Källorna är verifierade per **7 september 2026**.

## B.1 Tullverket

### Viktiga specialregler

**Tulldatalag (2026:127)** gäller behandling av personuppgifter i Tullverkets bland annat fiskala och kontrollrelaterade verksamhet. Lagen omfattar uttryckligen övervakning, revision och annan kontroll eller analys.

**Lag (2018:1694) om Tullverkets behandling av personuppgifter inom brottsdatalagens område** gäller tillsammans med brottsdatalagen när Tullverket behandlar personuppgifter för att förebygga, förhindra eller upptäcka brottslig verksamhet, utreda eller lagföra brott eller verkställa uppbörd. Lagen pekar dessutom vidare på flera andra specialförfattningar, bland annat om PNR, internationellt polisiärt samarbete och tullbefogenheter.

### Vad betyder det för AI?

För en AI-lösning räcker det därför inte att konstatera att GDPR eller brottsdatalagen i princip tillåter behandling. Arkitekten behöver kontrollera **vilken verksamhetsgren användningen tillhör och vilket ändamål den konkreta analysen har**.

Ett AI-baserat riskurval i tullkontroll kan exempelvis behöva bedömas mot:

- tillåtna ändamål för behandling,
- vilka uppgifter som får användas,
- åtkomst och elektroniskt utlämnande,
- behandlingstid,
- särskilda regler för brottsbekämpande verksamhet,
- regler om vilka befogenheter som faktiskt finns efter att ett urval gjorts.

**Praktisk arkitektfråga:**

> Använder vi AI för vanlig tull-/kontrollverksamhet eller för brottsbekämpning, och vilken specialreglering gäller för just den behandlingen?

### Primärkällor

- Tulldatalag (2026:127): https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/tulldatalag-2026127_sfs-2026-127/
- Lag (2018:1694) om Tullverkets behandling av personuppgifter inom brottsdatalagens område: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-20181694-om-tullverkets-behandling-av_sfs-2018-1694/
- Brottsdatalag (2018:1177): https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/brottsdatalag-20181177_sfs-2018-1177/

## B.2 Polismyndigheten

### Viktiga specialregler

**Brottsdatalag (2018:1177)** ger den generella ramen för personuppgiftsbehandling av behöriga myndigheter för brottsbekämpande ändamål.

**Lag (2018:1693) om polisens behandling av personuppgifter inom brottsdatalagens område** kompletterar denna med särskilda regler för Polismyndigheten. Den reglerar bland annat grundläggande behandling, gemensamt tillgängliga uppgifter, behandlingstider, register och forensiska ändamål.

### Vad betyder det för AI?

AI för exempelvis underrättelseanalys, matchning, prioritering eller riskbedömning måste därför utformas med hänsyn till mer än modellens träffsäkerhet.

Arkitekten behöver bland annat förstå:

- för vilket brottsbekämpande ändamål uppgifterna används,
- vilka uppgifter som får göras gemensamt tillgängliga,
- vilka sökningar och sammanställningar som är tillåtna,
- hur länge uppgifterna får behandlas,
- vem som får komma åt information och AI-resultat,
- hur felaktiga eller missvisande AI-indikationer kan påverka enskilda.

AI-förordningens klassificering måste samtidigt göras separat. Vissa AI-användningar inom brottsbekämpning finns bland de områden som kan vara högrisk enligt AI-förordningen.

**Praktisk arkitektfråga:**

> Vilken faktisk åtgärd eller bedömning kan AI-resultatet leda till, och är både databehandlingen och den efterföljande användningen rättsligt tillåtna?

### Primärkällor

- Lag (2018:1693) om polisens behandling av personuppgifter inom brottsdatalagens område: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-20181693-om-polisens-behandling-av_sfs-2018-1693/
- Brottsdatalag (2018:1177): https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/brottsdatalag-20181177_sfs-2018-1177/
- AI-förordningen, bilaga III: https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3

## B.3 Skatteverket

### Viktiga specialregler

**Beskattningsdatalag (2026:125)** gäller personuppgiftsbehandling i Skatteverkets beskattningsverksamhet. Den nya lagen trädde i kraft den 2 april 2026 och ersatte den tidigare lagen från 2001.

**Folkbokföringsdatalag (2026:126)** gäller personuppgiftsbehandling i folkbokföringsverksamheten. Den omfattar bland annat samordnad behandling, kontroll och analys av identifierings- och folkbokföringsuppgifter.

**Lag (2018:1696) om Skatteverkets behandling av personuppgifter inom brottsdatalagens område** gäller den brottsbekämpande verksamheten och innehåller särskilda regler, bland annat om sökning.

### Vad betyder det för AI?

Samma myndighet kan alltså behöva använda olika rättsliga ramar beroende på om AI-lösningen används för exempelvis:

- beskattning och skattekontroll,
- folkbokföring och identitetskontroll,
- brottsbekämpning.

Det är särskilt relevant för AI-baserad analys och urval. Att en datamängd finns hos Skatteverket innebär inte i sig att den får användas fritt i varje modell eller för varje nytt analysändamål.

Arkitekten behöver kontrollera:

- vilket lagreglerat ändamål AI-analysen stöder,
- vilka datakällor som får kombineras,
- regler för sökning, urval och åtkomst,
- behandlingstid,
- om användningen har gått från administrativ kontroll till brottsbekämpande ändamål.

**Praktisk arkitektfråga:**

> Vilken av Skatteverkets rättsliga verksamhetsdomäner befinner sig AI-användningen i, och förändras rättsläget om syftet eller användningen av resultatet ändras?

### Primärkällor

- Beskattningsdatalag (2026:125): https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/beskattningsdatalag-2026125_sfs-2026-125/
- Folkbokföringsdatalag (2026:126): https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/folkbokforingsdatalag-2026126_sfs-2026-126/
- Lag (2018:1696) om Skatteverkets behandling av personuppgifter inom brottsdatalagens område: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-20181696-om-skatteverkets-behandling-av_sfs-2018-1696/

## B.4 Den gemensamma lärdomen

De tre exemplen visar samma grundprincip:

> **AI ger inte en myndighet en ny rätt att behandla information, göra urval eller vidta åtgärder som myndigheten annars saknar rättsligt stöd för.**

Sektorsreglering avgör ofta inte om *AI som teknik* får användas. Den avgör i stället sådant som är minst lika viktigt för arkitekturen:

- vilka uppgifter som får behandlas,
- för vilka ändamål,
- vilka uppgifter som får kombineras,
- hur sökning och urval får ske,
- vem som får ha åtkomst,
- hur länge information får behandlas,
- vilka åtgärder myndigheten får vidta utifrån resultatet.

Det är därför den sektorsspecifika kontrollen bör göras **innan datamodell, integrationer och leverantörsval låses**.
