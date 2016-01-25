from math import sqrt
import sys

class Vector():
    """Base class for vector shapes."""
    
    def __init__(self, x = 0, y = 0, projection = "EPSG:4326", attr = 'None'):
        """ initialize function of vector class"""
        self.x = x
        self.y = y
        self.proj = projection
        self.attribute = {}
        self.coord = ()
        self.setAttribute(attr)
        self.setGeometry(x, y)

    def __str__(self):
        """String representation of Vector instance."""
        return "Coordinates: (%d,%d)\nProjection: %s\nAttributes: %s\n" % \
               (self.x, self.y, self.proj, self.attribute)
    
    def setProjection(self, projString):
        """Sets projection string"""
        self.proj = projString

    def getProjection(self):
        """Gets vector projection."""
        return self.proj
        
    def getGeometry(self):
        """Gets vector geometry."""
        return self.coord
        
    def setGeometry(self, x, y):
        """Sets vector geometry."""
        self.coord = self.x, self.y

    def setAttribute(self, attr):
        """Sets vector attributes."""
        self.attribute = attr

class Point(Vector):
    """Point class as subclass of Vector superclass."""
    def __init__(self, x=0, y=0, projection = 'None'):
        Vector.__init__(self, x, y, projection)
        Vector.setGeometry(self, x, y)

    def __add__(self, other):
        l = Line(self.x, self.y, other.x, other.y)
        return l
    
class Line(Point): 
    """Subclass of Vector superclass. Overrides several class functions."""
    def __init__(self, x = 0, y = 0, x1=1, y1=1, projection = 'None', attr = 'None'): ##use variable keyword lengths?
        self.p1 = Point(x,y,projection)
        self.p2 = Point(x1,y1,projection)
        self.proj = ''
        self.attribute = {}
        self._coord = []
        self.setGeometry(self.p1, self.p2)
        self.setProjection(projection)
        self.setAttribute(attr)

    def __str__(self): #overrides Line __str__ function 
        """String representation of a Line instance."""
        c = []
        for i in self._coord:
            c.append((i.x,i.y))
        return "Nodes:%s\nLength: %f\nProjection: %s\nAttribute: %s" \
               % (c, self.getLength(), self.proj, self.attribute)

    def __add__(self, other): #overrides __add__ function of Point class
        """Concantenates two Line instances to form a new Line instance."""
        newLine = Line(self.p1.x, self.p1.y, self.p2.x ,self.p2.y)
        newLine.setGeometry(other.p1, other.p2)
        return newLine
    
    def setGeometry(self, *arg):
        """Mutates instance list of coordinates."""       
        for i in arg:
            self._coord.append(i)

    def getProjection(self):
        """Returns vector projection."""
        return self.proj

    def setProjection(self, projection):
        """Sets vector projection."""
        self.proj = projection
    
    def getGeometry(self):
        """Returns line geometry."""
        c = [] 
        for i in self._coord:
            c.append((i.x,i.y))
        return c

    def getLength(self):
        """Calculates and returns length of the line."""
        l = self._coord
        j = 1 #counter for succeeding coordinate
        length = 0
        for i in range(len(l)-1):
            length += sqrt((l[j].x-l[i].x)**2.0 + (l[j].y-l[i].y)**2.0)
            j += 1
        return length

