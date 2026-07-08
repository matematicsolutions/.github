# MateMatic Solutions

🇬🇧 **English** · 🇵🇱 **Polski poniżej ↓** · [matematicsolutions.com/en](https://matematicsolutions.com/en/)

> **Local, GDPR-safe AI tooling for law firms.** Zero-cloud self-host. Auditable. Bring-your-own-model.

We build **[Patron](https://github.com/matematicsolutions/patron)** - an AI agent that never leaves the firm's server - plus **41 open MCP connectors** to public sources of law across 32 jurisdictions (Europe, the Americas, Asia-Pacific) and two open skill hubs for Claude Code / Cowork. European LegalTech infrastructure: the data stays where the duty of confidentiality lives. English overview: **[matematicsolutions.com/en](https://matematicsolutions.com/en/)** · full connector and skill catalogue: **[matematicsolutions.com/en/boutique](https://matematicsolutions.com/en/boutique)**.

*The catalogue below is in Polish, our home market.*

---

> **Lokalne, RODO-safe narzędzia AI dla polskich kancelarii prawnych.**
> Zero-cloud self-host. Audytowalne. Bring-your-own-model.

Budujemy [**Patron**](https://github.com/matematicsolutions/patron) - agenta
AI, który nie opuszcza serwera kancelarii. Wokół Patrona udostępniamy
publiczne, otwarte konektory MCP do prawa i dwa huby skilli Claude Code -
każdy może je wpiąć w swój produkt. Pełny katalog, aktualizowany na bieżąco:
[matematicsolutions.com/boutique](https://matematicsolutions.com/boutique).

## Patron - agent AI dla kancelarii (AGPL-3.0)

[**patron**](https://github.com/matematicsolutions/patron) - powłoka:
chat, dokumenty, audit trail z hash-chain (AI Act art. 12), Konstytucja AI
do podpisu przez kancelarię, docker-compose ready, vendor-agnostic LLM
(Gemini / Claude / Ollama lokalny).

Jedno repo, jeden [release](https://github.com/matematicsolutions/patron/releases),
siedem instalatorów Windows - **PL, EN, BR, IT, DE, ES, FR**. Każda wersja ma
domyślnie wpięty lokalny konektor prawa swojego rynku (Polska: SAOS/NSA/ISAP/KRS,
Brazylia: legis.senado.leg.br + DataJud CNJ, Włochy: Normattiva, Niemcy: NeuRIS,
Hiszpania: BOE, Francja: Legifrance/PISTE - wymaga darmowego klucza PISTE; EN to
wydanie unijne, agent po angielsku z EUR-Lex na pierwszym planie). Pozostałe
konektory dobiera się osobno z Boutique. Pobranie i szczegóły per wersja:
[matematicsolutions.com/pobierz](https://matematicsolutions.com/pobierz).

## Konektory MCP - 41 konektorów, 32 jurysdykcje, 10 mln+ dokumentów źródłowych

Każdy konektor to osobny serwer MCP (stdio transport, `uvx`/`npx` lub
sklonowanie repo). Każde wywołanie narzędzia zwraca `structuredContent.citations`
z tytułem, URL, sądem / aktem, datą i identyfikatorem (ELI / ECLI / CELEX /
sygnatura). Trzy kontynenty: Europa, Ameryki, Azja i Pacyfik. Pełny,
na bieżąco aktualizowany katalog z instrukcją instalacji każdego konektora:
[matematicsolutions.com/boutique/konektory](https://matematicsolutions.com/boutique/konektory).

### Polska (MIT / Apache-2.0)

| Konektor | Domena | Licencja |
|---|---|---|
| [**mcp-isap**](https://github.com/matematicsolutions/mcp-isap) | Legislacja PL (Dz.U. + M.P., Sejm ELI) - 96 tys.+ aktów od 1918 r. | MIT |
| [**mcp-saos**](https://github.com/matematicsolutions/mcp-saos) | Sądy powszechne i Sąd Najwyższy (baza SAOS) | MIT |
| [**mcp-nsa**](https://github.com/matematicsolutions/mcp-nsa) | Sądy administracyjne (NSA + 16 WSA, CBOSA) | MIT |
| [**mcp-krs**](https://github.com/matematicsolutions/mcp-krs) | Krajowy Rejestr Sądowy (oficjalne, darmowe API MS) | MIT |
| [**kio-orzeczenia-mcp**](https://github.com/matematicsolutions/kio-orzeczenia-mcp) | Krajowa Izba Odwoławcza, zamówienia publiczne (wczesny POC) | Apache-2.0 |

### Prawo UE - poziom unijny (MIT)

| Konektor | Domena |
|---|---|
| [**mcp-eu-sparql**](https://github.com/matematicsolutions/mcp-eu-sparql) | Legislacja UE + orzecznictwo TSUE (EUR-Lex / Cellar SPARQL) |
| [**mcp-eu-compliance**](https://github.com/matematicsolutions/mcp-eu-compliance) | Offline korpus 14 regulacji UE - RODO, AI Act, DORA, NIS2, DSA, DMA, Data Act, CRA i dalej (lokalny SQLite FTS5, verbatim, zero-LLM) |

### Linia eu-legal-mcp - Europa, kraj po kraju (Apache-2.0)

Jeden serwer MCP na krajowe źródło prawa, ten sam kontrakt cytowań co
konektory PL - `eli_uri` / ECLI, `human_readable_citation`, `source_url`.
Obejmuje kraje UE oraz trzy kraje spoza Unii, które kancelaria dotyka
w sprawach transgranicznych - Szwajcaria, Wielka Brytania, Turcja.

| Kraj | Konektor | Źródło |
|---|---|---|
| 🇦🇹 Austria | [at-eli-mcp](https://github.com/matematicsolutions/at-eli-mcp) | RIS (data.bka.gv.at) - legislacja + Judikatur |
| 🇧🇪 Belgia | [be-eli-mcp](https://github.com/matematicsolutions/be-eli-mcp) | Moniteur Belge / Belgisch Staatsblad |
| 🇨🇭 Szwajcaria | [ch-eli-mcp](https://github.com/matematicsolutions/ch-eli-mcp) | Fedlex - natywny ELI, DE/FR/IT/EN |
| 🇨🇿 Czechy | [cz-eli-mcp](https://github.com/matematicsolutions/cz-eli-mcp) | e-Sbirka (SPARQL/RDF) |
| 🇩🇪 Niemcy | [de-eli-mcp](https://github.com/matematicsolutions/de-eli-mcp) | NeuRIS (rechtsinformationen.bund.de) - legislacja + orzecznictwo |
| 🇩🇰 Dania | [dk-eli-mcp](https://github.com/matematicsolutions/dk-eli-mcp) | Retsinformation (LexDania XML) |
| 🇪🇸 Hiszpania | [es-eli-mcp](https://github.com/matematicsolutions/es-eli-mcp) | BOE (boe.es) |
| 🇫🇮 Finlandia | [fi-eli-mcp](https://github.com/matematicsolutions/fi-eli-mcp) | Finlex (Akoma Ntoso) |
| 🇫🇷 Francja | [fr-eli-mcp](https://github.com/matematicsolutions/fr-eli-mcp) | Legifrance / PISTE - LODA, kodeksy, JURI (ECLI); wymaga darmowego konta PISTE |
| 🇬🇧 Wielka Brytania | [gb-eli-mcp](https://github.com/matematicsolutions/gb-eli-mcp) | legislation.gov.uk (The National Archives, bez klucza) |
| 🇭🇷 Chorwacja | [hr-eli-mcp](https://github.com/matematicsolutions/hr-eli-mcp) | Narodne novine (JSON-LD) |
| 🇭🇺 Węgry | [hu-eli-mcp](https://github.com/matematicsolutions/hu-eli-mcp) | Nemzeti Jogszabálytár |
| 🇮🇪 Irlandia | [ie-eli-mcp](https://github.com/matematicsolutions/ie-eli-mcp) | Irish Statute Book |
| 🇮🇹 Włochy | [it-eli-mcp](https://github.com/matematicsolutions/it-eli-mcp) | Normattiva (Akoma Ntoso / URN:NIR / ELI) + Corte Costituzionale od 1956 |
| 🇱🇹 Litwa | [lt-eli-mcp](https://github.com/matematicsolutions/lt-eli-mcp) | TAR / data.gov.lt (Spinta) |
| 🇱🇺 Luksemburg | [lu-eli-mcp](https://github.com/matematicsolutions/lu-eli-mcp) | Legilux - jolux RDF + Akoma Ntoso |
| 🇲🇹 Malta | [mt-eli-mcp](https://github.com/matematicsolutions/mt-eli-mcp) | legislation.mt |
| 🇳🇱 Holandia | [nl-eli-mcp](https://github.com/matematicsolutions/nl-eli-mcp) | BWB (KOOP SRU) + Rechtspraak Open Data |
| 🇷🇴 Rumunia | [ro-eli-mcp](https://github.com/matematicsolutions/ro-eli-mcp) | Portal Legislativ (SOAP) |
| 🇸🇪 Szwecja | [se-eli-mcp](https://github.com/matematicsolutions/se-eli-mcp) | Riksdagen open-data (SFS) |
| 🇸🇰 Słowacja | [sk-eli-mcp](https://github.com/matematicsolutions/sk-eli-mcp) | Slov-Lex (static) |
| 🇹🇷 Turcja | [tr-eli-mcp](https://github.com/matematicsolutions/tr-eli-mcp) | Mevzuat Bilgi Sistemi / Bedesten (keyless), bez orzecznictwa |

Plus [**mcp-fr-legal**](https://github.com/matematicsolutions/mcp-fr-legal)
(Apache-2.0) - offline korpus pełnego tekstu francuskich kodów i ustaw
(Legifrance/DILA, lokalny SQLite FTS5, zero-LLM, bez klucza) - uzupełnia
`fr-eli-mcp`, który działa live przez PISTE i obejmuje orzecznictwo.

### Ameryki (Apache-2.0)

| Kraj | Konektor | Źródło |
|---|---|---|
| 🇧🇷 Brazylia | [br-eli-mcp](https://github.com/matematicsolutions/br-eli-mcp) | Câmara dos Deputados - projekty ustaw federalnych, bez klucza |
| 🇨🇦 Kanada | [ca-eli-mcp](https://github.com/matematicsolutions/ca-eli-mcp) | Justice Laws Website - legislacja federalna, dwujęzyczna |
| 🇨🇱 Chile | [cl-eli-mcp](https://github.com/matematicsolutions/cl-eli-mcp) | BCN Linked Open Data (SPARQL) |
| 🇨🇴 Kolumbia | [co-eli-mcp](https://github.com/matematicsolutions/co-eli-mcp) | Orzeczenia Trybunału Konstytucyjnego, bez klucza |
| 🇺🇸 USA | [us-eli-mcp](https://github.com/matematicsolutions/us-eli-mcp) | Congress.gov - projekty ustaw federalnych, darmowy klucz API |

### Azja i Pacyfik (Apache-2.0)

| Kraj | Konektor | Źródło |
|---|---|---|
| 🇦🇺 Australia | [au-eli-mcp](https://github.com/matematicsolutions/au-eli-mcp) | Federal Register of Legislation |
| 🇮🇱 Izrael | [il-eli-mcp](https://github.com/matematicsolutions/il-eli-mcp) | Knesset OData, bez klucza |
| 🇯🇵 Japonia | [jp-eli-mcp](https://github.com/matematicsolutions/jp-eli-mcp) | e-Gov - legislacja krajowa |
| 🇲🇾 Malezja | [my-eli-mcp](https://github.com/matematicsolutions/my-eli-mcp) | Laws of Malaysia Online |
| 🇸🇬 Singapur | [sg-eli-mcp](https://github.com/matematicsolutions/sg-eli-mcp) | Singapore Statutes Online |

### Wielojurysdykcyjny konektor (41. z 41)

[**legalize-mcp**](https://github.com/matematicsolutions/legalize-mcp) (Apache-2.0) -
jeden serwer MCP nad korpusem [legalize-dev](https://github.com/legalize-dev) (MIT):
legislacja 32 jurysdykcji (21 z UE) jako Markdown z identyfikatorem w stylu ELI
i historią zmian (każda reforma to commit). Nadbudowa nad otwartym korpusem,
nie osobny konektor per kraj.

### Monitoring (nie wlicza się do 41 konektorów)

[**eu-drift-watch**](https://github.com/matematicsolutions/eu-drift-watch) (Apache-2.0) -
comiesięczny automatyczny monitoring ustaw kotwicowych w 9 jurysdykcjach UE
przez konektory eu-legal-mcp - sprawdza, czy przepis nie zmienił nazwy ani
nie został uchylony u źródła. To watchdog nad flotą, nie kolejne źródło prawa.

## Skille Claude Code / Cowork - dwa huby (MIT)

| Hub | Zakres | Skille własne | Bundle |
|---|---|---|---|
| [**awesome-matematic-skills-pl**](https://github.com/matematicsolutions/awesome-matematic-skills-pl) | Polska jurysdykcja - orzecznictwo PL/UE, KRS, redline DOCX, RODO PL, cała procedura polskiej kancelarii | 41 | `fundament-weryfikacyjny`, `orzecznictwo-zrodla`, `dokumenty`, `governance-kancelarii`, `jakosc-tresci`, `ochrona-danych`, `multi-jurysdykcja-ue`, `dev-mcp` |
| [**awesome-matematic-skills-en**](https://github.com/matematicsolutions/awesome-matematic-skills-en) | Metoda niezależna od jurysdykcji - grounding, red-team review, scoring, prawo UE. Głęboka jurysdykcja PL zostaje w hubie polskim | 18 | `verification-foundation`, `content-quality`, `data-protection`, `ai-governance`, `eu-law-sources`, `eu-multi-jurisdiction` |

Oba huby linkują też do sprawdzonych, kuratorskich skilli innych zespołów
(z pełną atrybucją i oryginalną licencją) - lista rośnie, patrz README
każdego huba. Instalacja jedną komendą - `npx skills add matematicsolutions/<hub>`
(dowolny agent zgodny z Agent Skills: Cursor, Codex, Gemini CLI, Claude Code)
albo `/plugin marketplace add matematicsolutions/<hub>` natywnie w Claude Code.

## Praxis - przewodniki dla kancelarii (CC BY-SA 4.0)

[**praxis**](https://github.com/matematicsolutions/praxis) -
otwarte przewodniki praktyczne LegalTech i AI governance dla
polskich kancelarii. Mapy, podręczniki, checklisty.

## lpm-pl - skille zarządzania portfelem spraw (Apache 2.0)

[**lpm-pl**](https://github.com/matematicsolutions/lpm-pl) - otwarte
skille AI dla polskiej kancelarii zarządzającej portfelem spraw. Trzy
moduły, które można łączyć: cotygodniowe raporty z oceną czerwony /
żółty / zielony i prognozą na następny tydzień, kontroler zmian
zakresu (wykrywa scope creep i generuje wniosek o rozszerzenie
zakresu), rejestr RAID - ryzyka, założenia, problemy otwarte i
decyzje. Polskie realia billingu - stawki godzinowe,
ryczałt, success fee z ograniczeniami art. 16 KEA. Output `.docx` z
brand szablonem kancelarii. RODO-safe by default. Cherry-pick
patternu [legalopsconsulting/lpm-skills](https://github.com/legalopsconsulting/lpm-skills)
(Apache 2.0 snapshot), treść przepisana pod polski model współpracy
kancelaria-klient.

## matematic-contract-review-pl - tabular review umów (Apache 2.0)

[**matematic-contract-review-pl**](https://github.com/matematicsolutions/matematic-contract-review-pl) -
otwarty skill Claude Code do **bulk audit umów** w polskiej
kancelarii. Kopiujesz folder PDF/DOCX, definiujesz schemat kolumn
(data podpisania, strony, klauzule, prawo właściwe), skill zwraca
`.docx` z tabelą + czerwone flagi + cytaty źródłowe.

Cztery zasady konstytucyjne v1.0.0: **RODO-safe by default**
(pseudonimizacja PII PRZED każdym wywołaniem LLM, bezwzględnie),
**multi-provider LLM** (Ollama lokalny default, Claude/Gemini/GPT
opt-in - decyzja kancelarii), **cytat fizycznie obecny w tekście
źródłowym** (mechaniczna walidacja substring match, halucynacja
niemożliwa na warstwie struktury), **bez nazywania firm w summary**
("Strona A", "Dostawca", "Klient").

Use case: due diligence M&A na większym portfelu umów, audyt
portfela kontraktów dostawczych, weryfikacja umów powierzenia
danych (art. 28 RODO), przegląd NDA przed podpisaniem przez
kancelarię. Cherry-pick patternu UX z
[jamietso/Tabular_Review](https://github.com/jamietso/Tabular_Review)
(MIT), treść napisana od zera pod polskie realia z eliminacją 4
critical anti-patternów upstream (Gemini-only / API key w
frontendzie / brak persistence / Apple-only deps).

## matematic-anonimizacja-pl - anonimizacja danych "Let It Be" (Apache 2.0)

[**matematic-anonimizacja-pl**](https://github.com/matematicsolutions/matematic-anonimizacja-pl) -
samodzielny silnik **anonimizacji i pseudonimizacji polskich danych
osobowych** w tekście. Zero zależności, offline, deterministyczny -
treść nie opuszcza maszyny. Wykrywa PESEL/NIP/REGON/KRS, IBAN/NRB
(checksuma mod-97), dowód osobisty, e-mail, telefon, imiona i nazwiska
(gazetteer imion), firmy z formą prawną i adresy.

Dwa tryby RODO: **anonimizacja nieodwracalna** (mapa nie powstaje, motyw
26 - dane poza RODO) oraz **pseudonimizacja odwracalna** (mapa
token-oryginał, art. 4 pkt 5 - do pracy z LLM i odzyskania wyniku).
Bramka "no PII leaves" przerywa operację, gdy oryginał przetrwał
podmianę. Trzy interfejsy: skill Claude Code, CLI, biblioteka.

To wydzielona, osobno testowana warstwa pseudonimizacji, której wymaga
`matematic-contract-review-pl` (PII PRZED każdym wywołaniem LLM).
Logika polskich identyfikatorów pochodzi z własnej biblioteki
pl-entities (Patron); wzorce operacyjne (TTL na mapy, audit log dla
Inspektora, szyfrowane archiwum AES-GCM) to cherry-pick patternu z
[gregmos/PII-Shield](https://github.com/gregmos/PII-Shield) (MIT).

## matematic-readiness - audyt gotowości kancelarii do AI (CC BY-SA 4.0)

[**matematic-readiness**](https://github.com/matematicsolutions/matematic-readiness) -
otwarty pakiet do oceny gdzie polska kancelaria jest na drodze do
bezpiecznego wdrożenia AI. **30 pytań w 5 polskich wymiarach** (RODO
compliance / tajemnica zawodowa / AI Act gotowość / kompetencje
zespołu / architektura techniczna), scoring 1-5 z uzasadnieniem,
5-poziomowa mapa progresji (Poznający → Próbujący → Wdrażający →
Integrator → Architekt). Pozycja kancelarii = **minimum z
wymiarów**, nie średnia.

Plus **framework Build vs Buy** z polskim kontekstem regulacyjnym - 8
kryteriów z wagą, decision tree i porównanie 9 platform - lokalnych
(Patron, LEX AI, Legalis AI), zachodnich agentów prawnych (Harvey,
CoCounsel, Lexis AI) i platform ogólnego przeznaczenia (Claude
Enterprise, Microsoft 365 Copilot, Cline + Ollama). Plus kalkulator
TCO 3-letniego dla 1-100 osób. Cherry-pick patternu
[OneC0de/legal-ai-architect-toolkit](https://github.com/OneC0de/legal-ai-architect-toolkit)
(MIT), wszystkie treści napisane od zera pod polskie ustawy
zawodowe (art. 6 PoA, art. 3 URP), AI Act (CELEX 32024R1689), RODO
oraz DPF.

## matematic-legal-verify-pl - weryfikacja outputu AI prawnego (Apache 2.0)

[**matematic-legal-verify-pl**](https://github.com/matematicsolutions/matematic-legal-verify-pl) -
sześć composable skilli Claude Code, które pilnują, żeby praca z AI była
rzetelna od wejścia do wyjścia. Nie piszą pism - sprawdzają wejście i wynik,
zanim cokolwiek pójdzie do klienta lub sądu.

**intake-sufficiency-pl** - ocena wejścia: czy zlecenie ma dość kontekstu
(cel / zakres / podmiot / fakty / ograniczenia), by zacząć. Wypisuje luki,
generuje pytania uzupełniające do klienta, składa szkielet karty zlecenia.
**legal-request-router-pl** - klasyfikator zapytania: ocenia złożoność i
ryzyko, dobiera proporcjonalną ścieżkę kontroli wyniku (zwykła odpowiedź /
grounding / debata / paczka audytowa). Lustro intake - chroni przed paleniem
tokenów na rutynie i przed przepuszczeniem spraw wysokiej stawki.
**citation-grounding-pl** - mechaniczny weryfikator cytatu: string-matchem
sprawdza, czy każdy cytat z orzeczenia / ustawy / umowy faktycznie istnieje
w źródle (normalizacja cudzysłowów i myślników, obsługa luk `[...]`). Brak
trafienia = potencjalna halucynacja = blokada publikacji. Spina się z
konektorami mcp-saos / mcp-nsa / mcp-eu-sparql (pobranie źródła).
**adversarial-legal-review-pl** - kontradyktoryjny stress-test pisma
wysokiej stawki (builder buduje tezę, attacker atakuje kontr-orzecznictwem,
synthesizer godzi, verifier robi kontrolę 10-punktową), z bramką kosztu -
tylko dla high-stakes, nie dla rutyny. **deliverable-fidelity-pl** -
weryfikator wierności: czy finalny dokument oddaje ustalenia analizy (żadna
flaga RED nie wypadła z podsumowania); mechaniczny check + kontrola wyrywkowa
LLM, pominięte RED = blokada. **legal-ai-audit-bundle** - paczka
audytowa: deliverable + ślad rozumowania + raport cytatów + log kosztu w
jednym folderze z manifestem i hashami SHA256, artefakt zgodny z AI Act
art. 12 (rejestry), art. 14 (nadzór), art. 50 (poinformowanie o AI).

Skrypty wyłącznie na Node, bez zewnętrznych zależności, działają lokalnie. Mapa
pseudonimizacji nigdy nie trafia do paczki (art. 4 pkt 5 RODO). Cherry-pick
patternu z [AnttiHero/lavern](https://github.com/AnttiHero/lavern)
(Apache 2.0), kod i prompty napisane od zera pod polskie realia.

## matematic-pomoc-prawna-pl - plugin dla pomocy prawnej (Apache 2.0)

[**matematic-pomoc-prawna-pl**](https://github.com/matematicsolutions/matematic-pomoc-prawna-pl) -
otwarty plugin Claude Code dla **polskiej nieodpłatnej pomocy prawnej,
klinik prawa, fundacji i NGO** prowadzących poradnictwo. Przyspiesza
pracę pomocniczą wokół poradnictwa - kwalifikacja zgłoszenia,
ustrukturyzowane przyjęcie sprawy, pierwszy szkic pisma, szkielet
analizy IRAC - aby ten sam zespół obsłużył więcej osób. Nie zastępuje
prawnika; każdy wynik to szkic do analizy i nadzoru.

Kręgosłup nadzoru i weryfikacji: **7 artykułów konstytucji projektu**,
polskie markery pewności (`[DO WERYFIKACJI]`, `[POTRZEBNE BADANIE]`,
`[ANALIZA PRAWNIKA]`, `[OGRANICZENIE RODO/AI ACT]`), **trzy konfigurowalne
modele nadzoru koordynatora**, ślad audytowy AI Act art. 12. Kluczowa
zasada: **skille nie zaszywają prawa** - czytają konfigurację organizacji
ustawioną przy starcie, więc plugin działa wg aktualnych przepisów i
realiów konkretnej organizacji, nie wg reguł wbudowanych w kod.

**MateMatic dostarcza narzędzie, nie usługę prawną** - nie świadczy pomocy
prawnej, nie jest kancelarią, nie udziela porad. Odpowiedzialność
merytoryczna i nadzór są po stronie organizacji i jej uprawnionych
prawników. Wzorzec architektoniczny studiowany z
[anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal)
(Apache-2.0) i [lawdroidAI/legal-aid-plugin](https://github.com/lawdroidAI/legal-aid-plugin)
(Apache-2.0), cała treść polska napisana od zera. Wydane otwarcie, aby każdy
punkt npp, klinika prawa, fundacja i NGO mogły wdrożyć je za darmo.

## Dlaczego dual-license (AGPL + MIT/Apache-2.0)

- **Powłoka Patron pod AGPL-3.0** chroni przed SaaS-ification. Kancelaria
  self-host nie ma żadnych dodatkowych obowiązków. Konkurent
  oferujący Patrona jako SaaS dla osób trzecich musi otworzyć
  modyfikacje.
- **Konektory MCP pod MIT lub Apache-2.0** to infrastruktura do publicznych
  źródeł prawa - konektory polskie i unijnego poziomu na MIT, linia
  eu-legal-mcp (Europa, Ameryki, Azja i Pacyfik) na Apache-2.0. Im więcej
  osób ich używa, tym bardziej stają się standardem zwracania cytatów
  z prawa poszczególnych jurysdykcji.

Szczegóły:
[ADR-0002](https://github.com/matematicsolutions/patron/blob/main/governance/adr/0002-dual-license-agpl-shell-mit-connectors.md).

## Konstytucja AI

Każda kancelaria stawiająca Patrona przeczyta i podpisze
[**Konstytucję AI Patrona v1.2.0**](https://github.com/matematicsolutions/patron/blob/main/governance/CONSTITUTION.md)
- 9 zasad, granice produktu, role (Administrator / Operator /
Inspektor), audyt, ewolucja. Mapa do AI Act, RODO i Zasad etyki
adwokackiej / radcowskiej.

## Standard agentów AI (AGENTS.md / CONSTITUTION.md)

Patron, oba huby skilli i konektory pierwszej fali (PL + poziom UE) mają
plik [`AGENTS.md`](https://agents.md) w root - kanoniczne instrukcje dla
agentów AI zgodne ze standardem **Linux Foundation / Agentic AI Foundation**.
Czytany natywnie przez 20+ narzędzi (Cursor, Codex OpenAI, Jules Google,
Devin/Windsurf Cognition, Aider, Amp, Factory, GitHub Copilot, Claude Code).

Linia eu-legal-mcp (konektory generowane własnym pipeline'em od lipca 2026)
ma ten sam cel w dwóch osobnych plikach zamiast jednego: `CONSTITUTION.md`
(granice i zasady konektora) i `DISCOVERY.md` (źródło, licencja,
ograniczenia pokrycia). Inny format, ta sama funkcja - agent czyta zasady
repo, zanim zacznie na nim pracować.

Dlaczego: Patron i konektory MCP mają być produktem **vendor-neutral** -
żaden klient kancelarii ani deweloper nie powinien być przywiązany do
jednego narzędzia AI, żeby z nimi pracować. To ten sam argument w warstwie
devexp.

## Kontakt

- **Strona**: [matematicsolutions.com](https://matematicsolutions.com)
- **Katalog**: [matematicsolutions.com/boutique](https://matematicsolutions.com/boutique)
- **Email**: [kontakt@matematic.co](mailto:kontakt@matematic.co)
- **LinkedIn**: [Wiesław Mazur](https://www.linkedin.com/in/wies%C5%82aw-mazur-535428364/)

---

*Z Polski. Dla polskich kancelarii. Audytowalne, lokalne, vendor-neutral.*
