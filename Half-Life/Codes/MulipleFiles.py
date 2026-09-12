
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import linregress

# What file prefix did you choose on USX multi-run?(string)
filePrefix = 'Al_Run1'

# How many runs? (integer)
nRuns = 300

# what are your lower and upper limits for integration in channels? (integers)
lowerEnergy = 1600
upperEnergy = 1950

lowerLimit = int((lowerEnergy - 4.607)/(3.072))
upperLimit = int((upperEnergy - 4.607)/(3.072))

# Initialise time array, will contain the integrated 
# number of counts between lowerLimit and upperLimit
# for each run
timeArray = np.zeros(nRuns)

# Placeholder
headerLen = 1000


# Loop through each run file
for i in range(1, nRuns+1):

#   open file 
    fileName = filePrefix +'_'+ str(i) + '.tsv'
    fileObject = open(fileName, 'r')    
 
#   loop through file line-by-line    
    for l, line in enumerate(fileObject):

        if "Conversion Gain" in line: 
            # Extract parameters from header and initialise arrays
            nChannels = int(line.split(':')[1])
            if nChannels < upperLimit: upperLimit = nChannels
            if i == 1: sumArray = np.zeros(nChannels)
            countArray = np.zeros(nChannels) 
            
        if "Channel Data" in line: headerLen = l+2

        if l >= headerLen:
#           split line and convert number of counts per channel to float
#           populate countArray channel-by-channel            
            part = line.split()
            if (len(part)) > 2: countArray[l - headerLen] = float(part[2])
            else: countArray[l - headerLen] = float(part[1])

#   close run file to release memory
    fileObject.close()    
    
#   sum counts between lowerLimit and upperLimit
#   populate timeArray run-by-run    
    timeArray[i-1] = sum(countArray[lowerLimit:upperLimit])

#   add run spectrum to sumArray
    sumArray += countArray
    
    #print('fileName: %s\t integrated counts = %.0f' % (fileName, timeArray[i-1]))
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

with open('background_spectra.txt', 'r') as file:
    lines = file.readlines()
Coun = [line.split()[1] for line in lines]
count = [int(x) for x in Coun]


adjusted = sumArray - count


new_adjusted = [10 if x < 0 else x for x in adjusted]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
x = np.linspace(0, nChannels, num=nChannels)
t = np.linspace(0, nRuns, num= nRuns)
x2= 12*t
Energy = (3.072)*x + 4.607
backRed = t*0 + sum(timeArray)/len(timeArray)
liner = np.log(abs(timeArray-(sum(timeArray[200:nRuns])/len(timeArray[200:nRuns]))))

lowSec = 0
upSec = 600

lowCount = int(lowSec/12)
upCount = int(upSec/12)

x3 = x2[lowCount:upCount]
slope, intercept, r_value, p_value, std_err = linregress(x3, liner[lowCount:upCount])

y = x3*slope + intercept
print((-1)*slope)
#expn = np.exp()
plt.figure()    
plt.plot(x2,timeArray)

plt.xlabel('Time (sec)')
plt.ylabel('Counts')

plt.legend()
plt.grid(True)
plt.tight_layout()

plt.figure()
plt.scatter(x3, liner[lowCount:upCount])
plt.plot(x3, y)
plt.xlabel('Time (minutes)')
plt.ylabel('ln(Counts)')

plt.legend()
plt.grid(True)
plt.tight_layout()
print(len(timeArray))

plt.grid()


plt.figure()
plt.plot(Energy,sumArray)

#plt.plot(Energy,new_adjusted)
plt.yscale('log')
#plt.plot(Energy,count)

plt.grid()

plt.xlim(0, None)
#plt.ylim(0, None)
plt.show()    

