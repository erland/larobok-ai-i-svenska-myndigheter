# <span class="chapter-number">Kapitel 7</span><span class="chapter-name">Från idé till arkitekturbeslut</span>

Ett AI-initiativ börjar ofta med frågan *vilken modell ska vi använda?* För en myndighet bör arkitekturbeslutet börja tidigare i kedjan.

En bättre ordning är:

> **Vad ska AI:n göra, vilken information ska den använda, vem påverkas, vilken aktör får tillgång till informationen och vilka rättsliga eller säkerhetsmässiga gränser aktiveras?**

Först därefter är det meningsfullt att låsa teknik, leverantör och arkitektur.

Det här kapitlet samlar bokens tidigare delar till en praktisk första kontroll för IT- och verksamhetsarkitekter. Syftet är inte att ersätta jurist, dataskyddsombud, säkerhetsspecialist, arkivfunktion eller upphandlingskompetens. Syftet är att hjälpa arkitekten att **identifiera rätt frågor tidigt**, innan ett tekniskt vägval har blivit dyrt att ändra.

## Användningsfallet före produkten

Två verksamheter kan använda exakt samma AI-tjänst och ändå hamna i helt olika rättsliga situationer.

Att använda en språkmodell för att:

- förbättra språket i en redan offentlig text,
- sammanfatta interna mötesanteckningar,
- analysera ett socialförsäkringsärende,
- rangordna arbetssökande,
- prioritera objekt för kontroll,
- ge rekommendationer inför myndighetsbeslut,

är inte samma sak bara för att den tekniska modellen är densamma.

Det är därför **användningsfallet** som ska bedömas först.

En bra första beskrivning behöver inte vara lång. Den bör svara på fem frågor:

1. Vad ska AI-systemet göra?
2. Vilken information ska det använda?
3. Vem eller vad påverkas av resultatet?
4. Vem tillhandahåller och driver lösningen?
5. Vad händer med resultatet efter att AI:n har producerat det?

Om dessa frågor inte går att besvara är initiativet ännu inte moget för ett arkitekturbeslut.

## Grönt, gult och rött är triage – inte juridiska besked

Bokens grönt–gult–rött-modell ska hjälpa till att prioritera arbetet.

### Grönt – normalt möjligt

Grönt betyder att den första kontrollen inte visar någon tydlig särskild riskindikator.

Det kan exempelvis vara användning där:

- informationen är offentlig eller okänslig,
- inga personuppgifter behöver behandlas,
- AI:n inte påverkar enskildas rättigheter eller beslut,
- tjänsten är godkänd och informationshanteringen är känd,
- användningen ryms inom beslutad intern styrning,
- resultatet granskas på ett sätt som är rimligt för uppgiften.

Grönt betyder inte **regel-fritt**. Vanliga krav på säkerhet, kvalitet, upphandling, dokumentation och intern styrning gäller fortfarande.

### Gult – bedöm innan ni går vidare

Gult betyder att en eller flera frågor behöver klarläggas innan arkitekturen låses eller lösningen tas i bruk.

Vanliga gula signaler är:

- personuppgifter,
- känsliga personuppgifter,
- sekretessbelagda uppgifter,
- extern AI-leverantör,
- tredjelandsåtkomst,
- intern RAG över verksamhetsinformation,
- AI som påverkar prioritering eller bedömning av människor,
- osäker klassificering enligt AI-förordningen,
- oklart ansvar för promptar, loggar och AI-output,
- sektorsspecifik reglering som ännu inte analyserats.

Gult betyder inte att användningen är förbjuden. Det betyder att **en definierad fråga måste få ett svar**.

### Rött – gå inte vidare innan begränsningen är löst

Rött betyder att det finns en tydlig blockerande fråga eller en risk för att användningen träffar ett förbud eller ett krav som måste hanteras före fortsatt design.

Exempel kan vara:

