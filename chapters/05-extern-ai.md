# <span class="chapter-number">Kapitel 5</span><span class="chapter-name">När någon annan tillhandahåller AI:n</span>

Myndigheter använder ofta AI genom externa tjänster: SaaS, API:er, AI-funktioner i befintliga system eller leverantörsdrift.

Det kan vara både effektivt och lämpligt. Men när kontroll flyttas utanför myndigheten behöver arkitekten förstå inte bara **vad AI-funktionen gör**, utan också **vem som behandlar informationen, var den behandlas, vilka underleverantörer som används och vilka rättigheter leverantören får till data och resultat**.

En praktisk princip är:

> **En extern AI-tjänst bör bedömas som ett informationsflöde och ett beroende – inte bara som en funktion.**

## Utgå från behovet

Det är lätt att börja med frågan: *Kan vi använda produkt X?* En bättre startpunkt är:

- vilket verksamhetsbehov ska lösas,
- vilken information behöver behandlas,
- vilka personer eller beslut kan påverkas,
- vilken tillgänglighet och kvalitet behövs,
- vilka rättsliga och säkerhetsmässiga begränsningar gäller,
- vilken kontroll behöver myndigheten ha över data, modell och leverantör.

Digg och IMY rekommenderar att offentlig förvaltning utgår från verksamhetens behov när generativ AI anskaffas. Färdiga tjänster kan vara lämpliga för enklare användning och kompetenshöjning, medan mer verksamhetskritiska behov kan kräva tydligare kravställning och större kontroll.

Detta är viktigt för arkitekten eftersom en produkt som fungerar bra i en demonstration inte automatiskt är lämplig för myndighetens verkliga informationsmängder och processer.

## En AI-tjänst är ofta flera tjänster samtidigt

Det som för användaren ser ut som en enda AI-tjänst kan i praktiken bestå av flera delar:

- användargränssnitt,
- API-gateway,
- identitets- och behörighetstjänst,
- loggning och telemetri,
- modellleverantör,
- databas eller vektordatabas,
- modereringstjänster,
- support- och övervakningsfunktioner,
- underleverantörer för drift eller analys.

Det betyder att frågan *"var ligger tjänsten?"* ofta är för enkel.

Arkitekten behöver i stället kartlägga **hela behandlingskedjan**:

1. Var skickas prompten?
2. Var lagras den?
3. Vem kan administrera tjänsten?
4. Var behandlas bilagor och RAG-data?
5. Var lagras loggar och metadata?
6. Används en separat modellleverantör?
7. Finns supportåtkomst från andra länder?
8. Kan informationen användas för leverantörens egna ändamål?

Om leverantören inte kan ge tillräckligt tydliga svar är det i sig en arkitekturell risk.

## Upphandling handlar om mer än pris och funktion

Lag (2016:1145) om offentlig upphandling, LOU, gäller för många av de inköp en myndighet gör. AI förändrar inte grundprinciperna för offentlig upphandling.

Digg rekommenderar att offentliga aktörer först kontrollerar befintliga avtal och ramavtal och, om de inte täcker behovet, genomför upphandling enligt gällande regler. Licens- och avtalsvillkor behöver analyseras både inför anskaffningen och under användningen.

För AI-lösningar behöver kravställningen ofta vara bredare än vid ett vanligt funktionsköp.

Exempel på frågor som kan behöva bli krav eller avtalsvillkor:

- Vilka modeller får leverantören använda?
- Får modellen eller modellversionen bytas utan godkännande?
- Var får data behandlas och lagras?
- Vilka underleverantörer får användas?
- Hur meddelas förändringar i underleverantörskedjan?
- Får myndighetens data användas för träning eller förbättring av leverantörens modeller?
- Hur länge sparas promptar, svar, filer och loggar?
- Kan myndigheten få tillgång till relevanta loggar?
- Vilka säkerhetskontroller kan myndigheten verifiera?
- Hur hanteras incidenter?
- Vilka krav gäller vid avveckling och export av data?
- Hur kan myndigheten byta leverantör utan orimliga kostnader eller informationsförlust?

**Arkitekturfråga:** Är de krav som behövs för att lösningen ska vara laglig och kontrollerbar faktiskt möjliga att skriva in i avtalet och följa upp i praktiken?

## Personuppgiftsansvaret försvinner inte vid outsourcing

När myndigheten använder en extern AI-tjänst för sitt uppdrag är myndigheten som utgångspunkt fortfarande personuppgiftsansvarig för den personuppgiftsbehandling som sker för myndighetens ändamål.

Om leverantören behandlar personuppgifter för myndighetens räkning kan leverantören vara personuppgiftsbiträde. Då krävs normalt ett personuppgiftsbiträdesavtal och myndigheten måste kunna säkerställa att behandlingen uppfyller GDPR.

