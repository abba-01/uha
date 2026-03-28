#!/usr/bin/env python3
"""
Zenodo Metadata Update Script
Eric D. Martin — All Your Baseline LLC
2026-03-27

SAFE: Merges new fields INTO existing metadata. Never replaces full records.
Does NOT create new versions. Does NOT reset view/download counts.

Usage:
    export ZENODO_TOKEN=your_token_here
    python3 zenodo_metadata_update.py [--dry-run] [--record ID]

Options:
    --dry-run     Print what would change, don't POST anything
    --record ID   Run only for this record ID
"""

import os, sys, json, time, requests

TOKEN = os.environ.get("ZENODO_TOKEN", "")
BASE = "https://zenodo.org/api"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
DRY_RUN = "--dry-run" in sys.argv
ONLY_RECORD = None
for i, a in enumerate(sys.argv):
    if a == "--record" and i+1 < len(sys.argv):
        ONLY_RECORD = sys.argv[i+1]

if not TOKEN:
    print("ERROR: Set ZENODO_TOKEN environment variable")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Community slugs to add to ALL records
# ---------------------------------------------------------------------------
ALL_COMMUNITIES = ["cosmology", "astrophysics"]
COSMO_COMMUNITIES = ALL_COMMUNITIES + ["non-standard_cosmology_and_astrophysics"]

# ---------------------------------------------------------------------------
# External landmark DOIs (relation type: references)
# ---------------------------------------------------------------------------
EXT_PLANCK   = {"identifier": "10.1051/0004-6361/201833910", "relation": "references", "resource_type": "publication"}
EXT_RIESS    = {"identifier": "10.3847/2041-8213/ac5c5b",   "relation": "references", "resource_type": "publication"}
EXT_PANTHEON = {"identifier": "10.3847/1538-4357/ac8e04",   "relation": "references", "resource_type": "publication"}
EXT_VERDE    = {"identifier": "10.1038/s41550-019-0902-0",  "relation": "references", "resource_type": "publication"}
EXT_DIVALENTINO = {"identifier": "10.1088/1361-6382/ac086d", "relation": "references", "resource_type": "publication"}

def doi(zenodo_id, relation, rtype="software"):
    return {"identifier": f"10.5281/zenodo.{zenodo_id}", "relation": relation, "resource_type": rtype}

