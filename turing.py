#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libmicrocontest2 import *
from hashlib import sha1
from urllib import urlencode
from urllib2 import *
import re
import functools
import cookielib


"""
Machine de Turing : 
    6 états internes : A, B, C, D, E, F. L'état initial est A, et F est le seul état final.
    2 symboles, 0 et 1.
    table de transitions : 

Etat courant	Symbole courant	Symbole à écrire	Déplacer la tête vers	Prochain état
A			0		1		DROITE			B
A			1		1		GAUCHE			C
B			0		1		DROITE			C
B			1		1		DROITE			B
C			0		1		DROITE			D
C			1		0		GAUCHE			E
D			0		1		GAUCHE			A
D			1		1		GAUCHE			D
E			0		1		DROITE			F
E			1		0		GAUCHE			A


Le ruban initial est donné dans la variable tape. La position initiale de la tête sera toujours sur le premier symbole de ce ruban.
exemple : tape = "0 1 1 0 1"
Gardez en tête que ce ruban est infini et qu'il est rempli de 0 partout ailleurs.
Donc vous devrez juste renvoyer le ruban après la 1000e itération (si l'état final est atteint avant la 1000e itération, renvoyer alors l'état du ruban dans l'état final bien sur).

"""


def remplacer_valeur (bande, i, valeur) :
	new_bande = bande[0:i]+valeur+bande[i+1:len(bande)]
	return new_bande


username = ""
password = ""
cont_id = 45
url = "http://www.microcontest.com/contests/45/contest.php"
url_result = "http://www.microcontest.com/contests/45/validation.php"

data = [("username", username), ("password", sha1(password).hexdigest()),("ID", cont_id), ("contestlogin", 1), ("version", 2)]


opener = build_opener(HTTPCookieProcessor())
page = opener.open(url, urlencode(data)).read()
print (page)



#####Exemple de données retournées dans page#####
#page = "Nombre_variables=1<br/>[tape]<br/>Longueur=33<br/>Valeur=1 0 1 0 1 1 0 0 0 1 1 1 1 0 0 0 1<br/>"

#####Représentation de la machine de Turing sous forme de dictionnaire : (état,symbole):[nouvel_etat,deplacement,nouveau_symbole]
i=0
etat = "A"
turing = {("A","0"):["1", 1, "B"], ("A","1"):["1", -1, "C"], ("B","0"):["1", 1, "C"], ("B","1"):["1", 1, "B"], ("C","0"):["1", 1, "D"], ("C","1"):["0", -1, "E"], ("D","0"):["1", -1, "A"], ("D","1"):["1", -1, "D"], ("E","0"):["1", 1, "F"], ("E","1"):["0", -1, "A"]}
tour = 0


#####Extraction de la valeur de départ de la machine puis suppression des espaces#####
bande = re.compile(r"Valeur=(.*)<br/>").search(page).group(1)
bande = bande.replace(" ","")



#####début de la machine. Deux conditions d'arrêt : l'état final est atteint ou 1000 étapes#####
while etat is not "F" and tour<=1000 :
	nouvel_etat = turing[(etat,bande[i])]
	bande = remplacer_valeur(bande,i,nouvel_etat[0])
	#Si besoin on aggrandi la bande
	if i==len(bande)-1 :
		bande = bande+"0"
	elif i==0 :
		bande="0"+bande
		i=i+1
	etat = nouvel_etat[2]
	i = i+nouvel_etat[1]
	tour+=1



#####On remet les espaces et on renvoie la réponse#####
tape = " ".join(list(bande))

data_result = {"final_tape_state":tape}
page_result = opener.open(url_result, urlencode(data_result)).read()
print page_result

