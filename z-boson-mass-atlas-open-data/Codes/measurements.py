
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


