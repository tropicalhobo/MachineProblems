"""inputDem = False
while inputDem == False:
    try:
        demFile = raw_input("Enter the DEM file: ")
        f = open(demFile, 'r')
        inputDem = True
    except IOError:
        print "\nCannot detect file."""

#translation of coordinates to center of pixel
#def toCenter():
#parse image parameters from ASCII file

#calculate the coordinates of the center of the pixel

x = []
#function to open and read ASCII file
def readASCII(f):
    dem = open(f, 'r')
    for i in dem:
        
        j=i.replace(' ','')
        #r=j.split('')
        k=j.strip()
        #x.insert(0, k)
    #if k.isdigit()==True:
        
        print k
    dem.close()

demFile = "C:\Users\G Torres\Documents\UP Diliman Stuff\GmE 205\MachineProblems\dream_dem.asc"
readASCII(demFile)    
    
#parse header values and pass to lowerleft-to-center pixel function

#function to create and write XYZ file
#def writeXYZ():

#function to create histogram:
#def makeHistogram():
