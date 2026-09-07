# <span class="chapter-number">Kapitel 8</span><span class="chapter-name">Praktiska scenarier</span>

Huvudtexten avslutas med åtta typiska situationer där en myndighet kan vilja använda AI.

Scenarierna ger inte generella juridiska ja- eller nej-besked. Bedömningen beror bland annat på uppgifterna, påverkan på människor, leverantören och sektorsspecifik reglering.

Använd därför scenarierna som exempel på **hur man resonerar**, inte som facit för alla myndigheter.

Varje scenario använder samma struktur:

1. Vad vill verksamheten göra?
2. Vilka riskindikatorer finns?
3. Vilka regelverk blir särskilt relevanta?
4. Vilken preliminär färg får användningen?
5. Vad behöver arkitekten göra härnäst?

## Scenario 1 – språkgranska en redan offentlig text

### Situationen

En kommunikationsfunktion vill använda generativ AI för att förbättra språk, struktur och begriplighet i en text som redan är publicerad på myndighetens webbplats. Inga interna kommentarer, personuppgifter eller sekretessbelagda uppgifter ska skickas till tjänsten.

### Riskindikatorer

Risknivån är normalt låg. Den viktigaste frågan är om tjänsten är godkänd för användning och om den färdiga texten kvalitetssäkras innan publicering.

### Relevanta regler

- AI-förordningens allmänna krav och eventuella transparensregler.
- Myndighetens interna AI-policy och informationssäkerhetsregler.
- Upphovsrätt kan behöva beaktas om större mängder externt skyddat material används som underlag.

### Preliminär bedömning

**Grönt**, om underlaget verkligen är offentligt och okänsligt, tjänsten är godkänd och resultatet granskas av ansvarig medarbetare.

### Arkitektens nästa steg

Kontrollera att användningsfallet omfattas av beslutad intern användning och att tjänstens villkor inte skapar oväntad återanvändning av data eller andra beroenden.

Detta är ett bra exempel på varför myndigheter inte bör behandla all AI som högrisk. Ett väl avgränsat användningsfall kan vara relativt okomplicerat.

## Scenario 2 – sammanfatta offentliga dokument

### Situationen

En myndighet vill låta en AI-tjänst sammanfatta offentliga rapporter, remisser och andra publikationer för internt analysstöd.

### Riskindikatorer

Även om källdokumenten är offentliga kan AI:n göra fel, utelämna reservationer eller blanda ihop fakta. Om sammanfattningen senare används som beslutsunderlag ökar kraven på kvalitet och spårbarhet.

### Relevanta regler

- AI-förordningen.
- Förvaltningslagens krav blir relevanta om sammanfattningen får betydelse i ärendehandläggning.
- Offentlighet och arkivering kan bli relevanta beroende på hur resultatet används och sparas.

### Preliminär bedömning

**Grönt** för orientering och enklare internt kunskapsstöd.

**Gult** om sammanfattningen används som faktiskt underlag för beslut eller ersätter läsning av den auktoritativa källan.

### Arkitektens nästa steg

Utforma lösningen så att användaren enkelt kan gå tillbaka till originalkällan. För viktiga arbetsflöden bör det vara tydligt vilka dokument sammanfattningen byggde på och att AI-output inte är en auktoritativ källa i sig.

## Scenario 3 – sammanfatta ett ärende med personuppgifter

### Situationen

Handläggare vill använda AI för att sammanfatta inkomna handlingar i ett ärende. Underlaget innehåller personuppgifter och kan även innehålla känsliga personuppgifter eller sekretessbelagd information.

### Riskindikatorer

Här förändras situationen väsentligt. Frågan handlar inte längre bara om AI-resultatets kvalitet utan om **vilken information som lämnas till systemet, varför den får behandlas och vem som får åtkomst till den**.

### Relevanta regler

- GDPR och dataskyddslagen.
- Eventuell sektorsspecifik registerförfattning.
- offentlighets- och sekretesslagen.
- säkerhetsskyddsregleringen om säkerhetskänslig verksamhet berörs.
- förvaltningslagen om sammanfattningen får betydelse för handläggning eller beslut.

### Preliminär bedömning

**Gult** som utgångspunkt.

Det kan bli **rött** om uppgifter ska lämnas till en tjänst som inte får hantera dem, om rättsligt stöd eller ändamål saknas eller om säkerhetsskyddsklassificerad information förs till en otillåten miljö.

### Arkitektens nästa steg

Dokumentera:

- informationskategorier,
- rättsligt ändamål,
- leverantörens och underleverantörers åtkomst,
- lagrings- och loggningsflöden,
- eventuell tredjelandsöverföring,
- hur output granskas mot originalhandlingarna.