class Polygon(Line, Point):
    """Subclass of Vector and Line superclasses."""
    
    def __init__(self,*arg):
        """Inherits instance attributes from Line constructor."""
        self.pList = []
        self.proj = 'None'
        self.attribute = {}
        self.setGeometry(arg) #Passing the first point again ensures that the polygon is closed
        
    def __str__(self): #overrides inherited __str__ function
        """String representation of a Polygon instance."""
        d = []
        for p in self.pList:
            c = []
            for i in p:
                c.append((i.x,i.y))
            d.append(c)
            
        return "Vertices:%s\nPerimeter: %f\nArea: %f\nProjection: %s\nAttribute: %s" \
               % (d, self.getPerimeter(),self.getArea(), self.proj, self.attribute)

    def addPolygon(self, *arg):
        """Assumes the input is a tuple of x,y coordinates."""
        self.setGeometry(arg)
        
    def setGeometry(self, argList):
        """Sets list of the list of points."""
        b = self.pList
        a = [] #container list for Point instances
        if len(argList) < 3:
            print 'Less than three vertices! Now terminating...'
            sys.exit(1)
        for i, j in enumerate(argList):
            newP = Point(j[0],j[1])
            if i == 0: # condition to store the first point to close the polygon
                pLast = Point(j[0],j[1])
            a.insert(i, newP)
            if i == len(argList)-1: 
                a.append(pLast) #closing the polygon geometry
        b.append(a)
        
    def getArea(self):
        """Calculates the area of the polygon. If there are
            two lists of coordinates, function assumes the
            polygon is a a closed or open doughnut."""
        k = self.pList
        inArea = 0
        outArea = 0
        for i, p in enumerate(k): #iterate lists of coordinate lists
            if i == 0: #the first list within the master list is assumed to be outer polygon
                f = 1 #counter for succeeding coordinate pair
                for s in range(len(p)-1): #iterate coordinate tuples within inner lists
                    outArea += (p[s].x*p[f].y-p[f].x*p[s].y)/2.0
                    f += 1
            else:
                g = 1 #counter for succeeding coordinate pair
                for h in range(len(p)-1):
                    inArea += (p[h].x*p[g].y-p[g].x*p[h].y)/2.0
                    g += 1
        return abs(outArea) - abs(inArea)

    def checkClosed(self):
        """Checks if polygon geometry is closed and returns a bool value."""
        k = self.pList
        isClosed = True
        for l in k:
            if (l[0].x,l[0].y) == (l[len(l)-1].x,l[len(l)-1].y): #checks if the first and last coordinates are equal
                pass
            else:
                isClosed = False
                break #breaks iteration if a single list polygon coordinates is found to be open
        return isClosed
    
    def getPerimeter(self):
        """Calculates and returns length of the line."""
        k = self.pList
        perimeter = 0
        for r, l in enumerate(k):
            j = 1 #counter for succeeding coordinates
            for i in range(len(l)-1):
                perimeter += sqrt((l[j].x-l[i].x)**2.0+(l[j].y-l[i].y)**2.0)
                j += 1
        return perimeter

def main():
    #test for Point instance
    print 'Point test', '\n', '-'*len('Point test')
    p = Point(1,1)
    p2 = Point(100,1)
    print 'Point 1:\n', p, '\nPoint 2:\n', p2

    print 'Adding Point 1 and Point 2... \n'

    newLine = p + p2
    
    print "A new line was created: ", '\n', newLine, '\n'
    
    print '*'*70
    
    #test for Line instance
    print '\nLine test', '\n', '-'*len('Line test')

    line = Line(0,0,0,10)

    line2 = Line(10,10,20,10)
    print 'Line 1:\n', line,'\n\nLine 2:\n', line2
    
    print '\nConcatenating Line 1 and Line 2... \n'

    line3 = line + line2

    print line3, '\n'
    
    print '*'*70

    #test for Polygon instance
    print '\nPolygon Test', '\n', '-'*len('Polygon test')
    polygon = Polygon((0,0),(0,10),(10,10),(10,0))
    polygon.setProjection('EPSG:4326')
    print polygon
    print "\nIs it closed? ", polygon.checkClosed()

    print '\nAdding triangle hole with coordinates [(1,1),(2,2),(2,1)]...\n'
    
    polygon.addPolygon((1,1),(2,2),(2,1))
    print polygon
    print '\nIs it closed?', polygon.checkClosed()
    
if __name__ == "__main__":   
    main()
    
    
    
	
