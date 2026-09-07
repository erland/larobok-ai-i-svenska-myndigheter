# <span class="chapter-number">Kapitel 4</span><span class="chapter-name">När AI påverkar människor och myndighetsbeslut</span>

När AI påverkar hur en människa bedöms, prioriteras eller får sina rättigheter och skyldigheter bestämda ökar kraven på rättslig och organisatorisk kontroll.

AI kan fortfarande användas i handläggning och beslutsstöd. Men ju närmare lösningen kommer ett beslut om en enskild, desto viktigare blir rättsligt stöd, saklighet, mänsklig kontroll, dokumentation och möjlighet till efterhandskontroll.

En praktisk princip är:

> **Ju större betydelse AI-resultatet får för en människas situation, desto mindre bör arkitekturen förlita sig på att någon "kan kontrollera" resultatet i efterhand. Kontrollen måste vara verklig, möjlig och inbyggd i processen.**

## Skilj mellan arbetsstöd, beslutsstöd och beslut

Ordet *beslutsstöd* används lätt för mycket olika lösningar. För en rättslig och arkitekturell bedömning behöver användningen beskrivas mer precist.

En förenklad skala är:

1. AI förbättrar språk eller formatering.
2. AI sammanfattar information som handläggaren själv kan kontrollera.
3. AI söker fram eller strukturerar relevant material.
4. AI rekommenderar en åtgärd eller ett beslut.
5. AI rangordnar, riskklassificerar eller flaggar personer eller ärenden.
6. AI avgör en fråga utan meningsfull mänsklig bedömning.

De första stegen kan ofta hanteras som vanligt arbetsstöd. De senare stegen kräver normalt betydligt mer analys.

Det avgörande är inte vad systemet kallas i produktbeskrivningen utan **vilken faktisk betydelse outputen får i processen**.

## Förvaltningslagen tillåter automatiserade beslut – men ställer fortfarande krav

Förvaltningslagen anger att ett beslut kan fattas av en befattningshavare, av flera gemensamt eller automatiserat. Svensk förvaltningsrätt innehåller alltså inget generellt förbud mot automatiserat beslutsfattande.

Samtidigt gäller de grundläggande kraven på myndigheten. En myndighet får bara vidta åtgärder som har stöd i rättsordningen och ska vara saklig och opartisk. Ingrepp i enskildas intressen ska dessutom vara proportionerliga.

Förvaltningslagen kräver också bland annat att:

- ärenden handläggs enkelt, snabbt och kostnadseffektivt utan att rättssäkerheten eftersätts,
- uppgifter som kan ha betydelse för ett beslut dokumenteras när det behövs,
- skriftliga beslut dokumenteras,
- beslut som påverkar någon på ett inte obetydligt sätt normalt får en klargörande motivering.

Det betyder att automatisering inte minskar myndighetens ansvar för beslutets innehåll eller för processen som leder fram till det.

**Arkitekturfråga:** Kan myndigheten förklara vilka föreskrifter och vilka omständigheter som varit avgörande för beslutet även när AI har påverkat underlaget?

## GDPR artikel 22 träffar en snävare men viktig situation

När personuppgifter behandlas behöver även GDPR analyseras. Artikel 22 ger den registrerade rätt att inte bli föremål för ett beslut som:

- bygger **enbart** på automatiserad behandling, inklusive profilering, och
- får rättsliga följder eller på liknande sätt påverkar personen betydligt.

Bestämmelsen har undantag, bland annat när behandlingen är tillåten enligt unionsrätt eller nationell rätt och det finns lämpliga skyddsåtgärder.

Två saker är särskilt viktiga för arkitekten.

### All automatisering omfattas inte av artikel 22

En AI-modell som exempelvis sorterar dokument eller ger ett förslag som en handläggare självständigt bedömer behöver inte innebära att beslutet är *enbart automatiserat*.

Men en människa i processen gör inte automatiskt behandlingen mänskligt styrd i praktiken. Om handläggaren saknar tid, information, kompetens eller faktisk möjlighet att frångå modellens resultat kan processen i realiteten bli starkt automatiserad.

### Mänsklig kontroll måste kunna påverka utfallet

Om mänsklig kontroll ska vara en skyddsåtgärd behöver den vara mer än ett knapptryck på "godkänn".

Arkitekturen bör därför stödja att handläggaren kan:

