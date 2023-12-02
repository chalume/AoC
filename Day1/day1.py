import glob 
import os.path 
import csv
import os
import re
import requests

pattern=r"([1-9]|(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine))"
#Pattern pour extraire les 


def ImportTextFile(filename):
	with open(filename, "r") as file:
		sum=0
		for counter,line in enumerate(file):
			print(line)
			#boucle dans le fichier
			value=re.findall(pattern,line)
			print(value)
			firstdigit=value[0][0]
			print(firstdigit)
			firstdigitcorrected=kebab(firstdigit)
			print(firstdigitcorrected)
			index=len(value)-1
			seconddigit=(value[index][0])
			print(seconddigit)
			seconddigitcorrected=kebab(seconddigit)
			print(seconddigitcorrected)
			print(int(str(firstdigitcorrected)+str(seconddigitcorrected)))
			sum = sum + int(str(firstdigitcorrected)+str(seconddigitcorrected))
			print(sum)
	print(sum)

def kebab(data):
	digit=0
	if str(data)=="one":
		digit=1
	elif str(data)=="two":
		digit=2
	elif str(data)=="three":
		digit=3
	elif str(data)=="four":
		digit=4
	elif str(data)=="five":
		digit=5
	elif str(data)=="six":
		digit=6
	elif str(data)=="seven":
		digit=7
	elif str(data)=="eight":
		digit=8
	elif str(data)=="nine":
		digit=9
	else :
		digit=data

	return digit

#fpr test only
ImportTextFile("input1b.txt")

#a=GetPhotonEmissionFromLara("Tl-208")
#print(a)