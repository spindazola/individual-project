# Individual Project Context

## Project
**Title:** Marginal and condition-specific reliability of conformal prediction in chest X-ray classification

**Supervisor:** Dr Nery Riquelme-Granada

## Research problem
Conformal prediction gives marginal coverage guarantees, but good overall coverage can conceal under-coverage for individual conditions. The project investigates this in chest X-ray classification and studies how calibration choices, conformity scores and data splitting affect reliability and reproducibility.

## Dataset direction
CheXpert is the primary dataset. Initial work uses a simplified single-label multiclass formulation with approximately 10 selected conditions. Multi-label classification is a possible extension.

## Scope
- Focus on uncertainty quantification rather than state-of-the-art classifier performance.
- Use 2-3 relatively simple classifiers as controlled experimental models.
- Implement split conformal prediction and verify nominal marginal coverage.
- Measure condition-specific empirical coverage.
- Compare calibration strategies and conformity scores.
- Evaluate prediction-set size.
- Repeat experiments across calibration splits / seeds.
- Do not claim instance-wise conditional coverage or clinical diagnostic validity.

## Immediate deliverables
- Draft Report 1 before the next supervisor meeting.
- Begin CheXpert structure / label investigation.
- Project plan due 26 October 2026.
- Share Overleaf project with supervisor.
- Review risk assessment and data-management requirements.