- se vilket underlag AI-resultatet bygger på,
- förstå resultatets begränsningar,
- identifiera när resultatet är osäkert eller avvikande,
- hämta fram ursprungliga källor,
- bortse från eller ändra AI-resultatet,
- dokumentera en annan bedömning utan tekniska hinder.

Detta blir också viktigt enligt AI-förordningens regler om mänsklig kontroll för högrisk-AI.

## AI-förordningen kan träffa även beslutsstöd med människa i loopen

Det är ett vanligt missförstånd att ett AI-system undgår högriskklassning bara för att en människa fattar det slutliga beslutet.

AI-förordningen klassificerar vissa användningar som högrisk utifrån **vad systemet är avsett att användas till och vilken betydelse det får**, inte bara efter om slutbeslutet formellt fattas av en människa.

Exempel i Annex III omfattar bland annat AI som används för:

- tillgång till vissa väsentliga offentliga stöd och tjänster,
- rekrytering och personalledning,
- vissa brottsbekämpande ändamål,
- migration, asyl och gränskontroll,
- rättskipning.

EU-kommissionens **utkast till riktlinjer** om högriskklassificering visar exempelvis att ett system som flaggar ansökningar om offentliga stöd för fördjupad kontroll kan vara högrisk även om en mänsklig handläggare senare gör bedömningen. Utkastet är inte bindande och de slutliga riktlinjerna är ännu inte antagna i september 2026. Flaggan kan i sig påverka granskning, fördröjning eller tillgång till förmånen.

På samma sätt kan ett AI-baserat juridiskt stöd som ger individanpassade rekommendationer till en handläggare vara högrisk om rekommendationen materiellt påverkar bedömningen av en persons rätt till en väsentlig offentlig tjänst.

**Arkitekturkonsekvens:** fråga inte bara *vem som trycker på besluts-knappen*. Fråga **hur mycket AI-resultatet styr vägen fram till beslutet**.

## Det finns också undantag för vissa begränsade stödfunktioner

Alla AI-funktioner som används i ett känsligt ärendeflöde blir inte automatiskt högrisk.

AI-förordningen innehåller undantag för vissa system som endast utför begränsade processuella eller förberedande uppgifter och inte materiellt påverkar beslutsresultatet.

EU-kommissionens **utkast till riktlinjer** innehåller bland annat exempel där översättning eller tal-till-text i ett ärende kan falla utanför högriskklassningen när funktionen är rent stödjande och handläggaren själv har möjlighet att kontrollera det relevanta innehållet.

Det gör arkitekturens avgränsning viktig. En lösning som bara sammanfattar ett dokument är något annat än en lösning som använder samma dokument för att föreslå om en person ska få eller nekas en förmån.

## Mänsklig kontroll är en funktion – inte en organisationsruta

När de relevanta högriskreglerna blir tillämpliga kräver AI-förordningen att mänsklig kontroll faktiskt kan utövas. Den som har kontrolluppgiften behöver ha tillräcklig kompetens, utbildning, befogenhet och stöd. För Annex III-fallen börjar dessa högriskregler tillämpas den 2 december 2027.

Systemet ska, i proportion till risken, göra det möjligt för personen att bland annat:

- förstå AI-systemets kapacitet och begränsningar,
- följa dess funktion,
- upptäcka fel och avvikelser,
- vara medveten om automation bias,
- tolka resultatet korrekt,
- bortse från, åsidosätta eller ändra resultatet,
- ingripa i eller stoppa systemets användning när det behövs.

Detta är en tydlig arkitekturfråga. En process är inte "human-in-the-loop" bara för att en människa finns ritad mellan två systemkomponenter.

**Gul signal:** handläggaren förväntas kontrollera AI-resultatet men saknar tillgång till källor, osäkerhetsinformation eller möjlighet att avvika från rekommendationen.

## Generativ AI kräver särskild försiktighet vid beslut

Digg och IMY rekommenderar att generativ AI används med stor försiktighet i beslutsfattande och att den inte tillåts fatta helt självständiga beslut som direkt påverkar människor.

Skälen är praktiska såväl som rättsliga. Generativa modeller kan:

- hallucinera fakta,
- utelämna relevant information,
- formulera osäkra slutsatser med hög språklig säkerhet,
- ge olika svar på liknande frågor,
- vara svåra att använda som ensam grund för en fullständig beslutsmotivering.

