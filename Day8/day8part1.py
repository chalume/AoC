import glob 
import os.path 
import csv
import os
import re
import requests
import math

pattern1=r"([RL]+)"
#Pattern pour extraire les cartes
pattern2=r"([A-Z]+)"
#Pattern pour extraire les bids (avec un esapce devant viré par le int())
pattern3=r"([A-Z]{2}[A])"
pattern4=r"([A-Z]{2}[Z])"

maps={}
output=[]

def PromenadeDansLesBois(data):
	trackingID=data
	steps=0
	while(1):
		for i in maps["inputRL"]:
			steps=steps+1
			trackingID=maps[trackingID][i]
			print("je teste" + trackingID)
			if(trackingID=="ZZZ"):
				print("J'ai trouvé la sortie " + trackingID)
				return(steps)


def WalkThroughDay8(filename):
	with open(filename, "r") as file:
		#Classement des data d'entrée et analyse de la power
		
		for counter,line in enumerate(file):
			if(counter==0):
				data=re.search(pattern1,line)
				maps["inputRL"]=data.group()
			elif(counter>1):
				data=re.findall(pattern2,line)
				maps[data[0]]={}
				maps[data[0]]["ID"]=data[0]
				maps[data[0]]["L"]=data[1]
				maps[data[0]]["R"]=data[2]

		for keys in maps:
			#print(keys)
			if(keys == "inputRL"):
				pass
			else:
				#print(maps[keys]["ID"])
				if (re.search(pattern3,maps[keys]["ID"])):
					entries=(re.findall(pattern3,maps[keys]["ID"]))
					for entry in entries:
						loopsize=listALoop(entry)
		print(output)
		result=output[0]
		for i in range(len(output)-1):
			#print(i)
			factor=result*(output[i+1])
			gcd=(math.gcd(result,output[i+1]))
			result=int(factor/gcd)
		print(result)


def listALoop(data):
	trackingID=data
	steps=0
	counter=0
	print(data)
	while(1):
		for i in maps["inputRL"]:
			steps=steps+1
			trackingID=maps[trackingID][i]
			#print("je teste" + trackingID)
			if (re.search(pattern4,trackingID)):
				print("End "+ trackingID + " indice " +str(steps))
				output.append(steps)
				return(0)

			
WalkThroughDay8("input8.txt")


