import re
import gzip
class System:

	def __init__(self, dir_name, sys_input_file):
		self.sys_input_file = dir_name+"/"+sys_input_file
		self.sys_name = sys_input_file
		self.retrieved_lists={}
		self.ranks_lists={}
		
		self.AP10_scores={}
		self.AP20_scores={}
		self.AP30_scores={}
		self.AP100_scores={}
		self.AP200_scores={}
		self.AP500_scores={}
		self.AP1000_scores={}

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

	def getAPScores(self):
		#print(self.ranks_lists)
		for topic_number, data in self.ranks_lists.items():

			x = len(data)

			sum_var = 0
			count = 0.0
			for i, rank in enumerate(data):
				
				if(rank>10):
					break

				sum_var = sum_var + ((i+1)*(1/rank))
				count = count + 1.0

			if(count != 0.0):	
				sum_var = sum_var / x
			self.AP10_scores[topic_number]=sum_var

			####################################

			sum_var = 0
			count = 0.0
			for i, rank in enumerate(data):
				
				if(rank>20):
					break

				sum_var = sum_var + ((i+1)*(1/rank))
				count = count + 1.0

			if(count != 0.0):	
				sum_var = sum_var / x
			self.AP20_scores[topic_number]=sum_var

			######################################

			sum_var = 0
			count = 0.0
			for i, rank in enumerate(data):
				
				if(rank>30):
					break

				sum_var = sum_var + ((i+1)*(1/rank))
				count = count + 1.0

			if(count != 0.0):	
				sum_var = sum_var / x
			self.AP30_scores[topic_number]=sum_var

			###################################

			sum_var = 0
			count = 0.0
			for i, rank in enumerate(data):
				
				if(rank>100):
					break

				sum_var = sum_var + ((i+1)*(1/rank))
				count = count + 1.0

			if(count != 0.0):	
				sum_var = sum_var / x
			self.AP100_scores[topic_number]=sum_var

			####################################

			sum_var = 0
			count = 0.0
			for i, rank in enumerate(data):
				
				if(rank>200):
					break

				sum_var = sum_var + ((i+1)*(1/rank))
				count = count + 1.0

			if(count != 0.0):	
				sum_var = sum_var / x
			self.AP200_scores[topic_number]=sum_var

			###################################

			sum_var = 0
			count = 0.0
			for i, rank in enumerate(data):
				
				if(rank>500):
					break

				sum_var = sum_var + ((i+1)*(1/rank))
				count = count + 1.0

			if(count != 0.0):	
				sum_var = sum_var / x
			self.AP500_scores[topic_number]=sum_var
		
			###################################

			sum_var = 0
			count = 0.0
			for i, rank in enumerate(data):

				if(rank>1000):
					break

				sum_var = sum_var + ((i+1)*(1/rank))
				count = count + 1.0

			if(count != 0.0):	
				sum_var = sum_var / x
			self.AP1000_scores[topic_number]=sum_var

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

	def generateTable(self):

		result=""
		for system in self.systems:
			result = result + system.sys_name+"\n"

			for key in system.AP10_scores.keys():
				result = result+str(key)+"\t"+str(system.AP10_scores[key])+"\t"+str(system.AP20_scores[key])+"\t"+str(system.AP30_scores[key])+"\t"+str(system.AP100_scores[key])+"\t"+str(system.AP200_scores[key])+"\t"+str(system.AP500_scores[key])+"\t"+str(system.AP1000_scores[key])+"\n"

		file = open ("aps.txt", "w")
		file.write(result)
		file.close()
	#def printScores(self):


