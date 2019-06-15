from classes import Evaluation
from classes import System

import os
systems_list = os.listdir("systems")

eval = Evaluation("gold/qrels.trec9.main_web")
print("Gold Standard Loaded.. ")
eval.setSystems(systems_list)
print("Systems Loaded.. ")
eval.setSystemsRanksLists()
print("Systems Rank Lists Generated.. ")
eval.getScores()
print("Scores Obtained.. ")
eval.generateTable()