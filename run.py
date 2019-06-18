from classes import Evaluation
from classes import System

import os
systems_list = os.listdir("systems")

eval = Evaluation("gold/qrels.trec9.main_web")
eval.getRelevantLists()
print("Gold Standard Loaded.. ")
eval.setSystems(systems_list)
print("Systems Loaded.. ")
eval.getScores()
print("Scores Obtained.. ")
eval.generateTable()