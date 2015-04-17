from math import sqrt

class Vector():
    """Base class for vector shapes."""
    
    def __init__(self, x = 0, y = 0, projection = "EPSG:4326", attr = 'None'):
        """ initialize function of vector class"""
        self.x = x
        self.y = y
        self.proj = projection
        if attr == 'None':
            self.attr = {}
        self.coord = ()
        Vector.setGeometry(self, x, y)

    def __str__(self):
        """String representation of Vector instance."""
        return "Coordinates: (%d, %d)\nProjection: %s\nAttributes: %s\n" % \
               (self.x, self.y, self.proj, self.attr)
    
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
        self.coord = self.x, self.y       

class Point(Vector):
    "Point class as subclass of Vector superclass."
    def __init__(self, x=0, y=0):
        Vector.__init__(self, x, y)
        Vector.setGeometry(self, x, y)
        Point.setProjection(self)
            
    def setProjection(self): #overrides setProjection of Vector class
        self.proj = 'None'
        return self.proj

    def __add__(self, other):
        p = Point(other.x, other.y)
        return p
    
    def getGeometry(self):
        return "%d, %d" % (self.x, self.y)
    
class Line(Vector, Point): 
    "Subclass of Vector superclass. Overrides several class functions."
    def __init__(self, x = 0, y = 0, x1=1, y1=1, projection = "EPSG:4326", attr='None'): ##use variable keyword lengths?
        self.p1 = Vector(x,y)
        self.p2 = Vector(x1,y1)
        self.proj = projection
        self._coord = []
        self.attribute = attr
                
    def __str__(self): #overrides Line __str__ function 
        "String representation of a Line instance."
        c = []
        for i in self._coord:
            c.append((i.x,i.y))
        return "Coordinates:%s\nLength: %f\nProjection: %s\nAttribute: %s" \
               % (c, self.getLength(), self.proj, self.attribute)

    def addPoint(self, newX, newY):
        """Add a new point to the line."""
        newP = Point(newX, newY)
        self.setGeometry(newP)
    
    def setGeometry(self, *arg):
        """Mutates instance list of coordinates."""       
        for i in arg:
            self._coord.append(i)

    def getProjection(self):
        pass

    def getGeometry(self):
        """Returns line geometry."""
        c = []
        for i in self._coord:
            c.append((i.x,i.y))
        return c

    def getLength(self):
        """Calculates and returns length of the line."""
        j = 1 #counter for succeeding coordinate
        length = 0
        for i in range(len(self._coord)-1):
            length += sqrt((self._coord[j].x-self._coord[i].x)**2.0+\
                        (self._coord[j].y-self._coord[i].y)**2.0)
        j += 1
        self._length = length
        return self._length

class Polygon(Line):
    "Subclass of Vector and Line superclasses."
    def __init__(self, x=0, y=0, x1=1, y1=1, x2=2, y2=2, projection="EPSG:4326", attr='None'):
        """Inherits instance attributes from Line constructor."""
        Line.__init__(self, x, y, x1, y1, projection, attr)
        self.p3 = Point(x2, y2)
        self.setGeometry(self.p1, self.p2, self.p3, self.p1)

    def __str__(self): #overrides Vector __str__ function 
        "String representation of a Line instance."
        c = []
        for i in self._coord:
            c.append((i.x,i.y))
        return "Coordinates:%s\nPerimeter: %f\nProjection: %s\nAttribute: %s" \
               % (c, self.getPerimeter(), self.proj, self.attribute)

    def setGeometry(self, *arg):
        for i in arg:
            self._coord.append(i)

    def getArea(self):
        pass

    def checkClosed(self):
        if self._coord[0] == self._coord[len(self._coord)-1]:
            return True
        else: return False

    def addPoint(self, newX, newY): #overrides addPoint function from Line class
        """Add a new point to the line."""
        newP = Point(newX, newY)
        self._coord.insert(len(self._coord)-1, newP)
    
    def getPerimeter(self):
        """Calculates and returns length of the line."""
        j = 1 #counter for succeeding coordinate
        perimeter = 0
        for i in range(len(self._coord)-1):
            perimeter += sqrt((self._coord[j].x-self._coord[i].x)**2.0+(self._coord[j].y-self._coord[i].y)**2.0)
        j += 1
        return perimeter

def main():
    """
    inputs = True
    line = Line()
    print "No. of items in _coord: %d\n" % len(line._coord)
    print line

    line.addPoint(10, 10)
    line.addPoint(20, 20)
    line.addPoint(1000,1000)
    
    j = 1 #counter for succeeding coordinate
    length = 0
    for i in range(len(line._coord)-1):
        length += sqrt((line._coord[j].x-line._coord[i].x)**2.0+\
                        (line._coord[j].y-line._coord[i].y)**2.0)
        j += 1
    print "\nlength now: %f" % length 
    print "No. of items in _coord: %d" % len(line._coord)
    print line.getGeometry()
    """
    polygon = Polygon(x1=0,y1=1,x2=1,y2=1)
    polygon.addPoint(1,0)
    print polygon
    print "\nIs it closed? ", polygon.checkClosed()
    
if __name__ == "__main__":   
    main()
    
    
    
	
