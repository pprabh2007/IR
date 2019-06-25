from classes import Evaluation
from classes import System

import os
systems_list = os.listdir("systems")

p_val = [0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.92, 0.94]

eval = Evaluation("gold/qrels.trec9.main_web")
eval.getRelevantLists()
print("Gold Standard Loaded.. ")
eval.setSystems(systems_list)
print("Systems Loaded.. ")
for p in p_val:
	eval.getScores(p)
	print("For p={}, Scores Obtained.. ".format(p))
	eval.generateTable(p)