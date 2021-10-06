import MelodicContourExaminer
import CounterMelody
import KnowledgeBase

class WorkingMemory:
	#sends C.F to melodic contour examiner
	#gets results
	#sends them back to inference engine
	#calls countermelody to find the counterpoint
	def __init__(self, cantusFirmusNodeList):
		self.cantusFirmusNodeList = cantusFirmusNodeList
		self.melodicContourExaminerObject = None
		self.counterMelodyObject = None
		self.knowledgeBaseObject = None
	
	def examineCantusFirmusMelody(self, cantusFirmusNodeList):
		self.melodicContourExaminerObject = MelodicContourExaminer.MelodicContourExaminer(cantusFirmusNodeList)
	
	def findCounterMelody(self, cantusFirmusNodeList, adjagencyList):
		self.counterMelodyObject = CounterMelody.CounterMelody(cantusFirmusNodeList, adjagencyList)
		return self.counterMelodyObject.getCountermelody(cantusFirmusNodeList, adjagencyList)
			
	def formNodeCost(self, nodeA, nodeB):
		self.melodicContourExaminerObject.getAdditionalCost(nodeA, nodeB)
	
	def getNodesEdge(self, nodeA, nodeB):
		self.knowledgeBaseObject = KnowledgeBase.KnowledgeBase()
		return self.knowledgeBaseObject.lap(nodeA, nodeB)
	
	def getCounterMelody(self, cantusFirmusNodeList, adjagencyList):
		self.counterMelodyObject.getCountermelody(cantusFirmusNodeList, adjagencyList)