# <span class="chapter-number">Kapitel 1</span><span class="chapter-name">Kartan över styrningen</span>

När en myndighet använder AI styrs den sällan av ett enda regelverk. AI-förordningen är den mest uppenbara AI-specifika regleringen, men den ersätter inte de regler som redan gäller för offentlig verksamhet, personuppgifter, sekretess, upphandling eller säkerhet.

Arkitektens första uppgift är därför inte att memorera paragrafer, utan att förstå **vilka lager av styrning som kan bli relevanta för ett användningsfall**.

## Sex lager av styrning

En praktisk karta kan beskrivas i sex lager:

1. **Grundläggande krav på offentlig verksamhet** – regeringsformen och förvaltningslagen.
2. **AI-specifik reglering** – framför allt EU:s AI-förordning.
3. **Regler om information** – GDPR, dataskyddslagen, offentlighets- och sekretesslagen, arkivreglering och säkerhetsskydd.
4. **Regler om hur lösningen anskaffas och används** – exempelvis LOU och avtalsmässiga krav.
5. **Sektorsspecifik reglering** – särskilda register- och verksamhetsförfattningar för den aktuella myndigheten.
6. **Icke-bindande styrning** – strategier, vägledningar, policyer och interna regler.

Ett användningsfall kan beröra flera lager samtidigt. En generativ AI-tjänst för att sammanfatta ärenden kan exempelvis beröra AI-förordningen, GDPR, sekretess, myndighetens interna informationsklassning och reglerna för den externa leverantören.

## Grundlag och förvaltningsrätt ligger under AI-lagret

Förvaltningslagen uttrycker tre principer som är särskilt användbara för AI-arkitektur: **legalitet, objektivitet och proportionalitet**. En myndighet får bara vidta åtgärder som har stöd i rättsordningen, ska vara saklig och opartisk och får inte ingripa mer långtgående än vad som behövs.

Regeringsformen innehåller dessutom objektivitetsprincipen: myndigheter ska beakta allas likhet inför lagen samt iaktta saklighet och opartiskhet.

Detta är viktigt för AI eftersom tekniken inte förändrar myndighetens grundläggande ansvar. Ett AI-system kan hjälpa till att analysera, prioritera eller rekommendera, men myndigheten måste fortfarande kunna säkerställa att de grunder som används är tillåtna, relevanta och sakliga.

**Arkitekturfråga:** Om AI:n påverkar hur människor prioriteras, bedöms eller behandlas – kan vi förklara vilka faktorer som får påverka resultatet och varför?

## AI-förordningen lägger till AI-specifika krav

EU:s AI-förordning, förordning (EU) 2024/1689, bygger på risk. Den innehåller bland annat:

- krav på AI-kompetens för leverantörer och användande organisationer,
- förbjudna AI-praktiker,
- regler för högrisk-AI,
- krav på mänsklig kontroll, dokumentation, loggning, robusthet och säkerhet i relevanta fall,
- transparenskrav för vissa AI-system och AI-genererat innehåll,
- särskilda regler för generella AI-modeller.

För myndigheten är den första praktiska uppgiften därför att förstå **vilken roll organisationen har och vilken kategori det aktuella användningsfallet hamnar i**.

Det är samtidigt viktigt att inte göra AI-förordningen större än den är. Den är inte en ersättning för GDPR, förvaltningsrätt eller sekretessregler. En deployer av ett högrisk-AI-system måste till exempel följa AI-förordningens skyldigheter utan att detta ersätter andra skyldigheter enligt unionsrätt eller nationell rätt.

**Arkitekturfråga:** Är detta ett vanligt lågriskanvändningsfall, ett transparensfall, ett högriskanvändningsfall eller något som kan träffa ett förbud?

## Personuppgifter: GDPR och svensk kompletterande lag

Om AI-systemet behandlar personuppgifter blir GDPR relevant oavsett om systemet är generativt, prediktivt eller regelbaserat på något annat sätt.

GDPR:s grundprinciper omfattar bland annat laglighet, korrekthet och transparens samt att personuppgifter ska samlas in för särskilda, uttryckligt angivna och berättigade ändamål. För AI-arkitektur gör det ändamålet centralt.

