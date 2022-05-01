import os
from numpy import vectorize 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import math
files = [doc for doc in os.listdir() if doc.endswith('.txt')]
fileContents = [open(File).readlines() for File in files]


vecFunc = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()
simCalc = lambda d1, d2: cosine_similarity([d1,d2])

vecS = list(zip(files, vecFunc(files)))



def plag():
    sln = set()
    global vecS
    for a, b in vecS:
        nVec = vecS.copy()
        cI = nVec.index((a,b))
        del nVec[cI]
        for c, d in nVec:
            SS = simCalc(b,d)[0][1]
            SP = sorted((a,c))
            S = SP[0], SP[1], SS
            sln.add(S)
    return sln 

for things in plag():
    print(things)