import glob 
import os.path 
import csv
import os
import re
import requests

pattern1=r"((Card)[ ]+[0-9]+:[ ]+)"
#Pattern pour enlever le début de la ligne
pattern2=r"(([0-9]+[ ]+){5})"
#Pattern pour extraire les data de references
pattern3=r"([0-9]+)"
pattern4=r"([|][ ]+)"

inputDict={}
score=[0,1,2,4,8,16,32,64,128,256, 512,1024,2048,4096]


def WalkThroughDay4(filename):
	inputDictLen=0
	with open(filename, "r") as file:
		#On boucle dans le fichier
		for counter,line in enumerate(file):
			headerToBeRemoved =re.match(pattern1,line)
			#print("linge d'origine " +line)
			data=(headerToBeRemoved.group())
			data=line.replace(data,"")
			#print("Après retrait du header " + data)
			extraction=re.match(pattern2,data)
			#print("Winning numbers " + extraction.group())
			winningNumber=re.findall(pattern3,extraction.group())
			#print("Winning numbers dans leur liste " + str(winningNumber))
			data=data.replace(extraction.group(),"")
			couilleAVirer=re.match(pattern4,data)
			data=data.replace(couilleAVirer.group(),"")
			myNumbers=re.findall(pattern3,data)
			#print(myNumbers)
			inputDict[counter]={}
			inputDict[counter]["winningNumber"]=winningNumber
			inputDict[counter]["myNumbers"]=myNumbers
			inputDict[counter]["cardCount"]=1
			inputDictLen=inputDictLen+1

	sum=0
	for keys in inputDict:
		winningCount=0
		for number in inputDict[keys]["winningNumber"]:
			for test in inputDict[keys]["myNumbers"]:
				if(test==number):
					#print("j'ai une correspondance dans la ligne "+str(keys)+ " sur les numéros "+ str(number) )
					winningCount=winningCount+1
		print("nombre de match de la ligne "+ str(keys) + "--> " +str(winningCount))
		for i in range(winningCount):
			if (i<(inputDictLen-keys)):
				if ((keys+i+1)<inputDictLen):
					print("j'ajoute "+ str(inputDict[keys]["cardCount"]) +" à la ligne " + str(keys+i+1))
					inputDict[keys+i+1]["cardCount"]=inputDict[keys+i+1]["cardCount"]+inputDict[keys]["cardCount"]
		sum=sum+inputDict[keys]["cardCount"]
		print("La somme est maintenant de "+ str(sum))

	print(inputDict)
	#print(sum)


WalkThroughDay4("input4example.txt")