Det finns en viktig komplikation med AI-tjänster: leverantören kan vilja använda uppgifterna för **egna ändamål**, exempelvis för att träna eller förbättra en grundmodell.

Digg/IMY framhåller att en leverantör som behandlar uppgifter enbart för verksamhetens räkning kan vara biträde. Om leverantören däremot har ett eget ändamål, till exempel vidareutveckling av grundmodellen med myndighetens personuppgifter, kan rollfördelningen förändras.

Detta gör avtalsvillkor om datanyttjande särskilt viktiga.

**Röd signal:** leverantören förbehåller sig en generell rätt att använda myndighetens indata, filer eller konversationer för egen modellträning och myndigheten behandlar uppgifter som inte får användas för detta ändamål.

## "Vi tränar inte på era data" löser inte hela frågan

Det är positivt om leverantören inte använder myndighetens data för modellträning, men det är bara en del av bedömningen.

Myndigheten behöver fortfarande förstå:

- om data lagras,
- hur länge data lagras,
- om loggar innehåller personuppgifter eller sekretesskyddade uppgifter,
- om supportpersonal kan få åtkomst,
- vilka underleverantörer som får åtkomst,
- om data kopieras för säkerhetskopiering,
- om metadata används för andra ändamål,
- om data kan behandlas utanför EU/EES.

Det är därför bättre att fråga **"hur behandlas vår information genom hela livscykeln?"** än enbart **"tränar ni på vår data?"**.

## Tredjelandsfrågan handlar om åtkomst, inte bara datacenter

I kapitel 3 konstaterade vi att personuppgifter kan överföras till tredjeland även utan att ett primärt datacenter ligger där. Åtkomst från ett land utanför EU/EES kan i vissa situationer innebära en tredjelandsöverföring.

För en extern AI-tjänst behöver därför frågor om:

- driftplats,
- administratörsåtkomst,
- support,
- underleverantörer,
- incidenthantering,
- rättsliga krav på leverantören i dess hemland

analyseras tillsammans.

Det räcker alltså inte med ett marknadsföringspåstående om "EU-region" om andra delar av tjänsten fortfarande innebär åtkomst från tredjeland.

**Gul signal:** tjänsten driftas i EU men leverantören kan inte tydligt beskriva vilka support- och administrationsflöden som kan nå informationen.

## Sekretess kräver en separat bedömning

Att ett personuppgiftsbiträdesavtal finns betyder inte automatiskt att sekretessreglerna är uppfyllda.

Offentlighets- och sekretesslagen och annan tystnadspliktsreglering måste bedömas separat. Digg rekommenderar uttryckligen att offentliga aktörer utreder om informationsöverföring till leverantör eller mellanhand är tillåten och säkerställer att uppgifter som ska stanna inom verksamheten inte lämnas ut utan rättsligt stöd.

Arkitekten behöver därför kunna skilja på minst tre frågor:

1. Får myndigheten behandla personuppgifterna på detta sätt?
2. Får uppgifterna lämnas till den externa aktören?
3. Är säkerhetsnivån tillräcklig för informationens skyddsvärde?

Ett ja på den första frågan innebär inte automatiskt ja på de två andra.

## Säkerhetsskydd kan förändra hela anskaffningen

Om AI-lösningen berör säkerhetskänslig verksamhet kan säkerhetsskyddslagen utlösa krav som går långt utöver en vanlig moln- eller SaaS-bedömning.

Det kan bland annat påverka:

- vilka leverantörer som över huvud taget är möjliga,
- vilken information de får ta del av,
- hur systemet får driftas,
- vilka kontroller som måste göras före anskaffning,
- behov av säkerhetsskyddsavtal,
- krav på åtkomstkontroll och personalsäkerhet.

**Röd signal:** en leverantör ska få åtkomst till säkerhetsskyddsklassificerade uppgifter eller till säkerhetskänslig verksamhet utan att säkerhetsskyddsfrågan har analyserats tidigt i anskaffningen.

## AI-förordningen gör leverantörskedjan juridiskt relevant

AI-förordningen skiljer mellan flera roller, bland annat provider och deployer. En myndighet som använder ett färdigt AI-system är ofta deployer, medan leverantören är provider.

Men rollerna är inte statiska.

En organisation som gör en väsentlig ändring av ett högrisk-AI-system eller sätter sitt eget namn på systemet kan under vissa förutsättningar själv få provider-ansvar.

Det innebär att en myndighet inte bör anta att **"vi köper bara tjänsten"** alltid betyder att alla regulatoriska skyldigheter ligger hos leverantören.

För högrisk-AI måste deployern dessutom kunna använda systemet enligt instruktionerna, ordna kompetent mänsklig kontroll och uppfylla andra egna skyldigheter. Det förutsätter att avtalet och tekniken ger myndigheten den information och kontroll som krävs.