# ---------------------------------------------------------------------------
# Per-record update specifications
# ---------------------------------------------------------------------------
UPDATES = {

    # --- N/U Algebra standalone (HIGHEST PRIORITY — 402 downloads) ---
    "17172694": {
        "communities": COSMO_COMMUNITIES + ["nasa-ads"],
        "keywords_add": [
            "N/U Algebra", "uncertainty quantification", "conservative uncertainty propagation",
            "interval arithmetic", "O(1) complexity", "4844x faster than Monte Carlo",
            "Hubble tension", "Universal Horizon Address", "UHA", "cosmological parameters",
            "uncertainty algebra", "reproducibility", "Python", "R", "open source"
        ],
        "related_add": [
            doi("19154280", "isReferencedBy", "publication"),
            doi("19230366", "isReferencedBy", "publication"),
            doi("19232340", "isReferencedBy", "publication"),
            doi("17221863", "isSupplementedBy", "dataset"),
            doi("17439632", "isSupplementedBy"),
            doi("17439738", "isSupplementedBy"),
            EXT_PLANCK, EXT_VERDE, EXT_DIVALENTINO,
        ],
        "description_append": (
            "\n\nThis work is the uncertainty propagation foundation (Layer 2) of the "
            "Universal Horizon Address (UHA) framework. Applied to the Hubble tension, "
            "N/U Algebra produces closed-form uncertainty bounds 4,844× faster than Monte Carlo "
            "while remaining strictly conservative. "
            "Companion paper: The Hubble Tension as a Measurement Artifact "
            "(10.5281/zenodo.19230366). Pre-registered predictions against Euclid DR1 "
            "(October 2026): 10.5281/zenodo.19232340."
        ),
    },

    # --- Hubble Tension manuscript — concept DOI ---
    "19154280": {
        "communities": COSMO_COMMUNITIES + ["nasa-ads"],
        "keywords_add": [
            "93% tension reduction", "ξ coordinate", "horizon-normalized coordinates",
            "frame-mixing artifact", "0.16σ residual", "MNRAS Letters submission",
            "UHA", "Universal Horizon Address", "observer domain tensor", "JWST", "TRGB"
        ],
        "related_add": [
            doi("19232340", "isReferencedBy", "publication"),
            doi("19230683", "isSupplementedBy"),
            doi("19230685", "isSupplementedBy"),
            doi("19230689", "isSupplementedBy", "dataset"),
            doi("17172694", "isSupplementedBy", "publication"),
            doi("19216432", "isSupplementedBy"),
            {"identifier": "10.1051/0004-6361/201833910", "relation": "references", "resource_type": "publication"},
            {"identifier": "10.3847/2041-8213/ac5c5b",   "relation": "references", "resource_type": "publication"},
            {"identifier": "10.3847/1538-4357/ac8e04",   "relation": "references", "resource_type": "publication"},
        ],
    },

    # --- Hubble Tension manuscript — v3 submitted ---
    "19230366": {
        "communities": COSMO_COMMUNITIES + ["nasa-ads"],
        "keywords_add": [
            "MNRAS Letters", "version 3", "submitted 2026-03-25",
            "93% tension reduction", "ξ normalization", "frame artifact",
            "0.16σ residual", "UHA", "JWST", "TRGB", "EDE reply"
        ],
        "related_add": [
            doi("19232340", "isReferencedBy", "publication"),
            doi("19230685", "isSupplementedBy"),
            doi("19230689", "isSupplementedBy", "dataset"),
            doi("17172694", "isSupplementedBy", "publication"),
            {"identifier": "10.1051/0004-6361/201833910", "relation": "references", "resource_type": "publication"},
            {"identifier": "10.3847/2041-8213/ac5c5b",   "relation": "references", "resource_type": "publication"},
            {"identifier": "10.3847/1538-4357/ac8e04",   "relation": "references", "resource_type": "publication"},
        ],
    },

    # --- Paper 2 pre-registration (currently almost empty) ---
    "19232340": {
        "resource_type": {"type": "publication", "subtype": "report"},
        "communities": COSMO_COMMUNITIES,
        "keywords_add": [
            "pre-registration", "Euclid DR1", "October 2026", "cosmological tensions",
            "dark energy", "w0wa", "w0=-0.634", "wa=-1.388",
            "baryon acoustic oscillations", "DESI DR1", "S8 tension", "H0 tension",
            "partition analysis", "falsifiable predictions", "UHA", "xi coordinate",
            "Omega_m deficit", "Delta-chi2=4.74", "structure growth", "patent pending"
        ],
        "related_add": [
            doi("19154280", "references", "publication"),
            doi("19230366", "references", "publication"),
            doi("19230683", "isSupplementedBy"),
            doi("19230689", "isSupplementedBy", "dataset"),
            doi("17172694", "isSupplementedBy", "publication"),
            doi("17482416", "isSupplementedBy"),
            EXT_PLANCK, EXT_RIESS, EXT_DIVALENTINO, EXT_VERDE,
        ],
        "description_set": (
            "Pre-registration timestamping three falsifiable predictions ahead of Euclid DR1 "
            "(expected October 21, 2026): "
            "(1) S8 = 0.808 ± 0.017 confirmed by Euclid weak lensing; "
            "(2) w₀wₐ dark energy signal with Δχ² > 4, w₀ ≈ −0.634, wₐ ≈ −1.388; "
            "(3) Lyα D_H/r_s excess consistent with w(z>2) < −1. "
            "Builds on Paper 1 (10.5281/zenodo.19230366). "
            "Three-component tension hierarchy: ~93% H₀ frame artifact (removed by ξ-normalization), "
            "~5% Ω_m deficit (DESI DR1 confirmed, Ω_m = 0.295 ± 0.010), "
            "~2% w₀wₐ dark energy signal. "
            "Framework: Universal Horizon Address (UHA), patent pending US 63/902,536. "
            "Companion manuscript submitted to ApJL 2026-03-27."
        ),
    },

    # --- N/U Algebra dataset ---
    "17221863": {
        "communities": COSMO_COMMUNITIES,
        "keywords_add": [
            "N/U Algebra", "uncertainty dataset", "benchmark data",
            "fixed random seeds", "reproducibility", "Monte Carlo comparison",
            "Hubble tension", "cosmological parameters"
        ],
        "related_add": [
            doi("17172694", "isSupplementTo", "publication"),
            doi("17439632", "isSupplementTo"),
            doi("19230366", "isReferencedBy", "publication"),
        ],
    },

    # --- hubble-tension-resolution (69 views — creator: "abba-01") ---
    "17435578": {
        "fix_creators": True,
        "communities": COSMO_COMMUNITIES,
        "keywords_add": [
            "Hubble tension resolution", "UHA", "xi normalization",
            "frame artifact", "conservative uncertainty", "open source", "Python"
        ],
        "related_add": [
            doi("19154280", "isSupplementTo", "publication"),
            doi("19230366", "isSupplementTo", "publication"),
            doi("17172694", "isSupplementedBy", "publication"),
            EXT_PLANCK, EXT_RIESS,
        ],
    },

    # --- hubble-bubble (58 views) ---
    "17388283": {
        "communities": COSMO_COMMUNITIES,
        "keywords_add": [
            "Hubble bubble", "local void", "KBC void", "bulk flow",
            "peculiar velocity", "local structure", "Hubble tension"
        ],
        "related_add": [
            doi("19154280", "isSupplementTo", "publication"),
            doi("17172694", "isSupplementedBy", "publication"),
            EXT_PLANCK,
        ],
    },

    # --- hubble-97pct-observer-tensor ---
    "17438915": {
        "communities": COSMO_COMMUNITIES,
        "keywords_add": [
            "observer domain tensor", "97% concordance", "epistemic distance",
            "UHA", "Hubble tension", "measurement context"
        ],
        "related_add": [
            doi("19154280", "isSupplementTo", "publication"),
            doi("17172694", "isSupplementedBy", "publication"),
            doi("19216432", "references"),
        ],
    },

    # --- hubble-91pct-concordance v1.2.0 ---
    "19216432": {
        "communities": COSMO_COMMUNITIES,
        "keywords_add": [
            "91% concordance", "UHA restoration", "xi encoding",
            "NGC 4258 anchor", "52 HII objects", "N/U Algebra", "v1.2.0"
        ],
        "related_add": [
            doi("17438911", "isNewVersionOf"),
            doi("19230366", "isSupplementTo", "publication"),
            doi("17172694", "isSupplementedBy", "publication"),
        ],
    },

    # --- hubble-91pct v1.0.1 ---
    "17438911": {
        "communities": COSMO_COMMUNITIES,
        "keywords_add": ["91% concordance", "v1.0.1", "N/U Algebra", "Hubble tension"],
        "related_add": [
            doi("19216432", "isNewVersionOf"),
            doi("19154280", "isSupplementTo", "publication"),
            doi("17172694", "isSupplementedBy", "publication"),
        ],
    },

    # --- hubble-99pct-montecarlo ---
    "17438913": {
        "communities": COSMO_COMMUNITIES,
        "keywords_add": ["Monte Carlo", "MCMC", "99% concordance", "Hubble tension", "reproducibility"],
        "related_add": [
            doi("19154280", "isSupplementTo", "publication"),
            doi("17172694", "isSupplementedBy", "publication"),
        ],
    },

    # --- uha (abba-01) — WRONG CREATORS: djbrout/ariess1/dscolnic/EDM/Anthony Carr ---
    "19230683": {
        "fix_creators": True,
        "communities": COSMO_COMMUNITIES,
        "keywords_add": [
            "Universal Horizon Address", "UHA", "xi normalization", "horizon address",
            "Hubble tension", "cosmological coordinates", "patent pending", "US 63/902,536"
        ],
        "related_add": [
            doi("19154280", "isSupplementTo", "publication"),
            doi("19232340", "isSupplementTo", "publication"),
            doi("17172694", "isSupplementedBy", "publication"),
            doi("19230685", "isSupplementedBy"),
        ],
    },

    # --- uha_hubble ---
    "19230685": {
        "communities": COSMO_COMMUNITIES,
        "keywords_add": ["UHA", "Hubble tension analysis", "xi normalization", "cosmological distances"],
        "related_add": [
            doi("19230683", "isSupplementTo"),
            doi("19154280", "isSupplementTo", "publication"),
            doi("17172694", "isSupplementedBy", "publication"),
        ],
    },

    # --- uha-blackbox (creator: "abba-01") ---
    "17435574": {
        "fix_creators": True,
        "communities": COSMO_COMMUNITIES,
        "keywords_add": ["UHA", "blackbox", "xi encoding", "horizon address", "Hubble tension"],
        "related_add": [
            doi("19230683", "references"),
            doi("19154280", "isSupplementTo", "publication"),
        ],
    },

    # --- cosmological-data ---
    "19230689": {
        "resource_type": {"type": "dataset"},
        "communities": COSMO_COMMUNITIES,
        "keywords_add": [
            "Pantheon+", "SH0ES", "Planck CMB", "cosmological dataset",
            "Hubble tension data", "open data", "reproducibility"
        ],
        "related_add": [
            doi("19154280", "isSupplementTo", "publication"),
            doi("19230366", "isSupplementTo", "publication"),
            EXT_PLANCK, EXT_RIESS, EXT_PANTHEON,
        ],
    },

    # --- nu-algebra software ---
    "17439632": {
        "communities": COSMO_COMMUNITIES,
        "keywords_add": [
            "N/U Algebra", "uncertainty propagation", "Python", "R",
            "conservative bounds", "reproducibility", "open source"
        ],
        "related_add": [
            doi("17172694", "isSupplementTo", "publication"),
            doi("17221863", "isSupplementedBy", "dataset"),
            doi("19154280", "isReferencedBy", "publication"),
        ],
    },

    # --- un-algebra ---
    "17439738": {
        "communities": COSMO_COMMUNITIES,
        "keywords_add": ["U/N Algebra", "uncertainty algebra", "inverse N/U", "Hubble tension"],
        "related_add": [
            doi("17172694", "references", "publication"),
            doi("17444740", "isNewVersionOf"),
            doi("19154280", "isReferencedBy", "publication"),
        ],
    },

    # --- un-algebra-reanchor ---
    "17444740": {
        "communities": COSMO_COMMUNITIES,
        "keywords_add": ["U/N Algebra", "reanchor", "uncertainty reanchoring", "Hubble tension"],
        "related_add": [
            doi("17439738", "isNewVersionOf"),
            doi("17172694", "references", "publication"),
        ],
    },

    # --- unalgebra (abba-01) ---
    "19230687": {
        "communities": COSMO_COMMUNITIES,
        "keywords_add": ["N/U Algebra", "uncertainty algebra", "open source", "Python"],
        "related_add": [
            doi("17172694", "isSupplementTo", "publication"),
            doi("19154280", "isReferencedBy", "publication"),
        ],
    },

    # --- cosmo-sterile-audit ---
    "17482416": {
        "communities": COSMO_COMMUNITIES,
        "keywords_add": ["sterile neutrino", "cosmological audit", "Hubble tension", "ΛCDM"],
        "related_add": [
            doi("19154280", "references", "publication"),
            doi("17172694", "references", "publication"),
        ],
    },

    # --- multiresolution-cosmology ---
    "17487909": {
        "communities": COSMO_COMMUNITIES,
        "keywords_add": ["multiresolution", "cosmology", "Hubble tension", "UHA"],
        "related_add": [
            doi("19154280", "references", "publication"),
            doi("19230683", "references"),
        ],
    },

    # --- hubble-mc-package2 ---
    "19230720": {
        "communities": COSMO_COMMUNITIES,
        "keywords_add": ["Monte Carlo", "Hubble tension", "MCMC", "uncertainty quantification"],
        "related_add": [
            doi("17438913", "isNewVersionOf"),
            doi("17172694", "isSupplementedBy", "publication"),
            doi("19154280", "isSupplementTo", "publication"),
        ],
    },

    # --- ommp (creator: "EDM") ---
    "17438948": {
        "fix_creators": True,
        "communities": ALL_COMMUNITIES,
        "keywords_add": ["OMMP", "observer measurement model", "epistemic framework"],
        "related_add": [
            doi("17172694", "references", "publication"),
            doi("19154280", "references", "publication"),
        ],
    },

    # --- said (creator: "EDM") ---
    "17438950": {
        "fix_creators": True,
        "communities": ALL_COMMUNITIES,
        "keywords_add": ["SAID", "AI transparency", "scientific AI disclosure", "open science"],
        "related_add": [
            doi("19230718", "isNewVersionOf"),
        ],
    },

    # --- said-framework (aybllc) ---
    "19230718": {
        "communities": ALL_COMMUNITIES,
        "keywords_add": ["SAID framework", "AI transparency", "scientific AI", "open science"],
        "related_add": [
            doi("17438950", "isPreviousVersionOf"),
        ],
    },

    # --- ebios ---
    "17477521": {
        "communities": ALL_COMMUNITIES,
        "keywords_add": [
            "eBIOS", "formal verification", "Lean 4", "100% proof coverage",
            "October 2025", "8/8 theorems", "zero sorry"
        ],
        "related_add": [
            doi("19230683", "references"),
            doi("17172694", "references", "publication"),
        ],
    },

    # --- autonomoustheory (creator: "EDM") ---
    "17438961": {
        "fix_creators": True,
        "communities": ALL_COMMUNITIES,
        "keywords_add": ["autonomous theory", "open science", "theoretical framework"],
        "related_add": [],
    },

    # --- uha-api-service ---
    "19230695": {
        "communities": COSMO_COMMUNITIES,
        "keywords_add": ["UHA", "API", "horizon address service", "Python", "open source"],
        "related_add": [
            doi("19230683", "isSupplementTo"),
        ],
    },

    # --- aiwared ---
    "19230677": {
        "communities": ALL_COMMUNITIES,
        "keywords_add": ["AIWared", "AI awareness", "AI transparency", "open source"],
        "related_add": [],
    },

    # --- uha v1 (Hubble Tension manuscript v1) ---
    "19154281": {
        "communities": COSMO_COMMUNITIES,
        "keywords_add": ["version 1", "initial submission", "Hubble tension", "UHA"],
        "related_add": [
            doi("19154280", "isVersionOf", "publication"),
            doi("19211662", "isNewVersionOf", "publication"),
            {"identifier": "10.1051/0004-6361/201833910", "relation": "references", "resource_type": "publication"},
            {"identifier": "10.3847/2041-8213/ac5c5b",   "relation": "references", "resource_type": "publication"},
        ],
    },

    # --- Hubble Tension manuscript v2 ---
    "19211662": {
        "communities": COSMO_COMMUNITIES,
        "keywords_add": ["version 2", "March 2026", "Hubble tension", "UHA"],
        "related_add": [
            doi("19154280", "isVersionOf", "publication"),
            doi("19154281", "isPreviousVersionOf", "publication"),
            doi("19230366", "isNewVersionOf", "publication"),
            {"identifier": "10.1051/0004-6361/201833910", "relation": "references", "resource_type": "publication"},
            {"identifier": "10.3847/2041-8213/ac5c5b",   "relation": "references", "resource_type": "publication"},
        ],
    },
}

