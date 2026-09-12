# Galactic Plane Rotation Report

## Overview

This repository/document contains an astrophysics laboratory report titled **"Galactic Plane Rotation Report"** by Thato Nombewu (NMBTHA004) from the Department of Physics, University of Cape Town, for the AST3003S Galactic and Extragalactic Lab course (September 2025).

The report details an experiment using **neutral hydrogen (H I) 21 cm line observations** to study the structure and motion of gas in the Milky Way. The Tony Fairall Teaching Telescope was used to observe 21 cm line emission at three Galactic longitudes along the Galactic plane, and the resulting spectra were calibrated and analysed to extract maximum relative velocities.

---

## Objective

The primary objectives of this experiment were:

1. **Observe 21 cm line emission** from neutral hydrogen (H I) at three Galactic longitudes (l = 22°, 276°, and 324°) along the Galactic plane (b = 0°).

2. **Calibrate the observed spectra** using the standard source S8 and the Leiden/Argentine/Bonn (LAB) all-sky H I survey to convert detector counts (ADU) into absolute brightness temperature (K).

3. **Extract maximum relative velocities** from the calibrated frequency spectra using the non-relativistic Doppler equation.

4. **Correct velocities to the Local Standard of Rest (LSR)** to account for the Earth's rotation and orbital motion, as well as the Sun's peculiar motion.

5. **Interpret the measured velocities** in the context of Galactic rotation and identify plausible physical causes for the observed redshifted and blueshifted velocities.

6. **Identify and discuss uncertainties and observational limitations**, including statistical errors from spectral line fitting and systematic errors from instrumental issues.

---

## Problem the Paper Tries to Solve

The experiment addresses the following fundamental questions:

- **Can 21 cm H I line observations be used to trace Galactic kinematics** and measure the rotation of the Milky Way?

- **What are the maximum relative velocities** of neutral hydrogen gas at different Galactic longitudes?

- **Do the observed velocities fit the general trend expected from Galactic rotation**, with redshifts and blueshifts on opposite sides of the Galactic Centre?

- **How do local gas motions and peculiar velocities contribute** to deviations from purely circular rotation?

- **What are the limitations of the observations**, and how do statistical and systematic uncertainties affect the reliability of the results?

- **Can the galactocentric radius be inferred** from the maximum velocity using the tangent point method?

---

## How It Was Solved

### 1. Observational Setup

- **Telescope**: Tony Fairall Teaching Telescope (TFTT) at the Observatory in Cape Town, South Africa.
- **Site coordinates**: Longitude 33.933°, Latitude 18.476° (note: the report lists "site longitude" twice; likely a typo for latitude and longitude).
- **Targets**: Three Galactic longitudes along the Galactic plane (b = 0°):
  - l = 22°
  - l = 276°
  - l = 324°
- **Receiver**: Tuned to a center frequency near **1428.75 MHz** with a bandwidth of **6.25 MHz** to include both redshifted and blueshifted 21 cm line emission.

### 2. Observational Methodology

- **ON-OFF mode**: Alternating between the target position and a nearby reference position.
  - Subtracting the OFF scan from the ON scan removes background system noise and instrumental baselines.
- **Calibration scan**: Dedicated scan of the standard source **S8**.
  - Used to convert measured detector counts (ADU) into absolute brightness temperature by comparing with the LAB all-sky H I survey.
- **Stacking**: Multiple repeated scans for each pointing were stacked to increase the signal-to-noise ratio.
- **Baseline fitting**: A low-order polynomial baseline was fitted to line-free regions and subtracted to remove instrumental drifts and continuum emission.
- **Frequency axis**: Derived using the base frequency and channel spacing from the FITS header; corrections applied where the header centre frequency was offset.
- **LSR correction**: Observed frequency axis shifted into the Local Standard of Rest (LSR) frame using the telescope location and time of observation.
- **S8 calibration**: Linear relation fitted between the stacked S8 spectrum in ADU and the LAB survey brightness temperature in Kelvin; calibration factor and offset applied to all target spectra.
- **Velocity conversion**: Corrected frequency axis converted to radial velocity using the non-relativistic Doppler formula with the 21 cm rest frequency (f_rest = 1420.40575177 MHz).

