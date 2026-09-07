# <span class="chapter-number">Kapitel 6</span><span class="chapter-name">Offentlighet, dokumentation och spårbarhet</span>

Dataskydd, sekretess och säkerhet får ofta mest uppmärksamhet. För en svensk myndighet är ytterligare ett perspektiv centralt: **informationen måste kunna hanteras så att offentlighet, dokumentation och efterhandskontroll fungerar**.

AI förändrar inte offentlighetsprincipen. Men tekniken kan göra det svårare att se **vilken information som finns, var den finns, när den har skapats och vad som behöver bevaras**.

En praktisk princip är:

> **Designa inte bara för att AI ska kunna producera ett resultat. Designa också för att myndigheten i efterhand ska kunna förstå vilken information som användes, vad AI:n gjorde och vilket underlag som faktiskt fick betydelse.**

Det betyder inte att varje prompt, token eller teknisk mellanprodukt alltid måste sparas. Det betyder att informationshanteringen behöver analyseras med samma omsorg som själva AI-funktionen.

## Offentlighetsprincipen är utgångspunkten

Tryckfrihetsförordningen, TF, ger var och en rätt att ta del av allmänna handlingar. För att avgöra om något är en allmän handling behöver man förenklat bedöma om det är en **handling**, om den **förvaras hos myndigheten** och om den är **inkommen eller upprättad**.

Begreppet handling är teknikneutralt. Det omfattar inte bara traditionella dokument utan också upptagningar som kan läsas, avlyssnas eller uppfattas med tekniska hjälpmedel.

Det gör offentlighetsprincipen direkt relevant för moderna AI-miljöer.

Exempel på information som kan behöva bedömas är:

- promptar,
- AI-genererade svar,
- uppladdade filer,
- resultat från RAG-sökningar,
- loggar,
- klassificeringar och poäng,
- sammanställningar,
- automatiskt skapade beslutsunderlag,
- konfigurationsdata och systeminstruktioner.

Men det följer inte att allt detta automatiskt är allmänna handlingar.

**Arkitektens uppgift är därför inte att själv avgöra alla offentlighetsrättsliga gränsfall, utan att utforma lösningen så att myndigheten kan göra bedömningen.**

## Prompt och svar är inte en särskild juridisk kategori

Det är lockande att fråga: *Är en prompt en allmän handling?* eller *Är svaret från en språkmodell en allmän handling?*

Frågorna är förståeliga men för generella.

En prompt kan exempelvis vara:

- en kort instruktion som skrivs och omedelbart försvinner,
- en sparad del av en chattjänsts historik,
- en sammanställning av uppgifter ur ett ärende,
- en instruktion som ingår i ett dokumenterat arbetsflöde,
- en systemprompt som är en del av myndighetens konfiguration.

På motsvarande sätt kan ett AI-svar vara:

- tillfällig text som aldrig används,
- arbetsmaterial,
- ett underlag som tillför ett ärende sakuppgifter,
- en färdig text som expedieras,
- ett dokumenterat beslutsunderlag,
- data som lagras i en extern molntjänst.

TF:s vanliga kriterier måste därför tillämpas på den konkreta situationen.

Detta är också ett område där rättstillämpningen fortfarande behöver klarläggas. I september 2026 beslutade regeringen om en särskild utredning som bland annat ska analysera i vilken utsträckning upptagningar som genereras eller lagras genom AI-verktyg och externa molntjänster utgör allmänna handlingar. Uppdraget ska redovisas senast den 15 november 2027.

**Gul signal:** verksamheten använder AI på ett sätt som genererar eller lagrar betydande informationsmängder, men det finns ingen beslutad modell för hur dessa informationsmängder ska klassificeras och hanteras ur offentlighets- och arkivperspektiv.

## Förvarad information kan finnas utanför myndighetens egna servrar

För elektroniska upptagningar är det inte bara den fysiska lagringsplatsen som är relevant.

TF anger att en upptagning kan anses förvarad hos en myndighet om den är tillgänglig för myndigheten med tekniska hjälpmedel som myndigheten själv använder.

Det gör en enkel likställning problematisk:

> *"Informationen ligger hos leverantören, alltså finns den inte hos myndigheten."*

En SaaS- eller molntjänst kan vara tekniskt placerad hos en extern leverantör samtidigt som informationen är tillgänglig för myndigheten genom tjänsten.

För AI-arkitektur innebär det att följande behöver kartläggas:

