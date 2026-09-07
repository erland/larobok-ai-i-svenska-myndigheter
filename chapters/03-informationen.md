# <span class="chapter-number">Kapitel 3</span><span class="chapter-name">Informationen – vad matar vi AI:n med?</span>

Diskussionen börjar lätt med modellval, kvalitet eller molndrift. För en myndighet kommer en viktigare fråga först:

> **Vilken information ska AI-lösningen få tillgång till, och för vilket ändamål?**

När den frågan är besvarad går det att bedöma om användningen är okomplicerad, kräver skyddsåtgärder eller behöver en fördjupad analys.

Det här kapitlet handlar därför inte främst om AI-modellen. Det handlar om informationsflödet runt modellen: promptar, dokument, databaser, RAG-index, loggar, träningsdata, metadata och resultat.

## Kartlägg informationen först

En arkitekt bör kunna beskriva informationsflödet innan en AI-tjänst väljs:

1. Vilka informationsmängder går in i lösningen?
2. Varifrån kommer de?
3. Varför behöver AI:n just dessa uppgifter?
4. Vem eller vad får tillgång till dem?
5. Var behandlas de?
6. Sparas de, loggas de eller används de för träning?
7. Vilken information kommer ut ur lösningen?
8. Hur används resultatet vidare?

Det gör det möjligt att skilja mellan flera rättsliga frågor som annars lätt blandas ihop.

En uppgift kan exempelvis vara en personuppgift utan att omfattas av sekretess. En sekretessbelagd uppgift behöver inte vara en personuppgift. Och information som inte omfattas av någon av dessa kategorier kan ändå vara så verksamhetskritisk att den behöver ett starkt skydd.

## Personuppgifter: GDPR gäller även när AI:n bara är ett verktyg

När personuppgifter behandlas i samband med utveckling eller användning av AI gäller GDPR. IMY framhåller att verksamheten bland annat måste följa de grundläggande principerna, ha rättslig grund och informera de registrerade om behandlingen.

Det är alltså inte AI-användningen i sig som skapar rätten att behandla personuppgifter.

För arkitekten är särskilt fyra GDPR-principer praktiskt viktiga:

### Ändamålsbegränsning

Personuppgifter får samlas in för särskilda, uttryckligt angivna och berättigade ändamål och får inte senare användas på ett sätt som är oförenligt med dessa ändamål.

Det gör formuleringen **”vi vill använda vår data för AI”** otillräcklig. Arkitekturen behöver bygga på ett mer konkret ändamål, exempelvis:

- sammanfatta inkomna handlingar för en handläggare,
- hitta relevanta stycken i ett avgränsat dokumentbestånd,
- klassificera ärenden för manuell vidare behandling,
- identifiera tekniska avvikelser i systemloggar.

Ju bredare och mer otydligt ändamålet är, desto svårare blir det att motivera vilka personuppgifter AI:n behöver.

### Uppgiftsminimering

AI-lösningen ska inte få tillgång till fler personuppgifter än vad som behövs för ändamålet.

Detta är en viktig arkitekturprincip. Ett RAG-system behöver exempelvis inte automatiskt indexera hela myndighetens dokumentlager bara för att det är tekniskt möjligt. Ett analysflöde kan ofta filtrera, pseudonymisera eller ta bort irrelevanta fält innan informationen når modellen.

**Arkitekturfråga:** Kan samma verksamhetsnytta uppnås med mindre information?

### Riktighet

Personuppgifter ska vara riktiga och vid behov uppdaterade. AI kan samtidigt skapa felaktiga slutsatser, sammanblandningar eller påståenden.

Det innebär att output som innehåller personuppgifter inte bör betraktas som korrekt bara för att den är språkligt övertygande. Ju större betydelse resultatet får för en person, desto viktigare blir verifiering mot auktoritativa källor.

### Lagringsminimering

Personuppgifter ska normalt inte sparas längre än vad som behövs för ändamålet. För AI-lösningar behöver man därför förstå vad som faktiskt lagras:

- promptar,
- bifogade dokument,
- chatt- eller sessionshistorik,
- embeddings och vektordatabaser,
- tekniska loggar,
- feedbackdata,
- modelloutput.

Samtidigt kan annan lagstiftning, exempelvis arkivregler, innebära att viss information behöver bevaras. Radering enligt GDPR och bevarande enligt arkivrätten måste därför hanteras tillsammans, inte som två isolerade tekniska krav.

## Känsliga och särskilt skyddsvärda personuppgifter

Vissa personuppgifter kräver större försiktighet. GDPR innehåller särskilda regler för känsliga personuppgifter, och IMY pekar även ut andra integritetskänsliga uppgifter som kan kräva högre säkerhetsnivå.

Exempel är uppgifter om:

