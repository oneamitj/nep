#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import sys
import csv

site = sys.argv[1]
data = file(site).read()

lst_file = sys.argv[2]
l = file(lst_file).read()

y_file = open("yes.txt","w")
n_file = open("no.txt","w")

#lst = l.text.encode('utf-8','strict')
#para = soup.text.encode('utf-8','strict')

# sign=['। ', '? ']
# for end in sign:
# 	para=para.replace(end,end+'|\n')

# for l_ord in lst.split():
# 	if l_ord == ' ':
# 		continue
# 	for line in para.split("।"):
# 	    for woord in line.split():
# 	    	if word == ' ':
# 	    		continue
# 	    	if l_ord == word:
# 	    		print l_ord
# 	    		break
	    	

for key in l.split():
	if key == " ": continue
	for line in data.split("।" or "?"):
		for word in line.split():
			if word == " ": continue
			if word == key:
				#print word
				y_file.write(line+"।"+"\n")
				break
y_file.close()
n_file.close()

#print para


