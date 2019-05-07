# NumLib 
- I need code for the purposes listed in in the <b>purposes</b> section of this readme
- More often than not I have just copied my old code and modified it in the new 
project as needed leaving a comment stating that it originated from another of my projects; 
- Now I will have an easy means of maintaining consistant code across projects as well as 
 a standerdized implementation. 
## Purposes
- Access large quantities of numerical info from a constant
- Display Data with plotting and graphing libraries
## Installation
- clone the repo then 
- ```pip install -e NumLib```
## File ```NumLib.py``` class ```NumLib```
- Is a script for loading constants into attributes of the instance of NumLib
- Constants can be redefined to change the file the code looks for number data in 
(WARNING this does not mean the parsing algorithm will understand the file)
- (WARNING) for reasons pertaining to github's limit on file sizes ```pi-billion.txt```
is not provided in this repo... but can be obtained by a simple google search and finding
MIT's publicly available link to a billion digits of pi. (https://stuff.mit.edu/afs/sipb/contrib/pi/pi-billion.txt)
Using the ```wget insert-link-here``` command in linux may be helpfull... The author of this code cannot be held responsible for misuse of this link ... or any similar scenario pertaining
to the download of such a large volume of data...
- Notice! all other constant files were from public online sources; the author of this code in no way claims 
reliability nor authorship of these files. 

### constants 
```
PRIMES_FILE_NAME="Primes1mil.txt"
PHI_FILE_NAME="GOLDEN_RATIO_20k_Places.txt"
ZETAFUNC_ZEROS_NAME="ZetaZerosIM.txt"
PI_FILE_NAME="pi-billion.txt"
```
### method
- ```loadPrimes``` loads numbers into ```self.primes```
- ```loadPhiDigits``` loads numbers into ```self.phiDigits```
- ```loadZetaZeros``` loads numbers into ```self.zetaZeros```
- ```loadPiDigits``` loads numbers into ```self.primes```

### Planned
- add Euler's constant
- add in Collatz Path length lookup data

## File ```PlotUtil.py``` class ```PlotUtil```
- Previously in my other repos was called ```PlottingUtil``` this class combines 
the most useful (and best working) versions of my previous code
- (friendly reminder )Do not forget ```%matplotlib notebook``` in matlab if plotting 
and that if using Jupyter Notebook the kernel may cache the library not actually updating 
any changes made to PlotUtil between runs... a kernel restart is needed. 
- class ```PlotUtil``` can be used in two different ways: as a static methods class as well
as an object oriented class which holds data
### methods (static use --> no init)
- ```PlotUtil.plot({'name':'insert label name here','data':[[x data here],[y data here]]})```: takes an object as described above and plots x points vs y with a random color 
- ```PlotUtil.plotSeries([{'name':'insert label name here','data':[[x data here],[y data here]]}])```: similar to ```PlotUtil.plot()``` except it plots multiple data series and the first 3 colors are predefined then random colors 