- en användning som kan omfattas av ett förbjudet AI-fall,
- behandling utan identifierat rättsligt stöd,
- sekretessbelagda uppgifter som ska lämnas till en aktör utan klarlagd rättslig grund för utlämnandet,
- säkerhetsskyddsklassificerade uppgifter i en lösning som inte är godkänd för dem,
- ett beslutssystem där obligatorisk mänsklig kontroll eller annan rättssäkerhetsmekanism saknas,
- arkivpliktig information som endast finns i en tjänst där den raderas enligt leverantörens egna standardvillkor.

Rött betyder inte nödvändigtvis **aldrig**. Det betyder **inte så här, inte ännu**.

## AI-kontrollen i tio frågor

Följande tio frågor kan användas i tidig analys, arkitekturforum, initiativberedning eller inför upphandling.

De ska besvaras för det konkreta användningsfallet – inte för AI som teknik i allmänhet.

## 1. Vad ska AI:n faktiskt göra?

Beskriv funktionen med verksamhetsspråk.

Undvik formuleringar som:

> "Vi ska införa generativ AI."

Skriv hellre:

> "Handläggare ska kunna få förslag på en sammanfattning av inkomna handlingar. Sammanfattningen ska granskas av handläggaren och får inte automatiskt tillföras beslutet."

eller:

> "Systemet ska rangordna kontrollobjekt utifrån uppgifter i myndighetens register och presentera en prioriteringslista för kontrollverksamheten."

Ju mer konkret funktionen beskrivs, desto lättare blir det att avgöra vilka regler som aktiveras.

**Grönt:** avgränsat stöd med låg påverkan.

**Gult:** funktionen analyserar, klassificerar, rangordnar eller rekommenderar.

**Rött:** funktionen kan träffa förbjuden användning eller fatta/påverka beslut utan nödvändiga skyddsmekanismer.

## 2. Vilken information ska AI:n använda?

Lista informationskategorierna innan teknik väljs.

Fråga bland annat:

- Är informationen offentlig?
- Innehåller den personuppgifter?
- Innehåller den känsliga personuppgifter?
- Omfattas den av sekretess?
- Är den säkerhetsskyddsklassificerad eller del av säkerhetskänslig verksamhet?
- Finns verksamhetsspecifika begränsningar för hur den får användas?

En viktig princip är:

> **Klassificera informationen före tjänsten.**

Om lösningen behöver fem olika informationsklasser kan det vara klokare att skapa flera tekniska zoner eller användningsmönster än att försöka få en enda AI-tjänst godkänd för allt.

**Grönt:** offentlig eller lågt skyddsvärd information som får användas för ändamålet.

**Gult:** personuppgifter, intern information eller sekretess som kräver analys.

**Rött:** information som lösningen eller leverantören inte får eller kan hantera.

## 3. Varför får just dessa uppgifter användas för detta ändamål?

Det räcker inte att myndigheten redan har tillgång till uppgifterna.

Frågan är om de får behandlas **för det nya AI-ändamålet**.

Detta är särskilt viktigt när AI används för:

- nya typer av analys,
- profilering,
- urval,
- återanvändning av stora datamängder,
- modellträning eller finjustering,
- kombination av register som tidigare hållits åtskilda.

Här kan GDPR, dataskyddslagen, brottsdatalagen eller sektorsspecifika registerförfattningar sätta ramarna.

**Arkitektens uppgift:** kunna beskriva informationsflöde och ändamål så tydligt att ansvarig juridisk funktion kan bedöma dem.

**Gul signal:** argumentet är enbart "vi har redan datan".

## 4. Vem påverkas av AI-resultatet?

Risken ökar när AI går från att hjälpa till med text till att påverka människor.

Fråga:

- Påverkas en enskilds rättighet, förmån eller skyldighet?
- Påverkar resultatet vem som granskas, prioriteras eller kontrolleras?
- Används resultatet i rekrytering eller personalledning?
- Skapas profiler, riskpoäng eller rangordningar?
- Kan ett felaktigt resultat få betydande konsekvenser?

En människa i processen gör inte automatiskt användningen lågrisk.

Om handläggaren i praktiken förväntas följa AI-rekommendationen kan AI:n ha stor faktisk påverkan även om en människa formellt fattar beslutet.

**Grönt:** AI:n påverkar främst form, språk eller intern produktivitet.

