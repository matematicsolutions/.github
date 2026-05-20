# MateMatic Solutions

> **Lokalne, RODO-safe narzędzia AI dla polskich kancelarii prawnych.**
> Zero-cloud self-host. Audytowalne. Bring-your-own-model.

Budujemy [**Patron**](https://github.com/matematicsolutions/patron) — agenta
AI, który nie opuszcza serwera kancelarii. Do niego dokładamy publiczne,
otwarte konektory do polskiego prawa, które każdy może wpiąć w swój
produkt.

## Patron — agent AI dla kancelarii (AGPL-3.0)

[**patron**](https://github.com/matematicsolutions/patron) — powłoka:
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

## Praxis — przewodniki dla kancelarii (CC BY-SA 4.0)

[**praxis**](https://github.com/matematicsolutions/praxis) —
otwarte przewodniki praktyczne LegalTech i AI governance dla
polskich kancelarii. Mapy, podręczniki, checklisty.

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
— 9 zasad, granice produktu, role (Administrator / Operator /
Inspektor), audyt, ewolucja. Mapa do AI Act, RODO i Zasad etyki
adwokackiej / radcowskiej.

## Kontakt

- **Strona**: [matematic.co](https://matematic.co)
- **Email**: [kontakt@matematic.co](mailto:kontakt@matematic.co)
- **LinkedIn**: [Wiesław Mazur](https://www.linkedin.com/in/wieslawmazur/)

---

*Made by Poland. For Polish law firms.
Audytowalne, lokalne, vendor-neutral.*
