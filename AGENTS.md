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

- **Mapa portfolio** - aktualna lista wszystkich publicznych repo (Patron + 6 mcp-* + lpm-pl + matematic-readiness + praxis + .github + kolejne).
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
- **Marko-pl review** przed commitem jezeli zmiana > 5 linii tresci marketingowej.

## Czego NIE robic (twarde reguly)

- **NIE dodawaj sales-marketingu** ("liderzy w X", "innowacyjne Y") - GitHub buyer to nie marketing buyer.
- **NIE wstawiaj danych kontaktowych klientow** ani case studies z nazwami kancelarii.
- **NIE zostawiaj outdated linkow** - jezeli repo zostalo zarchiwizowane / zmienione nazwy, fix natychmiast.

## Powiazane repo (utrzymuj synchronizacje)

| Repo | Licencja | Status |
|---|---|---|
| [patron](https://github.com/matematicsolutions/patron) | AGPL-3.0 | aktywny rozwoj |
| [lpm-pl](https://github.com/matematicsolutions/lpm-pl) | Apache 2.0 | v0.2.0-alpha |
| [matematic-contract-review-pl](https://github.com/matematicsolutions/matematic-contract-review-pl) | Apache 2.0 | v0.1.0-alpha |
| [matematic-anonimizacja-pl](https://github.com/matematicsolutions/matematic-anonimizacja-pl) | Apache 2.0 | v0.1.0-alpha |
| [matematic-readiness](https://github.com/matematicsolutions/matematic-readiness) | CC BY-SA 4.0 | v0.1.0-alpha |
| [matematic-legal-verify-pl](https://github.com/matematicsolutions/matematic-legal-verify-pl) | Apache 2.0 | v0.4.0-alpha |
| [matematic-pomoc-prawna-pl](https://github.com/matematicsolutions/matematic-pomoc-prawna-pl) | Apache 2.0 | v0.1.0-alpha |
| [praxis](https://github.com/matematicsolutions/praxis) | CC BY-SA 4.0 | aktywny |
| [mcp-saos](https://github.com/matematicsolutions/mcp-saos) | MIT | stable |
| [mcp-nsa](https://github.com/matematicsolutions/mcp-nsa) | MIT | stable |
| [mcp-isap](https://github.com/matematicsolutions/mcp-isap) | MIT | stable |
| [mcp-krs](https://github.com/matematicsolutions/mcp-krs) | MIT | stable |
| [mcp-eu-sparql](https://github.com/matematicsolutions/mcp-eu-sparql) | MIT | stable |
| [mcp-eu-compliance](https://github.com/matematicsolutions/mcp-eu-compliance) | MIT | v0.1.0 |
| [awesome-matematic-skills-pl](https://github.com/matematicsolutions/awesome-matematic-skills-pl) | MIT | v0.1.0 |

## Kompatybilnosc agentow

Standard [AGENTS.md](https://agents.md). Dla Claude Code dodatkowo plik [CLAUDE.md](./CLAUDE.md).

Wszystkie publiczne repo MateMatic maja `AGENTS.md` w roocie (od 2026-05-21) - patrz tabela.

## Licencja

Repozytorium organizacji `.github` - tresc README na licencji [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) jak reszta materialow edukacyjnych MateMatic.
