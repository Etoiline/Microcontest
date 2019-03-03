#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libmicrocontest2 import *
from hashlib import sha1
from urllib import urlencode
from urllib2 import *
import re
import functools
import cookielib

#####Ne pas oublier de remplir#####
username = ""
password = ""
cont_id = 31
url = "http://www.microcontest.com/contests/31/contest.php"
url_result = "http://www.microcontest.com/contests/31/validation.php"

data = [("username", username), ("password", sha1(password).hexdigest()),("ID", cont_id), ("contestlogin", 1), ("version", 2)]


opener = build_opener(HTTPCookieProcessor())
page = opener.open(url, urlencode(data)).read()
print page

#####Exemple de données envoyées par le serveur#####
#Nombre_variables=2<br/>[donnees_a_compresser]<br/>Longueur=108<br/>Valeur=PPPPPPRRRRRRHHHHHHHHYYYYYYYYYYYYYYAAAAAAAAKYYYYYEEEEYYYYYYYIIIIIIIIHHHHHHHHRRRRRRRRRRTTTTTTTTTTTTTTTTQZZZZRS<br/>[donnees_a_decompresser]<br/>Longueur=60<br/>Valeur=2P6E2P4D4S2A3P10V1E5M4J9C6O7W9X4B3Q4O4A8A4R9L1U5O10X4S7J9R9F<br/>


#####Extraction des deux valeurs à traiter#####
rev1 = re.compile(r"Valeur=([A-Z]+)<br/>")
rev2 = re.compile(r"Valeur=(\d[A-Z,0-9]+)<br/>")
donnees_a_compresser = rev1.search(page).group(1)
donnees_a_decompresser = rev2.search(page).group(1)


#####Premier cas : compresser une chaine#####
resultat_compression = ""
lettre = donnees_a_compresser[0]
cpt = 0
i = 0
for l in donnees_a_compresser :
	if (l==lettre) :
		cpt+=1
	else :
		resultat_compression += str(cpt)+lettre
		cpt = 1
		lettre = donnees_a_compresser[i]
	i+=1
resultat_compression += str(cpt)+lettre


#####Second cas : décompresser une chaine#####
resultat_decompression = ""
nb = 0
i = 0
lettre=""
for l in donnees_a_decompresser :
	if re.search(r"\d",l) is not None :
		nb = int(l)
		lettre = donnees_a_decompresser[i+1]
		for j in range (0,nb) :
			resultat_decompression += lettre
	i+=1


data_result = {"resultat_compression":resultat_compression, "resultat_decompression":resultat_decompression}
page_result = opener.open(url_result, urlencode(data_result)).read()
print page_result


