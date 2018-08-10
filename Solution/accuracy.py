import codecs
from decimal import Decimal
import math

def main():
    fp = codecs.open('vanillaoutput.txt', 'r', "utf-8")
    lines = fp.read().splitlines()
    fp.close()

    fp2 = codecs.open('dev-key.txt', 'r', "utf-8")
    lines2 = fp2.read().splitlines()
    fp2.close()

    count = 0
    count2 = 0
    total = len(lines)

    wout = []
    wkey = []
    pwout = []
    pwkey = []

    if (len(lines) != len(lines2)):
        return

    for line in lines:
        words = line.split(" ")
        wout.append(words[1])
        pwout.append(words[2])

    for w in lines2:
        w2 = w.split(" ")
        wkey.append(w2[1])
        pwkey.append(w2[2])


    for i in range(len(wout)):
        if wout[i] == wkey[i]:
            count += 1
        if pwout[i] == pwkey[i]:
            count2 += 1
    accuracy = Decimal(count)/Decimal(total)
    accuracy2 = Decimal(count2)/Decimal(total)

    #print lines2
    print ((accuracy + accuracy2)/2)

main()