# ---------------------------------------------------------------------------
# API helpers
# ---------------------------------------------------------------------------

def get_deposit(record_id):
    """Get the editable deposit for a record (unlocks it)."""
    r = requests.get(f"{BASE}/deposit/depositions", params={"q": f"recid:{record_id}"}, headers=HEADERS)
    r.raise_for_status()
    results = r.json()
    if not results:
        # Try direct
        r2 = requests.get(f"{BASE}/deposit/depositions/{record_id}", headers=HEADERS)
        if r2.status_code == 200:
            return r2.json()
        return None
    return results[0]

def unlock_deposit(deposit_id):
    """Unlock a published record for editing."""
    r = requests.post(f"{BASE}/deposit/depositions/{deposit_id}/actions/edit", headers=HEADERS)
    if r.status_code == 201:
        return r.json()
    elif r.status_code == 400:
        # Already unlocked
        return requests.get(f"{BASE}/deposit/depositions/{deposit_id}", headers=HEADERS).json()
    r.raise_for_status()

CANONICAL_CREATOR = {"name": "Martin, Eric D.", "orcid": "0009-0006-5944-1742", "affiliation": "All Your Baseline LLC"}
BAD_CREATOR_NAMES = {"djbrout", "ariess1", "dscolnic", "EDM", "Anthony Carr", "abba-01"}

