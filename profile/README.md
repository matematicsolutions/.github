# MateMatic Solutions

> **Lokalne, RODO-safe narzędzia AI dla polskich kancelarii prawnych.**
> Zero-cloud self-host. Audytowalne. Bring-your-own-model.

Budujemy [**Patron**](https://github.com/matematicsolutions/patron) - agenta
AI, który nie opuszcza serwera kancelarii. Do niego dokładamy publiczne,
otwarte konektory do polskiego prawa, które każdy może wpiąć w swój
produkt.

## Patron - agent AI dla kancelarii (AGPL-3.0)

[**patron**](https://github.com/matematicsolutions/patron) - powłoka:
chat, dokumenty, audit trail z hash-chain (AI Act art. 12), Konstytucja AI
do podpisu przez kancelarię, docker-compose ready, vendor-agnostic LLM
(Gemini / Claude / Ollama lokalny).

## 6 konektorów MCP polskiego i unijnego prawa (MIT)

Każdy konektor to osobny serwer MCP (stdio transport). Wpina się przez
`mcp-servers.json` w dowolnym produkcie zgodnym z protokołem. Każde
wywołanie narzędzia zwraca `structuredContent.citations` z tytułem,
URL, sądem / aktem, datą i identyfikatorem (ELI / CELEX / sygnatura).

| Konektor | Domena | Tooly |
|---|---|---|
| [**mcp-saos**](https://github.com/matematicsolutions/mcp-saos) | Sądy powszechne, SN, TK, KIO (baza SAOS) | `search`, `get_judgment`, `search_by_case` |
| [**mcp-nsa**](https://github.com/matematicsolutions/mcp-nsa) | Sądy administracyjne (NSA + 16 WSA, CBOSA) | `search`, `get_judgment`, `search_by_case` |
| [**mcp-isap**](https://github.com/matematicsolutions/mcp-isap) | Legislacja PL (Dz.U. + M.P., Sejm ELI) | `search_acts`, `get_act`, `get_act_text` |
| [**mcp-krs**](https://github.com/matematicsolutions/mcp-krs) | Krajowy Rejestr Sądowy (MS) | `get_entity`, `get_entity_full`, `get_board` |
| [**mcp-eu-sparql**](https://github.com/matematicsolutions/mcp-eu-sparql) | Prawo UE + CJEU (EUR-Lex / Cellar) | `search_by_celex`, `search_by_date_range`, `search_cjeu` |
| [**mcp-eu-compliance**](https://github.com/matematicsolutions/mcp-eu-compliance) | Compliance UE offline - GDPR, AI Act, DORA, NIS2, eIDAS 2.0, CRA (verbatim z lokalnego SQLite FTS5) | `eu_search`, `eu_article`, `eu_compare`, `eu_check_applicability`, `eu_evidence` |

## Praxis - przewodniki dla kancelarii (CC BY-SA 4.0)

[**praxis**](https://github.com/matematicsolutions/praxis) -
otwarte przewodniki praktyczne LegalTech i AI governance dla
polskich kancelarii. Mapy, podręczniki, checklisty.

## lpm-pl - skille zarządzania portfelem spraw (Apache 2.0)

[**lpm-pl**](https://github.com/matematicsolutions/lpm-pl) - otwarte
skille AI dla polskiej kancelarii zarządzającej portfelem spraw. Trzy
MVP composable: status raporty z RAG forward-looking,
scope-change controller (wykrywa scope creep i generuje wniosek o
rozszerzenie zakresu), rejestr RAID ryzyk (Risks / Assumptions /
Issues / Decisions). Polskie realia billingu - stawki godzinowe,
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

Use case: due diligence M&A (47 umów w 2h zamiast 2 tygodni
juniora), audyt portfela kontraktów dostawczych, weryfikacja
umów powierzenia danych (art. 28 RODO), przegląd NDA przed
podpisaniem przez kancelarię. Cherry-pick patternu UX z
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
5-poziomowa mapa progresji (Eksplorator → Adopter → Konstruktor →
Architekt → Orkiestrator). Pozycja kancelarii = **minimum z
wymiarów**, nie średnia.

Plus **framework Build vs Buy** z polskim kontekstem regulacyjnym - 8
kryteriów z wagą, decision tree, porównanie 9 platform (Patron /
Harvey / CoCounsel / Lexis AI / LEX AI / Legalis AI / Claude
Enterprise / Microsoft 365 Copilot / Cline + Ollama), kalkulator TCO
3-letniego dla 1-100 osób. Cherry-pick patternu
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

Skrypty w czystym Node (zero zależności), działają lokalnie. Mapa
pseudonimizacji nigdy nie trafia do paczki (art. 4 pkt 5 RODO). Cherry-pick
patternu z [AnttiHero/lavern](https://github.com/AnttiHero/lavern)
(Apache 2.0), kod i prompty napisane od zera pod polskie realia.

## matematic-pomoc-prawna-pl - plugin dla pomocy prawnej (Apache 2.0)

[**matematic-pomoc-prawna-pl**](https://github.com/matematicsolutions/matematic-pomoc-prawna-pl) -
otwarty plugin Claude Code dla **polskiej nieodpłatnej pomocy prawnej,
klinik prawa, fundacji i NGO** prowadzących poradnictwo. Przyspiesza pracę
*wokół* poradnictwa - kwalifikacja zgłoszenia, ustrukturyzowane przyjęcie
sprawy, pierwszy szkic pisma, szkielet analizy IRAC - aby ten sam zespół
obsłużył więcej osób. Nie zastępuje prawnika; każdy wynik to szkic do
analizy i nadzoru.

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

## awesome-matematic-skills-pl - hub kuratorski skilli AI (MIT)

[**awesome-matematic-skills-pl**](https://github.com/matematicsolutions/awesome-matematic-skills-pl) -
kuratorska lista i pakiet 14 umiejętności Agent Skills dla polskiej praktyki
kancelaryjnej, in-house, naukowej i NGO. Format zgodny z
[Agent Skills](https://github.com/anthropics/skills) (Anthropic, otwarty
standard) - skille działają w Claude Code, Claude Cowork, Claude.ai,
OpenAI Codex CLI, Gemini CLI, Manus, Mistral Vibe.

Repo porządkuje sześć warstw weryfikacji outputu LLM dla pisma prawnego
w jeden łańcuch (intake → router → grounding → adversarial → fidelity →
audit-bundle), dokłada redline DOCX z natywnymi Word Track Changes,
warstwę orzecznictwa PL/UE (SAOS, EU SPARQL) oraz konwerter
PDF/Word/PPT do Markdown.

`.claude-plugin/marketplace.json` w root - jeden install w Claude Code
instaluje cały pakiet skilli. Otwarte na PR od polskich prawników,
in-house counseli i naukowców prawa - patrz CONTRIBUTING.md.

## Dlaczego dual-license (AGPL + MIT)

- **Powłoka Patron pod AGPL-3.0** chroni przed SaaS-ification. Kancelaria
  self-host nie ma żadnych dodatkowych obowiązków. Konkurent
  oferujący Patrona jako SaaS dla osób trzecich musi otworzyć
  modyfikacje.
- **6 konektorów MCP pod MIT** to infrastruktura do publicznych źródeł
  prawa. Im więcej osób je używa, tym bardziej stają się standardem
  zwracania cytatów z polskiego prawa.

Szczegóły:
[ADR-0002](https://github.com/matematicsolutions/patron/blob/main/governance/adr/0002-dual-license-agpl-shell-mit-connectors.md).

## Konstytucja AI

Każda kancelaria stawiająca Patrona przeczyta i podpisze
[**Konstytucję AI Patrona v1.2.0**](https://github.com/matematicsolutions/patron/blob/main/governance/CONSTITUTION.md)
- 9 zasad, granice produktu, role (Administrator / Operator /
Inspektor), audyt, ewolucja. Mapa do AI Act, RODO i Zasad etyki
adwokackiej / radcowskiej.

## Standard agentów AI (AGENTS.md)

Wszystkie publiczne repozytoria MateMatic mają plik [`AGENTS.md`](https://agents.md)
w root - kanoniczne instrukcje dla agentów AI zgodne ze standardem
**Linux Foundation / Agentic AI Foundation**. Czytany natywnie przez 20+
narzędzi (Cursor, Codex OpenAI, Jules Google, Devin/Windsurf Cognition,
Aider, Amp, Factory, GitHub Copilot, Claude Code).

Dlaczego: Patron i konektory MCP mają być produktem **vendor-neutral** -
żaden klient kancelarii ani deweloper nie powinien być przywiązany do
jednego narzędzia AI, żeby z nimi pracować. AGENTS.md to ten sam argument
w warstwie devexp.

## Kontakt

- **Strona**: [matematic.co](https://matematic.co)
- **Email**: [kontakt@matematic.co](mailto:kontakt@matematic.co)
- **LinkedIn**: [Wiesław Mazur](https://www.linkedin.com/in/wies%C5%82aw-mazur-535428364/)

---

*Made by Poland. For Polish law firms.
Audytowalne, lokalne, vendor-neutral.*
