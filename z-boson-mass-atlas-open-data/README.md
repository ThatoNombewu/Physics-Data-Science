# Z-Boson Mass Reconstruction from ATLAS Open Data

## 1. Overview

- **Research question:** Can real proton–proton collision data from ATLAS Open Data be used to reproduce an established Standard Model measurement of the Z-boson mass?
- **Objective:** Reconstruct the invariant mass of oppositely charged dimuon events, fit the resulting mass spectrum, and compare the extracted Z-boson mass with the Particle Data Group (PDG) reference value. A second objective was to search for the Higgs boson in the diphoton channel.
- **Domain:** Experimental particle physics / high-energy physics, with applications to data analysis, statistical modelling, event selection, and scientific computing.

## 2. Repository Context

The analysis used the `UCT3rdYrLabATLASOpenData` GitHub repository.

The workflow consisted of:

- Cloning the source repository.
- Creating a Python 3 virtual environment.
- Installing dependencies using `requirements.txt`.
- Downloading reduced ATLAS Open Data containing reconstructed four-vectors for muons and photons.
- Processing the data using Jupyter Notebooks.
- Reconstructing invariant masses and performing statistical analysis.

The exact directory structure and location of this report within the larger repository are not specified in the research file.

## 3. Data

### Dataset

- **Source:** ATLAS Open Data / CERN Open Data.
- **Data type:** Proton–proton collision events.
- **Particles analysed:** Muons and photons.
- **Primary variables discussed:**
  - Four-momentum
  - Transverse momentum (`pT`)
  - Pseudorapidity (`η`)
  - Electric charge
  - Isolation information

### Z-Boson Analysis

Events were selected using:

- Two oppositely charged muons.
- Muons originating from the primary vertex.
- Pseudorapidity:

  `|η| < 2.4`

- Two transverse-momentum selection thresholds:
  - `pT > 20 GeV`
  - `pT > 40 GeV`
- Muon isolation was varied, with negligible impact on the final mass uncertainty.

### Feature Engineering

The primary derived feature was the dimuon invariant mass:

```text
m²μμ = (pμ+ + pμ−)²

## Methods

The analysis used proton–proton collision events from **ATLAS Open Data** to reconstruct the Z-boson mass from its decay into a pair of oppositely charged muons.

The main steps were:

1. Load the reduced ATLAS Open Data files containing muon four-vector information into Python/Jupyter.
2. Select events containing two oppositely charged muons originating from the primary vertex.
3. Apply a pseudorapidity requirement of `|η| < 2.4`.
4. Apply two transverse-momentum (`pT`) selections:
   - `pT > 20 GeV`
   - `pT > 40 GeV`
5. Calculate the dimuon invariant mass using

   $$
   m_{\mu\mu}^2 = (p_{\mu^+} + p_{\mu^-})^2
   $$

6. Construct the dimuon invariant-mass spectrum.
7. Fit the Z-boson peak using a Breit–Wigner/Cauchy-like distribution together with a smooth background.
8. Compare the reconstructed Z-boson mass with the Particle Data Group (PDG) reference value.

The analysis was implemented using **Python and Jupyter**, with the supplied project environment and dependencies.

---

## Statistical Methods

The Z-boson signal was identified through the invariant-mass distribution of oppositely charged muon pairs.

A **Breit–Wigner/Cauchy-like distribution** was used to model the resonance peak, while a smooth background component accounted for non-resonant events.

The fitted peak position was used as the estimate of the reconstructed Z-boson mass.

Two event-selection thresholds were compared:

- `pT > 20 GeV`
- `pT > 40 GeV`

The statistical uncertainties obtained from the fits were used to assess the precision of the reconstructed mass.

The PDG reference value used for comparison was:

$$
m_Z = 91187.6 \pm 2.1\ \text{MeV}
$$

The analysis demonstrates the statistical trade-off between retaining more events and applying stricter selection criteria.

---

## Z-Boson Results

The reconstructed Z-boson masses were:

| Event Selection | Reconstructed Z Mass |
|---|---:|
| `pT > 20 GeV` | `91140.67 ± 2112.18 MeV` |
| `pT > 40 GeV` | `90732.06 ± 2238.02 MeV` |
| PDG Reference | `91187.6 ± 2.1 MeV` |

Both reconstructed values were consistent with the expected Z-boson mass within the relatively large statistical uncertainties of the analysis.

The `pT > 20 GeV` selection produced:

$$
m_Z = (91140.67 \pm 2112.18)\ \text{MeV}
$$

while the stricter `pT > 40 GeV` selection produced:

$$
m_Z = (90732.06 \pm 2238.02)\ \text{MeV}
$$

The results successfully reproduced the Z-boson resonance using publicly available collider data.

---

## Effect of Event Selection

The transverse-momentum requirement had a measurable effect on the reconstructed mass and its uncertainty.

### `pT > 20 GeV`

The lower threshold allowed more muon events to be retained. This increased the available statistics and resulted in a slightly smaller statistical uncertainty.

The reconstructed mass was also slightly closer to the PDG reference value.

### `pT > 40 GeV`

The stricter requirement selected higher-momentum muons and reduced the number of events available for the fit.

Although the resulting invariant-mass spectrum remained consistent with the Z-boson resonance, the statistical uncertainty increased:

$$
2112.18\ \text{MeV}
\rightarrow
2238.02\ \text{MeV}
$$

The reconstructed mass also shifted downward by approximately `400 MeV` relative to the `pT > 20 GeV` selection.

This demonstrates an important analysis trade-off:

> **Stricter event selection can improve event quality while reducing the statistical power of the dataset.**

The results also show that event-selection choices can influence the measured value of a physical quantity.

---

## Limitations & Assumptions

Several limitations affected the analysis:

- The dataset was limited, resulting in relatively large statistical uncertainties.
- The analysis used simplified event-selection and fitting procedures.
- The study did not perform a complete detector simulation.
- Systematic uncertainties were not fully evaluated.
- Changes in event-selection criteria can influence the reconstructed mass.
- The higher `pT` selection reduced the number of available events, increasing statistical fluctuations.
- The analysis focused primarily on the Z-boson mass measurement.
- The Higgs-boson diphoton analysis was exploratory and was **not completed as a full analysis because of time constraints**.
- The agreement with the PDG value should therefore be interpreted within the statistical and methodological limitations of the study.

A more complete analysis would require a larger dataset, detailed detector effects, systematic uncertainty studies, and a more comprehensive treatment of backgrounds and reconstruction effects.