**Arkitekturfråga:** Ger leverantören tillräcklig dokumentation, loggning och kontroll för att myndigheten ska kunna fullgöra sina egna skyldigheter?

## Versionsbyten kan ändra riskbilden

AI-tjänster förändras ofta snabbare än traditionella IT-system. Leverantören kan byta:

- grundmodell,
- systemprompt,
- säkerhetsfilter,
- verktygsintegrationer,
- lagringspolicy,
- underleverantörer,
- region för behandling,
- funktioner i användargränssnittet.

En myndighet kan därför ha godkänt en lösning som senare ändras på ett sätt som påverkar:

- informationssäkerhet,
- dataskydd,
- kvalitet,
- förklarbarhet,
- AI Act-klassificering,
- avtalsenlighet.

Avtalet och förvaltningsmodellen behöver därför hantera förändringar över tid.

Exempel på lämpliga kontrollpunkter är:

- krav på förhandsinformation om väsentliga förändringar,
- möjlighet att stoppa eller avvisa en förändring,
- test innan ny modellversion tas i bruk,
- dokumenterad omprövning av riskbedömning,
- tydlig ansvarsfördelning mellan verksamhet, IT, juridik och säkerhet.

## Loggar är både en tillgång och en risk

Loggar kan behövas för:

- felsökning,
- spårbarhet,
- incidentutredning,
- uppföljning av modellkvalitet,
- kontroll av mänsklig användning,
- efterlevnad av AI-förordningen.

Samtidigt kan loggar innehålla:

- promptar,
- personuppgifter,
- sekretessbelagda uppgifter,
- modellresultat,
- användaridentiteter,
- känslig metadata.

Arkitekten behöver därför behandla loggningen som en egen informationsmängd med egna regler för behörighet, lagring, gallring och export.

**Vanligt misstag:** att kräva "full loggning" utan att samtidigt definiera vem som får läsa loggarna och hur länge de får sparas.

## Exit är en del av säkerheten

Regeringens molnpolicy för offentlig förvaltning från 2026 betonar bland annat minskat beroende, bättre kontroll över data och möjligheten att välja och byta digitala lösningar.

Det är särskilt relevant för AI, där beroendet inte bara kan ligga i infrastrukturen utan också i:

- proprietära promptformat,
- embeddings,
- vektordatabaser,
- leverantörsspecifika agenter,
- finjusteringar,
- utvärderingsdata,
- loggar och historik,
- modellbeteende som byggts in i verksamhetsprocessen.

En fungerande exitplan bör därför besvara:

- Vilken data kan exporteras?
- I vilket format?
- Kan RAG-index byggas om hos en ny leverantör?
- Vad händer med historiska konversationer och loggar?
- Hur verifieras radering hos den gamla leverantören?
- Kan verksamheten fortsätta om leverantören stänger en modell med kort varsel?
- Hur stor del av lösningen är portabel?

**Arkitekturprincip:** undvik att göra verksamhetskritiska processer beroende av egenskaper som endast en leverantör kan tillhandahålla om det inte är ett medvetet och accepterat beslut.

## Leverantörslåsning är inte automatiskt fel

All leverantörsberoende är inte dåligt. Ibland kan en specifik tjänst ge så stora fördelar att beroendet är motiverat.

Det viktiga är att beroendet är **synligt och beslutat**, inte något som upptäcks när myndigheten vill byta tjänst.

Arkitekten bör därför beskriva:

- vilka delar som är standardiserade,
- vilka delar som är leverantörsspecifika,
- kostnaden för byte,
- vilken data som riskerar att gå förlorad,
- vilka juridiska eller säkerhetsmässiga antaganden som är knutna till leverantören.

Det gör det möjligt för beslutsfattare att väga innovation mot långsiktig kontroll.

## En enkel leverantörskontroll för arkitekten

Före beslut om extern AI kan arkitekten använda följande frågor.

### 1. Behov

- Vilket konkret problem löser tjänsten?
- Finns enklare alternativ med lägre risk?

### 2. Information

- Vilka uppgifter skickas till tjänsten?
- Förekommer personuppgifter, sekretess eller säkerhetskänslig information?

### 3. Dataflöde

- Var behandlas data?
- Vilka underleverantörer och supportfunktioner kan få åtkomst?

### 4. Ändamål

- Behandlar leverantören data endast för myndighetens räkning?
- Får uppgifter användas för modellträning, produktutveckling eller andra egna ändamål?

### 5. Avtal

- Finns rätt avtal och personuppgiftsbiträdesavtal?
- Regleras underleverantörer, incidenter, loggar, ändringar och radering?

### 6. AI-förordningen

- Vilken roll har myndigheten respektive leverantören?
- Kan tjänsten vara högrisk eller omfattas av transparenskrav?
- Får myndigheten den dokumentation som behövs?

