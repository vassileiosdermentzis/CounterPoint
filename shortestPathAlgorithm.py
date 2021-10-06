#A* algorithm implementation
#f(n) = g(n) + h(n) where
#g(n) the additional cost of each node
#h(n) heuristic
#openSet: A list with all unvisited nodes
#closedSet: A list with all visited nodes.
import KnowledgeBase

class ShortestPathAlgorithm:
    
    def __init__(self, cantusFirmusNodeList, adjagencyList):
        self.cantusFirmusNodeList = cantusFirmusNodeList
        self.adjagencyList = adjagencyList
        self.f = 0
        self.g = 0
        self.h = 0
        self.openSet = []
        self.closedSet = []
        
        self.ListAuxiliaryList = [] #
        self.alternativePathList = [] #holds nodes for checking alternative solutions:
        self.countermelodyPath = [] #the final contrapuntal path
        
        self.knowledgeBaseObject = None
    
    #get the adjagency graph
    #apply shortest path lgorithm
    #return countermelody
    
    def __candidates(self, adjagencyList, NodeItem):
        auxiliaryList = []
        auxiliaryDictionary={}
        for key in adjagencyList:
            #search candiates of specific nodeItem 
            if self.__isEqual(key, NodeItem):
                for item in adjagencyList[key]: #values {node:weight}
                    #opt out the nodes that contain '@'
                    if not (item.getNodeContent() == '@'):
                        print(type(item.getAdditionalCost()))
                        self.g = item.getAdditionalCost()
                        print(type(adjagencyList[key][item]))
                        self.h = adjagencyList[key][item]
                        self.f = self.g + self.h
                        auxiliaryDictionary.update({self.f:item})
         #sort list by additional cost+lap auxiliaryList.append(key)
        for key in sorted(auxiliaryDictionary.keys()):
            auxiliaryList.append(auxiliaryDictionary[key])
        auxiliaryList.reverse()
        return auxiliaryList
    
    def __drawPath(self, list_):
        for listItem in list_:
            print(listItem.getCoordinates(), end='\t')
            
    def __gatherPossibleNodesInTheBeginning(self, adjagencyList):
        auxiliaryList = []
        for key in adjagencyList:
            if key.getCoordinateY()==0 and not key.getNodeContent() == '@':
                auxiliaryList.append(key)
        auxiliaryList.sort(key=self.__sortByAdditionalCost)
        auxiliaryList.reverse()
        print('possible nodes in the beginning:')
        self.__drawPath(auxiliaryList)
        return auxiliaryList
    
    def __isEmpty(self, List):
		#pythonic way of checking is the implicit way of checking
		#for more info:
		#https://stackoverflow.com/questions/32901416/python-explicit-condition-checking-compared-to-implicit
        return 1 if not List else 0
    
    def __isEqual(self, node1, node2):
		#overriding equal (==) method to check if two nodes are identical.
		#Since the nodes will be stored in different address in memory, the '==' operator won't work.
		#in Python the == operator will only return true iff the two objects refer to the same address in memory
		#for more info:
		#https://stackoverflow.com/questions/6423814/is-there-a-way-to-check-if-two-object-contain-the-same-values-in-each-of-their-v
		#Thus I use this snippet
        return (
            node1.getNodeContent() == node2.getNodeContent()
            and node1.getCoordinateX() == node2.getCoordinateX()
            and node1.getCoordinateY() == node2.getCoordinateY()
            and node1.getAdditionalCost() == node2.getAdditionalCost()
            )
    
    def __sortByAdditionalCost(self, node):
        return node.getAdditionalCost()
    
    def calculateCounterMelody(self, cantusFirmusNodeList, adjagencyList):
        self.knowledgeBaseObject = KnowledgeBase.KnowledgeBase()
        index = 0
        alternativePathIndex = 0
        self.alternativePathList.extend(self.__gatherPossibleNodesInTheBeginning(adjagencyList))
        self.countermelodyPath.append(self.alternativePathList.pop(-1)) #by default -1 pops the last item
        while( index < len(cantusFirmusNodeList) and alternativePathIndex >= 0): #negative indexing means beginning from the end
            self.alternativePathList.extend(self.__candidates(adjagencyList, self.countermelodyPath[index]))
            index = self.alternativePathList[-1].getCoordinateY()#by default -1 returns the last item of the list
            while(alternativePathIndex != len(self.alternativePathList)-1 ):
                self.countermelodyPath.append(self.alternativePathList.pop(-1))
                print('altList:')
                self.__drawPath(self.alternativePathList)
                print('pathList:')
                self.__drawPath(self.countermelodyPath)
				# print('index:', index)
				# print('alternative index:', alternativePathIndex)
				
                if(
					self.knowledgeBaseObject.consecutiveFifths(self.countermelodyPath, cantusFirmusNodeList, index)\
					or self.knowledgeBaseObject.parallelFifths(self.countermelodyPath, cantusFirmusNodeList, index)\
					or self.knowledgeBaseObject.consecutiveEights(self.countermelodyPath, cantusFirmusNodeList, index)\
					or self.knowledgeBaseObject.parallelEights(self.countermelodyPath, cantusFirmusNodeList, index)\
                    or self.knowledgeBaseObject.unison(self.countermelodyPath[index], cantusFirmusNodeList[index])\
                    or self.knowledgeBaseObject.consecutiveThirds(self.countermelodyPath,cantusFirmusNodeList)\
                    or self.knowledgeBaseObject.consecutiveSixths(self.countermelodyPath,cantusFirmusNodeList)\
                    or self.knowledgeBaseObject.crossing(self.countermelodyPath, cantusFirmusNodeList, index)\
                    or self.knowledgeBaseObject.obliqueMotion(self.countermelodyPath, cantusFirmusNodeList, index)\
                    or self.knowledgeBaseObject.interval(self.countermelodyPath[index], cantusFirmusNodeList[index]) > 13\
                    or self.knowledgeBaseObject.leapOfSeven(self.countermelodyPath,index)\
                    or self.knowledgeBaseObject.highLeaps(self.countermelodyPath,index)
                    ):
                    print('node', self.countermelodyPath[index].getCoordinates(), 'could not meet requirements')
                    self.countermelodyPath.pop(-1)
                    index = self.alternativePathList[-1].getCoordinateY()
					
                    if(alternativePathIndex == len(self.alternativePathList)-1):
						#none of nodes inside ListAuxiliaryList couldn't meet requirements
						#check again possible nodes for the node in CantusFirmusList where index = index - 1
                        alternativePathIndex = alternativePathIndex - 1
                        index = self.alternativePathList[-1].getCoordinateY()
                        if index == 0 and not self.__isEmpty(self.alternativePathList):
                            self.countermelodyPath.clear()
                            self.countermelodyPath.append(self.alternativePathList.pop(-1))
                            break
                        else:
                            del self.countermelodyPath[index:]
                else:
                    print('node', self.countermelodyPath[index].getCoordinates(), 'seems to be ok.')
                    alternativePathIndex = len(self.alternativePathList)-1
            if index == 7:
                break
        if(index < len(cantusFirmusNodeList)-1):
            print('no possible solution for this cantus firmus')
            print('attempting mirror...')
        else:
            print('the final contrapuntal path:')
            self.__drawPath(self.countermelodyPath)
            
    def getCountermelodyPath(self, ):
        return self.countermelodyPath