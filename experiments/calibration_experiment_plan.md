# Experiment Plan — Calibration Decisions

## Research idea
Hold the underlying classifier and conformal method fixed as far as possible, then vary calibration design decisions. This isolates calibration methodology from classifier quality.

## Experiment A — Calibration unit
### A1: Image-level calibration
Randomly select calibration images.

### A2: Patient-level calibration
Partition patients first so images from the same patient do not cross the relevant split boundary.

### Compare
- marginal coverage;
- per-condition coverage;
- mean/median set size;
- set-size distribution;
- worst-condition coverage.

## Experiment B — View composition
### B1: Mixed-view calibration
Calibration contains frontal and lateral images.

### B2: Frontal-only calibration
Calibration contains frontal images only.

### Compare
- marginal coverage;
- efficiency;
- condition-specific behaviour.

## Experiment C — Calibration-set size
Repeat A/B at several calibration sizes and random seeds. Track realised coverage, class-wise coverage, and prediction-set size.

## Interpretation
A calibration design may be statistically valid but inefficient, efficient on average but poor for a subset, or well matched to one image type but unreliable under view mismatch.
