import shortestPathAlgorithm

class CounterMelody:
	
	def __init__(self, cantusFirmusNodeList, adjagencyList):
		self.cantusFirmusNodeList = cantusFirmusNodeList
		self.adjagencyList = adjagencyList
		self.shortestPathAlgorithmObject = None 
	
	def getCountermelody(self, cantusFirmusNodeList, adjagencyList):
		self.shortestPathAlgorithmObject = shortestPathAlgorithm.ShortestPathAlgorithm()
		self.shortestPathAlgorithmObject.calculateCounterMelody(cantusFirmusNodeList, adjagencyList)
		self.shortestPathAlgorithmObject.getCountermelodyPath()