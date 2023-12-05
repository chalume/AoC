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
pattern4=r"([|][ ]+)"

seedsDict={}
mapsDict={}
output=[]

def WalkThroughDay5(filename):
	section=0
	with open(filename, "r") as file:
		#On boucle dans le fichier
		for counter,line in enumerate(file):
			if (counter == 0):
				seeds=re.findall(pattern1,line)
				for seedNumber, seed in enumerate(seeds):
					seedsDict[seedNumber]=seed
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

		for keys in seedsDict:
			#print("seed: "+str(seedsDict[keys]))
			value=int(seedsDict[keys])
			for sections in mapsDict:
				#print(sections)
				for mapRange in mapsDict[sections]:
					start=int(mapsDict[sections][mapRange]["rangeStart"])
					length=int(mapsDict[sections][mapRange]["rangeLength"])
					destination=int(mapsDict[sections][mapRange]["rangeDestination"])
					if(value >= start and value < (start+length)):
						#print("start "+ str(start) +" destination "+ str(destination))
						#print("Ma seed était à " + str(value) +" et elle passe à " + str(value-start+destination))
						value=(value-start+destination)
						break
			#print("Resulting value = " +str(value))
			output.append(value)
		#print(output)
		result=(min(output))
		print(result)

WalkThroughDay5("input5.txt")