Koppla in dataskydds- och juridisk kompetens samt säkerhetsfunktion efter behov innan teknikvalet låses.

## Scenario 4 – intern RAG över myndighetens dokument

### Situationen

Myndigheten vill bygga en intern AI-assistent som med RAG kan söka i styrdokument, handböcker, tidigare rapporter och andra interna kunskapskällor.

### Riskindikatorer

"Intern" betyder inte automatiskt lågrisk. Kunskapsbasen kan innehålla personuppgifter, sekretess, inaktuella dokument eller information som olika användargrupper inte ska kunna se.

RAG skapar dessutom fler informationsobjekt än originaldokumentet: exempelvis textsegment, embeddings, index, cache och loggar.

### Relevanta regler

- GDPR om personuppgifter förekommer.
- OSL och informationsklassning.
- arkiv- och informationshanteringsregler.
- säkerhetsskydd där det är relevant.
- AI-förordningen beroende på hur assistentens svar används.

### Preliminär bedömning

**Gult** tills informationsmängder, behörighetsmodell och driftmiljö är klarlagda.

Det kan därefter bli relativt **grönt** för en avgränsad kunskapsassistent med okänsligt material och tydliga källhänvisningar.

### Arkitektens nästa steg

Säkerställ bland annat:

- källstyrning och versionshantering,
- dokumentbehörigheter även i sök-/vektorskiktet,
- möjlighet att spåra svar till källor,
- hantering av borttagna och gallrade dokument,
- separation mellan informationsklasser om samma lösning inte bör hantera allt.

## Scenario 5 – AI för riskurval och prioritering

### Situationen

En myndighet vill använda AI för att rangordna objekt eller ärenden så att kontrollresurser läggs där sannolikheten för fel bedöms vara högst.

### Riskindikatorer

Detta är ett tydligt exempel på att ett system kan påverka människor även om AI:n inte fattar det slutliga beslutet. Den som hamnar högt i ett riskurval kan bli föremål för kontroll, utredning eller annan myndighetsåtgärd.

Här blir sektorsspecifik reglering särskilt viktig. Det kan finnas uttryckliga regler om vilka uppgifter som får användas, för vilka analysändamål och hur urval får göras.

### Relevanta regler

- AI-förordningens riskklassificering, beroende på verksamhetsområde och användning.
- GDPR eller brottsdatalagen beroende på behandlingens syfte.
- sektorsspecifika datalagar och verksamhetsförfattningar.
- regeringsformens och förvaltningslagens krav på legalitet, saklighet och proportionalitet där de är tillämpliga.
- diskrimineringsreglering och grundläggande rättigheter.

### Preliminär bedömning

**Gult**, ofta mörkgult.

I vissa verksamheter kan användningen omfattas av AI-förordningens högriskregler eller andra särskilt strikta krav. Ett användningsfall får inte klassificeras som lågrisk bara för att en människa fattar det slutliga beslutet.

### Arkitektens nästa steg

Beskriv hela kedjan från data till faktisk konsekvens:

- vilka egenskaper påverkar riskpoängen,
- vilka datakällor används,
- hur modeller testas för systematiska fel,
- hur en människa kan förstå och frångå resultatet,
- hur utfallet följs upp,
- vilken sektorslagstiftning som ger rättsligt stöd för analysen.

## Scenario 6 – AI som handläggarstöd

### Situationen

AI:n läser ett ärende och föreslår vilken regel eller åtgärd som är relevant. Handläggaren fattar fortfarande beslutet.

### Riskindikatorer

Den centrala frågan är hur stor **faktisk påverkan** AI-rekommendationen får.

Om systemet bara hjälper användaren att hitta relevanta dokument är risken lägre. Om systemet däremot föreslår rättslig bedömning, utfall eller beslut och handläggare normalt förväntas följa rekommendationen är påverkan betydligt större.

### Relevanta regler

- förvaltningslagen.
- GDPR, inklusive artikel 22 när förutsättningarna för den bestämmelsen är uppfyllda.
- AI-förordningen, inklusive möjliga högriskregler och krav på mänsklig kontroll.
- sektorsspecifik reglering.
- diskrimineringsregler och grundläggande rättigheter.

Förvaltningslagen medger att myndighetsbeslut kan fattas automatiserat, men det innebär inte att varje AI-baserad beslutsarkitektur automatiskt är tillåten. Övrig tillämplig rätt måste fortfarande uppfyllas.

### Preliminär bedömning

**Gult** som normal utgångspunkt när AI:n materiellt påverkar bedömningen.