- vilka informationsmängder myndighetens användare kan nå,
- vilka historikfunktioner tjänsten har,
- vilka sammanställningar som kan genereras,
- hur länge information är tillgänglig,
- om administratörer kan söka eller exportera den,
- vad som ligger hos underleverantörer,
- vad som endast är en teknisk mellanprodukt.

Detta är ytterligare ett skäl till att informationsarkitektur inte bör begränsas till myndighetens egna databaser.

## Inkommen och upprättad är avgörande begrepp

En handling blir inte allmän enbart för att den är elektronisk eller förvarad hos myndigheten. Den måste också vara inkommen eller upprättad enligt TF.

Det kan få praktisk betydelse i AI-flöden.

En handling som någon utanför myndigheten skickar in via en AI-baserad kanal kan exempelvis vara inkommen även om AI-systemet först analyserar eller klassificerar innehållet.

Ett AI-genererat underlag inom myndigheten kan i stället behöva bedömas utifrån reglerna om när en handling är upprättad och vad som gäller för minnesanteckningar, utkast och andra handlingar under beredningen.

Det betyder att arkitekturen bör kunna skilja mellan exempelvis:

1. information från den enskilde,
2. automatisk analys av den informationen,
3. internt arbetsmaterial,
4. underlag som tillförs ett ärende,
5. expedierat beslut eller annan färdig handling.

Om allt blandas ihop i en odifferentierad AI-chatt blir både juridisk bedömning och informationsförvaltning svårare.

## Tekniska mellanled behöver inte få samma status

TF innehåller särskilda regler för information som endast hanteras för teknisk bearbetning eller teknisk lagring.

Det är viktigt i moln- och AI-arkitektur eftersom samma informationsmängd kan passera flera tekniska komponenter utan att varje komponent automatiskt förändrar handlingens rättsliga status.

Det innebär dock inte att uttrycket **"teknisk bearbetning"** kan användas som en generell etikett på all AI-användning.

En språkmodell som sammanfattar, värderar, klassificerar eller producerar nytt innehåll kan ha en betydligt mer verksamhetsnära funktion än exempelvis ren lagring, formatkonvertering eller säkerhetskopiering.

**Arkitekturfråga:** Är komponenten faktiskt bara ett tekniskt mellanled, eller utför den en bearbetning som har självständig betydelse för myndighetens verksamhet?

Den frågan bör avgöras tillsammans med juridisk kompetens när gränsdragningen är viktig.

## Offentlighet behöver byggas in i informationshanteringen

Offentlighets- och sekretesslagen ställer krav på hur myndigheter organiserar hanteringen av allmänna handlingar. Myndigheten ska bland annat beakta möjligheten att lämna ut handlingar skyndsamt och kunna skilja allmänna handlingar från andra handlingar samtidigt som sekretesskyddet upprätthålls.

Detta är i hög grad en arkitekturfråga.

En AI-lösning bör därför inte skapa ett informationslandskap där:

- ingen vet vilka konversationer som finns,
- bara leverantören kan söka i historiken,
- information inte kan exporteras i begriplig form,
- sekretessbelagda och offentliga uppgifter inte går att skilja åt,
- viktiga resultat försvinner när en användares konto stängs,
- beslutsunderlag saknar koppling till ärendet de hör till.

En bra lösning gör i stället informationsobjektens status och livscykel tydlig.

## Diarieföring och registrering är inte samma sak som att spara allt

En vanlig överreaktion är att dra slutsatsen att all AI-interaktion måste diarieföras.

Så enkelt är det inte.

Frågan om registrering beror bland annat på om handlingen är allmän, om den omfattas av sekretess och vilka regler och rutiner som gäller för myndighetens hantering av handlingar.

Arkitektens viktigaste bidrag är därför att säkerställa att lösningen kan:

- identifiera relevant information,
- föra över information till rätt ärende- eller dokumenthanteringssystem,
- bevara nödvändiga metadata,
- tillämpa beslutade gallringsregler,
- separera verksamhetsinformation från rent teknisk telemetri.

**Grönt exempel:** AI används för språklig förbättring av ett utkast och den färdiga handlingen hanteras i myndighetens ordinarie dokumentprocess.

**Gult exempel:** handläggare använder en AI-chatt för att analysera ärendehandlingar och viktiga resonemang finns endast kvar i chattens historik.

## Arkivlagen börjar där myndighetens handlingar finns

