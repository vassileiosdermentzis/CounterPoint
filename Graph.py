import Node
class Graph:
    #this class describes a graph and its basic behavior in counterpoint application
    #based in
    #https://bradfieldcs.com/algos/graphs/representing-a-graph/#:~:text=The%20adjacency%20list%20is%20really%20a%20mapping%2C%20so,and%20one%20just%20using%20a%20plain%20dict%20directly.
    
    def __init__(self):
        self.__DictionaryAdjagencyList = {} #key:node values:{node:weight}
    
    def __contains__(self, key):
        return key in self.__DictionaryAdjagencyList
    
    #getters
    def getAdjagencyList(self):
        return self.__DictionaryAdjagencyList
    
    def addEdge(self, nodeA, nodeB, weight=0):
        if nodeA not in self.__DictionaryAdjagencyList:
            self.__addNode(nodeA)
        if nodeB not in self.__DictionaryAdjagencyList:
            self.__addNode(nodeB)
        nodeA.setNeighbor(nodeB, weight)
        self.__DictionaryAdjagencyList.update({nodeA:nodeA.getNeighbors()})
        
    def __addNode(self, node):
        self.__DictionaryAdjagencyList.update({node:{}})

    def __append(self, object_):
        if object_ not in self.ListNodeList:
            self.ListNodeList.append(object_)
#------------------TEST------------------------------
# graphObj = Graph()
# #print("create some Node objects\n")
# #ListNodeLis
#  
# node1 = Node.Node('.', 0, 0, 0)
# node2 = Node.Node('.', 0, 1, 0)
# node3 = Node.Node('-', 1, 1, 20)
# node4 = Node.Node('@', 1, 0, 50)
# 
# graphObj.addEdge(node1, node2, 1)
# graphObj.addEdge(node1, node3, 2)
# graphObj.addEdge(node1, node4, 3)
# node2.setAdditionalCost(15)
# graphObj.addEdge(node2, node3, 2)
# graphObj.addEdge(node2, node4, 3)
# 
# 
# thisdict_= graphObj.getAdjagencyList()
# 
# for item in thisdict_:
#     print(item.getCoordinates(),':')
#     for item2 in thisdict_[item]:
#         print(item2.getCoordinates(),' ',item2.getAdditionalCost(), ' ', thisdict_[item][item2])