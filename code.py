
def calculatePearson(list1, list2):

	list1 = list(list1)
	list2 = list(list2)

	length = len (list1)

	m1=0.0
	r1=0.0
	for val in list1:
		m1 = m1 + val
		r1 = r1 + (val*val)
	m1 = m1/length
	r1 = r1/length

	m2=0.0
	r2=0.0
	for val in list2:
		m2 = m2 + val
		r2 = r2 + (val*val)
	m2 = m2/length
	r2 = r2/length

	m1m2 = 0.0
	for i in range(length):
		m1m2 = m1m2 + (list1[i]*list2[i])
	m1m2 = m1m2/length

	numerator = m1m2 - (m1*m2)
	denominator = ((r1 - (m1*m1))*(r2 - (m2*m2)))**0.5

	return numerator/denominator

import re

seven=[]
eight=[]
eightfive = []
nine=[]
ninetwo = []
ninefour = []

p5=[]
p10=[]
p15=[]
p20=[]
p30=[]
p100=[]
p200=[]
p500=[]
p1000=[]


file=open("xd.txt")
for line in file:
	line_array = re.split("\\s+|\\t+", line)
	if(line_array[0]=="P5"):
		p5.append(float(line_array[2]))
	elif(line_array[0]=="P10"):
		p10.append(float(line_array[2]))
	elif(line_array[0]=="P15"):
		p15.append(float(line_array[2]))
	elif(line_array[0]=="P20"):
		p20.append(float(line_array[2]))
	elif(line_array[0]=="P30"):
		p30.append(float(line_array[2]))
	elif(line_array[0]=="P100"):
		p100.append(float(line_array[2]))
	elif(line_array[0]=="P200"):
		p200.append(float(line_array[2]))
	elif(line_array[0]=="P500"):
		p500.append(float(line_array[2]))
	elif(line_array[0]=="P1000"):
		p1000.append(float(line_array[2]))
		if(int(line_array[1])==500):
			break

file = open("7.txt")
for line in file:
	line_array = re.split("\\s+|\\t+", line)
	if(len(line_array)<2):
		break
	seven.append(float(line_array[1]))
file.close()

file = open("8.txt")
for line in file:
	line_array = re.split("\\s+|\\t+", line)
	if(len(line_array)<2):
		break
	eight.append(float(line_array[1]))
file.close()

file = open("85.txt")
for line in file:
	line_array = re.split("\\s+|\\t+", line)
	if(len(line_array)<2):
		break
	eightfive.append(float(line_array[1]))
file.close()

file = open("9.txt")
for line in file:
	line_array = re.split("\\s+|\\t+", line)
	if(len(line_array)<2):
		break
	nine.append(float(line_array[1]))
file.close()

file = open("92.txt")
for line in file:
	line_array = re.split("\\s+|\\t+", line)
	if(len(line_array)<2):
		break
	ninetwo.append(float(line_array[1]))
file.close()

file = open("94.txt")
for line in file:
	line_array = re.split("\\s+|\\t+", line)
	if(len(line_array)<2):
		break
	ninefour.append(float(line_array[1]))
file.close()

print("****PEARSONS r****")

