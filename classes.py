import re
import gzip
class System:

	def __init__(self, dir_name, sys_input_file):
		self.sys_input_file = dir_name+"/"+sys_input_file
		self.sys_name = sys_input_file
		self.retrieved_lists={}
		self.ranks_lists={}
		self.AP_scores={}
		self.MAP_score=None

	def getRetrievedLists(self):
		file = gzip.open(self.sys_input_file, "rb")

		for line in file:
			line = line.decode('utf-8')
			line = line[:-1]
			split_line = re.split("\\t+|\\s+", line)
			
			topic_number = int(split_line[0])
			if(topic_number not in self.retrieved_lists.keys()):			
				self.retrieved_lists[topic_number]=[]

			self.retrieved_lists[topic_number].append([split_line[2], float(split_line[4])  ])

		self.retrieved_lists[topic_number].sort(key= lambda x: x[1], reverse=True)
		#print(self.retrieved_lists)
		file.close()
	
	def printRankLists(self):
		for topic_number in self.ranks_lists.keys():
			print(topic_number)
			print(self.ranks_lists[topic_number])
			print()

	def getMAPScore(self):
		count=0
		sum_val = 0
		for x in self.AP_scores.values():
			sum_val = sum_val + x
			count = count + 1
		#print(count)
		self.MAP_score = float(sum_val)/float(count)

	def getAPScores(self):
		#print(self.ranks_lists)
		for topic_number, data in self.ranks_lists.items():

			sum_var = 0
			for i, rank in enumerate(data):
				sum_var = sum_var + ((i+1)*(1/rank))

			sum_var = sum_var / float(len(data))
			self.AP_scores[topic_number]=sum_var
		
	def getRankLists(self, eval):
		for topic_num in eval.relevant_lists.keys():
			
			topic_relev=eval.relevant_lists[topic_num]
			topic_all = self.retrieved_lists[topic_num]
			
			ideal_size = len (topic_relev)
			self.ranks_lists[topic_num]=[]

			for doc_name in topic_relev:
				for i, doc_name_score in enumerate(topic_all):
					if(doc_name==doc_name_score[0]):
						self.ranks_lists[topic_num].append(i+1)
						break
			x= len(self.ranks_lists[topic_num])
			while(x!=ideal_size):
				self.ranks_lists[topic_num].append(float("inf"))
				x=x+1

			self.ranks_lists[topic_num].sort()

class Evaluation:
	
	def __init__ (self, file):
		self.file_name = file
		self.systems = []
		self.relevant_lists={}

	def getRelevantLists(self):
		file=open(self.file_name)

		for line in file:
			line = line[:-1]
			split_line = re.split("\\t+|\\s+", line)
			
			if(int(split_line[-1])==0):
				continue

			topic_number = int(split_line[0])
			if(topic_number not in self.relevant_lists.keys()):			
				self.relevant_lists[topic_number]=[]

			self.relevant_lists[topic_number].append(split_line[2])
		file.close()

	def setSystems(self, array):
		for string in array:
			s = System("systems", string)
			s.getRetrievedLists()
			self.systems.append(s)

	def setSystemsRanksLists(self):
		self.getRelevantLists()

		for system in self.systems:
			system.getRankLists(self) 

	def getScores(self):
		for system in self.systems:
			system.getAPScores()
			system.getMAPScore()

	def generateTable(self):

		result=""
		for system in self.systems:
			result = result + system.sys_name+"\t"+ str(system.MAP_score) +"\n\n"

			for a, b in system.AP_scores.items():
				result = result + str(a) + "\t" + str(b) +"\n"

			result = result + "\n\n"

		file = open ("results.txt", "w")
		file.write(result)
		file.close()
	#def printScores(self):


