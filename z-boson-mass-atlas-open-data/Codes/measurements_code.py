
import numpy as np
import matplotlib.pyplot as plt
import awkward as ak
import uproot as uproot
import vector
import pandas as pd
from scipy import stats
from scipy.stats import cauchy
from scipy.stats import norm

eventsData = uproot.open("data_Skim_mumu.root")["mini"]  #this command tells uproot where to find the file

df = eventsData.arrays(["muon_E", "muon_pt", "muon_phi", "muon_eta", "muon_charge", "muon_etcone20", "muon_ptcone30"], library="pd")
print("File has been successfully opened!")

df

#cut0: we require the charges of the muons to be opposite (by requiring the sum to be 0)
cuts0 = df[ df['muon_charge'].apply(lambda x: x[0] + x[1] == 0)]

#cut1: we require the transervse momentum of each muon to be above 20000 MeV'
cuts1 = cuts0[(cuts0["muon_pt"]).apply(lambda x: x[0] > 20000) & (cuts0["muon_pt"]).apply(lambda x: x[1] > 20000)]

#cut2: we require the absolute pseudorapidity of each muon to be below 2.4'

cuts2 = cuts1[(cuts1["muon_eta"]).apply(lambda x: np.abs(x[0]) < 2.4) & (cuts1["muon_eta"]).apply(lambda x: np.abs(x[0]) < 2.4)  ]

#we copy our finally selected dataframe to a new variable 'finalData' for convenience
finalData =  cuts2 # you will have to change this line when you want to include the muon 

#let's check how many events we have selected after all our criteria have been applied
print("Number of selected events = " + str(len(finalData.index))) # this should be 540579! 

# and have a look at our finally selected dataframe
finalData


#first we make arrays of four-vectors for the muons. we make separate arrays for leading and sub-leading muons
pt0 = finalData['muon_pt'].apply(lambda x: x[0]).to_numpy()
eta0 = finalData['muon_eta'].apply(lambda x: x[0]).to_numpy()
phi0 = finalData['muon_phi'].apply(lambda x: x[0]).to_numpy()
E0 = finalData['muon_E'].apply(lambda x: x[0]).to_numpy()

pt1 = finalData['muon_pt'].apply(lambda x: x[1]).to_numpy()
eta1 = finalData['muon_eta'].apply(lambda x: x[1]).to_numpy()
phi1 = finalData['muon_phi'].apply(lambda x: x[1]).to_numpy()
E1 = finalData['muon_E'].apply(lambda x: x[1]).to_numpy()

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

# the vector package conveniently allows us to simply add the arrays to get an array of four-vectors representing the dimuon system in each event
lvArray = lvArray0 + lvArray1
lvArray

# let's make some simple histograms of the kineamtic information associated with the muons.
# as an example I look at muon[0] only, but you can look at muon[1] and compare the distributions.

# plot the mu[0] pt histogram.
plt.figure()
plt.xlabel("mu pt")
plt.ylabel("events per bin")
plt.hist(lvArray0.pt, bins=35, range=[0,120000], alpha=0.6, color='g')

# plot the mu[0] pseudorapdity histogram.
plt.figure()
plt.xlabel("mu eta")
plt.ylabel("events per bin")
plt.hist(lvArray0.eta, bins=25, range=[-3.0,3.0], alpha=0.6, color='g')

# plot the mu[0] phi histogram.
plt.figure()
plt.xlabel("mu phi")
plt.ylabel("events per bin")
plt.hist(lvArray0.phi, bins=15, range=[-3.14,3.14], alpha=0.6, color='g')

#we set up a few parmaters for our histogram, min and max of the x-axis (mass)
minMass = 71000
maxMass = 110000

#the number of bins
nBins = 250 

# creating the histogram as two arrays (bin edges & counts in the bins) numpy
countsData, edges = np.histogram(lvArray.mass, bins=nBins, range=(minMass, maxMass))

# get the width of each bin
bin_width = edges[1] - edges[0]
# sum over number in each bin and multiply by bin width, which can be factored out.
# This gives us the integral
integral = bin_width * sum(countsData[0:nBins])

# we can make an array of the centre of each bin directly from the edges array this will be useful in plotting our pdf
centres = (edges[1:] + edges[:-1]) / 2

#fit a Cauchy distributions to the dimuon mass data
#mu, std = cauchy.fit(lvArray.mass)
#print("mu = " + str(mu))
#print("std = " + str(std))

mZPDG  = 91187.6
sigmaZPDG = 2495.2

