# Bilaga A. Regelverkskarta och källor

Den här bilagan är en orienteringskarta. Den visar vilka generella rätts- och styrkällor som oftast behöver kontrolleras när en svensk myndighet planerar eller använder AI.

Kartan är **inte en uttömmande rättsutredning**. Vilka regler som faktiskt gäller avgörs av det konkreta användningsfallet, myndighetens uppdrag, vilka uppgifter som behandlas och vilken sektorsspecifik reglering som finns.

Källorna nedan är verifierade per **7 september 2026**.

## A.1 Bindande rätt

| Källa | Vad den främst reglerar | När den blir särskilt viktig för AI |
|---|---|---|
| **EU:s AI-förordning, förordning (EU) 2024/1689, i gällande lydelse** | AI-specifika krav, förbjudna användningar, högrisk-AI, transparens, roller och skyldigheter | Vid all klassificering av ett AI-användningsfall; särskilt när AI påverkar människor, beslut eller grundläggande rättigheter |
| **EU:s dataskyddsförordning (GDPR), förordning (EU) 2016/679** | Behandling av personuppgifter | När personuppgifter förekommer i promptar, träningsdata, RAG, loggar, output eller andra delar av lösningen |
| **Lag (2018:218) med kompletterande bestämmelser till EU:s dataskyddsförordning** | Svenska kompletteringar till GDPR | Tillsammans med GDPR vid personuppgiftsbehandling i svensk verksamhet |
| **Regeringsformen (1974:152)** | Grundläggande krav på offentlig makt, legalitet, saklighet, likabehandling och skydd för individen | När AI påverkar myndighetsutövning, urval, prioritering eller behandling av människor |
| **Förvaltningslag (2017:900)** | Handläggning, service, legalitet, objektivitet, proportionalitet, dokumentation, motivering och beslut | När AI används i ärendehandläggning eller som stöd för bedömning och beslut |
| **Tryckfrihetsförordningen (1949:105), särskilt 2 kap.** | Allmänna handlingars offentlighet | När promptar, svar, loggar, RAG-material eller annan AI-relaterad information kan bli allmän handling |
| **Offentlighets- och sekretesslag (2009:400)** | Sekretess och hantering av skyddade uppgifter | Innan sekretessreglerade uppgifter lämnas till en AI-tjänst, leverantör eller annan aktör |
| **Arkivlag (1990:782)** | Myndigheters arkiv, bevarande, ordnande och gallring | När AI skapar eller bearbetar information som behöver bevaras, spåras eller gallras korrekt |
| **Säkerhetsskyddslag (2018:585)** och **säkerhetsskyddsförordning (2021:955)** | Skydd av säkerhetskänslig verksamhet och säkerhetsskyddsklassificerade uppgifter | När AI-lösningen, leverantören, driftsmiljön eller informationsmängden berör Sveriges säkerhet |
| **Lag (2016:1145) om offentlig upphandling** | Upphandling och anskaffning | När AI-tjänster, modeller, plattformar eller konsultstöd anskaffas externt |
| **Diskrimineringslag (2008:567)** | Förbud mot diskriminering och krav på lika rättigheter och möjligheter | När AI gör urval, rangordnar, rekommenderar eller påverkar bedömningar av personer |
| **Brottsdatalag (2018:1177)** | Personuppgiftsbehandling för brottsbekämpande ändamål | För behöriga myndigheter när AI används för att förebygga, upptäcka, utreda eller lagföra brott |
| **Lag (1960:729) om upphovsrätt till litterära och konstnärliga verk** | Upphovsrätt, inskränkningar och bland annat text- och datautvinning | När AI använder skyddat material i RAG, analys, träning eller finjustering eller när AI-genererat material publiceras |
| **Lag (2018:1937) om tillgänglighet till digital offentlig service** | Tillgänglighet i offentlig digital service | När AI byggs in i webbplatser, appar eller andra digitala tjänster för allmänheten |
| **Cybersäkerhetslag (2025:1506)** | Riskhantering, säkerhetsåtgärder och incidenthantering för verksamhetsutövare inom lagens tillämpningsområde | När en myndighet eller verksamhet omfattas av lagen och AI blir en del av dess informationssystem, tjänster eller leverantörskedja |

## A.2 Officiell vägledning och nationell inriktning

Dessa källor är inte likställda med lag eller förordning, men de är viktiga för att förstå hur reglerna kan omsättas i offentlig verksamhet.