def update_metadata(deposit_id, current_meta, spec):
    """Merge spec into current metadata and PUT."""
    meta = dict(current_meta)

    # Keywords: merge, deduplicate
    existing_kw = set(meta.get("keywords", []))
    new_kw = set(spec.get("keywords_add", []))
    meta["keywords"] = sorted(existing_kw | new_kw)

    # Related identifiers: merge, deduplicate by identifier+relation
    existing_rel = meta.get("related_identifiers", [])
    existing_keys = {(r["identifier"], r["relation"]) for r in existing_rel}
    for rel in spec.get("related_add", []):
        key = (rel["identifier"], rel["relation"])
        if key not in existing_keys:
            existing_rel.append(rel)
            existing_keys.add(key)
    meta["related_identifiers"] = existing_rel

    # Description: append or set
    if "description_set" in spec:
        meta["description"] = spec["description_set"]
    elif "description_append" in spec:
        meta["description"] = meta.get("description", "") + spec["description_append"]

    # Creator fix: remove bad names, ensure canonical creator present
    if spec.get("fix_creators"):
        creators = meta.get("creators", [])
        cleaned = [c for c in creators if c.get("name","") not in BAD_CREATOR_NAMES]
        # Normalize "Martin, Eric" / "Eric D. Martin" / "Martin, Eric D."
        final = []
        has_edm = False
        for c in cleaned:
            n = c.get("name","")
            if "Martin" in n or "martin" in n:
                if not has_edm:
                    final.append(CANONICAL_CREATOR)
                    has_edm = True
            else:
                final.append(c)
        if not has_edm:
            final.insert(0, CANONICAL_CREATOR)
        meta["creators"] = final

    # Resource type fix
    if "resource_type" in spec:
        meta["resource_type"] = spec["resource_type"]

    return meta

