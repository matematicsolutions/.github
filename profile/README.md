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

## 5 konektorów MCP polskiego i unijnego prawa (MIT)

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

## Dlaczego dual-license (AGPL + MIT)

- **Powłoka Patron pod AGPL-3.0** chroni przed SaaS-ification. Kancelaria
  self-host nie ma żadnych dodatkowych obowiązków. Konkurent
  oferujący Patrona jako SaaS dla osób trzecich musi otworzyć
  modyfikacje.
- **5 konektorów MCP pod MIT** to infrastruktura do publicznych źródeł
  prawa. Im więcej osób je używa, tym bardziej stają się standardem
  zwracania cytatów z polskiego prawa.

Szczegóły:
[ADR-0002](https://github.com/matematicsolutions/patron/blob/main/governance/adr/0002-dual-license-agpl-shell-mit-connectors.md).

## Konstytucja AI

Każda kancelaria stawiająca Patrona przeczyta i podpisze
[**Konstytucję AI Patrona v1.1.0**](https://github.com/matematicsolutions/patron/blob/main/governance/CONSTITUTION.md)
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
