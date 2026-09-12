import uproot as uproot
import numpy as np
import pandas as pd
import vector
import matplotlib.pyplot as plt
import scipy.stats

eventsData = uproot.open("data_Skim_GamGam.root")["mini"]
df = eventsData.arrays(["photon_pt", "photon_eta", "photon_phi", "photon_E",  "diphoton_mass"], library="pd")
df


cuts0 = df[(df['photon_pt'].apply(lambda x: x[0]) > 35000) & (df['photon_pt'].apply(lambda x: x[1]) > 25000)]

cuts1 = cuts0[(np.abs(cuts0['photon_eta'].apply(lambda x: x[0])) < 2.37) & (np.abs(cuts0['photon_eta'].apply(lambda x: x[1])) < 2.37)]


# These cuts exclude a small region of the ATLAS detector known to have poor efficiency and resolution.
cuts1a = cuts1[(np.abs(cuts1['photon_eta'].apply(lambda x: x[0])) < 1.37) | (np.abs(cuts1['photon_eta'].apply(lambda x: x[0])) > 1.52)]
cuts1b = cuts1a[(np.abs(cuts1a['photon_eta'].apply(lambda x: x[1])) < 1.37) | (np.abs(cuts1a['photon_eta'].apply(lambda x: x[1])) > 1.52)]

# Here we apply kinematic criteria that removes diphotons that are just random combinations
cuts2a = cuts1b[(cuts1b['photon_pt'].apply(lambda x: x[0]) / cuts1b['diphoton_mass']) > 0.35]
cuts2b = cuts2a[(cuts2a['photon_pt'].apply(lambda x: x[1]) / cuts2a['diphoton_mass']) > 0.25]

# finally we only look in the diphoton mass regions close to the known higgs mass
cuts3 = cuts2b[(cuts2b['diphoton_mass'].apply(lambda x: x)) > 105000.0]

finalData = cuts3

print("Number of selected events = " + str(len(finalData.index)))
finalData

#first we make arrays of four-vectors for the muons. we make separate arrays for leading and sub-leading muons
pt0 = finalData['photon_pt'].apply(lambda x: x[0]).to_numpy()
eta0 = finalData['photon_eta'].apply(lambda x: x[0]).to_numpy()
phi0 = finalData['photon_phi'].apply(lambda x: x[0]).to_numpy()
E0 = finalData['photon_E'].apply(lambda x: x[0]).to_numpy()

pt1 = finalData['photon_pt'].apply(lambda x: x[1]).to_numpy()
eta1 = finalData['photon_eta'].apply(lambda x: x[1]).to_numpy()
phi1 = finalData['photon_phi'].apply(lambda x: x[1]).to_numpy()
E1 = finalData['photon_E'].apply(lambda x: x[1]).to_numpy()

lvArray0 = vector.array(
    {
        "pt": pt0,
        "phi": phi0,
        "eta": eta0,
        "E": E0,
    }
)

lvArray1 = vector.array(
    {
        "pt": pt1,
        "phi": phi1,
        "eta": eta1,
        "E": E1,
    }
)

lvArray = lvArray0 + lvArray1
lvArray


mH = 124894.0
sigmaH = 210.0


nBins = 30
minMass = 105000
maxMass = 160000

countsData, edges = np.histogram(lvArray.mass, bins=nBins, range=(minMass,maxMass))

#create an array of the centre of each bin, useful for plotting the pdf later
centres = (edges[1:] + edges[:-1]) / 2

b = np.poly1d(np.polyfit(centres, countsData, 3))

#guess a signal integral for illustration purposes
integral = 10113802.23

s = ( scipy.stats.norm.pdf(centres, mH, sigmaH) * integral)
sb = s+b(centres)

plt.figure()
plt.xlabel("$ m_{\gamma\gamma}$")
plt.ylabel("events per bin")
plt.plot(centres, s, 'b', linewidth=1, label="Potential Signal")
plt.plot(centres, b(centres), 'k', linewidth=1, linestyle="--", label="Background")
plt.plot(centres, sb, 'r', linewidth=2, label="Signal+Background")

plt.errorbar(centres, countsData, yerr=np.sqrt(countsData), fmt='o', mfc='k', mec='k',ms=4, mew=0.2, ecolor='k',label="ATLAS Open Data",)
plt.legend()

#ratio plot 
residuals = countsData - b(centres) 
plt.figure()
plt.xlabel("$ m_{\gamma\gamma}$")
plt.ylabel("Data - background")
plt.errorbar(centres, residuals, yerr=np.sqrt(countsData), label="Estimated Signal (Data - background)", fmt='o', mfc='k', mec='k', mew=0.2, ecolor='k')

nSteps = 100

plt.plot(centres, s, 'b', linewidth=1, label="Potential signal")
plt.plot(centres, np.zeros(len(centres)), 'k', linewidth=1, linestyle="--", label="Background")
plt.legend()
plt.show()

#assume mass, sigma
from scipy.optimize import curve_fit

def gaussian(x, mean, amplitude, standard_deviation):
    return amplitude * np.exp( - ((x - mean) / standard_deviation) ** 2)

bestFitParams, covarianceMatrix = curve_fit(gaussian, centres, residuals, p0=[125000., 200., 1000.])

#the p0 values are that the 'starting points' for 𝑚𝐻, Γ𝐻 and 𝑁𝐻→𝛾𝛾 in the fit.

x_interval_for_fit = np.linspace(edges[0], edges[-1], 10000)
plt.plot(x_interval_for_fit, gaussian(x_interval_for_fit, *bestFitParams), label='$ H \gamma \gamma$ signal')
plt.errorbar(centres, residuals, yerr=np.sqrt(countsData), label="Data - Background", fmt='o', mfc='k', mec='k', mew=0.2, ecolor='k')
plt.legend()
plt.xlabel("$ m_{\gamma\gamma}$")
plt.ylabel("Data - prediction")

# add the values of thr fitted signal shape at a series of points to estimate the total 
# number of signal events
limA = 11500
limA = 13500
sigIntegral = 0.0
stepSize = (maxMass - minMass)/(nSteps)

xStep = minMass

for p in range(0, nSteps):
        xStep = xStep + stepSize
        sigHeight = gaussian(xStep, *bestFitParams)
        #print(sigHeight)
        sigIntegral = (sigIntegral + (sigHeight) )

print("best fitting parameters:")
print("MH = " + str(float(bestFitParams[0])))
print("sigmaH = " + str(float(bestFitParams[1]) ))
print("NH = " + str(float(sigIntegral) ))