#let's make the comparison plot
plt.figure()
p = (cauchy.pdf(centres, mZPDG, sigmaZPDG) * integral)
plt.plot(centres, p, 'k',label="Cauchy pdf (PDG values)", linewidth=2)
plt.hist(lvArray.mass, bins=nBins, range=[minMass, maxMass],label="ATLAS Data", alpha=0.6, color='g')
plt.legend()
plt.xlabel("mumu mass [MeV]")
plt.ylabel("# events")
plt.show()


#chi-squared function
def calcChiSq(obs, preds):
    chiSq = 0.0
    ndf = len(obs)
    for bin in range(0, len(obs)):
        diff = preds[bin] - obs[bin]
        var = ( np.abs(preds[bin])) # pearson's chi2 (approximate the prediction's variance as poisson, i.e., take the prediction as the variance)
        if (var != 0):
            chiSq += (diff**2)/(var)
    return chiSq, ndf


#some arrays to hold the z mass and chi-squared values
mZAr = np.array([])
chi2Ar = np.array([])

#deciding the range of z mass values and how fine the steps in this range will be
minMz = 90730
maxMz = 90765
step = 1

#vairables to use in the loop to find value of z mass that gives smallest chi2
bestFitMz1D = 0.0
minChi2 = 10000000

for mZ in range(minMz, maxMz, step): #starting loop
    countsPDF = (cauchy.pdf(centres, mZ, sigmaZPDG) * integral) #building pdf for these values
    #countsPDF = (norm.pdf(centres, mZ, sigmaZPDG) * integral) #building pdf for these values
    chi2, ndf = calcChiSq(countsData, countsPDF) # call chi2 function to get chi2 for this particular pdf and data
    mZAr = np.append(mZAr, mZ) #adding values to arrays
    chi2Ar = np.append(chi2Ar, chi2)
    if(chi2 < minChi2): #keeping track of what is the smallest chi2 value we have found
        minChi2 = chi2
        bestFitMz1D = mZ
                
# as we will only be interested in the change in chi2 w.r.t. mZ,  we can rescale all the chi2
#values such that the minimum chi2 value is 0. 
chi2Ar = chi2Ar - minChi2

#we expect the chi2 vs. mZ curve to be quadratic, so let's fit that fucntion to it.
z = np.polyfit(mZAr, chi2Ar, 2) #"2" for a second-order polynomial
p = np.poly1d(z)

#lets plot our chi2 values vs mz along with the fit
plt.figure()
fig, ax = plt.subplots()
ax.plot(mZAr, chi2Ar, 'r+', lw=5, alpha=0.6, label="chi2 evaluations")
ax.plot(mZAr, p(mZAr), 'b-', lw=5, alpha=0.6, label="quadratic fit")

# we can display the estimated uncertianty on mZ via critical values () of the delta chi-squared curve
y0 = 1.0
crit = (p - y0).roots # roots of the polynominal -1, i.e., the mz values where p = 1 

#shading in the uncertainty band 
px=np.arange(crit[1],crit[0],0.001)
ax.fill_between(px,p(px),alpha=0.5, color='g', label="uncertainty")
ax.legend()

#setting reasonable axis ranges and titles
ax.set_xlim(minMz, maxMz)
ax.set_ylim(0.0, 5.0)
plt.xlabel("mZ [MeV]")
plt.ylabel("delta chi-squared")

plt.show()

#print result and uncertainty
my1DResult = bestFitMz1D
my1DUncertainty = bestFitMz1D-crit[1]
print("best-fit = " + str(my1DResult) + " +/- " + str(my1DUncertainty))

# we now compare our data histogram with the cauchy distribution with the mean and standard deviation
# that minimise the chi-squared. This pdf should agree much better than the pdf with the PDG values.

plt.figure()
p = (cauchy.pdf(centres, my1DResult, sigmaZPDG))

pInt = bin_width * sum(p[0:nBins])
scale = integral/pInt
pScaled = (cauchy.pdf(centres, my1DResult, sigmaZPDG) *scale)

plt.plot(centres, pScaled, 'k', linewidth=2)

x = np.linspace(87000, 94000, 1000)
pScaledNorm = (norm.pdf(x, my1DResult, (sigmaZPDG*0.8) )*(0.6*scale))

#plt.plot(x, pScaledNorm, 'r', linewidth=2)

plt.hist(lvArray.mass, bins=nBins, range=[minMass, maxMass], alpha=0.6, color='g')
plt.xlabel("mumu mass [MeV]")
plt.ylabel("# events")
plt.show() 