Frågan blir alltså inte bara om uppgifterna redan finns hos myndigheten. Man behöver också förstå om de får användas **för den nya AI-behandlingen**.

Den svenska dataskyddslagen kompletterar GDPR och sektorsspecifika registerförfattningar kan i sin tur precisera eller begränsa behandlingen ytterligare.

**Arkitekturfråga:** Vilka personuppgifter behandlas, för vilket ändamål och med vilket rättsligt stöd?

## Offentlighet och sekretess är två olika frågor

I myndighetsmiljö måste arkitekten ofta hantera två frågor samtidigt:

1. Kan informationen bli en allmän handling?
2. Får informationen lämnas ut eller göras tillgänglig för den aktör som behandlar den?

Tryckfrihetsförordningen innehåller reglerna om allmänna handlingars offentlighet. Offentlighets- och sekretesslagen begränsar i vissa fall rätten att röja uppgifter.

Detta blir konkret när en myndighet använder en extern AI-tjänst. OSL innehåller en bestämmelse som under vissa förutsättningar gör det möjligt att lämna sekretessbelagda uppgifter till en aktör som endast tekniskt bearbetar eller lagrar dem för myndighetens räkning, men bestämmelsen är villkorad och innebär inte att varje AI-tjänst automatiskt är lämplig eller tillåten.

Att en AI-leverantör tränar egna modeller på informationen, använder den för andra ändamål eller på annat sätt gör mer än ren teknisk bearbetning kan därför vara en avgörande arkitekturfråga.

Dessutom är rättsläget kring AI och allmänna handlingar under fortsatt analys. Regeringen tillsatte den 4 september 2026 en utredning som särskilt ska analysera när upptagningar som genereras eller lagras genom AI-verktyg och externa molntjänster utgör allmänna handlingar. Det förändrar inte gällande rätt idag, men visar att området behöver följas.

**Arkitekturfråga:** Vad skickas till tjänsten, vad sparas där, vad kommer tillbaka och vilka aktörer kan få faktisk tillgång till informationen?

## Säkerhetsskydd: när konsekvensen är större än vanlig informationssäkerhet

Säkerhetsskyddslagen gäller verksamhet som är av betydelse för Sveriges säkerhet eller omfattas av ett bindande internationellt säkerhetsskyddsåtagande. Den kräver bland annat säkerhetsskyddsanalys och skyddsåtgärder för information och informationssystem som berör säkerhetskänslig verksamhet.

Detta är ett tydligt exempel på en situation där en vanlig riskbedömning för en moln- eller AI-tjänst inte räcker. Om en annan aktör genom en upphandling, ett avtal eller ett samarbete kan få tillgång till säkerhetskänslig verksamhet kan särskilda krav på säkerhetsskyddsavtal och andra åtgärder aktualiseras.

**Arkitekturfråga:** Kan AI-lösningen eller dess leverantör få tillgång till information, system eller beroenden som ingår i säkerhetskänslig verksamhet?

## Arkiv och spårbarhet

När AI används i handläggning eller andra myndighetsprocesser uppstår information som kan behöva bevaras, kunna återsökas eller omfattas av gallringsbeslut. Arkivlagen ger den generella ramen för myndigheternas arkiv, medan mer detaljerade regler kan följa av föreskrifter och myndighetens informationshantering.

Arkitekten behöver därför tänka på vilka artefakter som systemet skapar:

- promptar,
- indata,
- AI-genererade svar,
- loggar,
- modell- eller versionsinformation,
- bedömningar som görs av människor med stöd av AI.

Det betyder inte att allt alltid ska sparas. Men bevarande och gallring bör vara ett designbeslut, inte en bieffekt av vad leverantörens standardinställning råkar göra.

**Arkitekturfråga:** Vilken information behöver kunna rekonstrueras för att förstå vad som hände i efterhand?

## Anskaffning och leverantörsstyrning

När AI köps eller avropas kommer upphandlingsregler och avtal in i bilden. För arkitekten är den viktigaste poängen inte själva upphandlingsförfarandet utan att **rättsliga och säkerhetsmässiga krav måste bli tekniskt och avtalsmässigt verifierbara krav**.

Exempel:

