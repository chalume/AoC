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
datalength=0
validPart=0

def WalkThroughDay3(filename):
	with open(filename, "r") as file:
		sum=0
		#On boucle dans le fichier
		specialCharIndexes={}
		parts={}
		for counter,line in enumerate(file):
			specialCharIndexes[counter]=[]
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
		#print(specialCharIndexes)
		#print(parts)

		for counter,lines in enumerate(parts):
			datalength=counter

		for line in parts:
			#print(specialCharIndexes[line])
			#for each candidate part
			for partsInfo in parts[line]:
				validPart=0
				#print(parts[line][partsInfo]["value"])
				#print(parts[line][partsInfo]["start"])
				#print(parts[line][partsInfo]["stop"])
				#first case : all but first and last line	
				if (line>0 and line<datalength):
					for item in specialCharIndexes[line-1]:
						#print ("itemPos= "+ str(item))
						low=(parts[line][partsInfo]["start"]-1)
						high=(parts[line][partsInfo]["stop"]+1)
						if((low <= item) and (high > item)):
							print("va voir à la ligne " + str(line) + " la part " + parts[line][partsInfo]["value"] +" ca correspond à la colonne " + str(item) )
							validPart=1
					for item in specialCharIndexes[line+1]:
						#print ("itemPos= "+ str(item))
						low=(parts[line][partsInfo]["start"]-1)
						high=(parts[line][partsInfo]["stop"]+1)
						if((low <= item) and (high > item)):
							print("va voir à la ligne " + str(line) + " la part " + parts[line][partsInfo]["value"] +" ca correspond à la colonne " + str(item) )
							validPart=1
					for item in specialCharIndexes[line]:
						#print ("itemPos= "+ str(item))
						low=(parts[line][partsInfo]["start"]-1)
						high=(parts[line][partsInfo]["stop"]+1)
						#print("low " +str(low)+ "  High " +str(high))
						if((low <= item) and (high > item)):
							print("va voir à la ligne " + str(line) + " la part " + parts[line][partsInfo]["value"] +" ca correspond à la colonne " + str(item) )
							validPart=1
				#second case : first line	
				elif (line==0):
					for item in specialCharIndexes[line+1]:
						#print ("itemPos= "+ str(item))
						low=(parts[line][partsInfo]["start"]-1)
						high=(parts[line][partsInfo]["stop"]+1)
						if((low <= item) and (high > item)):
							print("va voir à la ligne " + str(line) + " la part " + parts[line][partsInfo]["value"] +" ca correspond à la colonne " + str(item) )
							validPart=1
					for item in specialCharIndexes[line]:
						#print ("itemPos= "+ str(item))
						low=(parts[line][partsInfo]["start"]-1)
						high=(parts[line][partsInfo]["stop"]+1)
						#print("low " +str(low)+ "  High " +str(high))
						if((low <= item) and (high > item)):
							print("va voir à la ligne " + str(line) + " la part " + parts[line][partsInfo]["value"] +" ca correspond à la colonne " + str(item) )
							validPart=1
				#last case : last line	
				elif (line==datalength):
					for item in specialCharIndexes[line-1]:
						#print ("itemPos= "+ str(item))
						low=(parts[line][partsInfo]["start"]-1)
						high=(parts[line][partsInfo]["stop"]+1)
						if((low <= item) and (high > item)):
							print("va voir à la ligne " + str(line) + " la part " + parts[line][partsInfo]["value"] +" ca correspond à la colonne " + str(item) )
							validPart=1
					for item in specialCharIndexes[line]:
						#print ("itemPos= "+ str(item))
						low=(parts[line][partsInfo]["start"]-1)
						high=(parts[line][partsInfo]["stop"]+1)
						#print("low " +str(low)+ "  High " +str(high))
						if((low <= item) and (high > item)):
							print("va voir à la ligne " + str(line) + " la part " + parts[line][partsInfo]["value"] +" ca correspond à la colonne " + str(item) )
							validPart=1

				if (validPart==1):
					print("j'ajoute " + parts[line][partsInfo]["value"])
					sum=sum+int(parts[line][partsInfo]["value"])
			print("Somme "+ str(sum))
				

#parts{[line][matchNumberInLine]["value"]
#                              ["start"]
#                              ["stop"]
#										}

#specialCharIndexes{[line][listOfPositions]
#										    }


#fpr test only
WalkThroughDay3("input3.txt")
