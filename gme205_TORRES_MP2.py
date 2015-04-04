class Vector():
    """Base class for vector shapes."""
    
    def __init__(self, x = 0, y = 0, projection = "EPSG:4326", attr = 'None'):
        """ initialize function of vector class"""
        self.coord = x, y
        self.proj = projection
        if attr == 'None':
            self.attr = {}

    def __str__(self):
        return "%d, %d" % (self.coord[0], self.coord[1])
        
    def setProjection(self, projString = ""):
        """sets projection string"""
        self.proj = projString

    def getProjection(self):
        """Gets vector projection."""
        return self.proj
        
    def getGeometry(self):
        """Gets vector geometry."""
        return self.coord
        
    def setGeometry(self, inputX, inputY):
        self.coord = inputX, inputY

class Point(Vector):
    def __init__(self): #inherits init function of the Vector class
        Vector.__init__()    

    def setProjection(self): #overrides setProjection of Vector class
        return "None"
    
class Line(Vector, Point):
    def __init__(self, x1 = 0, y1 = 0, x2 = 1, y2 = 1, projection = ""):
        Vector.__init__()
        self._coord = [(x1, y1), (x2, y2)] #mutates coord instance variable

    def __str__(self): #overrides Vector __str__ function
        counterX = 1
        counterY = 1
        for i in _coord:
            return "x" + str(counterX) + ":" + "%d" + "," + \
                   "y" + str(counterY) + ":" + "%d" \
                    % (i[0], i[1])
            counterX += 1
            counterY += 1    

    def setGeometry(self, inputX, inputY):
        if len(self._coord) <= 2:
            return "You must add another point."
        else:
            self.coord.append((inputX, inputY))

    def getLength(self): pass
        
        
class Polygon(Vector, Line, Point): pass
        
		
	
