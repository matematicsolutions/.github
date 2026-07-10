<div align="center">

<a href="https://matematicsolutions.com/en/">
  <img src="https://raw.githubusercontent.com/matematicsolutions/.github/main/assets/hero.svg" alt="MateMatic Solutions - AI that knows what it doesn't know. We know how." width="100%">
</a>

<br>

**Open, grounded legal-AI infrastructure for law firms - anywhere the law is public.** Self-hosted. Auditable. Vendor-neutral.

[![MCP connectors](https://img.shields.io/badge/MCP_connectors-42-1E3A5F?style=flat-square)](https://matematicsolutions.com/en/boutique)
[![Jurisdictions](https://img.shields.io/badge/jurisdictions-32-6C717A?style=flat-square)](https://matematicsolutions.com/en/boutique)
[![Source documents](https://img.shields.io/badge/source_documents-30M%2B-D4A537?style=flat-square)](https://matematicsolutions.com/en/boutique)
[![Skills](https://img.shields.io/badge/Claude_skills-59-10b981?style=flat-square)](https://github.com/matematicsolutions/awesome-matematic-skills-en)
[![License](https://img.shields.io/badge/license-AGPL_%2B_MIT_%2F_Apache-334155?style=flat-square)](#why-open-source)

[Website](https://matematicsolutions.com/en/) · [Boutique catalogue](https://matematicsolutions.com/en/boutique) · [Download Patron](https://matematicsolutions.com/en/pobierz) · [LinkedIn](https://www.linkedin.com/in/wies%C5%82aw-mazur-535428364/)

</div>

---

## The idea

Legal AI has one dominant failure mode: a confident, well-written citation to a case or statute that does not exist. In a law firm, that is not a glitch - it is malpractice.

So we build the opposite. Every tool in this fleet returns a **verifiable citation** - title, URL, court or act, date, and a stable identifier (ELI / ECLI / CELEX / docket number) - resolved live against the public source. The model does not recall the law from memory; it fetches it, and it can show you where every word came from. Citation checks run as mechanical string-matches, so a fabricated quote fails at the structural layer, before it ever reaches a client.

**AI that knows what it doesn't know** - and hands you the source instead of guessing.

---

## What we ship

| | | |
|---|---|---|
| **[Patron](https://github.com/matematicsolutions/patron)** | An AI agent that never leaves the firm's server | 9 desktop editions |
| **MCP connector fleet** | Grounded, keyless-first access to public law | 42 connectors · 33 jurisdictions |
| **Two skill hubs** | Method-neutral legal-AI skills for Claude Code / Cursor / Codex | 59 skills |
| **[Boutique](https://matematicsolutions.com/en/boutique)** | Install-ready catalogue of every connector and skill | Always current |

All of it is open source, and all of it runs on the firm's own hardware, with the model of its choice - Claude, Gemini, or a local Ollama.

---

## Patron - the agent that stays inside the firm

**[patron](https://github.com/matematicsolutions/patron)** (AGPL-3.0) is a self-hosted legal-AI shell: chat, documents, a hash-chained audit trail (EU AI Act art. 12), an **AI Constitution** the firm reads and signs, `docker-compose` ready, and a vendor-agnostic model layer. The data stays where the duty of confidentiality lives.

One repository, one [release](https://github.com/matematicsolutions/patron/releases), **nine Windows installers** - PL, EN, US, GB, BR, IT, DE, ES, FR. Each ships with its own market's law connector wired in by default (US: Congress.gov / GovInfo / Federal Register / eCFR / CourtListener · UK: legislation.gov.uk / Find Case Law / GOV.UK · Brazil: Senado + DataJud CNJ · and so on; the EN build is the EU edition, with EUR-Lex in front). Download and per-edition detail: **[matematicsolutions.com/en/pobierz](https://matematicsolutions.com/en/pobierz)**.

---

## Flagship connectors

Each is a standalone MCP server (stdio, `uvx` / `npx`, or clone-and-run). Featured first are our four highest-coverage markets; the full catalogue by region follows.

### 🇺🇸 United States - [`us-eli-mcp`](https://github.com/matematicsolutions/us-eli-mcp)

Five sources, ten tools. **Congress.gov** (the federal legislative process) · **GovInfo** (US Code, Statutes at Large, CFR, Federal Register packages) · **Federal Register** (1,003,504 documents, including 1,550 executive orders, keyless) · **CourtListener** (**8,294,123 court opinions** - the headline value is state case law for California, New York, Texas and beyond, which no federal source covers) · **eCFR** (412,846 current CFR sections with amendment history). Apache-2.0.

### 🇧🇷 Brazil - [`br-eli-mcp`](https://github.com/matematicsolutions/br-eli-mcp)

Eight keyless, no-registration open-data APIs. Federal bills (Camara dos Deputados) · enacted law via the real LexML URN resolver (Senado) · full article text (normas.leg.br) · court dockets across all branches (**DataJud CNJ**) · rulings from the STJ, **TST** (labor supreme court - 3,751,594 rulings), **TCU** (federal court of accounts, procurement - 525,620 rulings) and **CARF** (federal tax appeals). Apache-2.0.

### 🇪🇺 European Union - [`mcp-eu-sparql`](https://github.com/matematicsolutions/mcp-eu-sparql) + [`mcp-eu-compliance`](https://github.com/matematicsolutions/mcp-eu-compliance)

Live EU legislation and **57,103 CJEU rulings and Advocate-General opinions** (34,261 judgments, 8,362 orders, 14,480 opinions) via the Publications Office SPARQL endpoint (Cellar / EUR-Lex), each with CELEX + ECLI, plus national data-protection decisions from GDPRhub. Alongside it, an **offline** verbatim corpus of 14 digital-and-data regulations - GDPR, AI Act, DORA, NIS2, eIDAS 2.0, CRA, DSA, DMA, Data Act, DGA, LED, ePrivacy, Cybersecurity Act, CER - in local SQLite FTS5, zero-LLM, every snippet CELEX-stamped. MIT.

### 🇬🇧 United Kingdom - [`gb-eli-mcp`](https://github.com/matematicsolutions/gb-eli-mcp)

**legislation.gov.uk** (The National Archives) - Acts of Parliament and Statutory Instruments across Westminster, Holyrood, the Senedd and Stormont - plus **Find Case Law** (UK judgments as Akoma Ntoso) and the **GOV.UK Search API** (tribunal decisions, HMRC manuals, CMA cases). Eight tools, keyless, Open Government Licence v3.0. Britain pioneered URI-based legislation identifiers, so `eli_uri` carries the UK's own stable id. Apache-2.0.

---

## The full fleet - 32 jurisdictions across three continents

Every connector returns the same citation contract: `eli_uri` / ECLI / CELEX, a human-readable citation, and a `source_url`. Install instructions for each, always current: **[matematicsolutions.com/en/boutique](https://matematicsolutions.com/en/boutique)**.

### Europe (ordered by legal-market size)

| | Connector | Source |
|---|---|---|
| 🇩🇪 Germany | [de-eli-mcp](https://github.com/matematicsolutions/de-eli-mcp) | NeuRIS - federal legislation + case law at every court level + Bundestag DIP |
| 🇫🇷 France | [fr-eli-mcp](https://github.com/matematicsolutions/fr-eli-mcp) | Legifrance / PISTE - LODA, codes, JURI case law (ECLI); free PISTE key |
| 🇮🇹 Italy | [it-eli-mcp](https://github.com/matematicsolutions/it-eli-mcp) | Normattiva (Akoma Ntoso / URN:NIR / ELI) + Corte Costituzionale from 1956 |
| 🇪🇸 Spain | [es-eli-mcp](https://github.com/matematicsolutions/es-eli-mcp) | BOE, Tribunal Constitucional, DGT tax rulings, TEAC doctrine, AEPD |
| 🇳🇱 Netherlands | [nl-eli-mcp](https://github.com/matematicsolutions/nl-eli-mcp) | BWB (KOOP SRU) + Rechtspraak Open Data |
| 🇨🇭 Switzerland | [ch-eli-mcp](https://github.com/matematicsolutions/ch-eli-mcp) | Fedlex - native ELI, DE / FR / IT / EN |
| 🇸🇪 Sweden | [se-eli-mcp](https://github.com/matematicsolutions/se-eli-mcp) | Riksdagen open data (SFS) |
| 🇧🇪 Belgium | [be-eli-mcp](https://github.com/matematicsolutions/be-eli-mcp) | Moniteur Belge / Belgisch Staatsblad |
| 🇦🇹 Austria | [at-eli-mcp](https://github.com/matematicsolutions/at-eli-mcp) | RIS (data.bka.gv.at) - legislation + Judikatur |
| 🇮🇪 Ireland | [ie-eli-mcp](https://github.com/matematicsolutions/ie-eli-mcp) | Irish Statute Book |
| 🇩🇰 Denmark | [dk-eli-mcp](https://github.com/matematicsolutions/dk-eli-mcp) | Retsinformation (LexDania XML) |
| 🇫🇮 Finland | [fi-eli-mcp](https://github.com/matematicsolutions/fi-eli-mcp) | Finlex (Akoma Ntoso) |
| 🇨🇿 Czechia | [cz-eli-mcp](https://github.com/matematicsolutions/cz-eli-mcp) | e-Sbirka (SPARQL / RDF) |
| 🇷🇴 Romania | [ro-eli-mcp](https://github.com/matematicsolutions/ro-eli-mcp) | Portal Legislativ (SOAP) |
| 🇭🇺 Hungary | [hu-eli-mcp](https://github.com/matematicsolutions/hu-eli-mcp) | Nemzeti Jogszabalytar |
| 🇭🇷 Croatia | [hr-eli-mcp](https://github.com/matematicsolutions/hr-eli-mcp) | Narodne novine (JSON-LD) |
| 🇸🇰 Slovakia | [sk-eli-mcp](https://github.com/matematicsolutions/sk-eli-mcp) | Slov-Lex (static) |
| 🇱🇹 Lithuania | [lt-eli-mcp](https://github.com/matematicsolutions/lt-eli-mcp) | TAR / data.gov.lt (Spinta) |
| 🇱🇺 Luxembourg | [lu-eli-mcp](https://github.com/matematicsolutions/lu-eli-mcp) | Legilux - jolux RDF + Akoma Ntoso |
| 🇲🇹 Malta | [mt-eli-mcp](https://github.com/matematicsolutions/mt-eli-mcp) | legislation.mt |
| 🇹🇷 Turkey | [tr-eli-mcp](https://github.com/matematicsolutions/tr-eli-mcp) | Mevzuat Bilgi Sistemi / Bedesten (keyless) |

Plus [`mcp-fr-legal`](https://github.com/matematicsolutions/mcp-fr-legal) - an offline full-text corpus of French codes and statutes (Legifrance / DILA, local SQLite, zero-LLM), companion to the live `fr-eli-mcp`.

### The Americas

| | Connector | Source |
|---|---|---|
| 🇺🇸 United States | [us-eli-mcp](https://github.com/matematicsolutions/us-eli-mcp) | Congress.gov · GovInfo · Federal Register · CourtListener · eCFR *(flagship above)* |
| 🇧🇷 Brazil | [br-eli-mcp](https://github.com/matematicsolutions/br-eli-mcp) | Camara · Senado · DataJud · STJ · TST · TCU · CARF *(flagship above)* |
| 🇨🇦 Canada | [ca-eli-mcp](https://github.com/matematicsolutions/ca-eli-mcp) | Justice Laws Website - federal, bilingual |
| 🇨🇱 Chile | [cl-eli-mcp](https://github.com/matematicsolutions/cl-eli-mcp) | BCN Linked Open Data (SPARQL) |
| 🇨🇴 Colombia | [co-eli-mcp](https://github.com/matematicsolutions/co-eli-mcp) | Constitutional Court decisions, keyless |

### Asia-Pacific

| | Connector | Source |
|---|---|---|
| 🇯🇵 Japan | [jp-eli-mcp](https://github.com/matematicsolutions/jp-eli-mcp) | e-Gov national legislation |
| 🇦🇺 Australia | [au-eli-mcp](https://github.com/matematicsolutions/au-eli-mcp) | Federal Register of Legislation |
| 🇸🇬 Singapore | [sg-eli-mcp](https://github.com/matematicsolutions/sg-eli-mcp) | Singapore Statutes Online |
| 🇲🇾 Malaysia | [my-eli-mcp](https://github.com/matematicsolutions/my-eli-mcp) | Laws of Malaysia Online |
| 🇮🇱 Israel | [il-eli-mcp](https://github.com/matematicsolutions/il-eli-mcp) | Knesset OData, keyless |
| 🇵🇰 Pakistan | [pk-eli-mcp](https://github.com/matematicsolutions/pk-eli-mcp) | Pakistan Code + Supreme Court, corpus-based |

### Cross-jurisdiction and monitoring

- [`legalize-mcp`](https://github.com/matematicsolutions/legalize-mcp) - one server over the [legalize-dev](https://github.com/legalize-dev) corpus: legislation from 32 jurisdictions (21 EU) as Markdown with ELI-style ids and full change history (every reform is a commit).
- [`eu-drift-watch`](https://github.com/matematicsolutions/eu-drift-watch) - a monthly watchdog that checks whether anchor statutes across 9 EU jurisdictions have been renamed or repealed at the source. A guard over the fleet, not another source.

---

## Skill hubs - grounded legal-AI skills for any agent

Two open hubs of Claude Code / Cowork skills, installable in one command for any Agent-Skills-compatible tool (Claude Code, Cursor, Codex, Gemini CLI):

| Hub | Focus | Skills |
|---|---|---|
| [**awesome-matematic-skills-en**](https://github.com/matematicsolutions/awesome-matematic-skills-en) | Method-neutral: citation grounding, red-team review, output scoring, EU law | 18 |
| [**awesome-matematic-skills-pl**](https://github.com/matematicsolutions/awesome-matematic-skills-pl) | Polish jurisdiction: PL/EU case law, KRS, DOCX redlining, GDPR, full firm workflow | 41 |

```
npx skills add matematicsolutions/awesome-matematic-skills-en
```

The heart of both hubs is a **verification core**: grounding a citation against its source, stress-testing a high-stakes memo adversarially, scoring an output before it ships, and packaging the whole reasoning trail into an AI-Act-compliant audit bundle. The same discipline as the connectors, one layer up.

---

## Boutique - the platform that puts it all one command away

**[matematicsolutions.com/en/boutique](https://matematicsolutions.com/en/boutique)** is the front door to the whole ecosystem, built around two doors:

- **[For the lawyer - Skills](https://matematicsolutions.com/en/boutique/skills).** Ready-made abilities you load once and keep: reviewer, humaniser, devil's advocate, citation extraction, clause checklist, output scoring, EU-law and CJEU search.
- **[For the agent - MCP connectors](https://matematicsolutions.com/en/boutique/connectors).** Live sources of law wired straight into the agent - statutes, case law, the company register, the compliance corpus - each with a stable identifier and a link back to the source.

Both install with **one command** - `npx skills add ...` for any agent, or `/plugin marketplace add ...` inside Claude Code. Prefer not to touch a terminal? A Windows wizard places a skill for you: no Git, no config, nothing technical. Everything then runs locally, on your own documents, with your data staying with you.

Free to start, GDPR-safe by default. The catalogue grows steadily - from our own repositories and from real practice needs - with a premium tier coming later, always honest about authorship. If you want to wire one connector or skill into your own product, this is where to start.

---

<a id="why-open-source"></a>

## Why open source

- **Patron's shell is AGPL-3.0** - it protects against SaaS-ification. A firm self-hosting has no extra obligations; a competitor reselling Patron as SaaS to third parties must open its changes.
- **The connectors are MIT or Apache-2.0** - infrastructure to public sources of law. The more products depend on them, the more they become the default way to return grounded citations from each jurisdiction. That is the point.

Rationale: [ADR-0002](https://github.com/matematicsolutions/patron/blob/main/governance/adr/0002-dual-license-agpl-shell-mit-connectors.md).

## Governance you can audit

- **[AI Constitution v1.2.0](https://github.com/matematicsolutions/patron/blob/main/governance/CONSTITUTION.md)** - 9 principles, product boundaries, roles (Administrator / Operator / Auditor), mapped to the EU AI Act, GDPR and professional-ethics rules. Every firm reads and signs it.
- **[AGENTS.md](https://agents.md) everywhere** - canonical AI-agent instructions in the Linux Foundation / Agentic AI Foundation standard, read natively by 20+ tools. The connector fleet carries `CONSTITUTION.md` + `DISCOVERY.md` (boundaries, source, licence, coverage limits) so an agent reads the rules before it touches the repo.
- **Vendor-neutral by design** - no client and no developer should be locked to one AI tool to work with our software.

---

## Based in Poland - our home market and where we started

We began by solving this for Polish law firms, and that stack is the deepest we ship: the Polish edition of Patron, connectors for [ISAP](https://github.com/matematicsolutions/mcp-isap) (legislation), [SAOS](https://github.com/matematicsolutions/mcp-saos) (common and supreme courts), [NSA/CBOSA](https://github.com/matematicsolutions/mcp-nsa) (administrative courts, 2.39M rulings), [KRS](https://github.com/matematicsolutions/mcp-krs) (company register), [EUREKA](https://github.com/matematicsolutions/mcp-eureka) (517k+ tax interpretations) and [KIO](https://github.com/matematicsolutions/kio-orzeczenia-mcp) (public procurement), plus a full set of GDPR-native open skills for contract review, anonymization, output verification, AI-readiness assessment and legal-aid clinics. The 41-skill Polish hub covers the whole firm workflow. Polish catalogue: **[matematicsolutions.com](https://matematicsolutions.com)**.

## Contact

- **Website**: [matematicsolutions.com/en](https://matematicsolutions.com/en/)
- **Boutique**: [matematicsolutions.com/en/boutique](https://matematicsolutions.com/en/boutique)
- **Email**: [kontakt@matematic.co](mailto:kontakt@matematic.co)
- **LinkedIn**: [Wieslaw Mazur](https://www.linkedin.com/in/wies%C5%82aw-mazur-535428364/)

---

<div align="center">

*AI that knows what it doesn't know - we know how.*
<br>
Built in Poland, for law firms in every jurisdiction where the law is public. That is why Patron speaks nine languages, and counting.

</div>
