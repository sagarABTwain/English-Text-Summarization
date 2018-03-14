# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 20:29:19 2018

@author: Sagar Hossain
"""


import nltk
import math
with open("input.txt","r") as myfile:
    data= myfile.read()
#print data
if __name__ == "__main__":
    a = []
    sent = []
    splitingSent = []
    for i in range(len(data)-1):
        if (data[i] == '.' or data[i]=='?' or data[i]=='!') and data[i+1].isupper():
            a.append(data[i])
            splitingSent.append(''.join(a).split())
            sent.append(''.join(a))
            a = []
        else:
            if data[i] != ',' and data[i] != ';' and data[i]!='\n' and data[i]!='\r':
                a.append(data[i])
            if i+1==len(data)-1:
                a.append(data[i+1])
                splitingSent.append(''.join(a).split())
                sent.append(''.join(a))
'''
    for i in range(len(sent)):
        print (sent[i])'''
    words=nltk.word_tokenize(data)
    pos=nltk.pos_tag(words)
    nouns=[]
    for i in range(len(pos)):
        if pos[i][1] == 'NN' or pos[i][1] == 'NNP' or pos[i][1] == 'NNS' or pos[i][1] == 'NNPS':
            nouns.append(pos[i][0])
    #print(nouns)
    LengthOfPara=len(sent)
    NoOfNoun=len(nouns)

    print ("\n\nSplitting sentence")
    print("------------------------------------------------------------")
    for i in range(LengthOfPara):
        for j in range(len(splitingSent[i])):
            if splitingSent[i][j]=='He' or splitingSent[i][j]=='he':
                splitingSent[i][j]='Rooney'
        print (splitingSent[i])
    
    EachSent=[]
    for i in range(LengthOfPara):
        save = []
        for j in nouns:
            if j in splitingSent[i]:
                save.append(j)
        EachSent.append(save)
        
    print ("\n\nDistance calculation")
    print("------------------------------------------------------------")
    dis=[]
    for i in range(LengthOfPara):
        el=len(EachSent[i])
        if el>1:
            #print el, EachSent[i]
            for j in range(el):
                for k in range(j+1,el):
                    pot=[]
                    p=nouns.index(EachSent[i][j])
                    pot.append(p)
                    q = nouns.index(EachSent[i][k])
                    pot.append(q)
                    d=abs(splitingSent[i].index(EachSent[i][j])-splitingSent[i].index(EachSent[i][k]))
                    pot.append(d)
                    dis.append(pot)
                    print ("dist(",nouns[p],",",nouns[q],")= ",d)
    
    
    print ("\n\nRelevance calculation")
    print("------------------------------------------------------------")
    Rel=[]
    for i in range(NoOfNoun):
        sm=0
        for j in range(len(dis)):
            if dis[j][0]==i or dis[j][1]==i:
                sm+=dis[j][2]
        #keepRel=[]
        #keepRel.append(i)
        #keepRel.append(sum)
        Rel.append(sm)
        print ("Relavance of",nouns[i],"is :", Rel[i])
    
    
    print ("\n\nSentence scoring calculation")
    print("------------------------------------------------------------")
    scoreOfEachSent=[]
    for i in range(LengthOfPara):
        el = len(EachSent[i])
        total=0
        if el > 1:
            for j in range(el):
                index=nouns.index(EachSent[i][j])
                total+=Rel[index]
            keepSent = []
            keepSent.append(i)
            keepSent.append(total)
            #print keepSent
            scoreOfEachSent.append(keepSent)
    afterSort=[]
    l=len(scoreOfEachSent)
    for i in range(l):
        afterSort.append((scoreOfEachSent[i][0],scoreOfEachSent[i][1]))
        print (scoreOfEachSent[i][0],"no. sentence having scores :",scoreOfEachSent[i][1])
   
    print("\n\nGetting sentence number after sorting with their scores")
    print("----------------------------------------------------------------------")
    afterSort.sort(key=lambda x:x[1])
    afterSort.reverse()
    takingSent=[]
    
    takingWhichSent=math.ceil(LengthOfPara/3)
    for i in range(len(afterSort)):
        print(afterSort[i])
        if i<takingWhichSent:
            takingSent.append(afterSort[i][0])
    
    print("\n\nGetting Summary")
    print("-------------------------------------------------------------")
    takingSent.sort()
    for i in takingSent:
        print(sent[i],end='')
    
        