Det kan närma sig **grönt** om systemet endast erbjuder begränsad informationssökning som är enkel att verifiera.

Det kan bli **rött** om obligatoriska skyddsåtgärder saknas, rättsligt stöd inte är klarlagt eller användningen träffar ett förbud.

### Arkitektens nästa steg

Testa om den mänskliga kontrollen är verklig:

- Förstår handläggaren varför förslaget gavs?
- Finns tillgång till originalunderlaget?
- Kan förslaget enkelt frångås?
- Finns tid och organisatoriska förutsättningar att faktiskt granska det?
- Loggas AI-resultat och handläggarens beslut på ett ändamålsenligt sätt?

För vissa högrisk-AI-system som används av offentliga organ kommer AI-förordningen dessutom att kräva en konsekvensbedömning av påverkan på grundläggande rättigheter innan systemet tas i bruk när de berörda högriskreglerna blir tillämpliga. För Annex III-fallen är tillämpningsdatumet den 2 december 2027.

## Scenario 7 – AI-chatbot för allmänheten

### Situationen

Myndigheten vill erbjuda en chatbot på webbplatsen som svarar på frågor om regler, tjänster och myndighetens verksamhet.

### Riskindikatorer

Risknivån beror starkt på vad chatboten får göra.

En chatbot som hänvisar till publicerad information är något annat än en chatbot som:

- tar emot uppgifter om enskilda,
- ger individanpassade rättsliga besked,
- hjälper till att lämna in ärenden,
- bedömer rätt till en förmån,
- skapar myndighetens faktiska svar i ett enskilt ärende.

Dessutom finns en grundläggande risk att användaren uppfattar ett sannolikt men felaktigt AI-svar som myndighetens auktoritativa besked.

### Relevanta regler

- AI-förordningens transparenskrav för system som interagerar med människor.
- GDPR om användaren lämnar personuppgifter.
- förvaltningsrättsliga regler om service och handläggning beroende på funktion.
- lagen (2018:1937) om tillgänglighet till digital offentlig service när chatboten ingår i en digital tjänst som omfattas av lagen.
- offentlighet, dokumentation och arkivering beroende på om kommunikationen blir del av ett ärende.

### Preliminär bedömning

**Grönt till gult** för en tydligt avgränsad informationschatbot över publicerat material.

**Gult** eller högre om chatboten hanterar individuppgifter eller ger svar som får betydelse i konkreta ärenden.

### Arkitektens nästa steg

Utforma gränserna uttryckligt:

- vad chatboten får svara på,
- när den ska hänvisa till mänsklig handläggare,
- hur den visar källor,
- hur användaren informeras om att det är AI,
- vilka personuppgifter som får lämnas,
- hur konversationer sparas eller raderas.

## Scenario 8 – AI automatiserar delar av ett myndighetsbeslut

### Situationen

Myndigheten vill automatisera ett ärendeflöde där AI analyserar underlaget och producerar ett resultat som direkt leder till beslut för en fysisk person, eller där mänsklig medverkan är mycket begränsad.

### Riskindikatorer

Det här är ett av bokens tydligaste högriskområden.

Frågorna omfattar bland annat:

- om automatiserat beslutsfattande är tillåtet i den aktuella verksamheten,
- om GDPR artikel 22 är tillämplig,
- om användningen klassificeras som högrisk enligt AI-förordningen,
- om sektorsspecifika regler begränsar behandlingen,
- hur beslutet kan motiveras och förklaras,
- hur fel upptäcks och rättas,
- vilka möjligheter den enskilde har att få beslutet omprövat eller granskat.

AI-förordningens Annex III pekar uttryckligen ut flera användningar som högrisk, bland annat AI som används av offentliga myndigheter för att bedöma fysiska personers rätt till vissa väsentliga offentliga tjänster och förmåner. Dessa Annex III-regler börjar tillämpas den 2 december 2027. För offentliga organ kommer vissa sådana högriskanvändningar dessutom att kräva en bedömning av påverkan på grundläggande rättigheter före användning.

### Relevanta regler

- förvaltningslagen och eventuell specialförfattning.
- GDPR och dataskyddslagen.
- AI-förordningen, inklusive Annex III samt krav på mänsklig kontroll och konsekvensbedömning av grundläggande rättigheter där de är tillämpliga.
- diskrimineringsreglering och grundläggande rättigheter.
- dokumentations-, offentlighets- och arkivregler.

### Preliminär bedömning

**Rött tills den rättsliga och verksamhetsmässiga ramen är klarlagd.**

