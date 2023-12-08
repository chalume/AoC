from math import *
#Mise en équation :
# X = Temps d'appui sur le bouton
#On cherche = pushTime * 	speed 			= Record
#				X      * (B_raceTime)-X 	= C_record
#dev:		-X2 +		B_racetimes*X 	-	C_record 	= 0
C_record=-295173412781210
B_raceTime=45988373
A=-1

#Calcul du déterminant
determinant=B_raceTime*B_raceTime-(4*A*C_record)

#Calcul de la solution 1
solution_1 = floor(((-1*B_raceTime)-sqrt(determinant))/(2*A))

#Calcul de la solution 2
solution_2 = floor(((-1*B_raceTime)+sqrt(determinant))/(2*A))

print(solution_1-solution_2)
