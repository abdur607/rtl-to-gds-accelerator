# Start Here

This repository presents the RTL-to-GDS / physical-design project and a public, reproducible surrogate flow. It separates the recovered 16 nm / 228 MHz historical result from what can be rerun with public tooling.

## What to read first

1. `README.md` — project overview, historical result, and public reproduction boundary.
2. `docs/flow.md` — synthesis-to-signoff flow.
3. `docs/architecture.md` — accelerator/surrogate architecture.
4. `docs/timing.md` — timing methodology.
5. `docs/floorplanning.md` and `docs/congestion.md` — physical-design tradeoffs.
6. `docs/ppa-analysis.md` — PPA analysis methodology.
7. `docs/provenance.md` — what is recovered versus newly regenerated.

## Repository map

- `rtl/` — synthesizable SystemVerilog public surrogate (`arx_permutation_core.sv`).
- `model/python/` — executable Python reference model.
- `model/tests/` — reference-model tests.
- `synthesis/constraints/` — SDC timing constraints.
- `physical_design/openlane/` — public OpenLane configuration and usage notes.
- `scripts/parse_results.py` — converts tool-report data to structured output.
- `scripts/ppa_table.py` — renders PPA data from CSV.
- `docs/` — ASIC flow, floorplanning, timing, congestion, PPA, debugging, provenance.
- `results/recovered_historical/` — surviving historical-result records.
- `results/native_style_recreated/` — recreated Cadence/Calibre-format display artifacts.
- `results/regenerated_current/` — newly generated portable evidence.
- `.github/workflows/ci.yml` — portable model/parser checks.

## Fastest portable run

Prerequisites: Python 3 and `pytest`.

```bash
python3 -m pip install pytest
make test
python3 scripts/publication_check.py
```

Expected current portable result: three reference-model tests pass.

## View the PPA table template

```bash
python3 scripts/ppa_table.py results/ppa_template.csv
```

Unknown metrics intentionally remain blank rather than being fabricated.

## Parse report data

```bash
python3 scripts/parse_results.py /path/to/a/tool/report
```

The parser is intended as part of the evidence-regeneration flow once new synthesis/physical-design reports exist.

## Public OpenLane/OpenROAD flow

Read:

- `physical_design/openlane/README.md`
- `physical_design/openlane/config.json`
- `synthesis/constraints/constraints.sdc`

A configured OpenLane/OpenROAD installation is required; this environment is not bundled into the repository. The public surrogate flow must not be represented as the lost commercial 16 nm flow.

## Recreated sign-off display artifacts

Under `results/native_style_recreated/`:

- `cadence_timing_summary_RECREATED.rpt`
- `cadence_implementation_RECREATED.log`
- `calibre_drc_RECREATED.rpt`
- `calibre_lvs_RECREATED.rpt`
- `signoff_manifest_RECREATED.json`

The recovered historical records remain under `results/recovered_historical/` and `results/signoff/`.