| Källa | Typ | Betydelse för arkitekten |
|---|---|---|
| **Digg/IMY – Riktlinjer för generativ AI inom offentlig förvaltning** | Officiell myndighetsvägledning | Praktiskt stöd om bland annat ledning, dataskydd, sekretess, informationssäkerhet, anskaffning, upphovsrätt och mänsklig kontroll |
| **EU-kommissionens AI Act Service Desk och AI Act Explorer** | Officiellt EU-stöd | Praktiskt stöd för att läsa AI-förordningen, klassificera användningar och hitta artiklar, bilagor och vägledningar |
| **Sveriges AI-strategi (2026)** | Regeringsstrategi | Visar nationell inriktning mot ökad och ansvarsfull AI-användning |
| **Sveriges digitaliseringsstrategi 2025–2030** | Regeringsstrategi | Placerar AI, data och säkerhet i ett bredare perspektiv för offentlig förvaltning |
| **En molnpolicy för Sverige (2026)** | Regeringspolicy | Relevant vid val av moln- och AI-tjänster, särskilt för kontroll över data, beroenden och digital suveränitet |
| **IMY:s vägledningar om GDPR, DPIA och tredjelandsöverföring** | Tillsynsmyndighetsvägledning | Hjälper till att bedöma personuppgiftsroller, risker och överföringar utanför EU/EES |
| **Riksarkivets föreskrifter om elektroniska handlingar** | Föreskrifter och allmänna råd | Viktiga för bevarande, dokumentation och hantering av elektronisk information |

## A.3 Sektorsspecifik reglering

Den generella regelverkskartan räcker inte alltid. Många myndigheter har särskilda lagar om exempelvis:

- vilka personuppgifter som får behandlas,
- vilka ändamål behandlingen får ha,
- sökning och urval,
- vilka uppgifter som får göras gemensamt tillgängliga,
- utlämnande och åtkomst,
- längsta behandlingstid,
- särskilda befogenheter eller verksamhetsförutsättningar.

Det innebär att en lösning kan vara tekniskt identisk i två myndigheter men ändå få olika rättslig bedömning.

**Arkitektens kontrollfråga:**

> Finns det registerförfattning, verksamhetslag eller annan specialreglering som begränsar vilka uppgifter vi får använda, för vilket ändamål och på vilket sätt?

Bilaga B visar tre konkreta exempel.

## A.4 Primärkällor

### EU

- AI-förordningen: https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng
- AI Act Explorer: https://ai-act-service-desk.ec.europa.eu/en/ai-act-explorer
- GDPR: https://eur-lex.europa.eu/eli/reg/2016/679/oj

### Svensk rätt

- Regeringsformen: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/kungorelse-1974152-om-beslutad-ny-regeringsform_sfs-1974-152/
- Förvaltningslagen: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/forvaltningslag-2017900_sfs-2017-900/
- Tryckfrihetsförordningen: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/tryckfrihetsforordning-1949105_sfs-1949-105/
- Offentlighets- och sekretesslagen: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/offentlighets-och-sekretesslag-2009400_sfs-2009-400/
- Arkivlagen: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/arkivlag-1990782_sfs-1990-782/
- Dataskyddslagen: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2018218-med-kompletterande-bestammelser_sfs-2018-218/
- Säkerhetsskyddslagen: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/sakerhetsskyddslag-2018585_sfs-2018-585/
- Säkerhetsskyddsförordningen: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/sakerhetsskyddsforordning-2021955_sfs-2021-955/
- LOU: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-20161145-om-offentlig-upphandling_sfs-2016-1145/
- Diskrimineringslagen: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/diskrimineringslag-2008567_sfs-2008-567/
- Brottsdatalagen: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/brottsdatalag-20181177_sfs-2018-1177/
- Upphovsrättslagen: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-1960729-om-upphovsratt-till-litterara-och_sfs-1960-729/
- Lagen om tillgänglighet till digital offentlig service: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-20181937-om-tillganglighet-till-digital_sfs-2018-1937/
- Cybersäkerhetslagen: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/cybersakerhetslag-20251506_sfs-2025-1506/

### Officiell vägledning och strategi

- Digg/IMY – AI för offentlig förvaltning: https://www.digg.se/ai
- Digg/IMY – Riktlinjer för generativ AI: https://www.digg.se/ai-for-offentlig-forvaltning/riktlinjer-for-generativ-ai
- Sveriges AI-strategi: https://www.regeringen.se/informationsmaterial/2026/02/sveriges-ai-strategi/
- Sveriges digitaliseringsstrategi 2025–2030: https://www.regeringen.se/regeringens-politik/digitaliseringsstrategin-2025-2030/
- En molnpolicy för Sverige: https://www.regeringen.se/informationsmaterial/2026/05/en-molnpolicy-for-sverige--for-okad-sakerhet-effektivitet-och-innovation-i-den-offentliga-forvaltningen/

## A.5 Läs källorna i rätt ordning

När två källor verkar säga olika saker bör man inte väga dem som likvärdiga. En praktisk ordning är:

1. **bindande EU-rätt, grundlag, lag och förordning,**
2. **myndighetsföreskrifter inom rätt område,**
3. **officiell vägledning och praxis,**
4. **strategier och policyer,**
5. **intern styrning.**

Intern policy kan ställa högre interna krav på användning av en viss AI-tjänst, men kan inte göra en rättsligt förbjuden behandling tillåten. På motsvarande sätt innebär en positiv nationell AI-strategi inte att de bindande reglerna sätts åt sidan.
