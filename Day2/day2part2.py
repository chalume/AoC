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

minimumred=0
minimumblue=0
minimumgreen=0
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
			#On ventile par games et on initialise les mins
			minimumred=0
			minimumblue=0
			minimumgreen=0
			for iteration,tirages  in enumerate(games):
				print("On attaque le tirage "+str(iteration+1)+" du game " +str(gameID) )
				print(tirages)

				red=re.search(pattern4,tirages)
				if red :
					redLine=red.group()
					redCount=re.match(pattern7,redLine)
					if (int(redCount.group())>minimumred):
						minimumred=(int(redCount.group()))
						print("minimum red is this gamle is "+ str(minimumred))
					else :
						print("minimum red is still "+ str(minimumred))
				else :
					print("minimum red is still "+ str(minimumred))

				blue=re.search(pattern5,tirages)
				if blue :
					blueLine=blue.group()
					blueCount=re.match(pattern7,blueLine)
					if (int(blueCount.group())>minimumblue):
						minimumblue=(int(blueCount.group()))
						print("minimum blue is this gamle is "+ str(minimumblue))
					else :
						print("minimum blue is still "+ str(minimumblue))
				else :
					print("minimum blue is still "+ str(minimumblue))

				green=re.search(pattern6,tirages)
				if green :
					greenLine=green.group()
					greenCount=re.match(pattern7,greenLine)
					if (int(greenCount.group())>minimumgreen):
						minimumgreen=(int(greenCount.group()))
						print("minimum green is this gamle is "+ str(minimumgreen))
					else :
						print("minimum green is still "+ str(minimumgreen))
				else :
					print("minimum green is still "+ str(minimumgreen))
			print("Game power is"+ str(minimumred) + " "+ str(minimumblue)+ " "+str(minimumgreen))
			power=minimumred*minimumblue*minimumgreen
			print(power)	
			sum=sum+power
		print(sum)






#fpr test only
ImportTextFile("input2.txt")

#a=GetPhotonEmissionFromLara("Tl-208")
#print(a)