Rött betyder inte att automatiserade myndighetsbeslut generellt är förbjudna. Förvaltningslagen anger uttryckligen att beslut kan fattas automatiserat. Färgen betyder i stället att ett sådant AI-användningsfall inte bör gå vidare som en vanlig teknisk implementation innan rättsligt stöd, riskklassificering, skyddsåtgärder, dokumentation och ansvar är utredda.

### Arkitektens nästa steg

Detta användningsfall bör ha ett formaliserat tvärfunktionellt beslut före implementation. Arkitekturbeskrivningen behöver åtminstone visa:

- rättsligt stöd och ändamål,
- AI-systemets roll i beslutet,
- datakällor och kvalitetskontroller,
- hur diskriminerings- och felrisker testas,
- mänsklig kontroll när sådan krävs,
- motivering och förklarbarhet,
- loggning och spårbarhet,
- incident- och rättelseprocess,
- ansvarig systemägare och verksamhetsägare.

## Vad scenarierna visar

De åtta scenarierna ger tre återkommande slutsatser.

### 1. Produkten avgör inte risknivån

Samma generativa AI-tjänst kan vara relativt okomplicerad i ett användningsfall och olämplig i ett annat.

Bedöm därför:

> **användning + information + påverkan + aktör + rättslig kontext**

inte bara produktnamnet.

### 2. Gult är en normal färg i reglerad verksamhet

Många värdefulla AI-användningar kommer att börja som gula därför att de innehåller personuppgifter, intern information eller påverkar en verksamhetsprocess.

Det betyder inte att de ska stoppas.

Det betyder att nästa fråga ska vara konkret:

> **Vad behöver vi få klarlagt för att kunna gå vidare?**

En mogen myndighet bör därför inte mäta framgång i hur många initiativ som klassificeras gröna. Den bör mäta sin förmåga att snabbt och korrekt lösa de gula frågorna.

### 3. Rött betyder ofta "inte så här"

Ett rött resultat kan ibland lösas genom att ändra arkitekturen.

Exempel:

- använd en annan driftmiljö,
- ta bort en informationskategori,
- inför verklig mänsklig kontroll,
- begränsa AI:n till informationssökning i stället för bedömning,
- separera verksamheter med olika rättsliga förutsättningar,
- ändra avtalsvillkor eller leverantör,
- bygg den nödvändiga dokumentationen och riskhanteringen innan användning.

Det är här arkitekturkompetensen blir särskilt värdefull. Regler behöver inte bara skapa stoppunkter; de kan omsättas till **designkrav**.

## En sista kontroll före nästa steg

När ett AI-initiativ har analyserats bör arkitekten kunna sammanfatta det på en sida:

| Fråga | Kort svar |
|---|---|
| Vad gör AI:n? | Avgränsad funktion och syfte |
| Vilka uppgifter används? | Informationskategorier och skyddsvärde |
| Vem påverkas? | Personer, ärenden eller endast intern produktion |
| Vem får åtkomst? | Myndighet, leverantör, underleverantör och land/region |
| Vilka regler är centrala? | Generella och sektorsspecifika |
| Hur klassificeras AI-användningen? | Förbjuden, högrisk, transparenskrav eller annan användning |
| Hur sker mänsklig kontroll? | Konkret arbetsmoment, inte bara rollnamn |
| Vad dokumenteras? | Underlag, output, modell/version, beslut och loggar efter behov |
| Vilka frågor är fortfarande gula? | Namngivna öppna bedömningar |
| Vem äger beslutet att gå vidare? | Tydlig verksamhets- och systemägare |

Om detta går att beskriva tydligt är initiativet betydligt lättare att granska, upphandla, bygga och förvalta.

## Viktigaste källorna

- Förvaltningslag (2017:900), särskilt 5, 27, 28 och 32 §§: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/forvaltningslag-2017900_sfs-2017-900/
- Förordning (EU) 2016/679 (GDPR), särskilt artikel 22: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- AI-förordningen – AI Act Explorer: https://ai-act-service-desk.ec.europa.eu/en/ai-act-explorer
- AI-förordningen – Annex III: https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3
- AI-förordningen – artikel 27 om konsekvensbedömning av grundläggande rättigheter: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-27
- Digg/IMY – Riktlinjer för generativ AI inom offentlig förvaltning: https://www.digg.se/ai-for-offentlig-forvaltning/riktlinjer-for-generativ-ai
- Offentlighets- och sekretesslag (2009:400): https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/offentlighets-och-sekretesslag-2009400_sfs-2009-400/
- Arkivlag (1990:782): https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/arkivlag-1990782_sfs-1990-782/