**Gult:** AI:n rekommenderar, prioriterar eller klassificerar människor eller ärenden.

**Rött:** AI:n fattar eller i praktiken styr betydande beslut utan tillräcklig rättslig och mänsklig kontroll.

## 5. Hur klassificeras användningen enligt AI-förordningen?

Kontrollera åtminstone:

- Är detta ett AI-system enligt förordningen?
- Är myndigheten deployer, provider eller båda?
- Kan användningen omfattas av ett förbud?
- Kan den vara högrisk?
- Finns transparenskrav?
- Finns krav på AI-kompetens, loggning, mänsklig kontroll eller annan styrning?

För högriskbedömningen måste **syfte och användningskontext** analyseras. Det räcker inte att känna till produktnamnet.

En generell AI-modell kan användas i både lågrisk- och högriskfall.

**Gul signal:** "leverantören säger att produkten inte är högrisk" används som enda klassificeringsunderlag.

Myndigheten behöver förstå sin egen användning och sitt eget ansvar.

## 6. Vem får tillgång till informationen – tekniskt och juridiskt?

Rita informationsflödet hela vägen.

Ta med:

- myndighetens användare,
- leverantören,
- underleverantörer,
- modellleverantör,
- driftleverantör,
- logg- och övervakningstjänster,
- supportfunktioner,
- eventuella mottagare utanför EU/EES.

Fråga sedan:

- Får uppgifterna lämnas till dessa aktörer?
- Vilka dataskyddsroller har de?
- Får leverantören använda uppgifterna för egna ändamål?
- Kan information användas för träning eller tjänsteutveckling?
- Var sker behandling och åtkomst?
- Vilka möjligheter finns att radera och exportera data?

**Grönt:** känt och kontrollerat informationsflöde med avtalad behandling.

**Gult:** komplex leverantörskedja eller tredjelandsfrågor.

**Rött:** myndigheten kan inte förklara vilka aktörer som får åtkomst till skyddsvärd information.

## 7. Vilken mänsklig kontroll behövs?

"Human in the loop" är inte tillräckligt som kravformulering.

Beskriv i stället vad människan faktiskt ska kunna göra.

Exempel:

- förstå att resultatet är AI-genererat,
- bedöma dess rimlighet,
- se relevant underlag,
- upptäcka avvikande resultat,
- frångå rekommendationen,
- korrigera fel,
- stoppa processen,
- dokumentera varför AI-resultatet följdes eller inte följdes när det är relevant.

Mänsklig kontroll måste också vara realistisk.

Om systemet producerar tusentals rekommendationer per timme och en handläggare har några sekunder per rekommendation kan den formella kontrollen vara svag i praktiken.

**Arkitekturfråga:** Har användaren information, tid, kompetens och mandat att faktiskt kontrollera AI:n?

## 8. Vad måste kunna förstås och visas i efterhand?

En AI-lösning bör utformas för efterhandskontroll från början.

Fråga vad myndigheten behöver kunna svara på senare:

- Vilket system och vilken modellversion användes?
- Vilken instruktion eller konfiguration var aktiv?
- Vilken information låg till grund för resultatet?
- Vilket resultat producerades?
- Vem tog del av resultatet?
- Påverkade det ett beslut eller en annan åtgärd?
- Vilken mänsklig kontroll gjordes?
- När skedde detta?

Allt behöver inte loggas i alla lösningar. Men den nödvändiga spårbarheten måste definieras med utgångspunkt i verksamhet, rättsliga krav och risk.

**Gul signal:** organisationen upptäcker först efter driftsättning att det inte går att rekonstruera ett viktigt AI-stött beslut.

## 9. Finns sektorsspecifik reglering?

Detta är en av bokens viktigaste kontrollfrågor.

De generella reglerna är inte hela regelverket för en myndighet.

Kontrollera om användningsfallet berör exempelvis:

- särskilda registerförfattningar,
- brottsdatalagens område,
- tull-, skatte- eller polislagstiftning,
- hälso- och sjukvårdsregler,
- socialtjänstregler,
- utbildningsregler,
- verksamhetsspecifika sekretessbestämmelser,
- särskilda befogenhetslagar.

