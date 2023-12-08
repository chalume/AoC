import glob 
import os.path 
import csv
import os
import re
import requests

pattern1=r"([A-Za-z:]+[ ]+)"
#Pattern pour extraire les seeds de la première ligne
pattern2=r"([0-9]+)"
#Pattern pour extraire les data de references
pattern3=r"([0-9]+[ ][0-9]+[ ][0-9]+)"
#Lignes de data des maps
pattern4=r"([|][ ]+)"

raceDict={}
output=[1]

def WalkThroughDay6(filename):
	with open(filename, "r") as file:
		raceDict["Time"]={}
		raceDict["Distance"]={}
		raceDict["Scores"]={}
		for counter,line in enumerate(file):
			headerToBeRemoved =re.match(pattern1,line)
			data=line.replace(headerToBeRemoved.group(),"")
			listOfData=re.findall(pattern2,data)
			if (counter==0):
				for dataCounter, element in enumerate(listOfData):
					raceDict["Time"][dataCounter]=element
			elif (counter==1):
				for dataCounter, element in enumerate(listOfData):
					raceDict["Distance"][dataCounter]=element
		print(raceDict)

	
	for durationElements in raceDict["Time"]:
		print("Durée de la course "+ str(raceDict["Time"][durationElements]))
		raceDict["Scores"][durationElements]=0
		for i in range(int(raceDict["Time"][durationElements])):
			totalTime=int(raceDict["Time"][durationElements])
			pushingTime=totalTime-(i+1)
			boatingTime=totalTime-pushingTime
			distance=boatingTime*pushingTime
			record=int(raceDict["Distance"][durationElements])
			if (distance > record):
				print("record battu :")
				raceDict["Scores"][durationElements]=raceDict["Scores"][durationElements]+1
	print(raceDict)
	for scores in raceDict["Scores"]:
		print(raceDict["Scores"][scores])
		output[0]=output[0]*int(raceDict["Scores"][scores])
	print(output)




WalkThroughDay6("input6.txt")
