import glob 
import os.path 
import csv
import os
import re
import requests

pattern=r"([0-9]+)"
#Pattern pour extraire un bloc de chiffres
pattern2=r"([-&/@*=#+$%]+)"
#Pattern pour extraire les caractères spéciaux
pattern3=r"([*]+)"
datalength=0
validPart=0
gearValidity=0


def WalkThroughDay3(filename):
	with open(filename, "r") as file:
		sum=0
		#On boucle dans le fichier
		specialCharIndexes={}
		starIndexes={}
		starIndexesCount=[]
		parts={}
		pos={}
		for counter,line in enumerate(file):
			specialCharIndexes[counter]=[]
			starIndexes[counter]=[]
			#detecte les blocs de chiffres
			parts[counter]={}
			for matchNumber,match in enumerate(re.finditer(pattern,line)):
   				parts[counter][matchNumber]={}
   				partValue=match.group()
   				parts[counter][matchNumber]["value"]=partValue
   				data=match.span()
   				parts[counter][matchNumber]["start"]=data[0]
   				parts[counter][matchNumber]["stop"]=data[1]
			for stringer,charac in enumerate(line):
				if re.match(pattern2,charac):
					specialCharIndexes[counter].append(stringer)
				if re.match(pattern3,charac):
					starIndexes[counter].append(stringer)

		#print(parts)

		for counter,lines in enumerate(parts):
			datalength=counter
		#print(starIndexes)

		event=0
		for line in parts:
			#for each candidate part
			for partsInfo in parts[line]:
				gearValidity=0
				#first case : all but first and last line
				print("part "+str(parts[line][partsInfo]["value"]))	
				if (line>0 and line<datalength):
					for item in starIndexes[line-1]:
						low=(parts[line][partsInfo]["start"]-1)
						high=(parts[line][partsInfo]["stop"]+1)
						if((low <= item) and (high > item)):
							#print("Position de l'étoile : ligne "+ str(line-1) +" index "+ str(item))
							pos[event]={}
							pos[event]["line"]=(line-1)
							pos[event]["row"]=item
							pos[event]["value"]=int(parts[line][partsInfo]["value"])
							event=event+1
							
					for item in starIndexes[line+1]:
						low=(parts[line][partsInfo]["start"]-1)
						high=(parts[line][partsInfo]["stop"]+1)
						if((low <= item) and (high > item)):
							#print("Position de l'étoile : ligne "+ str(line+1) +" index "+ str(item))
							pos[event]={}
							pos[event]["line"]=(line+1)
							pos[event]["row"]=item
							pos[event]["value"]=int(parts[line][partsInfo]["value"])
							event=event+1
							
					for item in starIndexes[line]:
						low=(parts[line][partsInfo]["start"]-1)
						high=(parts[line][partsInfo]["stop"]+1)
						if((low <= item) and (high > item)):
							#print("Position de l'étoile : ligne "+ str(line) +" index "+ str(item))
							pos[event]={}
							pos[event]["line"]=(line)
							pos[event]["row"]=item
							pos[event]["value"]=int(parts[line][partsInfo]["value"])
							event=event+1
							
				#second case : first line	
				elif (line==0):
					for item in starIndexes[line+1]:
						low=(parts[line][partsInfo]["start"]-1)
						high=(parts[line][partsInfo]["stop"]+1)
						if((low <= item) and (high > item)):
							#print("Position de l'étoile : ligne "+ str(line+1) +" index "+ str(item))
							pos[event]={}
							pos[event]["line"]=(line+1)
							pos[event]["row"]=item
							pos[event]["value"]=int(parts[line][partsInfo]["value"])
							event=event+1
							
					for item in starIndexes[line]:
						low=(parts[line][partsInfo]["start"]-1)
						high=(parts[line][partsInfo]["stop"]+1)
						if((low <= item) and (high > item)):
							#print("Position de l'étoile : ligne "+ str(line) +" index "+ str(item))
							pos[event]={}
							pos[event]["line"]=(line)
							pos[event]["row"]=item
							pos[event]["value"]=int(parts[line][partsInfo]["value"])
							event=event+1
							
				#last case : last line	
				elif (line==datalength):
					for item in starIndexes[line-1]:
						low=(parts[line][partsInfo]["start"]-1)
						high=(parts[line][partsInfo]["stop"]+1)
						if((low <= item) and (high > item)):
							#print("Position de l'étoile : ligne "+ str(line-1) +" index "+ str(item))
							pos[event]={}
							pos[event]["line"]=(line-1)
							pos[event]["row"]=item
							pos[event]["value"]=int(parts[line][partsInfo]["value"])
							event=event+1
							
					for item in starIndexes[line]:
						low=(parts[line][partsInfo]["start"]-1)
						high=(parts[line][partsInfo]["stop"]+1)
						if((low <= item) and (high > item)):
							#print("Position de l'étoile : ligne "+ str(line) +" index "+ str(item))
							pos[event]={}
							pos[event]["line"]=(line)
							pos[event]["row"]=item
							pos[event]["value"]=int(parts[line][partsInfo]["value"])
							event=event+1
		
		pointsToPop=[]				
		for keys in pos:
			pos[keys]["counter"]=0
			for key2 in pos:
				if((pos[keys]["line"]==pos[key2]["line"]) and(key2 > keys) and pos[keys]["row"] == pos[key2]["row"] ):
					pos[keys]["counter"]=pos[keys]["counter"]+1
					pos[keys]["value"]=pos[keys]["value"]*pos[key2]["value"]
					pointsToPop.append(key2)
		for ref in pointsToPop:
			if (ref in pos):
				pos.pop(ref)
		print(pos)

		sum=0
		for keys in pos:
			if(pos[keys]["counter"]==1):
				sum=sum+(pos[keys]["value"])
				print(sum)

#parts{[line][matchNumberInLine]["value"]
#                              ["start"]
#                              ["stop"]
#										}

#specialCharIndexes{[line][listOfPositions]
#										    }


#fpr test only
WalkThroughDay3("input3.txt")
