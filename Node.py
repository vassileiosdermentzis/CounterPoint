#important: variable vs. class attribute
#https://stackoverflow.com/questions/12790114/python-why-is-this-class-variable-not-defined-in-the-method
class Node:
    dictionaryPitch = {
        'C': [0,7,14],
        'D': [6,13],
        'E': [5,12],
        'F':[4,11],
        'G':[3,10],
        'A':[2,9],
        'B':[1,8]
    }
    
    def __init__(self, charContent, intCoordinateX, intCoordinateY, intAdditionalCost):
        self.charContent = charContent
        self.intCoordinateX = intCoordinateX
        self.intCoordinateY = intCoordinateY
        self.intAdditionalCost = intAdditionalCost
        self.neighbors={} #key:node, value:weight
        self.pitch = None

    #getters
    def getAdditionalCost(self):
        return self.intAdditionalCost
    
    def getCoordinates(self):
        return (self.intCoordinateX, self.intCoordinateY)
    
    def getCoordinateX(self):
        return self.intCoordinateX
    
    def getCoordinateY(self):
        return self.intCoordinateY
    
    def getNodeConnections(self):
        for item in self.neighbors:
            print('the node is connectedTo:', item.getCoordinates(), ' with weight ', self.neighbors[item])
    
    def getNeighbors(self, ):
        return self.neighbors

    def getNodeContent(self):
        return self.charContent
    
    def getPitch(self,intCoordinateX):
        #look coordinateX
        #look it up in dictionary
        #print the key
        for key in self.dictionaryPitch:
            for listObj in self.dictionaryPitch[key]:
                if listObj==intCoordinateX:
                    self.pitch = key
        return self.pitch
    
    def getWeight(self, neighborNode):
        return self.neighbors[neighborNode] 

    #setters
    def setAdditionalCost(self, intAdditionalCost):
        self.intAdditionalCost = intAdditionalCost
    
    def setCoordinateX(self, intCoordinateX):
        self.intCoordinateX = intCoordinateX
    
    def setCoordinateY(self, intCoordinateY):
        self.intCoordinateY = intCoordinateY
    
    def setNeighbor(self, node, intWeight=0):
        self.neighbors.update({node:intWeight})
        
    def setNodeContent(self, charContent):
        self.charContent = charContent