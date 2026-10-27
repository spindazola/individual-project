# Project Decisions

## 2026-10-13 - Dataset
Use CheXpert as the primary dataset rather than the medical-school tabular dataset.

## 2026-10-13 - Initial formulation
Begin with a simplified single-label multiclass problem using approximately 10 conditions. Multi-label classification remains optional if time permits.

## 2026-10-13 - Objective
The project is about uncertainty quantification, calibration, reliability and reproducibility rather than state-of-the-art diagnostic performance.

## 2026-10-13 - Writing strategy
Build the dissertation incrementally through short technical reports. Report 1 covers conformal prediction theory; Report 2 covers CheXpert and the medical-ML context.
# DECISIONS — Additions from 20 October 2026

## Compare patient-level and image-level calibration
**Decision:** Test both image-level and patient-level calibration.

**Rationale:** Patient-level calibration is closer to the clinical decision unit, while image-level calibration provides a useful comparison.

## Compare calibration view composition
**Decision:** Compare mixed frontal+lateral calibration with frontal-only calibration.

**Rationale:** Calibration should resemble deployment conditions; view mismatch may affect coverage and efficiency.

## Efficiency metric
**Decision:** Treat prediction-set size as the primary efficiency measure alongside coverage.

## Immediate dataset task
**Decision:** Compute CheXpert label statistics before more model development.

Required statistics:
- exactly-one-positive count/proportion;
- single-positive counts by condition;
- positive/uncertain/negative/blank counts by observation;
- frontal/lateral breakdown;
- patient repetition.