- var data får behandlas,
- om leverantören får använda data för träning,
- vilka underleverantörer som får anlitas,
- vilka loggar som finns,
- hur data raderas,
- hur myndigheten kan byta leverantör,
- vilka säkerhetskrav som gäller,
- hur incidenter rapporteras,
- vilken dokumentation myndigheten får tillgång till.

Digg och IMY:s gemensamma riktlinjer för generativ AI inom offentlig förvaltning behandlar därför inte bara dataskydd utan också anskaffning, sekretess, informationssäkerhet, upphovsrätt, arbetsrätt, etik och ledningsansvar.

**Arkitekturfråga:** Kan vi formulera och följa upp de rättsliga förutsättningarna som konkreta krav på lösningen och leverantören?

## Några tvärgående regler får inte tappas bort

Tre regelområden behöver inte dominera boken, men kan bli avgörande i vissa AI-lösningar.

**Upphovsrätt** blir relevant när myndigheten använder skyddat material som underlag, bygger större kunskapsbaser, tränar eller finjusterar modeller eller publicerar AI-genererat material som bygger på andras verk. Den svenska upphovsrättslagen innehåller bland annat regler om text- och datautvinning. AI-förordningen innehåller dessutom upphovsrättsrelaterade skyldigheter för leverantörer av generella AI-modeller.

**Digital tillgänglighet** blir relevant när AI byggs in i webbplatser eller andra digitala tjänster för allmänheten. Lagen (2018:1937) om tillgänglighet till digital offentlig service gäller digital service som tillhandahålls av offentliga aktörer och ställer tillgänglighetskrav på de tekniska lösningar som omfattas. En AI-chatbot på myndighetens webbplats måste därför bedömas som en del av den digitala tjänsten, inte bara som en AI-komponent.

**Cybersäkerhetslagen (2025:1506)** genomför delar av NIS 2-direktivet och gäller verksamhetsutövare som omfattas av lagens tillämpningsområde. För sådana myndigheter och verksamheter kan AI-tjänster, integrationspunkter och leverantörsberoenden behöva ingå i den övergripande cybersäkerhetsstyrningen och riskhanteringen.

Dessa områden är typiska **gula kontrollfrågor**: de gör inte AI-användningen otillåten i sig, men kan skapa krav som måste byggas in i lösningen.

## Sektorsspecifik reglering kan ändra svaret

De generella regelverken är bara basen. Många myndigheter har specialregler om vilka uppgifter som får behandlas, för vilka ändamål, hur sökning och analys får ske och hur länge information får bevaras.

Det är särskilt tydligt inom exempelvis:

- brottsbekämpning,
- beskattning,
- tullverksamhet,
- folkbokföring,
- hälso- och sjukvård,
- socialtjänst.

En arkitekt bör därför aldrig avsluta regelanalysen med konstaterandet ”GDPR är hanterat”.

**Arkitekturfråga:** Finns det registerförfattning, verksamhetslag eller annan specialreglering för den process och de uppgifter som AI:n ska använda?

Bilaga B visar kort hur detta kan se ut för Tullverket, Polismyndigheten och Skatteverket.

## Strategi, vägledning och intern policy är inte samma sak som lag

Bokens sista lager är också viktigt, men har en annan rättslig karaktär.

Sveriges AI-strategi från 2026 uttrycker en tydlig ambition att offentlig förvaltning ska använda AI för högre effektivitet, kvalitet och service samtidigt som förtroende, rättssäkerhet, integritet och säkerhet värnas. Digg och IMY har samtidigt tagit fram praktiska riktlinjer för generativ AI i offentlig förvaltning.

Dessa källor är viktiga för hur myndigheter bör arbeta, men de ska inte beskrivas som om varje rekommendation vore ett uttryckligt lagkrav.

Samma sak gäller myndighetens interna AI-policy. Den kan vara bindande internt och mer restriktiv än vad lagen kräver, men den är fortfarande ett annat slags styrning än lag och förordning.

För arkitekten är skillnaden central:

