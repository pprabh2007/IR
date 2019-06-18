import re
import gzip
import math
class System:

	def __init__(self, dir_name, sys_input_file):
		self.sys_input_file = dir_name+"/"+sys_input_file
		self.sys_name = sys_input_file
		self.retrieved_lists={}
		self.CG={}
		self.DCG={}

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

	def getCG(self, eval):
		for topic_number in eval.relevant_lists.keys():
			#print(topic_number)
			ans = 0
			current_list = self.retrieved_lists[topic_number]
			for elem in current_list:
				doc = elem[0]
				score=elem[1]

				try:
					ans = ans + eval.relevant_lists[topic_number][doc]
				except:
					pass

			self.CG[topic_number]=ans

	def getDCG(self, eval):
		for topic_number in eval.relevant_lists.keys():
			ans = 0
			current_list = self.retrieved_lists[topic_number]
			for i, elem in enumerate(current_list):
				doc = elem[0]
				score=elem[1]

				try:
					val = eval.relevant_lists[topic_number][doc]
					if(i==0):
						ans = ans + val
					else:
						ans = ans +(val/math.log2(i+1))

				except:
					pass
			self.DCG[topic_number]=ans

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
				self.relevant_lists[topic_number]={}

			self.relevant_lists[topic_number][split_line[2]]=int(split_line[-1])
		file.close()

	def setSystems(self, array):
		for string in array:
			s = System("systems", string)
			s.getRetrievedLists()
			self.systems.append(s)

	def getScores(self):
		for system in self.systems:
			system.getCG(self)
			system.getDCG(self)

	def generateTable(self):

		result=""
		for system in self.systems:
			result = result + system.sys_name+"\n\n"

			for a, b in system.CG.items():
				result = result + str(a) + "\t" + str(b) +"\n"

			result = result + "\n\n"

		file = open ("results_CG.txt", "w")
		file.write(result)
		file.close()

		result=""
		for system in self.systems:
			result = result + system.sys_name+"\n\n"

			for a, b in system.DCG.items():
				result = result + str(a) + "\t" + str(b) +"\n"

			result = result + "\n\n"

		file = open ("results_DCG.txt", "w")
		file.write(result)
		file.close()
	#def printScores(self):