print("P5 & p=0.7: ", calculatePearson(p5, seven))
print("P5 & p=0.8: ",calculatePearson(p5, eight))
print("P5 & p=0.85: ",calculatePearson(p5, eightfive))
print("P5 & p=0.9: ",calculatePearson(p5, nine))
print("P5 & p=0.92: ",calculatePearson(p5, ninetwo))
print("P5 & p=0.94: ",calculatePearson(p5, ninefour))
print()
print("P10 & p=0.7: ", calculatePearson(p10, seven))
print("P10 & p=0.8: ",calculatePearson(p10, eight))
print("P10 & p=0.85: ",calculatePearson(p10, eightfive))
print("P10 & p=0.9: ",calculatePearson(p10, nine))
print("P10 & p=0.92: ",calculatePearson(p10, ninetwo))
print("P10 & p=0.94: ",calculatePearson(p10, ninefour))
print()
print("P15 & p=0.7: ", calculatePearson(p15, seven))
print("P15 & p=0.8: ",calculatePearson(p15, eight))
print("P15 & p=0.85: ",calculatePearson(p15, eightfive))
print("P15 & p=0.9: ",calculatePearson(p15, nine))
print("P15 & p=0.92: ",calculatePearson(p15, ninetwo))
print("P15 & p=0.94: ",calculatePearson(p15, ninefour))
print()
print("P20 & p=0.7: ", calculatePearson(p20, seven))
print("P20 & p=0.8: ",calculatePearson(p20, eight))
print("P20 & p=0.85: ",calculatePearson(p20, eightfive))
print("P20 & p=0.9: ",calculatePearson(p20, nine))
print("P20 & p=0.92: ",calculatePearson(p20, ninetwo))
print("P20 & p=0.94: ",calculatePearson(p20, ninefour))
print()
print("P30 & p=0.7: ", calculatePearson(p30, seven))
print("P30 & p=0.8: ",calculatePearson(p30, eight))
print("P30 & p=0.85: ",calculatePearson(p30, eightfive))
print("P30 & p=0.9: ",calculatePearson(p30, nine))
print("P30 & p=0.92: ",calculatePearson(p30, ninetwo))
print("P30 & p=0.94: ",calculatePearson(p30, ninefour))
print()
print("P100 & p=0.7: ", calculatePearson(p100, seven))
print("P100 & p=0.8: ",calculatePearson(p100, eight))
print("P100 & p=0.85: ",calculatePearson(p100, eightfive))
print("P100 & p=0.9: ",calculatePearson(p100, nine))
print("P100 & p=0.92: ",calculatePearson(p100, ninetwo))
print("P100 & p=0.94: ",calculatePearson(p100, ninefour))
print()
print("P200 & p=0.7: ", calculatePearson(p200, seven))
print("P200 & p=0.8: ",calculatePearson(p200, eight))
print("P200 & p=0.85: ",calculatePearson(p200, eightfive))
print("P200 & p=0.9: ",calculatePearson(p200, nine))
print("P200 & p=0.92: ",calculatePearson(p200, ninetwo))
print("P200 & p=0.94: ",calculatePearson(p200, ninefour))
print()
print("P500 & p=0.7: ", calculatePearson(p500, seven))
print("P500 & p=0.8: ",calculatePearson(p500, eight))
print("P500 & p=0.85: ",calculatePearson(p500, eightfive))
print("P500 & p=0.9: ",calculatePearson(p500, nine))
print("P500 & p=0.92: ",calculatePearson(p500, ninetwo))
print("P500 & p=0.94: ",calculatePearson(p500, ninefour))
print()
print("P1000 & p=0.7: ", calculatePearson(p1000, seven))
print("P1000 & p=0.8: ",calculatePearson(p1000, eight))
print("P1000 & p=0.85: ",calculatePearson(p1000, eightfive))
print("P1000 & p=0.9: ",calculatePearson(p1000, nine))
print("P1000 & p=0.92: ",calculatePearson(p1000, ninetwo))
print("P1000 & p=0.94: ",calculatePearson(p1000, ninefour))
'''
------------------------------------------------------------------
import re
dcg=[]
seven=[]
eight=[]
eightfive = []
nine=[]
ninetwo = []
ninefour = []

file = open("dcg.txt")
for line in file:
	line_array = re.split("\\s+|\\t+", line)
	if(len(line_array)<2):
		break
	dcg.append(float(line_array[1]))
file.close()

file = open("7.txt")
for line in file:
	line_array = re.split("\\s+|\\t+", line)
	if(len(line_array)<2):
		break
	seven.append(float(line_array[1]))
file.close()

file = open("8.txt")
for line in file:
	line_array = re.split("\\s+|\\t+", line)
	if(len(line_array)<2):
		break
	eight.append(float(line_array[1]))
file.close()

file = open("85.txt")
for line in file:
	line_array = re.split("\\s+|\\t+", line)
	if(len(line_array)<2):
		break
	eightfive.append(float(line_array[1]))
file.close()

file = open("9.txt")
for line in file:
	line_array = re.split("\\s+|\\t+", line)
	if(len(line_array)<2):
		break
	nine.append(float(line_array[1]))
file.close()

file = open("92.txt")
for line in file:
	line_array = re.split("\\s+|\\t+", line)
	if(len(line_array)<2):
		break
	ninetwo.append(float(line_array[1]))
file.close()

file = open("94.txt")
for line in file:
	line_array = re.split("\\s+|\\t+", line)
	if(len(line_array)<2):
		break
	ninefour.append(float(line_array[1]))
file.close()

print("****PEARSONS r****")

print("DCG & p=0.7: ", calculatePearson(dcg, seven))
print("DCG & p=0.8: ",calculatePearson(dcg, eight))
print("DCG & p=0.85: ",calculatePearson(dcg, eightfive))
print("DCG & p=0.9: ",calculatePearson(dcg, nine))
print("DCG & p=0.92: ",calculatePearson(dcg, ninetwo))
print("DCG & p=0.94: ",calculatePearson(dcg, ninefour))

-----------------------------------------------------------------------
-----------------------------------------------------------------------

import re

file = open("xd.txt")

bprefs={}
aps={}
p_1000 = {}
bprefs_div_aps={}
aps_div_bprefs={}

for line in file:
	line_array = re.split("\\s+|\\t+", line)

	try:
		temp = int(line_array[1])
	except:
		break

	if(line_array[0]=="bpref"):
		bprefs[int(line_array[1])]=float(line_array[2])
	elif(line_array[0]=="map"):
		aps[int(line_array[1])]=float(line_array[2])
	elif(line_array[0]=="P1000"):
		p_1000[int(line_array[1])]=float(line_array[2])
file.close()

file=open("xd2.txt")

for line in file:
	line_array = re.split("\\s+|\\t+", line)

	bprefs[int(line_array[0])]=float(line_array[1])

file.close()

for key in bprefs.keys():
	if(aps[key]==0):
		bprefs_div_aps[key]=0
	else:	
		bprefs_div_aps[key] = bprefs[key]/aps[key]

	if(bprefs[key]==0):
		aps_div_bprefs[key]=0
	else:	
		aps_div_bprefs[key] = aps[key]/bprefs[key]

print('b/w bpref and aps {}'.format(calculatePearson(bprefs.values(), aps.values())))
print('b/w bpref and p_1000 {}'.format(calculatePearson(bprefs.values(), p_1000.values())))
print('b/w aps and p_1000 {}'.format(calculatePearson(aps.values(), p_1000.values())))
print('b/w bpref/aps and p_1000 {}'.format(calculatePearson(bprefs_div_aps.values(), p_1000.values())))
print('b/w aps/bpref and p_1000 {}'.format(calculatePearson(aps_div_bprefs.values(), p_1000.values())))

x = [17, 13, 12, 15, 16, 14, 16, 16, 18, 19]
y = [94, 73, 59, 80, 93, 85, 66, 79, 77, 91]
print(calculatePearson(x, y))

---------------------------------------------------------------------
'''