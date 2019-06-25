
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

x10=[]
x20=[]
x30=[]
x100=[]
x200=[]
x500=[]
x1000=[]

y10=[]
y20=[]
y30=[]
y100=[]
y200=[]
y500=[]
y1000=[]


file=open("aps.txt")
for line in file:
	line_array = re.split("\\s+|\\t+", line)
	
	x10.append(float(line_array[1]))
	x20.append(float(line_array[2]))
	x30.append(float(line_array[3]))
	x100.append(float(line_array[4]))
	x200.append(float(line_array[5]))
	x500.append(float(line_array[6]))
	x1000.append(float(line_array[7]))
file.close()

file=open("recalls.txt")
for line in file:
	line_array = re.split("\\s+|\\t+", line)
	
	y10.append(float(line_array[1]))
	y20.append(float(line_array[2]))
	y30.append(float(line_array[3]))
	y100.append(float(line_array[4]))
	y200.append(float(line_array[5]))
	y500.append(float(line_array[6]))
	y1000.append(float(line_array[7]))
file.close()

print("****PEARSONS r****")

print("recall@10 vs ap@10: ", calculatePearson(x10, y10))
print("recall@20 vs ap@20: ", calculatePearson(x20, y20))
print("recall@30 vs ap@30: ", calculatePearson(x30, y30))
print("recall@100 vs ap@100: ", calculatePearson(x100, y100))
print("recall@200 vs ap@200: ", calculatePearson(x200, y200))
print("recall@500 vs ap@500: ", calculatePearson(x500, y500))
print("recall@1000 vs ap@1000: ", calculatePearson(x1000, y1000))
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