Specialregleringen kan exempelvis begränsa:

- ändamål,
- vilka uppgifter som får kombineras,
- sökningar och urval,
- åtkomst,
- utlämnande,
- behandlingstid,
- vilka åtgärder myndigheten får vidta.

AI skapar inte nya befogenheter.

> **Om myndigheten inte får använda uppgifterna eller fatta åtgärden utan AI, får tekniken normalt inte användas som genväg runt den begränsningen.**

Bilaga B visar korta exempel från Tullverket, Polismyndigheten och Skatteverket.

## 10. Vem behöver godkänna eller medverka innan lösningen går vidare?

Den sista frågan är organisatorisk.

Identifiera vilka funktioner som faktiskt behöver vara med.

Beroende på användningsfallet kan det vara:

- verksamhetsansvarig,
- informationsägare,
- jurist,
- dataskyddsombud eller dataskyddsfunktion,
- informationssäkerhet,
- säkerhetsskydd,
- arkiv/informationsförvaltning,
- upphandling/inköp,
- HR,
- tillgänglighet eller kommunikation,
- systemägare och arkitekturforum.

Alla behöver inte delta i varje AI-initiativ.

Poängen är att **rätt kompetens ska kopplas in när en faktisk trigger finns**.

Det är bättre än två ytterligheter:

- att låta varje AI-idé gå genom en stor generell kommitté,
- eller att låta teknikteamet försöka göra alla bedömningar själva.

## Sammanfatta kontrollen i ett beslutskort

Efter de tio frågorna bör initiativet kunna sammanfattas på en sida.

Ett enkelt beslutskort kan innehålla:

| Område | Bedömning | Kort motivering | Åtgärd/ägare |
|---|---|---|---|
| Användningsfall | Grönt/Gult/Rött | Vad AI:n gör | Verksamhet |
| Information | Grönt/Gult/Rött | Informationsklasser | Informationsägare |
| Dataskydd | Grönt/Gult/Rött | Personuppgifter/ändamål | Dataskydd/juridik |
| Sekretess/säkerhet | Grönt/Gult/Rött | Skyddsvärde och extern åtkomst | Säkerhet |
| AI-förordningen | Grönt/Gult/Rött | Roll/riskklass | Juridik/AI-styrning |
| Mänsklig påverkan | Grönt/Gult/Rött | Beslut, urval, profilering | Verksamhet/juridik |
| Leverantör | Grönt/Gult/Rött | Roller, plats, underleverantörer | Inköp/IT |
| Dokumentation | Grönt/Gult/Rött | Loggar, allmän handling, arkiv | Informationsförvaltning |
| Sektorsregler | Grönt/Gult/Rött | Identifierade specialregler | Juridik/verksamhet |
| Nästa beslut | – | Gå vidare / utred / stoppa | Beslutsägare |

Det viktiga är inte färgen i sig utan att varje gul eller röd markering har:

1. en konkret fråga,
2. en ansvarig funktion,
3. ett villkor för när frågan anses löst.

## Exempel: intern AI-assistent för ärendehandläggare

Anta att en myndighet vill införa en AI-assistent som kan söka i interna styrdokument och sammanfatta information åt handläggare.

Första beskrivningen låter relativt okomplicerad.

### Steg 1 – funktion

AI:n ska söka i interna styrdokument och ge förslag på sammanfattningar.

**Bedömning: grönt/gult.**

Det är stöd, inte automatiserat beslut. Men nästa frågor avgör om risknivån stiger.

### Steg 2 – information

RAG-indexet innehåller interna styrdokument, men vissa dokument kan innehålla personuppgifter och delar av materialet omfattas av sekretess.

**Bedömning: gult.**

Informationsmängden behöver avgränsas och klassificeras.

### Steg 3 – ändamål

Materialet används för att stödja handläggning inom samma verksamhetsområde som dokumenten skapats för.

Det kan vara rimligt, men rättsligt stöd och eventuella sektorsregler behöver verifieras för personuppgifterna.

**Bedömning: gult.**

### Steg 4 – påverkan på människor

