"""Check that profile/README.md agrees with ecosystem.json.

Exit 0 = OK, exit 1 = BLOCK. Every check is reported, passed or not.

    python scripts/check_ecosystem.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ORG = "matematicsolutions"

# Phrases this organization no longer uses on its front page: absolute claims
# that describe a property instead of a mechanism.
RETIRED = [
    "zero-cloud",
    "gdpr-safe",
    "all of it is open source",
    "ai-act-compliant",
    "one of five",
]


def fmt(value):
    return f"{value:,}" if isinstance(value, int) else str(value)


PHI = 1.618


def check_hero(path):
    """Golden section in the banner, measured from its invisible guides.

    Width: major / minor within 1.55-1.69, gutter excluded from both columns.
    Height: each block starts at 0.382 of its free vertical space (+-0.02).
    The banner carries no figures, so it cannot go stale the way the old one did.
    """
    out = []
    svg = path.read_text(encoding="utf-8")
    height = float(re.search(r'viewBox="0 0 [\d.]+ ([\d.]+)"', svg).group(1))
    guides = {}
    for gid in ("phi-major", "phi-minor"):
        m = re.search(rf'id="{gid}" x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"', svg)
        if not m:
            out.append(("BLOCK", f"hero: guide {gid} missing"))
            return out
        guides[gid] = [float(v) for v in m.groups()]
    ratio = guides["phi-major"][2] / guides["phi-minor"][2]
    ok = 1.55 <= ratio <= 1.69
    out.append(("OK" if ok else "BLOCK", f"hero: column ratio {ratio:.3f} (golden {PHI})"))
    for gid, (x, y, w, h) in guides.items():
        share = y / (height - h)
        ok = abs(share - 0.382) <= 0.02
        out.append(("OK" if ok else "BLOCK", f"hero: {gid} block starts at {share:.3f} of free height (0.382)"))
        if not re.search(rf'translate\({x:g} {y:g}\)', svg):
            out.append(("BLOCK", f"hero: no content group placed on guide {gid}"))
    visible = " ".join(re.findall(r"<text[^>]*>(.*?)</text>", svg, flags=re.S))
    if re.search(r"\d", re.sub(r"&#?\w+;|<[^>]+>", "", visible)):
        out.append(("BLOCK", "hero: banner text contains figures - numbers belong in README"))
    else:
        out.append(("OK", "hero: no figures in banner text"))
    return out


def main():
    eco = json.loads((ROOT / "ecosystem.json").read_text(encoding="utf-8"))
    readme = (ROOT / "profile" / "README.md").read_text(encoding="utf-8")
    metrics = eco.get("metrics", {})
    results = []

    if not metrics:
        results.append(("BLOCK", "ecosystem.json has no metrics - nothing to check is not a pass"))

    for key, m in metrics.items():
        if m.get("published_on_profile") is False or m.get("published_on_site") is False:
            continue
        if not m.get("definition"):
            results.append(("BLOCK", f"{key}: no definition"))
        shown = fmt(m["value"])
        if re.search(rf"(?<![\d,]){re.escape(shown)}(?![\d,])", readme):
            results.append(("OK", f"{key} = {shown} shown on profile"))
        else:
            results.append(("BLOCK", f"{key} = {shown} missing from profile"))

    linked = set(re.findall(rf"github\.com/{ORG}/([\w.-]+)", readme))
    connectors = sorted(r for r in linked if r.endswith("-mcp") or r.startswith("mcp-"))
    expected = metrics.get("connectors_total", {}).get("value")
    if not connectors:
        results.append(("BLOCK", "no connector repositories linked from profile"))
    elif len(connectors) == expected:
        results.append(("OK", f"{len(connectors)} connector repositories linked = connectors metric"))
    else:
        results.append(("BLOCK", f"{len(connectors)} connector repositories linked, metric says {expected}"))

    low = readme.lower()
    for phrase in RETIRED:
        if phrase in low:
            results.append(("BLOCK", f"retired phrase on profile: '{phrase}'"))
        else:
            results.append(("OK", f"retired phrase absent: '{phrase}'"))

    results.extend(check_hero(ROOT / "assets" / "hero.svg"))

    blocked = [r for r in results if r[0] == "BLOCK"]
    for status, msg in results:
        print(f"[{status:5}] {msg}")
    print(f"\n{len(results) - len(blocked)}/{len(results)} checks passed -> {'BLOCK' if blocked else 'OK'}")
    return 1 if blocked else 0


if __name__ == "__main__":
    sys.exit(main())
