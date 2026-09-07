# <span class="chapter-number">Kapitel 2</span><span class="chapter-name">AI-förordningen – vilken sorts användning har vi framför oss?</span>

AI-förordningen är den mest uppenbara AI-specifika regleringen. För arkitekten fungerar den framför allt som en **klassificeringsmodell**, inte som ett enda ja- eller nej-svar på om AI får användas.

Det praktiska arbetet börjar därför med tre frågor:

1. Har vi ett AI-system som omfattas av förordningen?
2. Vilken roll har myndigheten i förhållande till systemet?
3. Vilken risk- eller transparenskategori hamnar det aktuella användningsfallet i?

Först därefter går det att förstå vilka AI-specifika krav som blir relevanta.

## Användningsfallet avgör

AI-förordningen definierar ett AI-system som ett maskinbaserat system som är utformat för att fungera med varierande grad av autonomi, som kan vara adaptivt efter driftsättning och som utifrån indata härleder hur det ska generera utdata som exempelvis prediktioner, innehåll, rekommendationer eller beslut som kan påverka fysiska eller virtuella miljöer.

Det betyder att arkitekten inte bör börja med frågan om organisationen använder exempelvis en "AI-produkt" eller en viss leverantör. Det avgörande är **vad systemet faktiskt gör i den aktuella lösningen**.

En språkmodell som används för att förbättra formuleringar i en redan offentlig text är ett annat användningsfall än samma modell när den används för att rangordna sökande, analysera misstänkta beteenden eller ge underlag till beslut om enskilda.

**Arkitekturfråga:** Vad är AI-systemets funktion i just denna process, vilka utdata producerar det och vad kan dessa utdata påverka?

## Myndigheten är ofta deployer – men inte alltid bara det

AI-förordningen skiljer mellan olika roller. Två är särskilt viktiga för en myndighet:

- **provider** – den som utvecklar eller låter utveckla ett AI-system och tillhandahåller eller tar det i bruk under eget namn eller varumärke,
- **deployer** – den organisation som använder ett AI-system under sin egen kontroll.

En myndighet som köper en färdig AI-tjänst är alltså ofta deployer. Men om myndigheten utvecklar ett eget system, låter bygga ett system som sedan tas i bruk under myndighetens namn eller gör vissa större förändringar kan providerrollen också bli relevant.

Det är därför farligt att tänka att "leverantören ansvarar för AI Act". Leverantören kan ha omfattande skyldigheter, men myndigheten kan samtidigt ha egna skyldigheter som deployer.

**Arkitekturfråga:** Är vi bara användare av en färdig tjänst, eller har vi utvecklat, förändrat, paketerat eller tagit systemet i bruk på ett sätt som förändrar vår roll?

## Fyra praktiska riskzoner

För arkitekten är det användbart att förenkla AI-förordningen till fyra praktiska zoner.

### 1. Förbjuden användning

Vissa AI-praktiker är förbjudna. Förbuden omfattar bland annat vissa manipulerande eller exploaterande tekniker, social scoring, vissa former av individuell brottsriskbedömning, ospecificerad insamling av ansiktsbilder för ansiktsigenkänningsdatabaser, viss känsloigenkänning och vissa former av biometrisk kategorisering.

Här är bokens färgkod **rött**. Om användningsfallet verkar träffa ett förbud ska arkitekten inte försöka "designa runt" problemet utan se till att rättslig specialistbedömning görs innan arbetet går vidare.

Det finns undantag och detaljvillkor för vissa förbud. Därför ska en kort beskrivning i en arkitekturbok aldrig användas som slutlig juridisk klassificering.

**Arkitekturfråga:** Finns någon del av användningen som bedömer, påverkar eller kategoriserar människor på ett sätt som ligger nära de uttryckligen förbjudna praktikerna?

### 2. Högrisk-AI

AI-system kan klassificeras som högrisk genom två huvudvägar:

- AI som säkerhetskomponent eller del av vissa reglerade produkter,
- AI i särskilt känsliga användningsområden enligt bilaga III.

Bilaga III omfattar bland annat vissa användningar inom biometrik, kritisk infrastruktur, utbildning, arbetsliv, tillgång till väsentliga offentliga och privata tjänster, brottsbekämpning, migration och gränskontroll samt rättskipning och demokratiska processer.

För offentlig sektor är detta en central kontrollpunkt. Ett AI-system blir inte högrisk bara för att det används av en myndighet. Det är **det avsedda användningsfallet och dess funktion** som är avgörande.

När högriskreglerna är tillämpliga ställs bland annat krav på riskhantering, data och datastyrning, dokumentation, loggning, information till deployer, mänsklig kontroll, robusthet, cybersäkerhet och noggrannhet.

För deployers tillkommer egna krav, exempelvis att använda systemet enligt instruktionerna, utse personer med tillräcklig kompetens och befogenhet för mänsklig kontroll, övervaka systemets drift och i relevanta fall behålla automatiskt genererade loggar.

För vissa offentliga deployers av högrisk-AI krävs dessutom en bedömning av påverkan på grundläggande rättigheter innan systemet tas i bruk. Den bedömningen kompletterar, snarare än ersätter, en eventuell konsekvensbedömning enligt dataskyddsreglerna.

**Arkitekturfråga:** Berör AI-systemet ett område i bilaga III eller en reglerad produkt, och påverkar det människor på det sätt som gör klassificeringen till högrisk relevant?

## Tillämpningsdatumen är en del av arkitekturen

AI-förordningen trädde i kraft den 1 augusti 2024, men olika delar började tillämpas vid olika tidpunkter. Efter 2026 års Digital Omnibus ser tidslinjen i stora drag ut så här:

| Regelområde | Tillämpning |
|---|---|
| AI-kompetens och huvuddelen av förbuden | 2 februari 2025 |
| Styrningsregler och regler för general-purpose AI-modeller | 2 augusti 2025 |
| Huvuddelen av AI-förordningen, inklusive transparensregler | 2 augusti 2026 |
| Vissa nya förbjudna praktiker efter 2026 års ändring | 2 december 2026 |
| Högriskfall enligt artikel 6.2 och bilaga III | 2 december 2027 |
| Produktanknutna högriskfall enligt artikel 6.1 och bilaga I | 2 augusti 2028 |

Det innebär att ett krav som ännu inte är fullt tillämpligt ändå kan vara viktigt i en arkitektur som ska leva i flera år. En lösning som införs 2026 och förväntas användas 2028 bör därför inte designas som om 2027–2028 års krav inte finns.

**Arkitekturfråga:** Vilka regler gäller när lösningen tas i bruk – och vilka kommer att gälla under dess planerade livslängd?

## 3. Transparens: ibland måste människor få veta att AI används

AI-förordningen innehåller transparensregler som gäller vissa användningar även när systemet inte är högrisk.

Exempel är att människor i vissa fall ska informeras när de interagerar direkt med ett AI-system. Det finns också särskilda regler för bland annat syntetiskt eller manipulerat innehåll, deepfakes och vissa AI-genererade texter som publiceras för att informera allmänheten om frågor av allmänt intresse.

För en myndighet kan detta bli relevant för exempelvis:

- chatbotar och digitala assistenter,
- automatiskt genererade texter på webbplatser,
- genererat ljud, bild eller video,
- tjänster där den enskilde annars rimligen kan tro att kontakten sker med en människa.

Transparens behöver därför finnas med i arkitekturen som funktion, inte läggas på sist som en informationsruta.

**Arkitekturfråga:** Behöver användaren eller den berörda personen informeras om att AI används, och var i tjänsten måste denna information i så fall lämnas?

## 4. Minimal eller begränsad AI-risk betyder inte "inga regler"

