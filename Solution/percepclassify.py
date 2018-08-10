import json
import math
import re

def main():   
    
    f1 = open("vanillaperceptron.txt", "r" , encoding="utf-8")
    f2 = open("dev-text.txt", "r", encoding="utf-8")
    f3 = open("vanillaoutput.txt", "w+" , encoding="utf-8")

    if f1.mode=="r":
        ff = f1.readlines()
        for lines in ff:
            jsonfile = json.loads(lines,encoding="utf-8")
            x_1=jsonfile["xvectors"]
            x_2=jsonfile["xvectors2"]
            w_1 = jsonfile["weights"]
            w_2 = jsonfile["weights2"]
            bias1 = jsonfile["bias"]
            bias2 = jsonfile["bias2"]
    
    if f2.mode=="r":
        fl = f2.readlines()
        #for each line
        for line in fl:
            a = line.split()
            reviewid = a[0]

            xvec = {}
            xv_1=[]
            xv_2=[]
            #for each word
            for x in range(3, len(a)):

                word = re.sub(r'\W', "", a[x]).lower()
                if word not in xvec:
                    xvec[word]=1
                else:
                    xvec[word]+=1
            
            for wrd in x_1:
                if wrd[0] in xvec:
                    xv_1.append(xvec[wrd[0]])
                else:
                    xv_1.append(0)
            
            for wrd in x_2:
                if wrd[0] in xvec:
                    xv_2.append(xvec[wrd[0]])
                else:
                    xv_2.append(0)

            #vector x to be tagged
            score1 = bias1
            for x in range(0,1000):
                score1+= w_1[x]*xv_1[x]

            score2 = bias2
            for x in range(0,1000):
                score2+= w_2[x]*xv_2[x]

            if(score1>0 and score2>0):
                f3.write(str(reviewid)+" True Pos\n")
            if(score1<0 and score2>0):
                f3.write(str(reviewid)+" True Neg\n")
            if(score1<0 and score2<0):
                f3.write(str(reviewid)+" Fake Neg\n")
            if(score1>0 and score2<0):
                f3.write(str(reviewid)+" Fake Pos\n")

if  __name__ ==  "__main__":
    main()           
            