def put_metadata(deposit_id, meta):
    payload = {"metadata": meta}
    r = requests.put(
        f"{BASE}/deposit/depositions/{deposit_id}",
        headers=HEADERS,
        data=json.dumps(payload)
    )
    r.raise_for_status()
    return r.json()

def publish(deposit_id):
    r = requests.post(f"{BASE}/deposit/depositions/{deposit_id}/actions/publish", headers=HEADERS)
    r.raise_for_status()
    return r.json()

def add_communities(deposit_id, community_slugs):
    """Add communities to a deposit."""
    for slug in community_slugs:
        r = requests.post(
            f"{BASE}/deposit/depositions/{deposit_id}/communities",
            headers=HEADERS,
            data=json.dumps({"identifier": slug})
        )
        # 200 = added, 400 = already member or doesn't exist — both ok
        if r.status_code not in (200, 201, 400):
            print(f"  WARNING: community {slug} returned {r.status_code}")

# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------

def process_record(record_id, spec):
    print(f"\n{'='*60}")
    print(f"Record: {record_id} | DOI: 10.5281/zenodo.{record_id}")

    # 1. Get deposit
    deposit = get_deposit(record_id)
    if not deposit:
        print(f"  ERROR: Could not find deposit for {record_id}")
        return

    deposit_id = deposit["id"]
    current_meta = deposit["metadata"]
    print(f"  Title: {current_meta.get('title', '(no title)')[:60]}")
    print(f"  Current keywords: {len(current_meta.get('keywords', []))}")
    print(f"  Current related: {len(current_meta.get('related_identifiers', []))}")
    print(f"  Adding keywords: {len(spec.get('keywords_add', []))}")
    print(f"  Adding related: {len(spec.get('related_add', []))}")
    print(f"  Adding communities: {spec.get('communities', [])}")

    if DRY_RUN:
        new_meta = update_metadata(deposit_id, current_meta, spec)
        print(f"  [DRY RUN] Would set {len(new_meta['keywords'])} keywords, "
              f"{len(new_meta.get('related_identifiers', []))} related identifiers")
        return

    # 2. Unlock
    print(f"  Unlocking deposit {deposit_id}...")
    unlocked = unlock_deposit(deposit_id)

    # 3. Build new metadata
    new_meta = update_metadata(deposit_id, current_meta, spec)

    # 4. PUT metadata
    print(f"  Writing metadata...")
    put_metadata(deposit_id, new_meta)

    # 5. Add communities (separate endpoint)
    if spec.get("communities"):
        print(f"  Adding communities...")
        add_communities(deposit_id, spec["communities"])

    # 6. Publish
    print(f"  Publishing...")
    publish(deposit_id)

    print(f"  DONE: 10.5281/zenodo.{record_id} updated.")
    time.sleep(1)  # Rate limit courtesy

