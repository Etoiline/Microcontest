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
DDans cette épreuve, vous allez devoir décrypter une chaîne de caractères cryptée grâce au chiffre de Cesar. Ce systême de cryptage très simple est certainement le plus célèbre, il suffit de décaler d'un certain nombre chaque lettre pour crypter un texte, et de décaler dans l'autre sens pour le décrypter, ce nombre constituant donc la clef.
Dans cette version de l'épreuve, cette clef vous est donnée dans la variable key.

Concrètement, voici des exemples de cryptage avec une clef de 3 :

Texte clair :    ABCDEFGHIJKLMNOPQRSTUVWXYZ
Texte crypté :    DEFGHIJKLMNOPQRSTUVWXYZABC

Texte clair :    MICROCONTESTCESTTROPFACILE
Texte crypté :    PLFURFRQWHVWFHVWWURSIDFLOH


Pour simplifier les choses, le texte crypté fournis sera toujours constitué que de majuscules, et sans espace, comme sur le deuxième exemple.

Pour décrypter, vous avez donc juste à faire le décalage dans l'autre sens, du nombre indiqué par la clef. Pour les lettres extrêmes de l'alphabet, il faut simplement reprendre à partir de l'autre extrêmité, comme sur l'exemple 1.
"""




username = ""
password = ""
cont_id = 4
url = "http://www.microcontest.com/contests/"+str(cont_id)+"/contest.php"
url_result = "http://www.microcontest.com/contests/"+str(cont_id)+"/validation.php"

data = [("username", username), ("password", sha1(password).hexdigest()),("ID", cont_id), ("contestlogin", 1), ("version", 2)]


opener = build_opener(HTTPCookieProcessor())
page = opener.open(url, urlencode(data)).read()
print (page)


"""
#####Exemple de données retournées dans page#####
page = "Nombre_variables=2<br/>[txt_crypte]<br/>Longueur=45<br/>Valeur=MFWJFVYDFUUFGPJTOFQVUSFQPOESFVOWJPMFOUBDDFTEF<br/>[key]<br/>Valeur=1<br/>"
"""


#####Extraction des données (texte crypté et clé)#####
valeurs = re.compile(r"\[txt_crypte]<br/>Longueur=\d+<br/>Valeur=(.*)<br/>\[key]<br/>Valeur=(.*)<br/>")

txt_crypte = valeurs.search(page).group(1)
key = valeurs.search(page).group(2)

print (txt_crypte, key)

#####Déchiffrage du texte : ici je choisis de convertir en ascii, puis je soustrais 65 afin d'avoir un nombre de 0 à 25. Enfin j'effectue le décalage et grâce au modulo j'obtiens un nombre dans le même intervalle. Pour finir, j'ajoute 65 afin d'avoir un nombre ascii correspondant au caractère.#####
txt_clair = ""
for lettre in txt_crypte :
    ascii_chr = ord(lettre)
    new_ascii_chr = chr ((((ascii_chr-65)-int(key))%26)+65)
    txt_clair+=new_ascii_chr
print (txt_clair)



#####On renvoie la réponse#####
data_result = {"txt_clair":txt_clair}
page_result = opener.open(url_result, urlencode(data_result)).read()
print (page_result)