Det betyder inte att generativ AI saknar plats i handläggning. Den kan exempelvis vara värdefull för att sammanfatta material, hitta relevanta avsnitt eller föreslå struktur. Men ju mer outputen påverkar själva bedömningen, desto större blir behovet av kontrollerbara källor och självständig mänsklig prövning.

## Saklighet och opartiskhet måste gälla även när modellen gör urvalet

Förvaltningslagens krav på saklighet och opartiskhet försvinner inte när ett statistiskt eller AI-baserat system används som mellanled.

Problem kan uppstå om en modell exempelvis:

- tränats på historiska beslut som innehåller systematiska skevheter,
- använder variabler som fungerar som indirekta proxyer för skyddade egenskaper,
- fungerar sämre för vissa grupper,
- ger olika felmarginaler beroende på språk, namn, ålder eller andra egenskaper,
- prioriterar vissa ärenden till kontroll på ett sätt som inte kan motiveras sakligt.

Diskrimineringslagen kan dessutom bli relevant när användningen sker inom lagens tillämpningsområden, exempelvis rekrytering. Diskrimineringsombudsmannen har särskilt uppmärksammat risken för diskriminering i automatiserade urvalsprocesser och vikten av att även upphandlade lösningar granskas ur diskrimineringsperspektiv.

**Arkitekturfråga:** Har vi testat systemets resultat för olika relevanta grupper och typer av ärenden, eller bara mätt genomsnittlig träffsäkerhet?

## Felprocent är inte samma sak som acceptabel risk

Ett system med 99 procents träffsäkerhet kan låta mycket bra. Men om det används för hundratusentals ärenden kan en procent fel innebära ett stort antal felaktigt bedömda personer.

Dessutom är genomsnittlig träffsäkerhet ofta otillräcklig. Arkitekten behöver fråga:

- Vilken typ av fel gör systemet?
- Vem drabbas av falska positiva respektive falska negativa resultat?
- Är felen jämnt fördelade mellan relevanta grupper?
- Vad händer med personen när systemet har fel?
- Hur snabbt kan felet upptäckas och rättas?
- Finns en fungerande väg för mänsklig omprövning?

Riskbedömningen måste alltså koppla teknisk kvalitet till **konsekvensen av felet**.

## Profilering och riskurval kan påverka människor före ett formellt beslut

AI-användning behöver inte mynna ut i ett formellt myndighetsbeslut för att få betydelse för en person.

Ett system kan exempelvis avgöra:

- vilka ärenden som granskas först,
- vilka personer som väljs ut för kontroll,
- vilka ansökningar som får fördjupad granskning,
- vilka signaler en handläggare ser först,
- vilka ärenden som automatiskt betraktas som avvikande.

Sådana mellanbeslut kan skapa faktisk påverkan även om den slutliga rättsliga bedömningen görs senare av en människa.

För arkitekten är det därför bättre att modellera **hela beslutskedjan** än att bara dokumentera slutpunkten.

## Dokumentera det som faktiskt påverkade beslutet

Om ett AI-resultat har betydelse för ett ärende behöver myndigheten kunna bedöma hur det ska dokumenteras utifrån bland annat förvaltningsrätt, offentlighet och arkivregler.

Det kan i praktiken behövas spårbarhet för:

- vilken modell eller systemversion som användes,
- vilket underlag som gavs till systemet,
- vilket resultat systemet gav,
- vilka källor eller data resultatet byggde på,
- vilka regler eller tröskelvärden som påverkade resultatet,
- hur handläggaren använde eller frångick resultatet.

Hur mycket som behöver sparas beror på användningen och övrig reglering. Men ett system som påverkar viktiga bedömningar utan att myndigheten i efterhand kan rekonstruera vad som hände skapar en tydlig rättssäkerhetsrisk.

Detta utvecklas vidare i kapitel 6.

## En kontroll före AI-stött beslutsfattande

