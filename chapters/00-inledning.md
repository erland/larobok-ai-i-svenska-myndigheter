# Inledning

AI kan ge svenska myndigheter bättre beslutsunderlag, kortare handläggningstider, effektivare administration och bättre service. Samtidigt arbetar myndigheter i en miljö där användningen av information, automatisering och beslutsstöd redan är starkt reglerad.

Det är lätt att dra fel slutsats av detta. Den ena ytterligheten är att se AI som en vanlig teknisk komponent och anta att samma arbetssätt kan användas överallt. Den andra är att betrakta AI som så juridiskt riskfyllt att det är säkrast att avstå.

Båda leder fel.

Sveriges AI-strategi från 2026 har tvärtom en tydlig ambition att öka användningen av AI i offentlig förvaltning, samtidigt som rättssäkerhet, integritet, säker informationshantering och förtroende ska upprätthållas. Det är en bra utgångspunkt för den här boken: **AI ska användas där det skapar värde och där reglerna medger det – men med tillräcklig förståelse för när en djupare bedömning behövs.**

## Bokens fråga är inte bara ”får vi använda AI?”

För en IT- eller verksamhetsarkitekt är frågan sällan om AI i allmänhet är tillåtet. Mer användbart är att fråga:

- Vad ska AI-systemet faktiskt göra?
- Vilka människor kan påverkas?
- Vilken information ska behandlas?
- För vilket ändamål får informationen användas?
- Var och av vem sker behandlingen?
- Ska AI:n ge stöd, prioritera, rekommendera eller fatta beslut?
- Finns det sektorsspecifika regler för just den verksamheten?

En myndighet kan exempelvis få använda AI som teknik, men ändå sakna rätt att använda vissa personuppgifter för det aktuella ändamålet. Sekretess kan hindra att information lämnas till en extern tjänst. Ett användningsfall kan omfattas av särskilda krav i AI-förordningen. Och ett tekniskt möjligt beslutsstöd kan vara olämpligt om det inte går att upprätthålla saklighet, mänsklig kontroll eller tillräcklig spårbarhet.

Det betyder inte att svaret automatiskt är nej. Det betyder att **arkitekturen måste göra rätt frågor synliga tidigt**.

## Tre lägen: grönt, gult och rött

Boken använder en enkel modell för den första bedömningen.

### Grönt – normalt möjligt

Det finns inga tydliga indikatorer på särskilda rättsliga eller säkerhetsmässiga hinder. AI-användningen kan normalt hanteras inom myndighetens ordinarie styrning, informationssäkerhet och kvalitetssäkring.

Ett exempel kan vara ett godkänt internt AI-verktyg som hjälper en medarbetare att förbättra språk och struktur i en text som inte innehåller skyddsvärd information och där människan ansvarar för slutresultatet.

### Gult – bedöm innan ni går vidare

En eller flera omständigheter gör att ytterligare analys behövs. Det kan handla om personuppgifter, sekretess, extern molntjänst, profilering, verksamhetskritisk information, beslut som påverkar enskilda eller sektorsspecifika registerregler.

**Gult betyder inte förbjudet.** Det betyder att arkitekten bör identifiera frågorna och se till att rätt kompetens kopplas in innan lösningen låses.

### Rött – gå inte vidare innan frågan är klarlagd

Användningen kan träffa ett uttryckligt förbud, en särskilt reglerad högriskanvändning, säkerhetsskydd eller annan begränsning som gör att lösningen inte bör designas vidare som om den vore godkänd.

AI-förordningen innehåller exempel på AI-praktiker som är förbjudna och särskilda krav för högrisk-AI. Den innebär samtidigt inte att all AI är högrisk. Regleringen är riskbaserad, vilket är en viktig motvikt mot föreställningen att varje AI-användning kräver samma omfattande kontroll.

## Arkitektens roll

Den här boken gör inte arkitekten till jurist. Målet är i stället att arkitekten ska kunna göra en **kvalificerad första bedömning**.

Det innebär att kunna:

1. känna igen vilka regelområden som sannolikt är relevanta,
2. formulera rätt frågor innan arkitekturen låses,
3. skilja mellan en hanterbar risk och ett faktiskt rättsligt hinder,
4. veta när jurist, dataskyddsombud, informationssäkerhet, säkerhetsskydd, arkivfunktion eller annan specialist behöver involveras,
5. dokumentera de arkitekturella antaganden som den fortsatta bedömningen bygger på.

Det är särskilt viktigt eftersom AI-lösningar ofta korsar flera traditionella ansvarsområden samtidigt. Samma lösning kan beröra dataskydd, sekretess, upphandling, informationssäkerhet, offentlighet och AI-förordningen.

## Boken beskriver en generell grund – inte varje myndighets hela regelverk

Svenska myndigheter har olika uppdrag och olika speciallagstiftning. Tullverket, Polismyndigheten och Skatteverket är exempel på myndigheter där särskilda regler om personuppgiftsbehandling kan påverka hur AI-baserad analys, urval och brottsbekämpande behandling får utformas.

Därför återkommer en princip genom hela boken:

> **Kontrollera alltid om verksamheten omfattas av sektors- eller myndighetsspecifika regler utöver de generella regelverken.**

Bilaga B ger tre korta exempel på detta. Exemplen är avsiktligt inte uttömmande.

## Ett område i rörelse

AI-regleringen utvecklas snabbt. AI-förordningen tillämpas stegvis, nya EU-vägledningar publiceras och svenska regler och policyer förändras. Den 4 september 2026 beslutade regeringen exempelvis om en särskild utredning av hur offentlighetsprincipen ska tillämpas när myndigheter använder AI och externa molntjänster. Uppdraget ska redovisas senast den 15 november 2027.

Det illustrerar en viktig skillnad som boken kommer att hålla fast vid:

- **gällande rätt** beskriver vad som gäller nu,
- **officiell vägledning** hjälper till med tillämpningen,
- **strategier och policyer** anger inriktning men är inte samma sak som lag,
- **pågående utredningar** visar att en fråga kan vara under utveckling utan att ännu ha förändrat gällande rätt.

Källbilden i boken är därför daterad och ska verifieras på nytt inför publicering.

## Så använder du boken

Du behöver inte läsa varje rättskälla från början till slut. Börja med kartan i nästa kapitel. Fortsätt sedan till det område som ditt användningsfall aktiverar: AI-förordningen, informationen, påverkan på människor och beslut, extern AI eller dokumentation och offentlighet.

Mot slutet samlar vi resonemangen i en praktisk kontrollmodell och ett antal scenarier.

Målet är att du efter boken ska kunna möta en ny AI-idé med en bättre fråga än både ”varför inte?” och ”det där får vi nog inte”.

Den bättre frågan är:

> **Vad behöver vara sant för att vi ska kunna göra detta på ett tillåtet, säkert och ansvarsfullt sätt?**

## Viktigaste källorna

- Europaparlamentets och rådets förordning (EU) 2024/1689, AI-förordningen: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- EU-kommissionens AI Act Service Desk: https://ai-act-service-desk.ec.europa.eu/
- Digg och IMY, *Riktlinjer för generativ AI inom offentlig förvaltning*: https://www.digg.se/ai-for-offentlig-forvaltning/riktlinjer-for-generativ-ai
- Regeringen, *Sveriges AI-strategi* (2026): https://www.regeringen.se/regeringens-politik/sveriges-ai-strategi/
- Regeringen, Dir. 2026:116, *En analys av tillämpningen av offentlighetsprincipen vid myndigheters användning av artificiell intelligens*: https://www.regeringen.se/rattsliga-dokument/kommittedirektiv/2026/09/dir.-2026116
