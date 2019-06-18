import re
import gzip
import math
class System:

	def __init__(self, dir_name, sys_input_file):
		self.sys_input_file = dir_name+"/"+sys_input_file
		self.sys_name = sys_input_file
		self.retrieved_lists={}
		self.bpref={}

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

	def getBPREF(self, eval):

		for topic_number in eval.relevant_lists.keys():

			ans = 0
			current_topic_list = self.retrieved_lists[topic_number]
			non_rel = 0

			denominator = min(eval.N[topic_number], eval.R[topic_number])

			for elem in current_topic_list:
				doc = elem[0]
				score = elem[1]

				try:
					x = eval.relevant_lists[topic_number][doc]

					ans = ans + (1 - (non_rel/denominator))

				except:
					non_rel= non_rel+1

			self.bpref[topic_number]=ans/eval.R[topic_number]
		

class Evaluation:
	
	def __init__ (self, file):
		self.file_name = file
		self.systems = []
		self.relevant_lists={}
		self.N={}
		self.R={}

	def getRelevantLists(self):
		file=open(self.file_name)

		for line in file:
			line = line[:-1]
			split_line = re.split("\\t+|\\s+", line)
			topic_number = int(split_line[0])
			if(topic_number not in self.relevant_lists.keys()):			
				self.relevant_lists[topic_number]={}
				self.N[topic_number]=0
				self.R[topic_number]=0


			if(int(split_line[-1])==0):
				self.N[topic_number]=self.N[topic_number]+1
				continue;

			self.relevant_lists[topic_number][split_line[2]]=int(split_line[-1])
			self.R[topic_number]=self.R[topic_number]+1
		file.close()

	def setSystems(self, array):
		for string in array:
			s = System("systems", string)
			s.getRetrievedLists()
			self.systems.append(s)

	def getScores(self):
		for system in self.systems:
			system.getBPREF(self)
			#print(system.bpref)

	def generateTable(self):

		result=""
		for system in self.systems:
			result = result + system.sys_name+"\n\n"

			for a, b in system.bpref.items():
				result = result + str(a) + "\t" + str(b) +"\n"

			result = result + "\n\n"

		file = open ("results_bpref.txt", "w")
		file.write(result)
		file.close()