- hälsa,
- biometrisk identifiering,
- politiska eller religiösa förhållanden,
- fackligt medlemskap,
- sexualliv eller sexuell läggning,
- lagöverträdelser,
- skyddade personuppgifter,
- värderande personprofiler.

Att en AI-tjänst tekniskt kan bearbeta uppgifterna säger inget om myndigheten får använda dem på det sättet.

**Gul signal:** Lösningen behandlar stora mängder personuppgifter, känsliga uppgifter, profiler eller information om sårbara grupper.

## Rättslig grund är inte samma sak som tekniskt behov

För myndigheter är rättslig grund ofta kopplad till rättslig förpliktelse eller uppgift av allmänt intresse/myndighetsutövning. Men den exakta bedömningen beror på verksamheten och den behandling som faktiskt sker.

Arkitektens uppgift är inte att själv slutligt avgöra rättslig grund. Däremot måste arkitekturbeskrivningen vara så konkret att jurist eller dataskyddsfunktion kan göra bedömningen.

Det innebär att man behöver kunna svara på:

- vilka uppgifter som behandlas,
- för vilka personer,
- i vilket steg av processen,
- vilket verksamhetsändamål behandlingen stödjer,
- vilka mottagare som får tillgång,
- hur länge uppgifterna behandlas.

En vag lösningsbeskrivning ger också en vag juridisk analys.

## Konsekvensbedömning: ibland måste riskerna analyseras före införandet

Om en planerad personuppgiftsbehandling sannolikt medför hög risk för människors fri- och rättigheter krävs en konsekvensbedömning enligt GDPR, en DPIA. IMY beskriver den som en pågående och dokumenterad process för högriskbehandlingar, inte som en engångsblankett.

AI kan bidra till att en sådan bedömning behövs, särskilt vid exempelvis:

- omfattande profilering eller systematiska bedömningar av personer,
- stora mängder känsliga personuppgifter,
- systematisk övervakning,
- ny teknik i kombination med andra riskfaktorer,
- behandling som kan få betydande konsekvenser för enskilda.

Om hög risk kvarstår trots planerade skyddsåtgärder kan förhandssamråd med IMY krävas innan behandlingen påbörjas.

**Arkitekturkonsekvens:** identifiera behovet av DPIA innan designen och avtalen är låsta. Då kan resultatet fortfarande påverka informationsmängder, integrationer, loggning, säkerhetsåtgärder och leverantörsval.

## Sekretess: får uppgiften lämnas till AI-tjänsten?

Sekretessfrågan är skild från GDPR.

När en myndighet använder en extern AI-tjänst kan leverantören eller en mellanhand få del av myndighetens uppgifter. Digg beskriver att det som utgångspunkt kan vara fråga om ett utlämnande till den externa parten. Därför måste myndigheten bedöma om uppgifter omfattas av sekretess eller annan tystnadsplikt och om det finns rättsligt stöd för att lämna dem vidare.

Det gäller även om:

- informationen bara finns i en prompt,
- dokumentet betraktas som ett utkast,
- leverantören bara har teknisk åtkomst,
- informationen inte används för träning,
- användaren tänker radera konversationen efteråt.

Sekretessen skyddar uppgiften, inte filformatet eller användargränssnittet.

### Teknisk bearbetning och teknisk lagring

Offentlighets- och sekretesslagen innehåller en sekretessbrytande bestämmelse som kan göra det möjligt att lämna sekretessbelagda uppgifter till en extern aktör som för myndighetens räkning **endast** tekniskt bearbetar eller tekniskt lagrar informationen, om utlämnandet inte är olämpligt med hänsyn till omständigheterna.

Digg konstaterar att generativa AI-verktyg i vissa fall kan omfattas av denna situation, men att det beror på avtalet, verktygets funktion och användningsområdet och därför måste utredas innan användning.

Det är en viktig nyans: begreppet ”molntjänst” eller ”AI-tjänst” avgör inte i sig om undantaget är tillämpligt.

**Arkitekturfråga:** Vad gör leverantören faktiskt med informationen – och enbart för vems räkning?

## Säkerhetsskydd: en annan nivå av krav

Om AI-lösningen berör säkerhetskänslig verksamhet blir säkerhetsskyddslagen central. Lagen gäller verksamhet av betydelse för Sveriges säkerhet och ställer krav på säkerhetsskyddsanalys och nödvändiga säkerhetsskyddsåtgärder.

Informationssäkerheten ska bland annat förebygga att säkerhetsskyddsklassificerade uppgifter obehörigen röjs, ändras, görs otillgängliga eller förstörs och förebygga skadlig påverkan på informationssystem i säkerhetskänslig verksamhet.

Detta är inte bara en fråga om att undvika att skriva hemliga uppgifter i en publik chatbot. En extern AI-lösning kan även ge en annan aktör tillgång till:

