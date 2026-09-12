# Neutron Activation of ²⁷Al

## Overview

This repository/document contains a nuclear physics laboratory report titled **"Neutron Activation of ²⁷Al"** by Thato Nombewu (NMBTHA004) from the Department of Physics, University of Cape Town, for the PHY3004W Nuclear Physics Laboratory course (May 23, 2025).

The report details an experiment using **neutron activation**, **gamma-ray spectroscopy**, and **time-resolved decay analysis** to identify radioactive isotopes produced when natural aluminium is exposed to a neutron source, and to measure their half-lives.

---

## Objective

The primary objectives of this experiment were:

1. **Activate natural aluminium (²⁷Al)** using a neutron source via the reaction:

   ²⁷Al(n,γ)²⁸Al

2. **Identify the radioactive isotope ²⁸Al** through its characteristic gamma-ray emission at **1779 keV**.

3. **Measure the half-life of ²⁸Al** using time-resolved decay analysis and compare it with the accepted literature value (**2.245 min**).

4. **Observe and identify any secondary activation products**, specifically ²⁷Mg, and measure its half-life.

5. **Develop an uncertainty budget** to evaluate the contributions of statistical and systematic errors in the analysis.

---

## Problem the Paper Tries to Solve

The experiment addresses the following fundamental questions:

- **Can neutron activation successfully produce measurable quantities of radioactive ²⁸Al** from stable ²⁷Al using an Am-Be neutron source?

- **Can the decay constant and half-life of ²⁸Al be accurately determined** using gamma-ray spectroscopy and exponential decay fitting?

- **What secondary activation products are produced** during the irradiation, and can they be identified and characterized?

- **How reliable are the measured values** when accounting for statistical and systematic uncertainties?

- **Do the experimentally determined half-lives agree with accepted literature values** from databases such as NuDat 3.0?

---

## How It Was Solved

### 1. Experimental Setup

- **Neutron source**: Am-Be source (2.2 GBq) placed in a water bath.
- **Samples**: Natural aluminium (²⁷Al) cylinders.
- **Detector**: 5 cm × 5 cm NaI(Tl) scintillator coupled to a multichannel analyzer (MCA).
- **Calibration**: Reference sources (Na-22, Cs-137, Mn-54) used to establish a linear energy-channel relation.

### 2. Data Acquisition

- Aluminium cylinders exposed to the neutron source for **longer than 4 hours**.
- Gamma spectra acquired in **12-second intervals** for a total of **1 hour** using the USX software's multiple run feature.

### 3. Gamma-Ray Identification

- Summed spectrum analysed to identify peaks.
- Dominant peak at **1771 keV** attributed to ²⁸Al decay.
- Secondary peak at **849 keV** attributed to ²⁷Mg.
- Compton edge also observed.

### 4. Decay Curve Analysis

- Counts integrated over specific energy intervals as a function of time.
- Decay equation used:

   N = N₀e^(−λt) + C_Background

- Linearized semi-log form:

   ln(N − C_B) = ln(N₀) − λt

- Linear fits applied to the data:
  - **²⁸Al**: first 10 min used (decay curve became constant around 700 s)
  - **²⁷Mg**: up to 30 min used
- Decay constant: λ = −m (negative gradient)
- Half-life calculated using:

   t₁/₂ = ln 2 / λ

### 5. Isotope Identification

- Calculated half-lives and gamma energies matched against **NuDat 3.0** nuclear database.

### 6. Uncertainty Budget

- Sources of uncertainty identified:
  - Count statistics (Poisson) — random
  - Energy calibration — systematic
  - Background estimation — systematic
  - Fitting method
- Combined uncertainty calculated.

---

## Results

### Measured Half-Lives

| Isotope | Decay Constant λ (s⁻¹) | Measured Half-Life (min) | Literature Half-Life (min) |
|---|---:|---:|---:|
| ²⁸Al | 0.00492 ± 0.00026 | 2.348 ± 0.0062 | 2.245 (or 2.248) |
| ²⁷Mg | 0.00129 ± 0.00012 | 8.96 ± 0.833 | 9.435 |

### Key Findings

- **²⁸Al successfully produced** via neutron activation of ²⁷Al.
- **Measured half-life of ²⁸Al**: 2.35 ± 0.06 min — in good agreement with accepted value of **2.245 min**.
- **²⁷Mg identified** as a secondary activation product with a peak at **849 keV**.
- **Measured half-life of ²⁷Mg**: 8.96 ± 0.83 min — consistent with literature value of **9.435 min**.
- **Uncertainty budget**:
  - Combined uncertainty for ²⁸Al half-life: **2.5%**
  - Dominant contributions: count statistics (1.5%), background estimation (0.8%), energy calibration (0.5%)

### Conclusion

The experiment demonstrated the effectiveness of **gamma spectroscopy** and **time-resolved analysis** in identifying activation products and quantifying nuclear decay parameters. The inclusion of an uncertainty budget provided insight into the reliability of the results.

---

## Limitations

### 1. Energy Discrepancies

- **²⁸Al gamma energy**: Abstract and introduction cite **1779 keV**, but results text reports the dominant peak at **1771 keV**.
- **²⁸Al literature half-life**: Abstract/introduction/conclusion cite **2.245 min**, while the NuDat section cites **2.248 min**.

### 2. Inconsistent Uncertainty Reporting

- Table 2 lists ²⁸Al half-life as 2.348 ± 0.0062 min, but the conclusion states 2.35 ± 0.06 min.
- The uncertainty in Table 2 appears inconsistent with the quoted λ uncertainty; the conclusion value uses ± 0.06 min.

### 3. Limited Data Range for Fitting

- **²⁸Al**: Only the first 10 minutes were used for fitting because the decay curve became constant around 700 s.
- **²⁷Mg**: Only up to 30 minutes were used due to the short-lived aluminium lifespan.

### 4. Background Subtraction

- Background estimation contributed **0.8%** to the combined uncertainty.
- The constant background term C_B may not fully account for all background processes.

### 5. Detector Resolution

- NaI(Tl) scintillator has limited energy resolution compared to HPGe detectors, which may affect peak identification and integration.

### 6. Systematic Errors

- Energy calibration contributed **0.5%** to the combined uncertainty.
- Other potential systematic effects (e.g., detector efficiency, geometry, dead time) were not explicitly quantified.

### 7. Statistical Limitations

- Count statistics (Poisson) contributed **1.5%** to the combined uncertainty.
- Longer acquisition times or higher source activity could reduce statistical uncertainty.

### 8. No Explicit Treatment of Compton Continuum

- The Compton edge was observed but not explicitly modelled or subtracted in the decay analysis, which could affect count integration in the energy intervals.

---

## References

1. Krane, K. S., *Introductory Nuclear Physics*, Wiley (1987).
2. NuDat 3.0 Nuclear Data Centre: https://www.nndc.bnl.gov/nudat3/
3. Bevington, P. R., *Data Reduction and Error Analysis*, McGraw-Hill (2003).

---

## File Information

- **File name**: `NMBTHA004_HALF_LIFE.pdf`
- **Author**: Thato Nombewu (NMBTHA004)
- **Course**: PHY3004W Nuclear Physics Laboratory
- **Institution**: University of Cape Town
- **Date**: May 23, 2025
