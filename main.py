import os
from numpy import vectorize 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import math
files = [doc for doc in os.listdir() if doc.endswith('.txt')]
fileContents = [open(File).readlines() for File in files]
dict1 = {}  #This will contain the word-frequency pairs for all words across all documents
minidict = {} #This will be used as a temprorary carrier variable. It will carry individual document word-frequency pairs to compilation.
compilation = [] #This is the set of all word-frequency pairs for each document. 
tf = {}  #term frequency list
df = dict1  #occurence of t in N documents
sizes = []
tfIDFz = []

#Constructs dict1
def SuperdictMaker(fileContents):
    for doc in fileContents:
        for line in doc:
            for words in line.split():
                words = words.lower()
                if (words not in dict1):
                    dict1[words] = 1; 
                else:
                    dict1[words] =  dict1[words] + 1


#Constructs compilation list
def MinidictMaker(doc):
    size = 0
    for lines in doc:
        for words in lines.split():
            words = words.lower()
            if (words not in minidict):
                    minidict[words] = 1; 
            else:
                    minidict[words] =  minidict[words] + 1
            size = size + 1
    sizes.append(size)
    compilation.append(minidict)


for doc in fileContents:
    MinidictMaker(doc)
    minidict = {}


#TF-IDF Computation
def tfIDF(dict1, compilation):
    N = len(fileContents)
    
    for i in range(N):
        for key in compilation[i]:
            tf[key, i] = (compilation[i][key] / sizes[i])
    #print(tf)

    count = 0
    for key in dict1:
        for i in range(N):
            if key in compilation[i]:
                count = count + 1
        df[key] = (math.log(N/(count)))  #this is IDF or log(N/df)
        count = 0
    #print(df)

    for x in df:
        for y in tf:
            if x in y:
                tfIDFz.append(tf[y]*df[x])
                print(tf[y]*df[x])
    


#Cosine Similarity
similarity = lambda doc1, doc2: cosine_similarity([doc1,doc2])


    

    


SuperdictMaker(fileContents)
tfIDF(dict1, compilation)