### 7. Förändringar

- Kan leverantören byta modell eller villkor utan att myndigheten hinner göra en ny bedömning?

### 8. Exit

- Kan data och funktion flyttas till en annan lösning?
- Finns en plan om tjänsten försvinner eller blir olämplig?

## Bedömning: grönt, gult eller rött

### Grönt – normalt möjligt

Exempel:

- lågkänslig information,
- tydligt avtal,
- kända underleverantörer,
- ingen otillåten vidareanvändning av data,
- hanterad tredjelandsfråga,
- dokumenterad exit,
- myndigheten kan uppfylla sina egna skyldigheter.

### Gult – utred först

Exempel:

- personuppgifter behandlas,
- leverantören använder flera underleverantörer,
- support kan ske från tredjeland,
- modellversionen kan ändras löpande,
- loggningen är otydlig,
- tjänsten ska användas i verksamhetskritiska processer,
- det är svårt att exportera data eller byta leverantör.

### Rött – gå inte vidare innan frågan är löst

Exempel:

- sekretesskyddade uppgifter lämnas till leverantör utan rättsligt stöd,
- säkerhetskänslig verksamhet exponeras utan korrekt säkerhetsskyddsanalys,
- leverantören får använda myndighetens uppgifter för egna oförenliga ändamål,
- myndigheten kan inte identifiera var eller av vem informationen behandlas,
- avtalet gör att myndigheten inte kan uppfylla tvingande krav enligt GDPR, AI-förordningen eller annan tillämplig rätt.

## Vanliga misstag

### "Det är en standardtjänst, så leverantören ansvarar"

Myndigheten ansvarar fortfarande för sin användning och för de behandlingar och beslut som sker inom myndighetens uppdrag.

### "Datat ligger i EU, alltså är allt löst"

Driftplats är bara en del av analysen. Support, underleverantörer och administrativ åtkomst kan vara lika viktiga.

### "Leverantören tränar inte på vår data"

Bra, men kontrollera även lagring, loggar, supportåtkomst, metadata och underleverantörer.

### "Vi kan alltid byta senare"

Byte kan bli svårt om verksamheten byggt in leverantörsspecifika funktioner, embeddings, arbetsflöden eller historik.

### "Mänsklig kontroll ligger hos verksamheten"

Det hjälper bara om tjänsten faktiskt ger verksamheten tillräcklig information, funktionalitet och befogenhet för att kontrollen ska fungera.


## Sammanfattning

När någon annan tillhandahåller AI:n behöver myndigheten behålla kontroll över **ändamål, information, ansvar och beroenden**.

De viktigaste principerna är:

- börja med verksamhetsbehovet, inte leverantörens produkt,
- kartlägg hela informations- och underleverantörskedjan,
- skilj på dataskydd, sekretess och säkerhetsskydd,
- säkerställ att leverantörens användning av data är tydligt reglerad,
- kravställ dokumentation, loggning och förändringshantering,
- förstå myndighetens egen roll enligt AI-förordningen,
- planera exit redan vid anskaffningen.

En extern AI-tjänst kan vara ett utmärkt sätt att snabbt få tillgång till avancerad AI. Men outsourcing innebär inte outsourcing av myndighetens ansvar.

## Viktigaste källorna

- Lag (2016:1145) om offentlig upphandling: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-20161145-om-offentlig-upphandling_sfs-2016-1145/
- Digg/IMY – Ta medvetna beslut om att skaffa generativ AI: https://www.digg.se/ai-for-offentlig-forvaltning/riktlinjer-for-generativ-ai/ta-medvetna-beslut-om-att-skaffa-generativ-ai
- Digg/IMY – Köp generativ AI enligt lagen om offentlig upphandling: https://www.digg.se/ai-for-offentlig-forvaltning/riktlinjer-for-generativ-ai/kop-generativ-ai-enligt-lagen-om-offentlig-upphandling
- Digg/IMY – Klargör rollfördelningen mellan personuppgiftsansvarig och personuppgiftsbiträde: https://www.digg.se/ai-for-offentlig-forvaltning/riktlinjer-for-generativ-ai/klargor-rollfordelningen-mellan-personuppgiftsansvarig-och-personuppgiftsbitrade
- Digg/IMY – Säkerställ sekretess vid användning av generativ AI: https://www.digg.se/ai-for-offentlig-forvaltning/riktlinjer-for-generativ-ai/sakerstall-sekretess-vid-anvandning-av-generativ-ai
- AI-förordningen, särskilt artiklarna 25 och 26: https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng
- Sveriges molnpolicy för offentlig förvaltning (2026): https://www.regeringen.se/informationsmaterial/2026/05/en-molnpolicy-for-sverige--for-okad-sakerhet-effektivitet-och-innovation-i-den-offentliga-forvaltningen/