Arkivlagen anger att en myndighets arkiv i huvudsak bildas av myndighetens allmänna handlingar och vissa handlingar som tas om hand för arkivering.

Arkiven ska bevaras, hållas ordnade och vårdas så att de tillgodoser:

- rätten att ta del av allmänna handlingar,
- förvaltningens och rättskipningens informationsbehov,
- forskningens behov.

Det innebär att AI inte får skapa en parallell informationsmiljö som hamnar utanför myndighetens informationsförvaltning.

Om en AI-tjänst producerar handlingar som ska bevaras behöver myndigheten kunna ta hand om dem på ett arkivmässigt hållbart sätt.

## Elektroniska handlingar kräver planerad förvaltning

För statliga myndigheter kompletteras arkivlagen av Riksarkivets föreskrifter. RA-FS 2009:1 innehåller föreskrifter och allmänna råd om elektroniska handlingar och är fortfarande giltig, med senare ändringar.

Föreskrifterna förstärker en viktig arkitekturprincip: elektroniska handlingar måste hanteras så att de kan **bevaras, skyddas och förstås över tid**.

I AI-system kan det bland annat innebära behov av dokumentation om:

- format,
- informationsstruktur,
- metadata,
- relationer mellan informationsobjekt,
- exportmöjligheter,
- säkerhetsåtgärder,
- förändringar över tid.

En kommersiell AI-tjänsts egen chattvy är därför sällan en tillräcklig långsiktig arkivlösning.

## Gallring måste vara beslutad – inte råka ske

AI-tjänster har ofta egna retentionstider. En leverantör kan exempelvis radera historik efter 30 eller 90 dagar.

Det kan vara bra ur dataminimerings- och säkerhetsperspektiv, men leverantörens standardinställning är inte i sig ett myndighetsbeslut om gallring.

På motsvarande sätt är obegränsad lagring inte automatiskt bättre.

Arkitekten behöver förstå:

- vilka informationsmängder som ska bevaras,
- vilka som får gallras,
- med vilket stöd gallring sker,
- när gallring ska ske,
- om information måste flyttas från AI-tjänsten före gallring,
- vem som ansvarar för att gallringen faktiskt genomförs.

**Röd signal:** verksamhetskritiska eller arkivpliktiga uppgifter finns endast i en extern AI-tjänst där de automatiskt raderas enligt leverantörens egna standardvillkor.

## Spårbarhet är mer än loggning

Det är lätt att likställa spårbarhet med att "slå på loggar".

Men en loggfil är bara värdefull om den hjälper myndigheten att förstå ett förlopp.

För en AI-lösning kan relevant spårbarhet exempelvis innebära att kunna svara på:

- vilket AI-system användes,
- vilken modell eller version användes,
- vilket underlag fick modellen tillgång till,
- vilka instruktioner styrde bearbetningen,
- vilket resultat genererades,
- om en människa granskade eller ändrade resultatet,
- vilket resultat som faktiskt användes i processen,
- när detta skedde.

Behovet varierar kraftigt.

En AI-funktion som rättar stavning behöver normalt inte samma spårbarhet som ett system som rangordnar ärenden eller producerar beslutsunderlag.

Det är därför bättre att fråga:

> **Vad behöver vi kunna bevisa eller förstå i efterhand?**

än att mekaniskt logga allt.

## Loggar kan själva bli skyddsvärda informationsmängder

Loggning skapar samtidigt nya risker.

En detaljerad AI-logg kan innehålla:

- personuppgifter,
- sekretessbelagda uppgifter,
- promptar och svar,
- interna instruktioner,
- säkerhetsinformation,
- användarbeteenden,
- tekniska identifierare.

Loggar måste därför omfattas av samma tänkande kring:

- åtkomst,
- ändamål,
- lagringstid,
- sekretess,
- säkerhet,
- arkivering och gallring.

**Gul signal:** organisationen inför omfattande AI-loggning för spårbarhet men har inte bestämt vem som får läsa loggarna eller hur länge de ska finnas kvar.

## Dokumentera det som faktiskt påverkar beslutet

I kapitel 4 behandlade vi AI som besluts- och handläggningsstöd. Där blir dokumentationsfrågan särskilt viktig.

Förvaltningslagen innehåller krav på dokumentation av uppgifter som kan ha betydelse för ett beslut och på motivering av beslut i de fall lagen kräver det.

Om AI påverkar handläggarens bedömning bör verksamheten därför kunna skilja mellan:

