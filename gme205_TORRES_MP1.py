from math import sqrt
from itertools import groupby

#global variables
hdr = {} #stores header keys and values

xyz = [] #stores xyz data for writing to file

z = [] #stores individual z values in preparation of histogram printing

zInt = [] #stores integer values of z for the histogram

h = '' #file path of empty xyz file

#function to transform lower left coordinates to center of pixel
def convertCoord(dx, dy): #dx and dy are coordinate pairs in the dictionary
    cenPix = hdr['dx']/2, hdr['dy']/2    
    return cenPix

#format values in XYZ and input into tuple nested in list
def formatXYZ(cols, rows, dx, dy, xll, yll, z, cX, cY):
    delimit = ' '
    yUpperLeft = dy*rows+yll+cY #transform lower left coordinates to center of pixel
    xll = xll + cX

    for o in range(0, rows, 1):#iterate per row 
        yUpperLeft -= 1
        xCoord = xll
        for p in range(0, cols, 1):#iterate per column
            values = str(xCoord)+delimit, str(yUpperLeft)+delimit, z[p]+'\n'
            xCoord += 1
            xyz.append(values)                              

#function to open and read ASCII file
def readASCII(f):
    
    line = f.readlines()
    for i in line: #read header and input keys and values into dictionary
        
        if 'ncols' in i:
            j = i.strip()
            j = j.split()
            hdr[j[0]] = int(j[1])
        elif 'nrows' in i:
            j = i.strip()
            j = j.split()
            hdr[j[0]] = int(j[1])
        elif 'xllcorner' in i:
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
        elif i.isalpha() == False:#insert z values into the z list            
            k = i.strip()
            k = k.split()
            for o in range(len(k)):
                z.append(k[o])
        f.close()
        
#function to write formatted values to an empty XYZ file
def writeXYZ(m, t):
    counter = 0
    for i in xyz:     
        m.writelines(xyz[counter])
        #print xyz[j][0].strip(),xyz[j][1].strip(),xyz[j][2].strip()
        counter += 1
    m.close()

#function to convert z values into integers:
def convertZtoInt():
    counter = 0
    for obs in z[0:hdr['ncols']*hdr['nrows']]: #user can change the max value of the slice
        s = int(float(obs))
        z.remove(obs)
        zInt.insert(counter, s)        
        counter += 1
        
#print histogram
def printHistogram(d):
    print "\nFrequency of values adjusted by 500."

    minZ = min(d)
    maxZ = max(d)
    d.sort()
    for i in range(minZ, maxZ, 1):
        countInt = d.count(i)
        if countInt > 500:
            print i, countInt/500*'*', countInt/500    

#file input and read
def fileInput():
    inputDem = False
    while inputDem == False:
        try:
            demFile = raw_input("\nEnter the DEM file path: ")
            h = raw_input("\nEnter the file path of the empty xyz file: ")
            #print "C:\Users\G Torres\Documents\UP Diliman Stuff\GmE 205\MachineProblems\dream_dem2.asc"
            #demFile = "C:\Users\G Torres\Documents\UP Diliman Stuff\GmE 205\MachineProblems\dream_dem2.asc"
            f = open(demFile, 'r')
            print "\nPrinting the histogram will take some time. Please wait..."
            readASCII(f)
            inputDem = True
        except IOError:
            print """\nCannot detect files.
Please type the name correctly."""

###################################################################3

fileInput()

c = convertCoord(hdr['dx'], hdr['dy'])
formatXYZ(hdr['ncols'], hdr['nrows'], hdr['dx'], hdr['dy'],
         hdr['xllcorner'], hdr['yllcorner'], z, c[0], c[1])

#Enter the file path of the empty xyz file
h = "C:\Users\G Torres\Documents\UP Diliman Stuff\GmE 205\MachineProblems\\new.xyz"

s = open(h, 'w')

writeXYZ(s, xyz)

convertZtoInt()

printHistogram(zInt)