- säkerhetskänsliga informationssystem,
- teknisk arkitektur,
- driftmönster,
- loggar,
- metadata,
- funktioner vars påverkan kan skada säkerhetskänslig verksamhet.

När en annan aktör kan få relevant tillgång kan säkerhetsskyddsavtal, särskild säkerhetsskyddsbedömning, lämplighetsprövning och andra krav aktualiseras.

**Röd signal:** AI-lösningen berör säkerhetskänslig verksamhet och säkerhetsskyddsfrågan är ännu inte analyserad.

## RAG gör inte informationen juridiskt ”lokal”

Retrieval-augmented generation, RAG, används ofta för att låta en språkmodell svara med stöd av myndighetens egna dokument.

Det kan vara en bra säkerhets- och kvalitetsarkitektur, men RAG löser inte automatiskt de rättsliga frågorna.

Arkitekten behöver fortfarande veta:

- vilka dokument som indexeras,
- vilka användare som får söka i vilka informationsmängder,
- om embeddings innehåller eller kan härleda skyddad information,
- var index och embeddings lagras,
- vilka textutdrag som skickas till modellen,
- om modellen eller leverantören loggar dessa utdrag,
- om åtkomstkontrollen i källsystemet följer med hela vägen till AI-svaret.

Ett vanligt arkitekturfel är att ett AI-lager skapar en ny sökväg som kringgår den behörighetsmodell som redan finns i källsystemen.

**Arkitekturfråga:** Kan en användare genom AI:n få information som samma användare inte får läsa direkt i källsystemet?

## Träning, finjustering och återanvändning är nya ändamål att analysera

Det är stor skillnad mellan att tillfälligt använda information som input och att låta den användas för:

- träning av en modell,
- finjustering,
- utvärdering,
- leverantörens produktutveckling,
- framtida analys,
- mänsklig kvalitetsgranskning hos leverantören.

Om personuppgifter ingår kan en sådan återanvändning innebära en ny behandling som måste bedömas mot bland annat ändamålsbegränsning och rättslig grund. Om informationen omfattas av sekretess eller andra skydd kan även utlämnandefrågan förändras.

Därför räcker det inte att fråga om leverantören ”tränar modellen”. Avtal och teknisk dokumentation behöver visa **alla former av sekundär användning och åtkomst**.

## Upphovsrätt kan påverka vilka källor som får användas

När ett AI-system använder stora mängder text, bilder, kod eller annat material behöver arkitekten också fråga om materialet är upphovsrättsligt skyddat och vilken användning som faktiskt sker. Frågan blir särskilt relevant vid modellträning, finjustering, text- och datautvinning och större RAG-lösningar med material som myndigheten inte själv äger rättigheterna till.

Det betyder inte att skyddat material generellt är förbjudet som AI-underlag. Upphovsrättslagen innehåller både ensamrätter och inskränkningar, bland annat regler om text- och datautvinning. Den konkreta bedömningen beror därför på materialet, användningen och vilken rätt eller licens myndigheten har.

**Gul signal:** lösningen bygger på stora mängder externt material och projektet har bara kontrollerat dataskydd och sekretess, inte användningsrätten till innehållet.

## Tredjelandsöverföring: fysisk lagringsplats är inte hela frågan

GDPR:s regler om tredjelandsöverföring kan aktualiseras när personuppgifter skickas eller görs tillgängliga för en mottagare utanför EU/EES.

IMY anger uttryckligen att även läsbehörighet från ett tredjeland kan innebära en överföring, även om uppgifterna lagras inom EU/EES. Molnarkitektur måste därför analyseras utifrån faktisk åtkomst, inte enbart datacentrets geografiska adress.

För AI-tjänster behöver man bland annat förstå:

- var leverantören och underleverantörerna är etablerade,
- var support och driftpersonal finns,
- var loggar behandlas,
- om fjärråtkomst från tredjeland förekommer,
- vilka överföringsmekanismer och skyddsåtgärder som används.

Den frågan utvecklas vidare i kapitel 5 om extern AI.

## Sektorsspecifik reglering kan sätta snävare gränser

GDPR är inte alltid den enda dataskyddsregeln. Många myndigheter har särskilda register- eller datalagar som anger vilka personuppgifter som får behandlas, för vilka ändamål, vilka sökningar som får göras, vem som får få tillgång och hur länge uppgifter får behandlas.

Det är därför farligt att resonera:

> ”Vi har rättslig grund enligt GDPR, alltså får vi göra analysen.”

Den sektorsspecifika regleringen kan innehålla ytterligare begränsningar.

Bilaga B visar detta översiktligt för Tullverket, Polismyndigheten och Skatteverket.

## En informationskontroll före AI-design

