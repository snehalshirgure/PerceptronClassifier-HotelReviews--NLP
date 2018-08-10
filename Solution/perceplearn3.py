import re
import operator
import json

f = open("train-labeled.txt", "r", encoding="utf8")

d_all={}

stopwords = ["a", "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "so", "than", "too", "very", "can", "will", "just", "should", "now"]

reviewcount = 0
wordcount = 0 

if f.mode == 'r':
    fl = f.readlines()
    #for each line
    for a in fl:
        reviewcount += 1
        b = a.split()
        #for each word
        for x in range(3, len(b)):
            word = re.sub(r'\W', "", b[x]).lower()
            if word not in stopwords:
                if word not in d_all:
                    d_all[word]=1
                else:
                    d_all[word]+=1

                  

w_1 = {}
w_2 = {}
wavg_1={}
wavg_2={}
u_1={}
u_2={}

#for k, v in list(d_all.items()):
 #   if(v==1):
  #      del d_all[k]

for wrds in d_all:
  wordcount+=1
  w_1[wrds]=0
  w_2[wrds]=0
  wavg_1[wrds]=0
  wavg_2[wrds]=0
  u_1[wrds]=0
  u_2[wrds]=0

#print(wordcount)

bias1 =0
bias2 =0

xvector_list =[]

y_1=[]
y_2=[]

f2 = open(fileinput,"r", encoding="utf8")

if f2.mode == 'r':
    fl = f2.readlines()
    #for each line
    for a in fl:
        b = a.split()
        class1 = b[1]
        class2 = b[2]

        if (class1 == 'Fake'):
            y_2.append(-1)
        if (class1 == 'True'):
            y_2.append(1)
        if (class2 == 'Neg'):
            y_1.append(-1)
        if (class2 == 'Pos'):
            y_1.append(1)
        
        xvec = {}
        #for each word
        for x in range(3, len(b)):
            word = re.sub(r'\W', "", b[x]).lower()
            if word not in xvec:
                xvec[word]=1
            else:
                xvec[word]+=1
        xvector_list.append(xvec)

for itr1 in range(0,25):
    for kk1 in range(0,reviewcount):
            score=bias1
            xvector1 = xvector_list[kk1]
            for k11 in xvector1:
                if k11 not in stopwords:
                    score += w_1[k11]*xvector1[k11]
            if(score*y_1[kk1] <= 0):
                for k12 in xvector1:
                    if k12 not in stopwords:
                        w_1[k12] += y_1[kk1]*xvector1[k12] 
                bias1 += y_1[kk1]


for itr2 in range(0,25):
    for kk2 in range(0,reviewcount):
            score=bias2
            xvector2 = xvector_list[kk2]
            for k21 in xvector2:
                if k21 not in stopwords:
                    score += w_2[k21]*xvector2[k21]
            if(score*y_2[kk2] <= 0):
                for k22 in xvector2:
                    if k22 not in stopwords:
                        w_2[k22] += y_2[kk2]*xvector2[k22] 
                bias2 += y_2[kk2]

f3 = open("vanillamodel.txt", "w+", encoding="utf8")
data_list1 = {"weights":w_1 ,"bias":bias1,"weights2":w_2 , "bias2":bias2}
data1 = json.dumps(data_list1, ensure_ascii=False)
f3.write(data1)

bias1=0
bias2=0
beta1=0
beta2=0
counter1=1
counter2=1

for itr1 in range(0,25):
    for kk1 in range(0,reviewcount):
            score=bias1
            xvector1 = xvector_list[kk1]
            for k11 in xvector1:
                if k11 not in stopwords:
                    score += wavg_1[k11]*xvector1[k11]
            if(score*y_1[kk1] <= 0):
                for k12 in xvector1:
                    if k12 not in stopwords:
                        wavg_1[k12] += y_1[kk1]*xvector1[k12]
                for k12 in xvector1:
                    if k12 not in stopwords:
                        u_1[k12] += y_1[kk1]*xvector1[k12]*counter1
                bias1 += y_1[kk1]
                beta1 += y_1[kk1]*counter1
            counter1+=1

for words in wavg_1:
    wavg_1[words]-= (u_1[words]/counter1)
bias1-= beta1/counter1

for itr2 in range(0,25):
    for kk2 in range(0,reviewcount):
            score=bias2
            xvector2 = xvector_list[kk2]
            for k21 in xvector2:
                if k21 not in stopwords:
                    score += wavg_2[k21]*xvector2[k21]
            if(score*y_2[kk2] <= 0):
                for k22 in xvector2:
                    if k22 not in stopwords:
                        wavg_2[k22] += y_2[kk2]*xvector2[k22]
                for k22 in xvector2:
                    if k22 not in stopwords:
                        u_2[k22] += y_2[kk2]*xvector2[k22]*counter2 
                bias2 += y_2[kk2]
                beta2 += y_2[kk2]*counter2
            counter2+=1

for words in wavg_2:
    wavg_2[words]-= (u_2[words]/counter2)
bias2-= beta2/counter2


f4 = open("averagedmodel.txt", "w+", encoding="utf8")
data_list2 = {"weights":wavg_1 ,"bias":bias1,"weights2":wavg_2 , "bias2":bias2}
data2 = json.dumps(data_list2, ensure_ascii=False) 
f4.write(data2)