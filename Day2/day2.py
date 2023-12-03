import glob 
import os.path 
import csv
import os
import re
import requests

pattern=r"([A-Z]\w+\s[0-9]+)"
#Pattern pour extraire "game X"
pattern2=r"([0-9]+)"
#Pattern pour extraire le numéro de game de "GameX"
pattern3=r"([:;]\s[0-9\sa-z,]+)"
#Pattern pour extraction des tirages
pattern4=r"([0-9]+\s(red))"
#pattenre pour extraction de "x red" dans un tirage
pattern5=r"([0-9]+\s(blue))"
#pattenre pour extraction de "x red" dans un tirage
pattern6=r"([0-9]+\s(green))"
#pattenre pour extraction de "x red" dans un tirage
pattern7=r"([0-9]+)"
#pattenre pour extraction de "x red" dans un tirage

redBudget=12
blueBudget=14
greenBudget=13
valideGame=1

def ImportTextFile(filename):
	with open(filename, "r") as file:
		sum=0
		#On boucle dans le fichier
		for counter,line in enumerate(file):
			gameID=(counter+1)
			print("On attaque le game "+str(gameID))
			print(line)
			#On extrait les tirages de chaque jeu
			games=re.findall(pattern3,line)
			#On boucle dans les tirages
			valideGame=1
			for iteration,tirages  in enumerate(games):
				print("On attaque le tirage "+str(iteration+1)+" du game " +str(gameID) )
				print(tirages)
				red=re.search(pattern4,tirages)
				if red :
					redLine=red.group()
					redCount=re.match(pattern7,redLine)
					if (int(redCount.group())>redBudget):
						valideGame=0
						print("game invalid : red")
				blue=re.search(pattern5,tirages)
				if blue :
					blueLine=blue.group()
					blueCount=re.match(pattern7,blueLine)
					if (int(blueCount.group())>blueBudget):
						valideGame=0
						print("game invalid : blue")
				green=re.search(pattern6,tirages)
				if green :
					greenLine=green.group()
					greenCount=re.match(pattern7,greenLine)
					if (int(greenCount.group())>greenBudget):
						valideGame=0
						print("game invalid : green")
			print("On est là")
			if (valideGame==1):
				print("Game valid : adding" + str(gameID))
				sum=sum+gameID
		print(sum)






#fpr test only
ImportTextFile("input2.txt")

#a=GetPhotonEmissionFromLara("Tl-208")
#print(a)