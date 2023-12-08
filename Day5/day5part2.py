import glob 
import os.path 
import csv
import os
import re
import requests

pattern1=r"([0-9]+)"
#Pattern pour extraire les seeds de la première ligne
pattern2=r"([a-z]+[-][a-z]+[-][a-z]+[ ][a-z:]+)"
#Pattern pour extraire les data de references
pattern3=r"([0-9]+[ ][0-9]+[ ][0-9]+)"
#Lignes de data des maps
pattern4=r"([0-9]+[ ][0-9]+)"


seedsDict={}
mapsDict={}
output=[]
rab=0

def WalkThroughDay5(filename):
	section=0
	with open(filename, "r") as file:
		#On boucle dans le fichier
		for counter,line in enumerate(file):
			if (counter == 0):
				seeds=re.findall(pattern4,line)
				for seedNumber, seed in enumerate(seeds):
						seedRange=re.findall(pattern1,seed)
						seedRangeStart=seedRange[0]
						seedRangeStop=seedRange[1]
						seedsDict[seedNumber]={}
						seedsDict[seedNumber]["seedRangeStart"]=seedRangeStart
						seedsDict[seedNumber]["seedRangeStop"]=seedRangeStop

			else :
				
				if (re.match(pattern2,line)):
					extraction=(re.match(pattern2,line))
					mapsDict[extraction.group()]={}
					section=extraction.group()
					sectionCounter=0

				elif(re.match(pattern3,line)):
					extraction=(re.findall(pattern1,line))
					mapsDict[section][sectionCounter]={}
					mapsDict[section][sectionCounter]["rangeDestination"]=extraction[0]
					mapsDict[section][sectionCounter]["rangeStart"]=extraction[1]
					mapsDict[section][sectionCounter]["rangeLength"]=extraction[2]
					sectionCounter=sectionCounter+1

		

def testdata(data):
	rabiot=10000000
	#print("seed: "+str(data))
	value=data
	for sections in mapsDict:
		#print(sections)
		for mapRange in mapsDict[sections]:
			start=int(mapsDict[sections][mapRange]["rangeStart"])
			length=int(mapsDict[sections][mapRange]["rangeLength"])
			stop=start+length-1
			destination=int(mapsDict[sections][mapRange]["rangeDestination"])
			#print("start "+ str(start) +" stop "+ str(stop))
			if(value >= start and value < (start+length)):
				#print("je rentre ici")
				if (stop-value)<rabiot:
					rabiot=stop-value
					#print ("rabiot "+ str(rabiot))
				#print("start "+ str(start) +" destination "+ str(destination))
				#print("Ma seed était à " + str(value) +" et elle passe à " + str(value-start+destination))
				value=(value-start+destination)
				break
	#print(value)
	#print("rabiot " +str(rabiot))
	rab=rabiot
	output.append(value)
	return(rab)

WalkThroughDay5("input5.txt")
print(seedsDict)

for keys in seedsDict:
	print(seedsDict[keys])
	dataToBeTested=int(seedsDict[keys]["seedRangeStart"])
	maxDataToBeTested= dataToBeTested+int(seedsDict[keys]["seedRangeStop"])
	while(dataToBeTested<maxDataToBeTested):
		print("jet teste la seed du lot " +str(keys) + " qui est la n° "+ str(dataToBeTested) + str(" j'ai un range qui va jusqu'à " +str(maxDataToBeTested-1)))
		rab=testdata(dataToBeTested)
		if (rab>0):
			dataToBeTested=dataToBeTested+rab
			print("on reteste : "+str(dataToBeTested))
			testdata(dataToBeTested)
		dataToBeTested=dataToBeTested+1

print(min(output))