AI:n rekommenderar inte beslut utan sammanfattar styrning. Handläggaren gör själv den materiella bedömningen.

**Bedömning: grönt**, förutsatt att användningsgränsen verkligen upprätthålls.

### Steg 5 – AI-förordningen

Användningen behöver klassificeras, men inget i beskrivningen pekar direkt på ett förbjudet eller typiskt högriskfall.

**Bedömning: grönt/gult** tills klassificeringen dokumenterats.

### Steg 6 – leverantör

Tjänsten är en extern SaaS-lösning och RAG-indexet lagras hos leverantören. Leverantörens underleverantörskedja är ännu inte analyserad.

**Bedömning: gult.**

Här behöver dataskydd, sekretess, lagringsplats, åtkomst och avtalsvillkor klarläggas.

### Steg 7 – mänsklig kontroll

Svar visas som förslag med källhänvisning till de interna dokument som hämtats. Handläggaren ansvarar för att kontrollera originalkällan innan information används i ett ärende.

**Bedömning: grönt**, om användargränssnitt, utbildning och arbetssätt faktiskt stödjer detta.

### Steg 8 – spårbarhet

Systemet loggar vilken källa som hämtats, men inte hela prompten eller svaret som standard.

Här måste myndigheten bestämma vilken dokumentation som behövs för användningen och hur betydelsefullt AI-material ska föras till ordinarie ärendehantering.

**Bedömning: gult.**

### Steg 9 – sektorsregler

Verksamheten omfattas av en särskild registerförfattning.

**Bedömning: gult** tills det har verifierats att sökning, sammanställning och åtkomst ryms inom regleringen.

### Steg 10 – ansvar

Juridik, dataskydd, informationssäkerhet och informationsförvaltning får var sin tydlig fråga. Arkitekturteamet fortsätter samtidigt med de delar som inte är blockerade.

Det samlade resultatet blir inte:

> "AI är för riskabelt."

Det blir:

> **"Användningsfallet ser möjligt ut, men fyra definierade frågor måste lösas innan produktionsarkitekturen godkänns."**

Det är precis vad den gula kategorin är till för.

## Undvik kontrollmodellens vanligaste missbruk

En checklista kan skapa falsk trygghet om den används mekaniskt.

### Misstag 1: grönt på nio frågor väger upp ett rött

Det gör det inte.

En enda blockerande fråga kan räcka för att stoppa den föreslagna lösningen.

### Misstag 2: "ingen personuppgift" betyder låg risk

En AI-lösning kan vara problematisk utan personuppgifter, exempelvis på grund av:

- sekretess,
- säkerhetsskydd,
- upphovsrätt,
- offentlighet och arkiv,
- felaktig information till allmänheten,
- AI-förordningens krav.

GDPR är viktigt men är inte hela AI-styrningen.

### Misstag 3: leverantörens compliance-rapport blir myndighetens bedömning

Leverantörens dokumentation är underlag.

Myndigheten måste fortfarande bedöma sin **egen användning**, sina uppgifter och sitt ansvar.

### Misstag 4: mänsklig kontroll skrivs in som en mening i kravspecifikationen

Mänsklig kontroll behöver omsättas i:

- gränssnitt,
- behörighet,
- arbetssätt,
- utbildning,
- tid,
- dokumentation,
- möjlighet att frångå AI-resultatet.

### Misstag 5: man granskar bara produktionslösningen

Risker uppstår även i:

- proof of concept,
- testdata,
- utvecklingsmiljö,
- manuella experiment,
- pilotprojekt,
- utvärdering hos leverantör.

"Det är bara en pilot" är inte ett undantag från sekretess, dataskydd eller säkerhetsskydd.

## Arkitekturprinciper som följer av kontrollen

När kontrollmodellen används konsekvent leder den till några generella arkitekturprinciper.

### Separera användningsfall med olika risk

En enda AI-plattform behöver inte automatiskt få tillgång till all information eller användas för alla typer av beslut.

Separata zoner, modeller eller tjänster kan göra styrningen enklare.

### Minimera information innan den når AI:n

Skicka inte mer data än användningsfallet kräver.

