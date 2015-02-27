from math import sqrt

#global variables
hdr = {}
xyz = []
z = []

#file input and read

inputDem = False
while inputDem == False:
    try:
        demFile = raw_input("Enter the DEM file path: ")
        f = open(demFile, 'r')
        inputDem = True
    except IOError:
        print """\nCannot detect file.
Please type the name correctly."""
        break

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
        elif i.isalpha() == False:#insert z values into a separate list            
            k = i.strip()
            k = k.split()
            for o in range(len(k)):
                z.append(k[o])
            
#function to write formatted values to an empty XYZ file
def writeXYZ(m, t):
    j = 0
    for i in xyz:     
        m.writelines(xyz[j])
        #print xyz[j][0].strip(),xyz[j][1].strip(),xyz[j][2].strip()
        j+=1
    m.close()

#function to convert z values into integers:
def convertZtoInt():
    counter = 0
    for obs in z:
        s = int(float(obs))
        z.remove(obs)
        z.insert(counter, s)
        countInt = z[0:1000].count(s)
        counter += 1
        print s, countInt
        
"""
#print histogram
def printHistogram():
    for integer in z:
        intCount = z.count(integer)
        print integer, intCount*'*'
"""       

demFile = "C:\Users\G Torres\Documents\UP Diliman Stuff\GmE 205\MachineProblems\dream_dem2.asc"

f = open(demFile, 'r')
readASCII(f)
c = convertCoord(hdr['dx'], hdr['dy'])
formatXYZ(hdr['ncols'], hdr['nrows'], hdr['dx'], hdr['dy'],
         hdr['xllcorner'], hdr['yllcorner'], z, c[0], c[1])
f.close()

h = "C:\Users\G Torres\Documents\UP Diliman Stuff\GmE 205\MachineProblems\\new.xyz"

s = open(h, 'w')
writeXYZ(s, xyz)

convertZtoInt()

#printHistogram()


