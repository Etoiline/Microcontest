#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libmicrocontest2 import *
from hashlib import sha1
from urllib import urlencode
from urllib2 import *
import re
import functools
import cookielib



username = ""
password = "*"
cont_id = 46
url = "http://www.microcontest.com/contests/46/contest.php"
url_result = "http://www.microcontest.com/contests/46/validation.php"

data = [("username", username), ("password", sha1(password).hexdigest()),("ID", cont_id), ("contestlogin", 1), ("version", 2)]


opener = build_opener(HTTPCookieProcessor())
page = opener.open(url, urlencode(data)).read()
print (page)


"""
#####Exemple de données retournées dans page#####
page = "Nombre_variables=3<br/>[nb_of_cards]<br/>Valeur=34<br/>[final_sequence]<br/>Longueur=169<br/>Valeur=S_10;H_Queen;C_5;D_Ace;S_6;S_Ace;S_5;H_8;S_Queen;D_9;C_9;D_4;H_Ace;H_2;D_King;H_9;S_4;H_King;C_Ace;D_5;C_King;C_2;C_4;D_10;H_10;C_Jack;S_8;D_3;C_3;C_6;D_Jack;S_9;S_3;H_4<br/>[cards_passed]<br/>Longueur=63<br/>Valeur=3;3;3;1;2;3;2;2;1;1;3;3;2;2;3;2;1;1;3;1;3;3;3;3;2;1;3;3;3;2;1;1<br/>"


page = "Nombre_variables=3<br/>[nb_of_cards]<br/>Valeur=34<br/>[final_sequence]<br/>Longueur=169<br/>Valeur=C_7;S_Ace;D_10;H_2;C_5;H_8;D_Jack;C_4;C_6;S_7<br/>[cards_passed]<br/>Longueur=63<br/>Valeur=3;1;3;2;3;2;2;1<br/>"
"""

#####Extraction de la suite de cartes et des nombres#####
valeurs = re.compile(r"\[final_sequence\]<br/>Longueur=\d+<br/>Valeur=(.*)<br/>\[cards_passed\]<br/>Longueur=\d+<br/>Valeur=(.*)<br/>")

suite_cartes = valeurs.search(page).group(1).split(";")
suite_nombre = valeurs.search(page).group(2).split(";")

#print (suite_cartes, suite_nombre)
nb_cartes = len(suite_cartes)
tas_cartes_magie = [""]*nb_cartes


j=0
k=1
tas_cartes_magie[0] = suite_cartes[0]
for elm in suite_nombre :
	
	indice_suivant = int(elm)
	for i in range (0,indice_suivant+1) :
		bool_suivant = False
		while not bool_suivant :
			j=(j+1)%(nb_cartes)
			if tas_cartes_magie[j]=="" :
				bool_suivant = True
	tas_cartes_magie[j] = suite_cartes[k]	
	k+=1

indice=0
for elm in tas_cartes_magie :
	if elm == "" :
		tas_cartes_magie[indice] = suite_cartes[nb_cartes-1]
	indice+=1

	
tas_cartes_magie = ";".join(tas_cartes_magie)



#####On renvoie la réponse#####
data_result = {"initial_sequence":tas_cartes_magie}
page_result = opener.open(url_result, urlencode(data_result)).read()
print page_result

