#Import libs
#sci kit learn for transform docs in TF IDF vectors.
from sklearn.feature_extraction.text import TfidfVectorizer
#sci kit learn for cosine_similarities
from sklearn.metrics.pairwise import linear_kernel

import datetime
import os
import glob
import sys


#documents: List, contains the content of each document
documents = list() 
#files: List, contains the name of each document
files = list()

#get path of the current folder
pathname = os.path.dirname(sys.argv[0])
#Get files from folder called dataset
path = glob.glob(pathname + "/dataset/*.txt")

#we take the content of each document
for doc in path:
    with open(doc, 'r') as content_file:
        content = content_file.read()
        documents.append(content.lower())
        files.append(os.path.basename(content_file.name))


print ("Documents in dataset/ folder: " , len(documents))

#@tfidf = the documents are now vectors with TF IDF strategy
tfidf = TfidfVectorizer().fit_transform(documents)

#set startedAt var for the timestamp when the process start
startedAt = datetime.datetime.now()

#create a new document for the results of cosine similarities between all documents with TXT extension
filename = "similitud.txt"
#if file called similitud.txt exists, delete the file.
if os.path.exists(filename): os.remove(filename)
#make new file similitud.txt
f = open(filename, "w")

#accumulators to travel the vector created with TfidfVectorizer
i = 0
j = 1

#Look vector for all documents and we assign the most similar to related_docs_indices var
while i < len(documents):
  #we calculate the cosine similarity for the vector tfidf[i:j] 
  cosine_similarities = linear_kernel(tfidf[i:j], tfidf).flatten()
  #we assign the most similar 
  related_docs_indices = cosine_similarities.argsort()[:-3:-1]
  #print result
  print ("Filename: ",files[i]," Filename similiar: ",files[ related_docs_indices[1] ]," distance:",cosine_similarities[related_docs_indices[1]])

  #save in similitud.txt 
  f.write("{}{}{}{}{}".format(files[i]," ",files[ related_docs_indices[1] ], " ", cosine_similarities[related_docs_indices[1]] ))
  f.write("\n")
  #increase variables in 1 for the next value of cosine_similarities
  i = i + 1
  j = j + 1
  
#close the file
f.close()

#print end hour
print("The process startedAt was: " , startedAt)
print("And the Finished At its: ", datetime.datetime.now())

