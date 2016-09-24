#Angela Yu & Ely Sandine
#Work 1
#Dyrland-Weaver pd 6

import random

def importation(filename):
    instream = open(filename, 'r') 
    content = instream.readlines() 
    instream.close()
    return content

def split(L):
    dict={}
    del L[0]
    del L[len(L)-1]
    for row in L:
        row=row.strip('\n').rsplit(',',1)
        dict[row[0]]=(float)(row[1])
    return dict
def randomOcc(d):
    rand = random.uniform(0,100)
    for key in d.keys():
        if(rand<d[key]):
            return key
        else:
            rand -= d[key]
    return rand

#Testing function                                                               
def doAlot():
    dict = {}
    dict["a"]=40
    dict["b"]=30
    dict["c"]=20
    dict["d"]=10
    a=0
    b=0
    c=0
    d=0
    x=0
    print "start"
    while x<10000:
        val = randomOcc(dict)
        if val=="a":
            a+=1
        if val =="b":
            b+=1
        if val =="c":
            c+=1
        if val =="d":
            d+=1
        x+=1
    print a
    print b
    print c
    print d
    print "end"

if __name__=='__main__':
    data=importation("occupations.csv")
    d = split(data)
    print "Keys:"
    print(d.keys())
    print "Values:"
    print(d.values())
    print "Random:"
    print(randomOcc(d))