Många AI-användningar faller inte in under förbud eller högriskregler. Det är viktigt, eftersom boken inte ska skapa intrycket att all AI i en myndighet är högrisk.

Exempel på relativt okomplicerade användningar kan vara:

- språkstöd för offentlig eller okänslig text,
- idé- och struktureringsstöd,
- sammanfattning av material som får behandlas i den valda tjänsten,
- tekniskt stöd där resultatet alltid granskas och inte påverkar enskildas rättigheter eller skyldigheter.

Men **minimal risk enligt AI-förordningen betyder bara att de mer omfattande AI Act-kraven inte aktiveras**. GDPR, sekretess, säkerhetsskydd, offentlighet, upphovsrätt, arkivregler och sektorsspecifik lagstiftning kan fortfarande vara avgörande.

Detta är ett av bokens viktigaste budskap:

> **Låg risk enligt AI-förordningen är inte samma sak som rättsligt oreglerad användning.**

## AI-kompetens är redan ett krav

Artikel 4 kräver efter 2026 års Digital Omnibus att providers och deployers vidtar åtgärder för att **stödja utvecklingen av AI-kompetens** hos personal och andra som hanterar eller använder AI-system för deras räkning. Vid utformningen ska bland annat teknisk kunskap, erfarenhet, utbildning och användningskontext beaktas. Den tidigare formuleringen om att säkerställa en viss "tillräcklig nivå" har tagits bort; skyldigheten att vidta kompetensåtgärder finns däremot kvar.

För en myndighet betyder det att AI-kompetens inte bör reduceras till en allmän introduktionskurs för alla. Åtgärderna behöver vara **roll- och användningsfallsanpassade**.

En arkitekt som utformar AI-baserat beslutsstöd behöver annan kompetens än en medarbetare som använder generativ AI för språklig bearbetning.

**Arkitekturfråga:** Vilken kompetens krävs för dem som designar, förvaltar, övervakar och använder just detta AI-system?

## Mänsklig kontroll måste vara verklig

Mänsklig kontroll återkommer på flera ställen i AI-förordningen och är särskilt viktig för högrisk-AI. När de relevanta högriskreglerna är tillämpliga ska deployers se till att personer som får ansvar för mänsklig kontroll har nödvändig kompetens, utbildning och befogenhet samt det stöd som behövs.

Det betyder att en "human in the loop" inte automatiskt löser problemet.

Om människan:

- inte förstår systemets begränsningar,
- saknar tid att göra en självständig bedömning,
- saknar åtkomst till underlaget,
- inte kan avvika från AI:ns rekommendation,
- eller i praktiken alltid accepterar resultatet,

är den mänskliga kontrollen svag även om processen formellt innehåller ett manuellt steg.

För arkitekten är detta en designfråga om gränssnitt, behörigheter, information, loggning och process – inte bara en organisationsfråga.

**Arkitekturfråga:** Kan den människa som ska utöva kontroll faktiskt förstå, ifrågasätta och ändra AI-systemets resultat?

## General-purpose AI: skilj på modellen och myndighetens användning

Generativa tjänster bygger ofta på så kallade general-purpose AI-modeller, GPAI. AI-förordningen innehåller särskilda skyldigheter för providers av sådana modeller, bland annat kring dokumentation, transparens och upphovsrätt. Modeller med systemrisk får ytterligare krav.

En svensk myndighet som använder en kommersiell språkmodell är normalt inte provider av grundmodellen. Men leverantörens skyldigheter är ändå relevanta för myndighetens kravställning.

Arkitekten behöver exempelvis förstå vilken dokumentation som finns, hur modellen används i den färdiga tjänsten, vilka begränsningar leverantören anger och hur uppdateringar av modellen kan påverka lösningens beteende.

Samtidigt måste myndighetens **eget användningsfall** klassificeras separat. Att grundmodellen är en GPAI-modell säger inte i sig om myndighetens lösning är högrisk.

**Arkitekturfråga:** Vad behöver vi veta om grundmodellen för att kunna bedöma och styra vår egen lösning?

