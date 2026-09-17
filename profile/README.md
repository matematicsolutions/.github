<div align="center">

<a href="https://matematicsolutions.com/en/">
  <img src="https://raw.githubusercontent.com/matematicsolutions/.github/main/assets/hero.svg" alt="MateMatic Solutions - AI that knows what it doesn't know. We know how." width="100%">
</a>

<br>

**European LegalTech infrastructure that leads a legal answer back to its source, its context and its provenance.**

**[Repertorium](https://github.com/matematicsolutions/repertorium)** · legal knowledge infrastructure &nbsp;|&nbsp; **[PATRON](https://github.com/matematicsolutions/patron)** · local-first legal workspace<br>
**[Boutique](https://matematicsolutions.com/en/boutique)** · connectors and skills &nbsp;|&nbsp; **MateMatic** · architecture, audit and deployment

[Website](https://matematicsolutions.com/en/) · [Hugging Face](https://huggingface.co/matematicsolutions) · [Where your data is](https://matematicsolutions.com/en/where-your-data-is)

</div>

---

## Architecture

Four layers. Each works on its own; none requires the others.

| Layer | What it is | How you reach it | Code | Runs on your machine |
|---|---|---|---|---|
| **[Repertorium](https://github.com/matematicsolutions/repertorium)** | Legal knowledge infrastructure: a corpus of Polish and EU law with a citation graph and PL-EU links | web console, remote MCP, REST | hosted service; interface and response contract documented in the open | as a local data pack, by agreement |
| **[PATRON](https://github.com/matematicsolutions/patron)** | Local-first legal workspace: case files, chat, tracked-changes drafting, audit trail | Windows desktop app, 9 language editions | AGPL-3.0 | yes; the model is local or a cloud one you choose |
| **[Boutique](https://matematicsolutions.com/en/boutique)** | Catalogue of MCP connectors and agent skills | `uvx` / `npx` / `npx skills add`, [`catalog.json`](https://matematicsolutions.com/catalog.json) | MIT / Apache-2.0 | yes; connectors query public sources from your machine |
| **MateMatic** | Architecture, reliability audit and deployment inside a firm | [contact](mailto:kontakt@matematic.co) | governance documents are open | - |

```
people ─────────► PATRON (desktop) ───► connectors ───► official sources
                                                        (live query)
AI agents ──────► any MCP client ─────► connectors
                                  └───► Repertorium     (corpus snapshot)
applications ───► REST / MCP ─────────► Repertorium
people ─────────► web console ────────► Repertorium
```

PATRON reaches Polish and EU sources through its own bundled connectors today; wiring it to Repertorium is planned.

## Corpus or live query

The two words mean different things here.

- **Corpus** (Repertorium, and the offline connectors `mcp-eu-compliance`, `mcp-fr-legal`, `pk-eli-mcp`): a snapshot of the law with a known state date. Fast, joinable, citable - and as current as its last build.
- **Live query** (most connectors): the request goes to the official source at the moment you ask. As current as the source itself - and only as available and as structured as that source is.

## Look under the hood

Claims are cheap; these are the parts you can inspect.

- **Citation contract** - [MCS v0.1](https://github.com/matematicsolutions/patron/blob/main/MCS-v0.1.md): the `source_id / url / exact_quote / locator / confidence` shape PATRON verifies citations against, with a conformance test a connector can run.
- **Response contract** - Repertorium answers are `ok`, `partial` (with the shards that failed named) or `search_unavailable`. An empty list is never passed off as an honest zero. [Details](https://github.com/matematicsolutions/repertorium).
- **Audit trail** - PATRON hash-chains every model interaction and exports a ZIP with its own verifier, and the documentation says what the trail does *not* prove ([ADR-0142](https://github.com/matematicsolutions/patron/tree/main/governance/adr), [audit trail](https://matematicsolutions.com/en/patron/audit-trail)).
- **Decisions** - [Architecture Decision Records](https://github.com/matematicsolutions/patron/tree/main/governance/adr) and the [AI Constitution](https://github.com/matematicsolutions/patron/blob/main/governance/CONSTITUTION.md) a firm reads before deployment.
- **Monitoring** - [`eu-drift-watch`](https://github.com/matematicsolutions/eu-drift-watch) checks monthly that anchor statutes in 9 EU jurisdictions still resolve at the source.
- **Numbers** - every figure below has a definition and a place where it is measured: [`ecosystem.json`](https://github.com/matematicsolutions/.github/blob/main/ecosystem.json).

## In numbers

| | |
|---|---|
| Repertorium corpus | 1,492,530 Polish and 236,944 EU documents · 1,443,748 PL-EU links |
| Connectors | 45 MCP connectors · 35 jurisdictions (34 countries and EU law) |
| Skills | 54 in the Boutique catalogue · hubs: [45 PL](https://github.com/matematicsolutions/awesome-matematic-skills-pl), [18 EN](https://github.com/matematicsolutions/awesome-matematic-skills-en) |
| PATRON | 9 installer editions · 7 Polish and EU sources bundled |

## Connectors

Source connectors are standalone MCP servers, one repository per source, returning a citation with a stable identifier (ELI / ECLI / CELEX / case number) and a `source_url`. Two exceptions: `prawo-pl-mcp` aggregates the Polish sources, and `boutique-mcp` returns install commands, not law.

**Poland** - one server for all of them: [`prawo-pl-mcp`](https://github.com/matematicsolutions/prawo-pl-mcp) (4 tools), or each source on its own: [`mcp-saos`](https://github.com/matematicsolutions/mcp-saos) (courts) · [`mcp-nsa`](https://github.com/matematicsolutions/mcp-nsa) (administrative courts) · [`mcp-isap`](https://github.com/matematicsolutions/mcp-isap) (legislation) · [`mcp-krs`](https://github.com/matematicsolutions/mcp-krs) (company register) · [`mcp-eureka`](https://github.com/matematicsolutions/mcp-eureka) (tax interpretations) · [`kio-orzeczenia-mcp`](https://github.com/matematicsolutions/kio-orzeczenia-mcp) (public procurement)

**European Union** - [`mcp-eu-sparql`](https://github.com/matematicsolutions/mcp-eu-sparql) (EUR-Lex and CJEU, live) · [`mcp-eu-compliance`](https://github.com/matematicsolutions/mcp-eu-compliance) (digital and data regulations, offline corpus)

<details>
<summary><b>National connectors - 33 countries</b></summary>

<br>

| Region | Connectors |
|---|---|
| Europe | [de](https://github.com/matematicsolutions/de-eli-mcp) · [fr](https://github.com/matematicsolutions/fr-eli-mcp) (+ offline [mcp-fr-legal](https://github.com/matematicsolutions/mcp-fr-legal)) · [it](https://github.com/matematicsolutions/it-eli-mcp) · [es](https://github.com/matematicsolutions/es-eli-mcp) · [nl](https://github.com/matematicsolutions/nl-eli-mcp) · [ch](https://github.com/matematicsolutions/ch-eli-mcp) · [se](https://github.com/matematicsolutions/se-eli-mcp) · [be](https://github.com/matematicsolutions/be-eli-mcp) · [at](https://github.com/matematicsolutions/at-eli-mcp) · [ie](https://github.com/matematicsolutions/ie-eli-mcp) · [dk](https://github.com/matematicsolutions/dk-eli-mcp) · [fi](https://github.com/matematicsolutions/fi-eli-mcp) · [cz](https://github.com/matematicsolutions/cz-eli-mcp) · [ro](https://github.com/matematicsolutions/ro-eli-mcp) · [hu](https://github.com/matematicsolutions/hu-eli-mcp) · [hr](https://github.com/matematicsolutions/hr-eli-mcp) · [sk](https://github.com/matematicsolutions/sk-eli-mcp) · [lt](https://github.com/matematicsolutions/lt-eli-mcp) · [lu](https://github.com/matematicsolutions/lu-eli-mcp) · [mt](https://github.com/matematicsolutions/mt-eli-mcp) · [gb](https://github.com/matematicsolutions/gb-eli-mcp) · [tr](https://github.com/matematicsolutions/tr-eli-mcp) |
| Americas | [us](https://github.com/matematicsolutions/us-eli-mcp) · [br](https://github.com/matematicsolutions/br-eli-mcp) · [ca](https://github.com/matematicsolutions/ca-eli-mcp) · [cl](https://github.com/matematicsolutions/cl-eli-mcp) · [co](https://github.com/matematicsolutions/co-eli-mcp) |
| Asia-Pacific | [jp](https://github.com/matematicsolutions/jp-eli-mcp) · [au](https://github.com/matematicsolutions/au-eli-mcp) · [sg](https://github.com/matematicsolutions/sg-eli-mcp) · [my](https://github.com/matematicsolutions/my-eli-mcp) · [il](https://github.com/matematicsolutions/il-eli-mcp) · [pk](https://github.com/matematicsolutions/pk-eli-mcp) |
| Cross-jurisdiction | [`legalize-mcp`](https://github.com/matematicsolutions/legalize-mcp) (law-as-git, 32 jurisdictions) · [`boutique-mcp`](https://github.com/matematicsolutions/boutique-mcp) (the catalogue itself, searched locally) |

</details>

Install commands for each: [matematicsolutions.com/en/boutique/connectors](https://matematicsolutions.com/en/boutique/connectors).

## Skills

A skill is a procedure an agent follows: grounding a citation, red-teaming a memo, scoring an output before it ships. Two hubs, installable in any Agent-Skills-compatible tool:

```
npx skills add matematicsolutions/awesome-matematic-skills-en
```

[`awesome-matematic-skills-en`](https://github.com/matematicsolutions/awesome-matematic-skills-en) - method-neutral and EU law · [`awesome-matematic-skills-pl`](https://github.com/matematicsolutions/awesome-matematic-skills-pl) - Polish jurisdiction, full firm workflow · [`praxis`](https://github.com/matematicsolutions/praxis) - open guides for law firms (CC BY-SA 4.0)

## What is open, what is not

- **Open source:** PATRON (AGPL-3.0), every connector in this organization (MIT or Apache-2.0), the skill hubs, the governance documents. Why the split: [ADR-0002](https://github.com/matematicsolutions/patron/blob/main/governance/adr/0002-dual-license-agpl-shell-mit-connectors.md).
- **Open interface, hosted service:** Repertorium. The contract is public; the corpus build pipeline and infrastructure are not.
- **Your data:** PATRON keeps case files on the machine it runs on. With a local model nothing leaves it; with a cloud model you choose, the request goes to that provider with names and identifiers masked, and the call is recorded in the audit trail. Connectors send your query to the public source they read.

## Contact

MateMatic Solutions · Kraków, Poland · [kontakt@matematic.co](mailto:kontakt@matematic.co) · [matematicsolutions.com](https://matematicsolutions.com/en/)
