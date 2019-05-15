'''
# NumLib
- Code By Michael Sherif Naguib
- license: (see LICENSE file)
- Date: 5/5/2019
- @University of Tulsa
- Description: easy access to numerical digit constants
'''
#This author does NOT take credit for the constants found in these files!
#this data was found (easily) online
PRIMES_FILE_NAME="Primes1mil.txt"
PHI_FILE_NAME="GOLDEN_RATIO_20k_Places.txt"
ZETAFUNC_ZEROS_NAME="ZetaZerosIM.txt"
PI_FILE_NAME="pi-billion.txt"
#Euler's constant
#Collatz Path Lengths
import PlotUtil# Hack but it works....
#NumLib: loads constants from files...
class NumLib():
    def __init__(self):
        pass
    def loadPrimes(self):
        with open(PRIMES_FILE_NAME, "r") as file:
            data_txt = file.read()  # read all the lines
            split_data = data_txt.split()  # split on white space
            self.primes = [int(a_prime) for a_prime in split_data]  # convert to integer from string
    def loadPhiDigits(self):
        with open(PHI_FILE_NAME, "r") as numberFile:
            # Read, get rid of newlines, combine, then take the desired digit count
            lines = numberFile.read().splitlines()
            numText = "".join(lines).replace(".","")
            self.phiDigits = list(map(lambda x: int(x), numText))
    def loadZetaZeros(self):
        unparsed_data_r = None
        # 100k ish datapoints of im solutions to zeta func available... courtesy of http://www.lmfdb.org/zeros/zeta/
        with open(ZETAFUNC_ZEROS_NAME, "r") as data_file:
            unparsed_data_r = data_file.readlines()
            self.zetaZeros = list(map(lambda x: float(x.split(" ")[1]), unparsed_data_r))
    def loadPiDigits(self):
        pi_txt=""
        with open(PI_FILE_NAME, "r") as pi_data_file:
            pi_txt = pi_txt.join(list(pi_data_file.readlines()))
            self.piDigits = list(map(lambda x: int(x), pi_txt))

