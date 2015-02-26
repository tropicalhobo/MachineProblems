<<<<<<< HEAD
"""inputDem = False
while inputDem == False:
    try:
        demFile = raw_input("Enter the DEM file: ")
        f = open(demFile, 'r')
        inputDem = True
    except IOError:
        print "\nCannot detect file."""
#global variables
hdr = {}
val = []

#translation of coordinates to center of pixel
"""def toCenter():
#parse image parameters from ASCII file
    
#calculate the coordinates of the center of the pixel
"""

#function to open and read ASCII file
def readASCII(f):
    dem = open(f, 'r')
    lines = dem.readlines()
    for i in lines: #read header and input keys and values into dictionary
        if 'ncols' in i:
            j = i.strip()
            j = j.split()
            hdr[j[0]] = int(j[1])
        elif 'nrows' in i:
            j = i.strip()
            j = j.split()
            hdr[j[0]] = int(j[1])
        elif 'hdrllcorner' in i:
            j = i.strip()
            j = j.split()
            hdr[j[0]] = float(j[1])
        elif 'yllcorner' in i:
            j = i.strip()
            j = j.split()
            hdr[j[0]] = float(j[1])
        elif 'dx' in i:
            j = i.strip()
            j = j.split()
            hdr[j[0]] = float(j[1])
        elif 'dy' in i:
            j = i.strip()
            j = j.split()
            hdr[j[0]] = float(j[1])
        
    print hdr
    print i
    
    dem.close()

demFile = "C:\Users\G Torres\Documents\UP Diliman Stuff\GmE 205\MachineProblems\dream_dem.asc"
readASCII(demFile)    
    
#parse header values and pass to lowerleft-to-center pixel function

#function to create and write XYZ file
"""def writeXYZ():

"""
#function to create histogram:
"""def makeHistogram():

"""
=======
#translation of coordinates to center of pixel
>>>>>>> parent of 6926110... ASCII to XYZ
