# AGENTS.md - matematicsolutions/.github

An [agents.md](https://agents.md) standard file (Linux Foundation / Agentic AI Foundation) - canonical instructions for AI agents working in this repository. Read natively by Cursor, Codex (OpenAI), Jules (Google), Devin / Windsurf, Aider, Amp, Factory, GitHub Copilot, Claude Code.

## Purpose

This is the **`.github`** repository of the [matematicsolutions](https://github.com/matematicsolutions) organization. It contains:

- `profile/README.md` - the org landing page shown at `https://github.com/matematicsolutions`
- `assets/hero.svg` - the banner rendered at the top of the profile
- (future) Issue / PR templates, security policy, FUNDING.yml

This is **not a product** - it is the organization's front door, the first thing a prospective user (a law firm, a developer, a partner) sees on our GitHub.

## MateMatic context (HARD CONSTRAINTS)

[MateMatic Solutions](https://matematicsolutions.com) builds **open, grounded, self-hosted legal-AI infrastructure for law firms - in any jurisdiction where the law is public.** Vendor-neutral, auditable, GDPR-safe. We started in Poland and that stack is our deepest, but the product serves law firms worldwide; the growing set of Patron language editions (PL, EN, US, GB, BR, IT, DE, ES, FR - and counting) is the expression of that reach.

The org profile README must be:

- **English-primary and world-facing.** The audience is global. Poland is presented as our home market and origin, not as the ceiling of who we serve. Do not reintroduce a Polish-primary body or a "for Polish law firms" framing.
- **A portfolio map** - a current list of the public repos: Patron (9 language editions), the 41-connector MCP fleet across 32 jurisdictions (Europe / Americas / Asia-Pacific), the two skill hubs (EN / PL), plus the open legal skills, praxis, and this repo.
- **Brand positioning** - the slogan "AI that knows what it doesn't know" / "We know how" ties directly to the product: every connector returns a verifiable citation, so the model shows its source instead of guessing.
- **No sales pitch.** GitHub is read by a technical buyer (a firm's CTO / IT), not a managing partner. Arguments: "signed AI Constitution", "AGPL-3.0 protects against SaaS-ification", "hash-chained audit trail, AI Act art. 12" - never "boost efficiency by 40%".

## Repo structure

```
profile/
  README.md     - org landing page (visible at github.com/matematicsolutions)
assets/
  hero.svg      - profile banner
  matematic-logo-400.png
README.md       - meta-readme for this repo
```

## Build and test

No compilation. "Test" = push, open `https://github.com/matematicsolutions`, and check the profile renders (banner, badges, tables, links).

## Writing rules (CRITICAL)

- **English.** The profile is English-primary and world-facing. The slogan and taglines are English.
- **Link every repo you list** - update `profile/README.md` whenever the organization gains a new public repo, and refresh flagship descriptions from the connector's own README (repo `description` fields go stale - e.g. us-eli-mcp is five sources, not "federal bills").
- **No em-dash** - use `-`.
- **No Polish characters in commit messages.**
- **Run reviewer-en on any content change over ~5 lines** before committing.

## What NOT to do (hard rules)

- **Do not add sales-marketing** ("leaders in X", "innovative Y") - the GitHub buyer is not a marketing buyer.
- **Do not narrow the positioning back to Poland** - we serve law firms globally; Poland is origin and deepest stack, not the target ceiling.
- **Do not include client contact data** or case studies naming firms.
- **Do not leave outdated links** - if a repo is archived or renamed, fix it immediately.

## Related repos (keep in sync)

Product repos - Patron, skill hubs, first-wave connectors (PL + EU level). The full 41-connector eu-legal-mcp fleet (Europe, Americas, Asia-Pacific) is NOT duplicated row-by-row here; the source of truth for the full list is `profile/README.md`.

| Repo | Licence | Status | Governance file |
|---|---|---|---|
| [patron](https://github.com/matematicsolutions/patron) | AGPL-3.0 | active, 9 language editions | AGENTS.md |
| [lpm-pl](https://github.com/matematicsolutions/lpm-pl) | Apache 2.0 | v0.2.0-alpha | AGENTS.md |
| [matematic-contract-review-pl](https://github.com/matematicsolutions/matematic-contract-review-pl) | Apache 2.0 | v0.1.0-alpha | AGENTS.md |
| [matematic-anonimizacja-pl](https://github.com/matematicsolutions/matematic-anonimizacja-pl) | Apache 2.0 | v0.1.0-alpha | AGENTS.md |
| [matematic-readiness](https://github.com/matematicsolutions/matematic-readiness) | CC BY-SA 4.0 | v0.1.0-alpha | AGENTS.md |
| [matematic-legal-verify-pl](https://github.com/matematicsolutions/matematic-legal-verify-pl) | Apache 2.0 | v0.4.0-alpha | AGENTS.md |
| [matematic-pomoc-prawna-pl](https://github.com/matematicsolutions/matematic-pomoc-prawna-pl) | Apache 2.0 | v0.1.0-alpha | CLAUDE.md |
| [praxis](https://github.com/matematicsolutions/praxis) | CC BY-SA 4.0 | active | AGENTS.md |
| [awesome-matematic-skills-pl](https://github.com/matematicsolutions/awesome-matematic-skills-pl) | MIT | 41 skills + curated | AGENTS.md |
| [awesome-matematic-skills-en](https://github.com/matematicsolutions/awesome-matematic-skills-en) | MIT | 18 skills + curated | no |
| [mcp-saos](https://github.com/matematicsolutions/mcp-saos) | MIT | stable | AGENTS.md |
| [mcp-nsa](https://github.com/matematicsolutions/mcp-nsa) | MIT | stable | AGENTS.md |
| [mcp-isap](https://github.com/matematicsolutions/mcp-isap) | MIT | stable | AGENTS.md |
| [mcp-krs](https://github.com/matematicsolutions/mcp-krs) | MIT | stable | AGENTS.md |
| [mcp-eureka](https://github.com/matematicsolutions/mcp-eureka) | MIT | PL tax interpretations | varies |
| [mcp-eu-sparql](https://github.com/matematicsolutions/mcp-eu-sparql) | MIT | stable | AGENTS.md |
| [mcp-eu-compliance](https://github.com/matematicsolutions/mcp-eu-compliance) | MIT | stable | AGENTS.md |
| [us-eli-mcp](https://github.com/matematicsolutions/us-eli-mcp) | Apache-2.0 | flagship, 5 sources | CONSTITUTION.md + DISCOVERY.md |
| [br-eli-mcp](https://github.com/matematicsolutions/br-eli-mcp) | Apache-2.0 | flagship, 8 sources | CONSTITUTION.md + DISCOVERY.md |
| [gb-eli-mcp](https://github.com/matematicsolutions/gb-eli-mcp) | Apache-2.0 | flagship | CONSTITUTION.md + DISCOVERY.md |
| [legalize-mcp](https://github.com/matematicsolutions/legalize-mcp) | Apache-2.0 | 32 jurisdictions | CONSTITUTION.md + DISCOVERY.md |
| [eu-drift-watch](https://github.com/matematicsolutions/eu-drift-watch) | Apache-2.0 | monitoring, not a connector | no |

## Agent compatibility

Standard: [AGENTS.md](https://agents.md). For Claude Code, an additional [CLAUDE.md](./CLAUDE.md) pointer.

Product repos and first-wave connectors (PL + EU level) carry `AGENTS.md` at root. The eu-legal-mcp fleet (generated by our own pipeline) carries `CONSTITUTION.md` + `DISCOVERY.md` instead - different format, same purpose: the agent reads the repo's rules, source, licence and coverage limits before it works on it.

## Licence

The `.github` organization repository - README content under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), like the rest of MateMatic's educational material.