if __name__ == "__main__":
    if not TOKEN or TOKEN == "YOUR_ZENODO_TOKEN_HERE":
        print("ERROR: ZENODO_TOKEN not set. Run:")
        print("  export ZENODO_TOKEN=your_token_here")
        print("  python3 zenodo_metadata_update.py --dry-run")
        sys.exit(1)

    # Priority order: heavy hitters first, then by view count
    priority_order = [
        "17172694",  # N/U Algebra standalone — 402 downloads
        "19154280",  # Manuscript concept DOI — 29 views
        "19230366",  # Manuscript v3 submitted — 29 views
        "19232340",  # Pre-registration — almost empty
        "17221863",  # N/U Algebra dataset — 146 views
        "17435578",  # hubble-tension-resolution — 69 views
        "17388283",  # hubble-bubble — 58 views
        "17438915",  # hubble-97pct — 29 views
        "19216432",  # hubble-91pct v1.2.0 — 21 views
        "17438911",  # hubble-91pct v1.0.1 — 21 views
        "17438913",  # hubble-99pct-montecarlo — 21 views
        "19230683",  # uha software — 19 views
        "17477521",  # ebios — 19 views
        "17487909",  # multiresolution-cosmology — 19 views
        "17439632",  # nu-algebra software — 18 views
        "19230695",  # uha-api-service — 18 views
        "17435574",  # uha-blackbox — 16 views
        "17439738",  # un-algebra — 20 views
        "17444740",  # un-algebra-reanchor — 20 views
        "17482416",  # cosmo-sterile-audit — 20 views
        "17438948",  # ommp — 9 views
        "19211662",  # manuscript v2
        "19154281",  # manuscript v1
        "19230687",  # unalgebra abba
        "19230689",  # cosmological-data
        "19230720",  # hubble-mc-package2
        "17438950",  # said abba
        "19230718",  # said-framework
        "17438961",  # autonomoustheory
        "19230677",  # aiwared
        "19230685",  # uha_hubble
    ]

    records_to_process = [r for r in priority_order if r in UPDATES]

    if ONLY_RECORD:
        records_to_process = [ONLY_RECORD] if ONLY_RECORD in UPDATES else []
        if not records_to_process:
            print(f"ERROR: Record {ONLY_RECORD} not in update spec")
            sys.exit(1)

    print(f"Zenodo Metadata Update — {'DRY RUN' if DRY_RUN else 'LIVE'}")
    print(f"Records to process: {len(records_to_process)}")

    for record_id in records_to_process:
        try:
            process_record(record_id, UPDATES[record_id])
        except Exception as e:
            print(f"  ERROR on {record_id}: {e}")
            continue

    print(f"\n{'='*60}")
    print("Complete.")
