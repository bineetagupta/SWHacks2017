import nltk
from nltk.corpus import wordnet as wn
#import amazing_semsim_package
 
from sys import argv
import nltk
import os
import re
import sys
import subprocess
import commands
import numpy as np

dist = []
i = 0

global_count = 0.0

search_list = ["writing","dancing","singing"]
resume1_list = ["writing","poem"]
resume2_list = ["dancing","poetry","sang"]

for word in search_list:
	a = wn.synsets(word)
	for word1 in a:
		dist.append(global_count)
		global_count = 0.0
		word1 = str(word1).split("'")[1]
		#print(str(wn.synsets(word)[0]).split("'")[1])
		aa = wn.synset(str(word1))
		for word2 in resume1_list:
			b = wn.synsets(word2)
			for word1 in b:
				word1 = str(word1).split("'")[1]
				bb = wn.synset(word1)
				print(float(aa.path_similarity(bb)))
				global_count = global_count + float(aa.path_similarity(bb))
#		print(similarity(b,a))
		#dist[i] = dist[i] + (a.path_similarity(b))
		#dist.append(a.path_similarity(b))
		#print(dist[len(dist) - 1])	