## En praktisk AI-förordningskontroll för arkitekten

När ett nytt AI-användningsfall kommer upp kan följande kontroll användas som första steg:

| Kontrollfråga | Varför den är viktig |
|---|---|
| Är detta ett AI-system enligt förordningen? | Avgör om AI-förordningen över huvud taget är tillämplig |
| Vilken roll har myndigheten? | Provider och deployer har olika skyldigheter |
| Vad är systemets avsedda användning? | Riskklassningen bygger på användningsfallet |
| Ligger användningen nära någon förbjuden praktik? | Kräver omedelbar fördjupad bedömning |
| Kan användningen omfattas av högriskreglerna? | Aktiverar omfattande krav för system och deployer |
| Finns transparenskrav? | Kan kräva information eller märkning i tjänsten |
| Vilken mänsklig kontroll krävs? | Påverkar process, gränssnitt, roller och behörigheter |
| Vilken AI-kompetens behöver organisationen? | Ett uttryckligt krav som måste omsättas praktiskt |
| Vilka tillämpningsdatum gäller under systemets livstid? | Krav kan börja gälla efter införandet |
| Vilken annan lagstiftning gäller parallellt? | AI-förordningen ersätter inte övrig rätt |

## Bedömning: grönt, gult eller rött

Den förenklade färgmodellen kan nu preciseras:

**Grönt**  
AI-systemet verkar ligga utanför förbjudna och högriskklassade användningar. Eventuella transparenskrav och övriga regelverk är hanterbara inom vanlig styrning.

**Gult**  
Användningen påverkar människor, ligger nära bilaga III, omfattar känsliga funktioner eller gör organisationens roll oklar. Klassificeringen och kraven behöver utredas innan arkitekturen låses.

**Rött**  
Användningen kan träffa en förbjuden praktik eller någon annan tydlig rättslig begränsning. Lösningen bör inte gå vidare innan rättsläget är klarlagt.

Färgmodellen är ett triageverktyg. Den är inte en juridisk klassificering.

## Sammanfattning

AI-förordningen ska inte läsas som en lista över allt en myndighet får eller inte får göra med AI. För arkitekten är den framför allt ett sätt att **klassificera användningsfallet och förstå vilka AI-specifika skyldigheter som aktiveras**.

Den praktiska ordningen är:

1. avgör om lösningen omfattar ett AI-system,
2. identifiera organisationens roll,
3. beskriv det avsedda användningsfallet,
4. kontrollera förbud, högrisk och transparens,
5. identifiera krav på mänsklig kontroll, kompetens, dokumentation och övervakning,
6. kontrollera tillämpningsdatumen,
7. gå därefter vidare till övrig lagstiftning.

Nästa kapitel lämnar klassificeringen av själva AI-systemet och fokuserar på informationen: **vad får vi egentligen mata AI:n med?**

## Viktigaste källorna

- Konsoliderad AI-förordning (EU) 2024/1689, lydelse efter ändring 2026-07-27: https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng
- Förordning (EU) 2026/1744, Digital Omnibus on AI: https://eur-lex.europa.eu/legal-content/SV/TXT/?uri=CELEX:32026R1744
- EU-kommissionen, *AI Act – Regulatory framework*: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- EU-kommissionen, *AI talent, skills and literacy* – artikel 4 efter Digital Omnibus: https://digital-strategy.ec.europa.eu/en/policies/ai-talent-skills-and-literacy
- AI Act Service Desk, artikel 3 – definitioner: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-3
- AI Act Service Desk, artikel 4 – AI literacy: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-4
- AI Act Service Desk, artikel 5 – förbjudna AI-praktiker: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5
- AI Act Service Desk, artikel 26 – deployers av högrisk-AI: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26
- AI Act Service Desk, artikel 27 – fundamental rights impact assessment: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-27
- AI Act Service Desk, artikel 50 – transparens: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50