### 3. Mathematical Reasoning

- **Non-relativistic Doppler formula**:

  v_rad = c (f_rest − f_obs) / f_rest

  where c is the speed of light and f_rest is the frequency corresponding to the 21 cm emission.

- **Tangent point method**: For directions along the inner Galaxy (0° < l < 90° and 270° < l < 360°), the maximum radial velocity along each line of sight corresponds to the tangent point, the closest approach of the line of sight to the Galactic centre.

- **Minimum galactocentric radius**:

  R_min = R₀ sin l

  where R₀ = 8.5 kpc is the Sun's distance from the Galactic centre and l is the Galactic longitude.

- **LSR correction**: Accounts for the Sun's peculiar velocity and the Earth's orbital motion, ensuring derived velocities reflect the motion of interstellar gas with respect to a common Galactic frame.

### 4. Data Filtration and Analysis

- **Observation log** (Table 1):

| Time (UTC) | Galactic Lat (b) [°] | Galactic Long (l) [°] | RA [°] | Dec [°] |
|---|---:|---:|---:|---:|
| 2025-09-16 13:46:37 | 0 | 22 | 18.52 | -9.70 |
| 2025-09-16 09:09:29 | 0 | 276 | 9.65 | -52.51 |
| 2025-09-16 09:56:19 | 0 | 324 | 15.54 | -56.16 |

- **Power spectra** (Figure 2): Stacked spectra for all three targets using accrued FITS files.
  - Number of observations varied due to software shutting down mid-observing.
  - Frequency axis adjusted to the correct range as suggested in the manual.
- **Isolation of range of interest** (Figure 3): Features around 1420.40575177 MHz in log scale with noise cut out.
- **Final calibrated spectra** (Figure 4): Calibrated spectrum for targets with data from the LAB survey.
  - Note: The LAB survey data is mistakenly labeled as the 'S8 calibration spectra' in the figure.

### 5. Results

- **Maximum relative velocities**:

| l [°] | Blue or Redshift | R_min [kpc] | v_max [km/s] |
|---|---:|---:|---:|
| 22 | Redshifted | 3.18 | 89.5 ± 9.0 |
| 276 | Almost None | 8.45 | 0.0 ± 6.3 |
| 324 | Blueshifted | 5.00 | -51.5 ± 11.0 |

- **Measured velocities**:
  - l = 22°: v = 89.52 ± 9 km/s (redshifted)
  - l = 276°: v = 0 ± 6.3 km/s (almost none)
  - l = 324°: v = -51.52 ± 11 km/s (blueshifted)

- **Galactocentric radius** calculated using:

  R_min = R₀ |sin(l)|

  with R₀ = 8.5 kpc (value from the manual without uncertainty).

---

## Results

### Measured Velocities and Radii

| Galactic Longitude l [°] | Shift Type | R_min [kpc] | v_max [km/s] |
|---|---:|---:|---:|
| 22 | Redshifted | 3.18 | 89.5 ± 9.0 |
| 276 | Almost None | 8.45 | 0.0 ± 6.3 |
| 324 | Blueshifted | 5.00 | -51.5 ± 11.0 |

### Key Findings

- **At l = 276°**: Measured velocity is v = 0 ± 6.3 km/s, effectively consistent with zero within uncertainties. The target shows no significant Doppler shift, meaning it is neither approaching nor receding relative to the observer.

- **At l = 324°**: Measured velocity is v = -51.52 ± 11 km/s. The negative sign indicates a clear blueshift, signifying that the source is moving toward the observer along the line of sight. The detection is significant at approximately **4.7σ**, making this a robust indication of approaching motion.

- **At l = 22°**: Measured velocity is v = 89.52 ± 9 km/s, indicating a strong redshift. This corresponds to the source moving away from the observer, with a significance level of nearly **10σ**, representing a very strong detection of recession.

- **General trend**: The observed pattern of redshifted and blueshifted velocities fits the general trend expected from Galactic rotation, with redshifts and blueshifts on opposite sides of the Galactic Centre.

### Plausible Physical Causes