Följande kontroll kan göras innan en AI-lösning designas eller anskaffas:

| Kontrollfråga | Om svaret är ja |
|---|---|
| Förekommer personuppgifter? | Identifiera ändamål, rättslig grund, principer, roller och säkerhetskrav |
| Förekommer känsliga eller särskilt skyddsvärda personuppgifter? | Höj risknivån och bedöm behov av DPIA och starkare skydd |
| Omfattas någon uppgift av sekretess eller tystnadsplikt? | Utred om och på vilken grund leverantör eller annan mottagare får ta del av uppgiften |
| Berör lösningen säkerhetskänslig verksamhet? | Koppla in säkerhetsskyddskompetens innan arkitekturen låses |
| Ska information indexeras i RAG eller embeddings? | Kontrollera åtkomstmodell, lagring, informationsspridning och livscykel |
| Ska data användas för träning, finjustering eller leverantörens förbättring? | Behandla detta som en särskild användning som kräver egen analys |
| Finns åtkomst eller behandling utanför EU/EES? | Utred tredjelandsöverföring och skyddsåtgärder |
| Finns sektorsspecifik data- eller registerlagstiftning? | Kontrollera dess ändamål, sökregler, åtkomst och lagringstider |

## Bedömning: grönt, gult eller rött

**Grönt**  
Lösningen arbetar med offentlig eller på annat sätt okänslig information, inga personuppgifter behöver behandlas, och informationsflödet är känt och kontrollerat.

Exempel: generativ AI används för att språkgranska redan publicerad myndighetstext i en godkänd tjänst.

**Gult**  
Personuppgifter, intern information, extern leverantör, RAG, omfattande loggning eller tredjelandsåtkomst förekommer. Användningen kan mycket väl vara tillåten, men informationsflödet och skyddsåtgärderna behöver analyseras innan lösningen låses.

**Rött**  
Sekretessbelagda eller säkerhetsskyddsklassificerade uppgifter riskerar att lämnas till en mottagare utan klarlagt rättsligt stöd, eller säkerhetskänslig verksamhet berörs utan genomförd säkerhetsskyddsbedömning.

Färgen beskriver behovet av analys – inte hur ”bra” eller ”dålig” AI-tekniken är.

## Sammanfattning

När en myndighet använder AI är informationsfrågan ofta mer avgörande än modellfrågan.

Arkitekten bör därför:

1. kartlägga informationsflödet,
2. identifiera personuppgifter och tillämpliga dataskyddsregler,
3. kontrollera ändamål och dataminimering,
4. identifiera sekretess och tystnadsplikt,
5. kontrollera om säkerhetsskydd aktualiseras,
6. förstå vad RAG, loggar, embeddings och träning faktiskt gör med informationen,
7. identifiera leverantörs- och tredjelandsåtkomst,
8. kontrollera sektorsspecifika regler.

Den viktigaste tumregeln är:

> **Fråga inte bara om AI får användas. Fråga om just dessa uppgifter får behandlas för just detta ändamål, på just detta sätt och av just dessa aktörer.**

Nästa kapitel går vidare från informationen till konsekvenserna för människor: **vad förändras när AI används i bedömningar, handläggning och myndighetsbeslut?**

## Viktigaste källorna

- Europaparlamentets och rådets förordning (EU) 2016/679, GDPR: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- Lag (2018:218) med kompletterande bestämmelser till EU:s dataskyddsförordning: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2018218-med-kompletterande-bestammelser_sfs-2018-218/
- IMY, *GDPR och AI*: https://www.imy.se/verksamhet/ai/gdpr-och-ai/
- IMY, *Grundläggande principer enligt GDPR*: https://www.imy.se/verksamhet/dataskydd/det-har-galler-enligt-gdpr/grundlaggande-principer
- IMY, *Konsekvensbedömning enligt GDPR*: https://www.imy.se/verksamhet/dataskydd/det-har-galler-enligt-gdpr/konsekvensbedomning/
- IMY, *Överföring av personuppgifter till tredjeland*: https://www.imy.se/verksamhet/dataskydd/det-har-galler-enligt-gdpr/overforing-till-tredje-land/
- Digg/IMY, *Säkerställ sekretess vid användning av generativ AI*: https://www.digg.se/ai-for-offentlig-forvaltning/riktlinjer-for-generativ-ai/sakerstall-sekretess-vid-anvandning-av-generativ-ai
- Offentlighets- och sekretesslag (2009:400), särskilt 10 kap. 2 a §: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/offentlighets-och-sekretesslag-2009400_sfs-2009-400/
- Säkerhetsskyddslag (2018:585): https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/sakerhetsskyddslag-2018585_sfs-2018-585/
- Säkerhetsskyddsförordning (2021:955): https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/sakerhetsskyddsforordning-2021955_sfs-2021-955/
