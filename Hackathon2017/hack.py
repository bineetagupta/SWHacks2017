# This is python scrip that implement Recruiting AI funciton
# The following is the steps we take
# 
# INPUT: 
#   KEYs        user defined keywords for job description
#   Resumes     resumes of canditate
# 
# OUTPUT:
#   Ranking_file    
#       candidate_ID    ranking_factor
#   the ranking factor describes the distance between candidate resume
# and job description
# 
# 


from sys import argv
import nltk
import os
import re
import sys
import subprocess
import commands
import numpy as np


#script, filename = argv
script = argv

## Read in Job Description Keys
#KEYS_FILE = "KEYs"
KEYS_FILE = "./glove.6B.50d.txt"
keys = open(KEYS_FILE)
#print keys.read()

glove_full = "./glove.6B.50d.txt"
glove_tag = "./glove.keys.ID"


## Read in Resumes
#resume_file = "resume"
#resume = open(resume_file)


## use NLTK to prerpocess the resume file to take off stop words
#sentences = ie_preprocess(keys)
#print sentences

setence = " at eight o'clock on Thursday morning"
print "origional text"
print setence

tokens = nltk.word_tokenize(setence)
print tokens

#tagged = nltk.pos_tag(tokens)
#print tagged

word_list = tokens


from nltk.corpus import stopwords
# ...
filtered_words = [word for word in word_list if word not in stopwords.words('english')]
print filtered_words



MAX = 100000000000

hash_dict = dict()
#glove_file = open("./glove.840B.300d.txt")

#sys.stdout = open('file', 'w')
#os.stdout = open('file','w')

count = 1
for key in keys:
    # print "--> Working on ", key
    # #find the key array in our glove array
    # #command = "cat ./glove.keys.ID |awk '$1==%s {print $0}'|awk 'NR==1 {print $0}'" % key 
    # command = "cat %s |grep -w '%s' |awk 'NR==1 {print $0}'" % ( glove_tag, key )
    # #command = "cat %s |awk '$1==\"%s\" {print $0}'" % (glove_tag, str(key))
    # print command
    # #command = ["cat" ,"glove.840B.300d.txt|grep -w PhD"]
    # print commands.getstatusoutput(command)
    # result =  commands.getstatusoutput(command)
    # input()
    # #print result
    # line_number = result[1].split(" ")[1]
    # #print line_number

    # command = "cat ./glove.840B.300d.txt |awk 'NR==%s {print $0}'" % line_number
    # #print command
    # result =  commands.getstatusoutput(command)
    # new_result =  result[1]
    # new_result = new_result.split(" ")
    # #print new_result
    # array = np.asarray(new_result)
    # pure_array = array[1:]
    # outfile_name = "./KEY_DIR/job_key.%d" % count

    #command = "cat ./glove.840B.300d.txt |awk '$1=='%s' {print $0}'|awk 'NR==1 {print $0}'" % key
    #command = "cat ./glove.tmp|awk '$1=='%s' {print $0}'|awk 'NR==1 {print $0}'" % key
    #command = "cat ./glove.tmp|awk '$1==\"%s\" {print $0}'" % key
    #command = "cat ./glove.840B.300d.txt  |grep -w '%s' |awk 'NR==1 {print $0}'" % key
    #print "command is ", command
    #result =  commands.getstatusoutput(command)
    #print result
    #input()



    #for i in xrange(0, len(pure_array)):
        #print pure_array[i]
    #out = open(outfile_name,"w")
    #with open(outfile_name,'w') as f:
        #np.savetxt(f,pure_array, newline=" ",fmt='%15.5f')
    #out.write(pure_array)
    #print outfile_name
    #print len(pure_array)

    kk = key.split(" ")
    array = np.asarray(kk)
    #print array

    super_key = array[0]
    super_vector = array[1:]
    #print super_key 
    #print super_vector
    
    hash_dict[hash(super_key)%MAX]  =  ( super_key, super_vector)
    #print hash_dict[hash(key)/MAX]
    #hash_dict[hash(key)/MAX]  =  ( key, pure_array)
    #count +=1

#print hash_dict
#tag = hash("sql")%MAX
#print tag
#print hash_dict[tag]

JOB_FILE = "./job.txt"
job_keys = open(JOB_FILE)
out = "./job_vectors.txt"
f = open(out,'w')


for job_key in job_keys:
	#print(job_key)
	#job_keyy = job_key.split(",")
	job_keyy = job_key.split("\n")
	arrayy = np.asarray(job_keyy)
	#print arrayy[0]
	tag = hash(arrayy[0])%MAX
	#print tag
	s = str(hash_dict[tag])
	f.write(s)
	f.write('\n')
	#f.write("yes")

f.close()

outt = "./resume_words.txt"
ff = open(outt,'w')

for filtered_word in filtered_words:
	print(filtered_word)
	tag = hash(filtered_word)%MAX
	print(hash_dict[tag])

ff.close()