Det kan innebära:

- filtrering,
- pseudonymisering,
- avgränsad RAG,
- borttagning av onödiga fält,
- rollbaserad åtkomst,
- separata index för olika informationsklasser.

### Gör källor synliga när resultatet ska kontrolleras

För RAG och beslutsstöd är ett svar utan källspår ofta svårare att kontrollera än ett svar som visar vilket underlag det bygger på.

### Bygg exit från början

Myndigheten bör kunna:

- exportera viktig information,
- byta leverantör,
- byta modell,
- flytta RAG-index,
- avsluta behandlingen,
- radera data hos leverantören enligt avtal och regler.

### Lägg verksamhetskritisk dokumentation i myndighetens informationsmiljö

En extern AI-tjänst bör inte vara den enda platsen där viktiga beslutsunderlag eller arkivpliktig information finns.

### Gör riskklassificeringen förändringsbar

Ett användningsfall kan byta riskprofil.

Exempel:

1. AI börjar som skrivstöd.
2. Den får tillgång till ärendedata.
3. Den börjar föreslå prioritering.
4. Rekommendationen kopplas till automatiserad handläggning.

Varje steg kan aktivera nya krav.

Därför behöver förändringshanteringen fråga:

> **Har ändringen förändrat ändamål, information, påverkan på människor, leverantörsflöde eller AI-förordningsklassificering?**

## När ska specialist kopplas in?

Det är ineffektivt att kräva full specialistgranskning av varje enkel AI-användning.

Men vissa triggers bör normalt leda till specialistbedömning.

### Juridik

Koppla in juridik när exempelvis:

- rättsligt stöd eller befogenhet är oklart,
- sektorsspecifik reglering behöver tolkas,
- AI påverkar myndighetsutövning eller enskildas rättigheter,
- AI-förordningens klassificering är osäker,
- sekretessutlämnande behöver bedömas.

### Dataskydd

Koppla in dataskyddskompetens när exempelvis:

- personuppgifter behandlas på nytt sätt,
- profilering eller omfattande analys förekommer,
- känsliga personuppgifter används,
- tredjelandsöverföring kan ske,
- konsekvensbedömning kan krävas.

### Informations- och cybersäkerhet

Koppla in säkerhetskompetens när:

- skyddsvärd information lämnar befintlig säkerhetszon,
- extern AI eller nya underleverantörer införs,
- AI integreras med verksamhetskritiska system,
- nya attackytor, prompt injection eller dataläckagerisker uppstår.

### Säkerhetsskydd

Koppla in säkerhetsskyddsfunktion tidigt om användningen berör säkerhetskänslig verksamhet eller säkerhetsskyddsklassificerade uppgifter.

### Arkiv och informationsförvaltning

Koppla in dessa funktioner när:

- AI skapar eller lagrar verksamhetsinformation,
- historik och loggar får betydelse,
- extern tjänst används som informationslager,
- bevarande, gallring eller utlämnande behöver lösas.

## Ett bra resultat är ofta villkorat – inte binärt

Arkitekturbeslut behöver inte alltid vara "godkänd" eller "avslagen".

Ett mer användbart beslut kan vara:

> **Godkänd för pilot med offentlig information, utan personuppgifter och utan koppling till myndighetsbeslut. Produktionsinförande med ärendedata kräver separat dataskydds-, sekretess- och informationssäkerhetsbedömning.**

eller:

> **Teknikvalet godkänns under förutsättning att leverantören stänger av användning av kunddata för modellträning, att EU/EES-behandling kan säkerställas och att export av loggar införs.**

Den typen av villkor gör styrningen möjliggörande utan att bli otydlig.

## Dokumentera också varför något bedömdes som grönt

Det är lätt att dokumentera problem och glömma de enkla fallen.

Men en kort motivering till varför ett användningsfall bedömts som låg risk har flera fördelar:

- samma fråga behöver inte utredas från början nästa gång,
- förändringar kan jämföras mot ursprungsbedömningen,
- verksamheten kan visa att en medveten bedömning gjorts,
- organisationen bygger upp återanvändbar erfarenhet.

