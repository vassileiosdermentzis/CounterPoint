import KnowledgeBase
class MelodicContourExaminer:
	
	def __init__(self, cantusFirmusNodeList):
		self.cantusFirmusNodeList = cantusFirmusNodeList
		self.knowledgeBaseObject = KnowledgeBase.KnowledgeBase()
		self.__DictionaryContourExaminationResults = {
			'step-wise motion':0,
			'skip-wise motion':0,
			'skip-wise laps':{},
			'repetitive motion':0,
			'ascending motion':0,
			'descending motion':0,
			'symmetric motion':0
		}
		
		self.__examineCantusFirmus(cantusFirmusNodeList)
	
	def getAdditionalCost(self, nodeA, nodeB):
		totalCost = 0
		if(self.knowledgeBaseObject.stepwiseMotion(nodeA, nodeB)):
			totalCost = totalCost + self.__DictionaryContourExaminationResults.get('step-wise motion')
		if(self.knowledgeBaseObject.skipwiseMotion(nodeA, nodeB)):
			totalCost = totalCost +self.__DictionaryContourExaminationResults.get('skip-wise motion')
		if(self.knowledgeBaseObject.repetitiveMotion(nodeA, nodeB)):
			totalCost = totalCost + self.__DictionaryContourExaminationResults.get('repetitive motion')
		if(self.knowledgeBaseObject.ascendingMotion(nodeA, nodeB)):
			totalCost = totalCost + self.__DictionaryContourExaminationResults.get('ascending motion')
		if(self.knowledgeBaseObject.descendingMotion(nodeA, nodeB)):
			totalCost = totalCost + self.__DictionaryContourExaminationResults.get('descending motion')
		
		return totalCost
		#TODO: examining cf stylistic approach
	
	def __examineCantusFirmus(self, cantusFirmusNodeList):
		#examining cf motions
		for i in range(len(cantusFirmusNodeList)-1):
			if(self.knowledgeBaseObject.stepwiseMotion(cantusFirmusNodeList[i],cantusFirmusNodeList[i+1])):
				self.__updateDictValues(self.__DictionaryContourExaminationResults, 'step-wise motion', 1/8)
			if(self.knowledgeBaseObject.skipwiseMotion(cantusFirmusNodeList[i],cantusFirmusNodeList[i+1])):
				self.__updateDictValues(self.__DictionaryContourExaminationResults, 'skip-wise motion', 1/8)
				self.__updateDictValues(self.__DictionaryContourExaminationResults.get('skip-wise laps'), self.knowledgeBaseObject.lap(cantusFirmusNodeList[i],cantusFirmusNodeList[i+1]),1/8)
			if(self.knowledgeBaseObject.repetitiveMotion(cantusFirmusNodeList[i],cantusFirmusNodeList[i+1])):
				self.__updateDictValues(self.__DictionaryContourExaminationResults, 'repetitive motion', 1/8)
			if(self.knowledgeBaseObject.ascendingMotion(cantusFirmusNodeList[i],cantusFirmusNodeList[i+1])):
				self.__updateDictValues(self.__DictionaryContourExaminationResults, 'ascending motion', 1/8)
			if(self.knowledgeBaseObject.descendingMotion(cantusFirmusNodeList[i],cantusFirmusNodeList[i+1])):
				self.__updateDictValues(self.__DictionaryContourExaminationResults, 'descending motion', 1/8)
			if(self.knowledgeBaseObject.symmetricMotion(cantusFirmusNodeList, i)):
				self.__updateDictValues(self.__DictionaryContourExaminationResults, 'symmetric motion', 1/8)
				
	def __updateDictValues(self, dictionary, key, value):
		if(key in dictionary):
			dictionary.update({key: dictionary.get(key)+value})