- **Galactic differential rotation**: Naturally produces opposite signs of radial velocities on opposite sides of the Galactic Centre. The negative velocity at l = 324° and the positive velocity at l = 22° are roughly symmetric in longitude, consistent with the expected kinematic signature of Galactic rotation.

- **Local peculiar motions**: Streaming flows along spiral arms, expanding or contracting shells, and large-scale motions within the interstellar medium can contribute to deviations from purely circular rotation, and may account for the relatively large absolute velocities observed.

- **Distance ambiguities**: Inside the solar circle, a single velocity can correspond to both near and far kinematic distances, complicating the interpretation.

- **Heliocentric vs LSR velocities**: Heliocentric velocities can differ from LSR velocities by approximately 10–20 km/s due to the Sun's peculiar motion; applying this correction is essential for accurate comparison with Galactic rotation models.

### Conclusion

The observations clearly show how H I 21 cm spectroscopy can be used to trace Galactic kinematics and why careful calibration and consistent observing are important. The results fit the general trend expected from Galactic rotation, with redshifts and blueshifts on opposite sides of the Galactic Centre, and may also include contributions from local gas motions.

---

## Limitations

### 1. Software Faults

- Data acquisition was affected by software faults, resulting in incomplete or corrupted datasets for certain observations.
- This limited the amount of reliable data available for analysis and may have introduced additional, unquantified errors into the velocity measurements.

### 2. Inconsistent Observing Times

- For one of the target sources, measurements were taken at different times during the day.
- Variations in instrumental calibration and environmental conditions (such as temperature changes affecting receiver stability) between these sessions could have contributed to small systematic shifts in the measured line positions.

### 3. Statistical vs Systematic Uncertainties

- The reported uncertainties for the measured velocities correspond to statistical errors derived from the spectral line fitting process.
- These uncertainties primarily reflect the noise level in the spectra and the fitting residuals after applying a Gaussian model to the observed line profiles.
- The overall uncertainty in the results is likely larger due to several systematic factors that are not fully captured by the quoted uncertainties.

### 4. Calibration Source Labeling Error

- In Figure 4, the LAB survey data is mistakenly labeled as the 'S8 calibration spectra'.

### 5. Site Coordinate Typo

- The report lists "site longitude 33.933° and site longitude 18.476°" — likely a typo where one should be latitude.

### 6. Assumption of R₀ Without Uncertainty

- The galactocentric radius calculation uses R₀ = 8.5 kpc from the manual without uncertainty, which propagates into the R_min values.

### 7. Limited Number of Targets

- Only three Galactic longitudes were observed, limiting the ability to construct a full rotation curve.

### 8. Distance Ambiguities

- Inside the solar circle, a single velocity can correspond to both near and far kinematic distances, complicating the interpretation of the results.

### 9. Local Gas Motions

- Local peculiar motions such as streaming flows along spiral arms, expanding or contracting shells, and large-scale motions within the interstellar medium can contribute to deviations from purely circular rotation, and may account for the relatively large absolute velocities observed.

### 10. No Explicit Treatment of Noise in Final Spectra

- While noise was cut out for feature isolation, the final calibrated spectra still show noise, and the fitting process may not fully account for all noise contributions.

---

## References

1. B. Carroll and D. Ostlie. *An Introduction to Modern Astrophysics*. Pearson Education Limited, Essex, 2 edition, 2014.
2. P. Kalberla, W. Burton, D. Hartmann, E. Arnal, E. Bajaja, R. Morras, and W. Poppel. The leiden/argentine/bonn (lab) survey of galactic hi. *Astronomy & Astrophysics*, 440(2):775–782, 2005.
3. Bret Yotti. *AST3003S Observational Project: Measuring the Rotational Velocity of the Galactic Plane Using HI Gas 1.4 GHz Emission*. University of Cape Town, September 2025.
4. P. Kalberla, U. Mebold, and K. Reif. Brightness temperature calibration for 21-cm line observations. *Astronomy and Astrophysics*, 106(2):190–196, 1982.

---

## File Information

- **File name**: `astro_obs_report (1).pdf`
- **Author**: Thato Nombewu (NMBTHA004)
- **Course**: AST3003S Galactic and Extragalactic Lab
- **Institution**: University of Cape Town
- **Date**: September 2025