Det behöver inte bli tung administration.

Ett par meningar kan räcka för ett enkelt användningsfall.

## Från enskilda projekt till återanvändbara mönster

När flera AI-initiativ har bedömts bör myndigheten börja skapa **godkända användningsmönster**.

Exempel:

### Mönster A – publikt skrivstöd

- endast offentlig eller icke skyddsvärd information,
- ingen ärendedata,
- mänsklig granskning före publicering,
- godkänd AI-tjänst,
- tydliga regler för vad som inte får matas in.

Detta kan ofta få en enkel grön väg.

### Mönster B – intern RAG

- definierade informationskällor,
- åtkomst följer källsystemens behörigheter,
- källhänvisning visas,
- personuppgifts- och sekretessbedömning är gjord,
- index och loggar omfattas av informationsförvaltningen.

Detta kan bli ett återanvändbart gult-till-grönt mönster när skyddsåtgärderna är etablerade.

### Mönster C – AI i beslut eller urval

- separat riskklassificering,
- juridisk bedömning,
- definierad mänsklig kontroll,
- dokumentation och loggning,
- bias- och kvalitetskontroller,
- uppföljning i drift.

Detta bör ha en tydligare och mer formaliserad väg.

När sådana mönster finns behöver varje nytt initiativ inte börja från noll.

Det är ett viktigt sätt att undvika att reglering blir liktydigt med långsamhet.

## Kapitlets arbetsmodell

När en ny AI-idé kommer in, gör följande:

1. **Beskriv användningsfallet.**
2. **Klassificera informationen.**
3. **Identifiera ändamål och rättsligt stöd.**
4. **Bedöm påverkan på människor.**
5. **Klassificera enligt AI-förordningen.**
6. **Kartlägg leverantör och informationsflöde.**
7. **Definiera mänsklig kontroll.**
8. **Bestäm dokumentation och spårbarhet.**
9. **Kontrollera sektorsspecifik reglering.**
10. **Fördela gula och röda frågor till rätt ansvarig.**

Därefter finns normalt tre möjliga utfall:

**Grönt:** gå vidare inom beslutad styrning.

**Gult:** gå vidare med de delar som är möjliga, men lös definierade villkor före nästa beslutspunkt.

**Rött:** stoppa den aktuella utformningen tills den blockerande frågan är löst eller välj ett annat användningsmönster.

## Det viktigaste att ta med sig

Arkitektens viktigaste bidrag är inte att kunna varje paragraf utantill.

Det är att kunna se **när arkitekturvalet aktiverar en rättslig eller organisatorisk fråga**.

En bra AI-arkitektur i en myndighet kan därför beskrivas som en lösning där:

- användningsfallet är tydligt,
- informationen används för rätt ändamål,
- rätt aktörer får tillgång till den,
- påverkan på människor är förstådd,
- AI-förordningens klassificering är gjord,
- mänsklig kontroll är verklig när den behövs,
- viktiga förlopp går att förstå i efterhand,
- sektorsregler har kontrollerats,
- och gula frågor har tydliga ägare.

Modellen ska göra det enklare att använda AI **där den är lämplig**, samtidigt som mer känsliga användningsfall identifieras innan de blivit tekniskt eller organisatoriskt inlåsta.

## Viktigaste källorna

Det här kapitlet sammanför de rättskällor och officiella vägledningar som introducerats i tidigare kapitel. De viktigaste är:

- Europaparlamentets och rådets förordning (EU) 2024/1689, AI-förordningen, i aktuell konsoliderad lydelse.
- Europaparlamentets och rådets förordning (EU) 2016/679, GDPR.
- Förvaltningslag (2017:900).
- Tryckfrihetsförordning (1949:105) och offentlighets- och sekretesslag (2009:400).
- Säkerhetsskyddslag (2018:585) och säkerhetsskyddsförordning (2021:955).
- Arkivlag (1990:782).
- Digg och IMY:s riktlinjer för generativ AI inom offentlig förvaltning.
- EU-kommissionens AI Act Service Desk och AI Act Explorer.

Se bilaga A för samlad regelverkskarta och fullständiga källhänvisningar.
