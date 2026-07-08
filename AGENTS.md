# AGENTS.md - matematicsolutions/.github

Plik standardu [agents.md](https://agents.md) (Linux Foundation / Agentic AI Foundation) - kanoniczne instrukcje dla agentow AI pracujacych z tym repozytorium. Czytany natywnie przez Cursor, Codex (OpenAI), Jules (Google), Devin / Windsurf, Aider, Amp, Factory, GitHub Copilot.

## Cel projektu

To repozytorium **`.github`** organizacji [matematicsolutions](https://github.com/matematicsolutions). Zawiera:

- `profile/README.md` - landing organizacji widoczny na `https://github.com/matematicsolutions`
- (w przyszlosci) szablony Issue / PR, polityka security, FUNDING.yml

To **nie jest produkt** - to wizytowka organizacji widoczna w pierwszej kolejnosci dla potencjalnych klientow (kancelarii) ogladajacych nasz GitHub.

## Kontekst MateMatic (TWARDE OGRANICZENIA)

[MateMatic Solutions](https://matematicsolutions.com) = lokalne RODO-safe narzedzia AI dla polskich kancelarii prawnych. Zero-cloud self-host, vendor-neutral, audytowalne.

Org profile README ma byc:

- **Mapa portfolio** - aktualna lista wszystkich publicznych repo: Patron (7 edycji jezykowych - PL/EN/BR/IT/DE/ES/FR), konektory MCP PL i poziomu UE, 41-konektorowa flota eu-legal-mcp (Europa/Ameryki/Azja-Pacyfik), dwa huby skilli (PL/EN), lpm-pl, matematic-readiness, praxis, .github, kolejne.
- **Pozycjonowanie marki** - "Made by Poland. For Polish law firms." - tagline na koncu.
- **Bez sales pitch** - GitHub czyta technical buyer (CTO / IT kancelarii), nie partner zarzadzajacy. Argument: "podpisana Konstytucja AI", "AGPL-3.0 chroni przed SaaS-ification", "hash-chain AI Act art. 12" - nie "zwiekszamy efektywnosc o 40%".

## Struktura repo

```
profile/
  README.md     - landing organizacji (visible at github.com/matematicsolutions)
README.md       - meta-readme tego repo
```

## Build i test

Brak kompilacji. "Test" = otworz `https://github.com/matematicsolutions` po push i sprawdz wizualnie.

## Zasady pisania (CRITICAL)

- **Polski jezyk** - tagline po angielsku ("Made by Poland. For Polish law firms.") to swiadomy choice; reszta po polsku.
- **Linkuj kazdy repo z listy** - aktualizuj `profile/README.md` przy KAZDYM nowym publicznym repo organizacji.
- **Bez em-dash** - uzywaj `-`.
- **Bez polskich znakow w commit messages**.
- **Wewnetrzny senior review** przed commitem jezeli zmiana > 5 linii tresci marketingowej.

## Czego NIE robic (twarde reguly)

- **NIE dodawaj sales-marketingu** ("liderzy w X", "innowacyjne Y") - GitHub buyer to nie marketing buyer.
- **NIE wstawiaj danych kontaktowych klientow** ani case studies z nazwami kancelarii.
- **NIE zostawiaj outdated linkow** - jezeli repo zostalo zarchiwizowane / zmienione nazwy, fix natychmiast.

## Powiazane repo (utrzymuj synchronizacje)

Ta tabela to repo "produktowe" - Patron, huby skilli, konektory pierwszej
fali (PL + poziom UE). Pelna flota 41 konektorow eu-legal-mcp (Europa,
Ameryki, Azja i Pacyfik) NIE jest tu duplikowana wiersz po wierszu -
zrodlem prawdy dla pelnej listy z linkami jest `profile/README.md`.

| Repo | Licencja | Status | AGENTS.md |
|---|---|---|---|
| [patron](https://github.com/matematicsolutions/patron) | AGPL-3.0 | aktywny rozwoj, 7 edycji jezykowych | tak |
| [lpm-pl](https://github.com/matematicsolutions/lpm-pl) | Apache 2.0 | v0.2.0-alpha | tak |
| [matematic-contract-review-pl](https://github.com/matematicsolutions/matematic-contract-review-pl) | Apache 2.0 | v0.1.0-alpha | tak |
| [matematic-anonimizacja-pl](https://github.com/matematicsolutions/matematic-anonimizacja-pl) | Apache 2.0 | v0.1.0-alpha | tak |
| [matematic-readiness](https://github.com/matematicsolutions/matematic-readiness) | CC BY-SA 4.0 | v0.1.0-alpha | tak |
| [matematic-legal-verify-pl](https://github.com/matematicsolutions/matematic-legal-verify-pl) | Apache 2.0 | v0.4.0-alpha | tak |
| [matematic-pomoc-prawna-pl](https://github.com/matematicsolutions/matematic-pomoc-prawna-pl) | Apache 2.0 | v0.1.0-alpha | nie (CLAUDE.md) |
| [praxis](https://github.com/matematicsolutions/praxis) | CC BY-SA 4.0 | aktywny | tak |
| [awesome-matematic-skills-pl](https://github.com/matematicsolutions/awesome-matematic-skills-pl) | MIT | 35 skilli + kuratorskie | tak |
| [awesome-matematic-skills-en](https://github.com/matematicsolutions/awesome-matematic-skills-en) | MIT | 18 skilli + kuratorskie | nie |
| [mcp-saos](https://github.com/matematicsolutions/mcp-saos) | MIT | stable | tak |
| [mcp-nsa](https://github.com/matematicsolutions/mcp-nsa) | MIT | stable | tak |
| [mcp-isap](https://github.com/matematicsolutions/mcp-isap) | MIT | stable | tak |
| [mcp-krs](https://github.com/matematicsolutions/mcp-krs) | MIT | stable | tak |
| [mcp-eu-sparql](https://github.com/matematicsolutions/mcp-eu-sparql) | MIT | stable | tak |
| [mcp-eu-compliance](https://github.com/matematicsolutions/mcp-eu-compliance) | MIT | stable | tak |
| [mcp-fr-legal](https://github.com/matematicsolutions/mcp-fr-legal) | Apache-2.0 | offline korpus | tak |
| [kio-orzeczenia-mcp](https://github.com/matematicsolutions/kio-orzeczenia-mcp) | Apache-2.0 | wczesny POC | nie (CONSTITUTION.md + DISCOVERY.md) |
| [legalize-mcp](https://github.com/matematicsolutions/legalize-mcp) | Apache-2.0 | 32 jurysdykcje | nie (CONSTITUTION.md + DISCOVERY.md) |
| [eu-drift-watch](https://github.com/matematicsolutions/eu-drift-watch) | Apache-2.0 | monitoring, nie konektor | nie |

## Kompatybilnosc agentow

Standard [AGENTS.md](https://agents.md). Dla Claude Code dodatkowo plik [CLAUDE.md](./CLAUDE.md).

Repo produktowe i konektory pierwszej fali (PL + poziom UE, od 2026-05-21)
maja `AGENTS.md` w rocie - patrz kolumna w tabeli, NIE jest to uniwersalne
dla calej organizacji. Flota eu-legal-mcp (generowana wlasnym pipeline'em
od 2026-07-01, 32 konektory) ma zamiast tego `CONSTITUTION.md` +
`DISCOVERY.md` w kazdym repo - inny format, ten sam cel. `awesome-matematic-skills-en`
i `matematic-pomoc-prawna-pl` maja wlasna strukture (odpowiednio: brak
osobnego pliku governance / `CLAUDE.md`).

## Licencja

Repozytorium organizacji `.github` - tresc README na licencji [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) jak reszta materialow edukacyjnych MateMatic.