| Typ av styrning | Exempel | Hur den ska läsas |
|---|---|---|
| Bindande rätt | AI-förordningen, GDPR, OSL | Sätter rättsliga krav och gränser |
| Sektorsregler | Register- och verksamhetsförfattningar | Preciserar vad som gäller i en viss verksamhet |
| Officiell vägledning | Digg/IMY, EU-kommissionen | Hjälper till att tolka och tillämpa regler |
| Strategi/policy | Sveriges AI-strategi, molnpolicy | Anger inriktning och prioriteringar |
| Intern styrning | AI-policy, informationsklassning, arkitekturprinciper | Styr den egna organisationens genomförande |

## En enkel första regelkarta

När ett nytt AI-användningsfall kommer upp kan arkitekten börja med följande kontroll:

| Fråga | Om svaret är ja – titta först på |
|---|---|
| Använder vi ett AI-system som omfattas av AI-förordningen? | AI-förordningen |
| Behandlas personuppgifter? | GDPR, dataskyddslagen och eventuell specialreglering |
| Berörs myndighetsutövning eller beslut om enskild? | Regeringsformen, förvaltningslagen, AI-förordningen och relevant specialreglering |
| Finns sekretessbelagda uppgifter? | OSL och informationssäkerhet |
| Är verksamheten säkerhetskänslig? | Säkerhetsskyddslagen och säkerhetsskyddsförordningen |
| Använder vi extern leverantör eller molntjänst? | OSL, dataskydd, säkerhet, LOU och avtal |
| Skapar AI:n handlingar, loggar eller beslutsunderlag? | TF, OSL, arkivregler och verksamhetens dokumentationskrav |
| Finns särskild lagstiftning för verksamhetsområdet? | Relevant register- och verksamhetsförfattning |

Detta är inte den fullständiga juridiska analysen. Det är **arkitektens karta över vart den fortsatta analysen behöver gå**.

## Sammanfattning

AI i en svensk myndighet styrs av flera lager samtidigt. AI-förordningen är central men aldrig ensam. Förvaltningsrätt, dataskydd, offentlighet och sekretess, säkerhetsskydd, arkiv, upphandling och sektorsspecifika regler kan vara lika avgörande för hur lösningen får utformas.

Den viktigaste vanan för en arkitekt är därför att flytta fokus från frågan:

> ”Vilka AI-regler finns?”

 till:

> **”Vilka delar av vår användning aktiverar vilka regelverk?”**

I nästa kapitel går vi djupare i AI-förordningen och den riskbaserade klassificering som avgör när särskilda AI-specifika krav träder in.

## Viktigaste källorna

- Regeringsformen (1974:152), särskilt 1 kap. 9 §: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/kungorelse-1974152-om-beslutad-ny-regeringsform_sfs-1974-152/
- Förvaltningslag (2017:900), särskilt 5 §: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/forvaltningslag-2017900_sfs-2017-900/
- Förordning (EU) 2024/1689, AI-förordningen: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- EU-kommissionens AI Act Service Desk: https://ai-act-service-desk.ec.europa.eu/
- Förordning (EU) 2016/679, GDPR, särskilt artikel 5: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- Lag (2018:218) med kompletterande bestämmelser till EU:s dataskyddsförordning: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2018218-med-kompletterande-bestammelser_sfs-2018-218/
- Tryckfrihetsförordning (1949:105), särskilt 2 kap.: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/tryckfrihetsforordning-1949105_sfs-1949-105/
- Offentlighets- och sekretesslag (2009:400): https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/offentlighets-och-sekretesslag-2009400_sfs-2009-400/
- Säkerhetsskyddslag (2018:585): https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/sakerhetsskyddslag-2018585_sfs-2018-585/
- Arkivlag (1990:782): https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/arkivlag-1990782_sfs-1990-782/
- Myndighetsförordning (2007:515): https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/myndighetsforordning-2007515_sfs-2007-515/
- Lag (2016:1145) om offentlig upphandling: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-20161145-om-offentlig-upphandling_sfs-2016-1145/
- Digg och IMY, *Riktlinjer för generativ AI inom offentlig förvaltning*: https://www.digg.se/ai-for-offentlig-forvaltning/riktlinjer-for-generativ-ai
- Regeringen, *Sveriges AI-strategi* (2026): https://www.regeringen.se/regeringens-politik/sveriges-ai-strategi/
- Regeringen, Dir. 2026:116: https://www.regeringen.se/rattsliga-dokument/kommittedirektiv/2026/09/dir.-2026116
