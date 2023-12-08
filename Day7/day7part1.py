import glob 
import os.path 
import csv
import os
import re
import requests

pattern1=r"([AKQTJ0-9]{5})"
#Pattern pour extraire les cartes
pattern2=r"([ ][0-9]+)"
#Pattern pour extraire les bids (avec un esapce devant viré par le int())


hands={}
output=[0]
test="QQQQQ"
strength={"A":13,"K":12,"Q":11,"J":10,"T":9,"9":8,"8":7,"7":6,"6":5,"5":4,"4":3,"3":2,"2":1}
cards=["A","K","Q","J","T","9","8","7","6","5","4","3","2"]

def WalkThroughDay7(filename):
	with open(filename, "r") as file:
		#Classement des data d'entrée et analyse de la power
		for counter,line in enumerate(file):
			hands[counter]={}
			hands[counter]["power"]={}
			hands[counter]["cards"]={}
			hands[counter]["bids"]={}
			hands[counter]["rank"]=1
			data=re.search(pattern1,line)
			cleanData=data.group()
			hands[counter]["cards"]=cleanData
			power=identifyCardSets(cleanData)
			hands[counter]["power"]=power
			data=re.search(pattern2,line)
			hands[counter]["bids"]=data.group()
		
		#classement
		for keys in hands:
			for subkeys in hands :
				side1=hands[keys]
				side2=hands[subkeys]
				if (side1["cards"]==side2["cards"]):
					pass
				elif(side1["power"]>side2["power"]):
					print(side1["cards"] +" > "+ side2["cards"])
					side1["rank"]=side1["rank"]+1
				elif(side1["power"] == side2["power"]):
					print("on doit comparer les cartes individuelles")
					ballot=compareStrength(side1["cards"],side2["cards"])
					if (ballot==1):
						side1["rank"]=side1["rank"]+1

		#comptage des points
		for keys in hands:
			output[0]=output[0]+(int(hands[keys]["rank"])*int(hands[keys]["bids"]))

def identifyCardSets(data):
	pairs=0
	threeOfAKind=0
	testStrongHand={}
	for i in cards:	
		if (data.count(i)==5):
			return(7)
		elif (data.count(i)==4):
			return(6)
		elif (data.count(i)==3):
			threeOfAKind=1
		elif (data.count(i)==2):
			pairs=pairs+1
		elif (data.count(i)==1):
			testStrongHand[i]=1
	if (pairs==1 and threeOfAKind==1):
		return(5)
	elif(threeOfAKind==1):
		return(4)
	elif(pairs==2):
		return(3)
	elif(pairs==1):
		return(2)
	elif(len(testStrongHand)==5):
		return(1)
	else:
		return(0)
		
def compareStrength(side1,side2):
	for i in range(len(side1)):
		print(strength[side1[i]])
		print(strength[side2[i]])
		if (strength[side1[i]] >  strength[side2[i]]):
			print("du coup " + side1 + " > " +side2)
			return(1)
		elif(strength[side1[i]] <  strength[side2[i]]):
			print("malheureusement " + side1 + " < " +side2)
			return(0)
	print("error = 2 identical hands")


WalkThroughDay7("input7.txt")
#a=identifyCardSets(test)
print(hands)
print(output)

