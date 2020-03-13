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
Vous allez recevoir un nom d'utilisateur dans username.
Votre rôle est de visiter la page http://www.wechall.net/en/profile/‹username› et de récupérer les informations suivantes :
    son score : vous devez le retourner dans la variable score
    son rang général : vous devez le retourner dans la variable rank
    sa date d'enregistrement : vous devez la retourner dans la variable register_date
    la date de sa dernière activité : vous devez la retourner dans la variable last_activity
"""



username = ""
password = ""
cont_id = 44
url = "http://www.microcontest.com/contests/44/contest.php"
url_result = "http://www.microcontest.com/contests/44/validation.php"

data = [("username", username), ("password", sha1(password).hexdigest()),("ID", cont_id), ("contestlogin", 1), ("version", 2)]


opener = build_opener(HTTPCookieProcessor())
page = opener.open(url, urlencode(data)).read()
print (page)

"""
#####Exemple de données retournées dans page#####
page="Nombre_variables=1<br/>[username]<br/>Longueur=6<br/>Valeur=brahim<br/>"
"""

#####Extraction des deux valeurs à traiter#####
nom = re.compile(r"Valeur=(.+)<br/>").search(page).group(1)


#####Récupération des données sur wechall#####
url_wechall = "http://www.wechall.net/en/profile/"+nom
page1 = opener.open(url_wechall).read()

score = re.compile(r"<th>Score</th><td><a href=\"/en/stats/"+nom+"\">(\d+)</a>").search(page1).group(1)
rank = re.compile(r"<th>Global Rank</th><td><a href=\"/en/ranking/player/"+nom+"#rank_(\d+)\">").search(page1).group(1)
register_date = re.compile(r"<th>Register Date</th><td>(.+)</td>").search(page1).group(1)
last_activity = re.compile(r"<th>Last Activity</th><td>(.+)</td>").search(page1).group(1)


#####Envoi des résultats#####
data_result = {"score":score, "rank":rank, "register_date":register_date, "last_activity":last_activity}
page_result = opener.open(url_result, urlencode(data_result)).read()
print (page_result)


