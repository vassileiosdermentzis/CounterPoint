import WorkingMemory
import Node
import Graph

class InferenceEngine:
	#1. gets C.F from U.I
	#2. modifies the maze (for demo use)
	#3. prepares cantus firmus list
	#4. send it to working memory to examine melodic contour
	#5. receives results
	#6. creates graph according to results
	#7. calls method to find countermelody
	#8 reform given cantus firmus grid
	
	def __init__(self, cantusFirmusGridList):
		self.cantusFirmusGridList=cantusFirmusGridList
		self.graphObject = None
		self.nodeObject = None
		self.cantusFirmusNodeList = []
		self.countermelodyFinalList = []
		self.adjagencyList = {}
		
		cantusFirmusGridList = self.__modifyMaze() #1,2
		self.cantusFirmusNodeList = self.__setCantusFirmusNodeList(cantusFirmusGridList) #3
		self.workingMemoryObject = WorkingMemory.WorkingMemory(self.cantusFirmusNodeList) #4
		self.workingMemoryObject.examineCantusFirmusMelody(self.cantusFirmusNodeList) #5,6
		self.adjagencyList = self.__createGraph(cantusFirmusGridList)
		self.countermelodyFinalList = self.workingMemoryObject.findCounterMelody(self.cantusFirmusNodeList, self.adjagencyList) #7.
		
		self.__mergeFinalCounterpointPathToGrid(cantusFirmusGridList, self.cantusFirmusNodeList, self.countermelodyFinalList) #8

	def __aux(self, node):
		#auxiliary function that returns the coordinate Y of a node
		return node.getCoordinateY()	
	
	def __createGraph(self, cantusFirmusGridList):
		self.graphObject = Graph.Graph()
		for x in range(len(cantusFirmusGridList)):
			for y in range(len(cantusFirmusGridList[x])):
				self.nodeObject = Node.Node( cantusFirmusGridList[x][y], x, y, 0)
				if( y < len(cantusFirmusGridList[x])-1 ):
					for i in range(len(cantusFirmusGridList)):
						nodeObject1 = Node.Node( cantusFirmusGridList[i][y+1], i, y+1, 0 )
						self.graphObject.addEdge(self.nodeObject, nodeObject1, self.workingMemoryObject.getNodesEdge(self.nodeObject,nodeObject1) )
		return self.graphObject.getAdjagencyList()
	
	def __mergeFinalCounterpointPathToGrid(self, cantusFirmusGridList, cantusFirmusNodeList, counterpointList):
		for x in range(len(cantusFirmusGridList)):
			for y in range(len(cantusFirmusGridList[x])):
				if(cantusFirmusGridList[x][y] == '@'):
					self.__replaceCharacterToPosition(cantusFirmusGridList, x, y, '.')
				else:
					for item in cantusFirmusNodeList:
						if x== item.getCoordinateX() and y == item.getCoordinateY():
							self.__replaceCharacterToPosition(cantusFirmusGridList, x, y, item.getPitch(item.getCoordinateX()))
					for item in counterpointList:
						if x == item.getCoordinateX() and y == item.getCoordinateY():
							self.__replaceCharacterToPosition(cantusFirmusGridList, x, y, item.getPitch(item.getCoordinateX()))
		return cantusFirmusGridList
	
	#TODO: mvc
	def __modifyMaze(self):
        # select each line in the grid
		for x in range(len(self.cantusFirmusGridList)):                                          
            # identify each character in the line
			for y in range(len(self.cantusFirmusGridList[x])):
                # assign the grid reference to the variable character
				charCharacter = self.cantusFirmusGridList[x][y]
                # if the array contains an * (cantus firmus melodic line)
				if charCharacter == "*":
                    #if y==0 or y==length put an '@' at every node but 1 and 8
					if y==0 or y==len(self.cantusFirmusGridList[x])-1:
						for iterator in range(x):
							if abs(iterator-x) != 7:
								self.__replaceCharacterToPosition(self.cantusFirmusGridList,iterator,y,'@')
                                #also put '@' in every node but leading nodes at measure before the last
								if y==len(self.cantusFirmusGridList[x])-1 and abs(iterator-x) !=8 and abs(iterator-x) !=6 and abs(iterator-x) !=1:
									self.__replaceCharacterToPosition(self.cantusFirmusGridList,iterator,y-1,'@')
					else:
                        #and at every path below of it
                        #put an '@' at every 2nd, 4th and 7th path above of it
						self.__replaceCharacterToPosition(self.cantusFirmusGridList,x-1,y,"@")
						self.__replaceCharacterToPosition(self.cantusFirmusGridList,x-3,y,"@")
						self.__replaceCharacterToPosition(self.cantusFirmusGridList,x-6,y,"@")
                    #and at every path below of it
					for iterator in range(x+1,len(self.cantusFirmusGridList)):
						self.__replaceCharacterToPosition(self.cantusFirmusGridList,iterator,y,"@")
		return self.cantusFirmusGridList
	
	def __replaceCharacterToPosition(self, list_, intPositionOfElement, intPositionOfCharacter, charCharacter):
        #Since Strings in Python are immutable I use this snippet
		StringListElement = list(list_[intPositionOfElement])
		StringListElement[intPositionOfCharacter] = charCharacter
		newStringFromListElement = "".join(StringListElement)
		list_[intPositionOfElement] = newStringFromListElement
	
	def __setCantusFirmusNodeList(self, cantusFirmusGridList):
		#this is the input-U.I (drumpad)
		for x in range(len(cantusFirmusGridList)):
			for y in range(len(cantusFirmusGridList[x])):
				charCharacter = cantusFirmusGridList[x][y]
                # if the array contains an * (cantus firmus melodic line)
				if charCharacter == "*":
					self.nodeObject = Node.Node(cantusFirmusGridList[x][y], x, y, 0)
					self.cantusFirmusNodeList.append(self.nodeObject)
        #because of the fact that the object is not callable
        #and for loops access items linearly
        #the nodes inside cantus firmus seem to be unordered.
        #The order has to do with time interval which in our case is the Y coordinate
        #Thus we order cantus firmus elements by Y ascending
		self.cantusFirmusNodeList.sort(key=self.__aux)
		return self.cantusFirmusNodeList
	
	def getGraph(self, ):
		return self.graphObject.getAdjagencyList()