- AI:ns råa resultat,
- fakta eller underlag som förs in i ärendet,
- handläggarens egen bedömning,
- det slutliga beslutet och dess motivering.

Det är riskabelt att låta ett ogenomskinligt AI-resultat bli ett informellt mellanlager som påverkar beslut utan att dess betydelse går att se i efterhand.

**Arkitekturprincip:** Ju större påverkan AI har på en enskild eller på ett myndighetsbeslut, desto större anledning finns att skapa tydlig och verksamhetsmässigt begriplig spårbarhet.

## Versionsinformation kan vara nödvändig

Generativ AI förändras över tid. Samma prompt kan ge olika svar efter ett modellbyte.

Om AI används i ett viktigt arbetsflöde kan därför information om modell och konfiguration bli relevant för reproducerbarhet och efterhandskontroll.

Det behöver inte betyda att myndigheten kan återskapa varje sannolikhetsberäkning i modellen. Men den kan behöva veta exempelvis:

- leverantör,
- tjänst,
- modellfamilj eller modellversion,
- datum,
- relevanta konfigurationsinställningar,
- version av systemprompt eller beslutad instruktion,
- vilken kunskapsbas som var ansluten.

Det är särskilt viktigt om lösningen förändras ofta.

## RAG skapar flera dokumentationslager

En RAG-lösning illustrerar varför traditionellt dokumenttänkande inte alltid räcker.

Ett svar kan bygga på:

1. användarens fråga,
2. sökning i en kunskapsbas,
3. ett antal hämtade textstycken,
4. systeminstruktioner,
5. modellens generering,
6. eventuell mänsklig redigering.

För enklare kunskapsstöd kan det räcka att visa källhänvisningar för användaren.

För mer verksamhetskritisk användning kan det behövas större spårbarhet, exempelvis vilka källdokument eller versioner som låg bakom ett resultat.

Det betyder inte att varje embedding eller intern vektorsökning behöver arkiveras. Det betyder att man behöver identifiera **vilken informationsnivå som är relevant för myndighetens ansvar och efterhandskontroll**.

## En arkitekt bör definiera informationslivscykeln

För varje viktig informationskategori i en AI-lösning bör arkitekturen kunna beskriva:

| Informationskategori | Exempel | Fråga att besvara |
|---|---|---|
| Indata | prompt, fil, ärendeuppgifter | Varifrån kommer den och får den behandlas? |
| Kontext | RAG-träffar, systemprompt | Behöver vi veta vad modellen fick se? |
| Resultat | svar, klassificering, sammanfattning | Är resultatet arbetsmaterial eller del av verksamhetshandlingen? |
| Beslutsunderlag | rekommendation, poäng, urval | Hur dokumenteras påverkan på handläggningen? |
| Logg | användning, modell, tidpunkt | Vad behövs för spårbarhet och hur länge? |
| Metadata | modellversion, källor, användare | Behövs den för förståelse eller bevarande? |
| Arkivobjekt | färdig handling, beslutsunderlag | Hur förs det till ordinarie informationsförvaltning? |

Tabellen behöver anpassas till varje lösning, men den tvingar fram rätt frågor tidigt.

## Kontrollfrågor för offentlighet och spårbarhet

### 1. Informationsobjekten

- Vilka promptar, svar, filer, loggar och sammanställningar skapas?
- Vilka av dem har självständig betydelse för verksamheten?

### 2. Förvaring och åtkomst

- Var finns informationen?
- Är den tekniskt tillgänglig för myndigheten även om leverantören lagrar den?

### 3. Handlingens status

- Kan informationen vara inkommen eller upprättad?
- Finns arbetsmaterial som senare tillförs ett ärende?

### 4. Offentlighet och sekretess

- Kan allmänna handlingar identifieras och lämnas ut?
- Kan sekretesskyddad information avskiljas och prövas korrekt?

### 5. Dokumentation

- Går det att se vilket underlag som faktiskt påverkade en handläggning eller ett beslut?

### 6. Arkivering och gallring

- Vilka handlingar ska tas om hand för arkivering?
- Vilka får gallras och med vilket stöd?
- Styrs retentionen av myndigheten eller av leverantören?

### 7. Spårbarhet

- Vad måste kunna förstås i efterhand?
- Behöver modellversion, källor eller systeminstruktion dokumenteras?

### 8. Exit

- Kan relevanta handlingar och metadata exporteras innan tjänsten avslutas?

## Bedömning: grönt, gult eller rött