| Kontrollfråga | Varför den är viktig |
|---|---|
| Påverkar AI-resultatet en fysisk persons rättighet, skyldighet, prioritet eller behandling? | Avgör hur högt riskläget bör sättas |
| Är resultatet endast förberedande, eller påverkar det materiellt bedömningen? | Viktigt för AI-förordningens klassificering |
| Behandlas personuppgifter? | Aktiverar GDPR och eventuellt artikel 22 |
| Är beslutet helt automatiserat eller finns verklig mänsklig prövning? | Centralt för GDPR och rättssäkerheten |
| Kan handläggaren förstå och frångå AI-resultatet? | Avgör om mänsklig kontroll är reell |
| Kan myndigheten motivera beslutet utan att hänvisa till en ogenomskinlig modell? | Förvaltningsrättslig motivering och möjlighet till rättelse/överklagande |
| Har resultatens kvalitet testats för relevanta grupper och typer av ärenden? | Saklighet, likabehandling och diskrimineringsrisk |
| Finns möjlighet att upptäcka och korrigera fel? | Begränsar konsekvenserna av felaktiga AI-resultat |
| Finns sektorsspecifika regler för urval, profilering eller automatiserade beslut? | Generella regler kan kompletteras eller begränsas |
| Är det tydligt vad som behöver loggas och dokumenteras? | Spårbarhet och efterhandskontroll |

## Bedömning: grönt, gult eller rött

**Grönt**  
AI används för en begränsad stöduppgift där resultatet är enkelt att kontrollera och inte materiellt styr bedömningen av en person.

Exempel: AI sammanfattar ett långt underlag, men handläggaren använder och kontrollerar originalhandlingarna innan bedömningen görs.

**Gult**  
AI rekommenderar, prioriterar, klassificerar, flaggar eller på annat sätt påverkar en bedömning av människor. Användningen kan vara tillåten men behöver analyseras avseende bland annat AI-förordningen, dataskydd, rättsligt stöd, bias, mänsklig kontroll och dokumentation.

**Rött**  
AI fattar eller styr beslut med betydande konsekvenser utan att nödvändigt rättsligt stöd, fungerande mänsklig kontroll eller andra obligatoriska skyddsåtgärder är klarlagda. Detsamma gäller om användningen träffas av ett förbud i AI-förordningen.

Rött betyder inte att varje avancerat beslutsstöd är förbjudet. Det betyder att arkitekturen inte bör gå vidare som en vanlig teknisk implementation innan den rättsliga och verksamhetsmässiga ramen är klar.

## Arkitektens viktigaste uppgift

Arkitektens uppgift är inte att ensam avgöra om ett automatiserat beslut är lagligt eller om en viss AI-användning är diskriminerande.

Den viktigaste uppgiften är att göra användningen **bedömningsbar**.

Det kräver att arkitekturbeskrivningen visar:

- vilken funktion AI:n har,
- vilken information den använder,
- vad outputen betyder i processen,
- hur människor påverkas,
- vilken mänsklig kontroll som finns,
- hur resultat kan ifrågasättas och ändras,
- hur beslut och underlag dokumenteras.

När det är tydligt kan jurister, dataskyddsombud, verksamhet, säkerhetsfunktion och andra specialister göra sina respektive bedömningar. När det är otydligt riskerar både teknik- och juridikdiskussionen att fastna i abstrakta frågor om "AI" i stället för den faktiska användningen.

## Viktigaste källorna

- Förvaltningslag (2017:900), särskilt 5, 9, 27, 28, 31 och 32 §§: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/forvaltningslag-2017900_sfs-2017-900/
- Förordning (EU) 2016/679 (GDPR), särskilt artikel 22: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- AI-förordningen – AI Act Explorer, särskilt artiklarna 14 och 26 samt Annex III: https://ai-act-service-desk.ec.europa.eu/en/ai-act-explorer
- EU-kommissionen – **utkast** till riktlinjer och exempel för klassificering av högrisk-AI (ej bindande; slutliga riktlinjer ännu inte antagna per 2026-09-07): https://ai-act-service-desk.ec.europa.eu/en/guideline-explorer
- Digg/IMY – Beslut med stöd av generativ AI bör ha mänsklig kontroll: https://www.digg.se/ai-for-offentlig-forvaltning/riktlinjer-for-generativ-ai/beslut-med-stod-av-generativ-ai-bor-ha-mansklig-kontroll
- Diskrimineringsombudsmannen – exempel om AI och automatiserade urval: https://e-guide.do.se/aktiva-atgarder/exempel/rekrytering-och-befordran/artificiell-intelligens-ai
- Diskrimineringslag (2008:567): https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/diskrimineringslag-2008567_sfs-2008-567/
