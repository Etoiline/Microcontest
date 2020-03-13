#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libmicrocontest2 import *
from hashlib import sha1
from urllib import urlencode
from urllib2 import *
import re
import functools
import cookielib
import nltk



"""
Dans ce challenge, le but est de détecter automatiquement la langue de 4 textes.
Ces textes peuvent être écrits dans 10 différentes langues. Voici la liste des langues possibles, ainsi que leur code associé :

Langage		Code associé
Français	fr
Anglais		en
Italien		it
Allemand	de
Suédois		sw
Espagnol	es
Portugais	po
Finlandais	fi
Hollandais	du
Danois		da

Vous devez renvoyer la langue de chacun des textes (contenus dans les variables txt1, txt2, txt3 and txt4) 
dans les variables lang1, lang2, lang3, and lang4. Remplissez ces variables avec les codes associés à chaque langue.

"""



#####Fonction pour extraire les variables#####
variables={}
def _parse(page):
	match = re.compile(r'Nombre_variables=(\d+)<br/>').match(page, 0)
	if not match:
		x = page.split(" : ", 1)
		if len(x) != 2:
			raise ParseError("Unknown server response: %r" % page)
		if x[0] == "Erreur authentification":
			raise AuthenticationError(x[1])
		if x[0] == "Erreur":
			raise Error(x[1])
		raise Exception(x[0], x[1])

	cnt = int(match.group(1))
	pos = match.end()
	try:
		while len(variables) < cnt:
			match = re.compile(r'\[([^\]]+)\]<br/>').match(page, pos)
			n = match.group(1)
			pos = match.end()
			match = re.compile(r'Longueur=(\d+)<br/>Valeur=').match(page, pos)
			if match:
				l = int(match.group(1))
				v = page[match.end():match.end() + l]
				pos = match.end() + l
				match = re.compile(r'<br/>').match(page, pos)
				if not match:
					print "Error: No <br/> at end of variable. Trying to fix..."
					_pos = page.find("<br/>", pos)
					if _pos < 0:
						raise Exception("<br/> not found")
					v += page[pos:_pos]
					pos = _pos
				pos += len("<br/>")
			else:
				match = re.compile(r'Valeur=(.*?)<br/>').match(page, pos)
				v = match.group(1)
				pos = match.end()
			variables[n] = v
	except:
		import sys
		_, exc, tb = sys.exc_info()
		raise ParseError("Couldn't parse variables: %r" % page[pos:pos+50], exc), None, tb


#####Fonciotns qui déterminent la langue du texte#####
#J'utilise la biliothèque nltk 
#Il s'agit de comparer les mots du texte avec une liste de mots de chaque langue
#et de déterminer de quelle langue il se rapproche le plus
def calc_ratios(text) :
	ratios={}
	tokens = nltk.wordpunct_tokenize(text)
	words = [word.lower() for word in tokens]
	for lang in nltk.corpus.stopwords.fileids() :
		stopwords_set = set(nltk.corpus.stopwords.words(lang))
		words_set = set(words)
		common_words = words_set.intersection(stopwords_set)
		ratios[lang] = len(common_words)
	return ratios

def detect_language(text) :
	ratios = calc_ratios(text)
	most_rated_language = max(ratios, key=ratios.get)
	most_common_words = ratios[most_rated_language]
	del ratios[most_rated_language]
	second_most_rated_language = max(ratios, key=ratios.get)
	second_most_common_words = ratios[second_most_rated_language]
	return most_rated_language



#dictionnaire associant la langue à son code
langage = {'french':'fr', 'english':'en', 'italian':'it', 'german':'de', 'swedish':'sw', 'spanish':'es', 'portuguese':'po', 'finnish':'fi', 'dutch':'du', 'danish':'da'}

username = ""
password = "*"
cont_id = 37
url = "http://www.microcontest.com/contests/"+str(cont_id)+"/contest.php"
url_result = "http://www.microcontest.com/contests/"+str(cont_id)+"/validation.php"
data = [("username", username), ("password", sha1(password).hexdigest()),("ID", cont_id), ("contestlogin", 1), ("version", 2)]


opener = build_opener(HTTPCookieProcessor())
page = opener.open(url, urlencode(data)).read()
_parse(page)

#détection des langues
lang1 = detect_language(variables['txt1'])
lang2 = detect_language(variables['txt2'])
lang3 = detect_language(variables['txt3'])
lang4 = detect_language(variables['txt4'])


#mise en forme et envoi des résultats
data_result = {"lang1":langage[lang1], 'lang2':langage[lang2], 'lang3':langage[lang3], 'lang4':langage[lang4]}
page_result = opener.open(url_result, urlencode(data_result)).read()
print (page_result)