### Grönt – normalt möjligt

Exempel:

- AI används för ett avgränsat stöd där slutprodukten tas om hand i myndighetens ordinarie dokumentprocess,
- informationskategorier och retention är definierade,
- relevanta handlingar kan exporteras och lämnas ut,
- ingen viktig verksamhetsinformation finns enbart i leverantörens historik,
- spårbarheten står i proportion till användningens betydelse.

### Gult – utred först

Exempel:

- promptar och svar sparas i en extern tjänst,
- AI-resultat används i handläggning men kopplas inte tydligt till ärendet,
- RAG bygger på föränderliga källor utan versionshantering,
- myndigheten är osäker på vilka AI-genererade upptagningar som är allmänna handlingar,
- omfattande loggar skapas utan fastställd informationshantering.

### Rött – gå inte vidare innan frågan är löst

Exempel:

- viktig beslutsinformation kan inte rekonstrueras eller dokumenteras,
- handlingar som måste bevaras försvinner enligt leverantörens retention,
- myndigheten kan inte söka fram eller exportera information som den kan behöva lämna ut,
- lösningen gör det praktiskt omöjligt att skilja allmänna handlingar från annan information eller att upprätthålla sekretesskyddet,
- verksamheten förlitar sig på AI-resultat som påverkar beslut men saknar begriplig spårbarhet.

## Vanliga misstag

### "Allt i AI-chatten är en allmän handling"

Inte nödvändigtvis. Vanliga kriterier i TF om handling, förvaring, inkommen och upprättad måste bedömas i den konkreta situationen.

### "Inget i AI-chatten är en allmän handling"

Inte heller detta är en säker utgångspunkt. Elektronisk information kan omfattas av offentlighetsprincipen, även när den finns i externa tekniska miljöer.

### "Leverantörens 30-dagars retention betyder att informationen får gallras efter 30 dagar"

Teknisk retention och rättsligt beslutad gallring är olika saker.

### "Om vi loggar allt är vi spårbara"

En stor loggmängd utan tydligt ändamål, struktur och åtkomst kan skapa mer risk än nytta.

### "Slutbeslutet räcker alltid"

Om AI tillför sakuppgifter eller får verklig betydelse för handläggningen kan även underlag och dokumentation bli viktiga för rättssäkerhet och efterhandskontroll.


## Sammanfattning

AI skapar inte ett undantag från offentlighets- och arkivreglerna. Däremot skapar tekniken nya former av information och nya platser där information kan finnas.

De viktigaste principerna är:

- bedöm AI-information med de vanliga kriterierna för allmän handling,
- anta varken att alla promptar är allmänna handlingar eller att inga är det,
- kartlägg även information som finns i externa molntjänster,
- bygg lösningen så att allmänna handlingar kan identifieras och hanteras,
- skilj teknisk retention från rättsligt beslutad gallring,
- flytta bevarandevärd information till en kontrollerad informationsförvaltning,
- dimensionera spårbarheten efter AI-användningens konsekvenser,
- dokumentera särskilt tydligt när AI faktiskt påverkar handläggning eller beslut.

För arkitekten är kärnfrågan därför:

> **Kommer myndigheten fortfarande att kunna förstå, förvalta, hitta och vid behov lämna ut den information som AI-lösningen skapar och använder?**

Om svaret är oklart behöver informationsarkitekturen lösas innan AI-lösningen blir verksamhetskritisk.

## Viktigaste källorna

- Tryckfrihetsförordning (1949:105), särskilt 2 kap.: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/tryckfrihetsforordning-1949105_sfs-1949-105/
- Offentlighets- och sekretesslag (2009:400), särskilt 4 kap.: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/offentlighets-och-sekretesslag-2009400_sfs-2009-400/
- Arkivlag (1990:782): https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/arkivlag-1990782_sfs-1990-782/
- Riksarkivets föreskrifter och allmänna råd RA-FS 2009:1 om elektroniska handlingar, konsoliderad med senare ändringar: https://foreskrifter.riksarkivet.se/rafs/105
- Förvaltningslag (2017:900), särskilt reglerna om dokumentation och motivering: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/forvaltningslag-2017900_sfs-2017-900/
- Dir. 2026:116 – En analys av tillämpningen av offentlighetsprincipen vid myndigheters användning av artificiell intelligens: https://www.regeringen.se/rattsliga-dokument/kommittedirektiv/2026/09/dir.-2026116
