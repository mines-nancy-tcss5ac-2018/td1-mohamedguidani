def valeur (ch) : 
    alph="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s=0
    for c in ch :
        for i in range (len(alph)) : 
            if alph[i ]==c : 
                s=s+i+1
    return s
assert valeur ("COLIN")==53


def trans() :
    f = open('p022_names.txt', 'r')
    l=[]
    for ligne in f :
        l=l+ligne.split(",")
    l=sorted (l)
    m=[]
    for i in range ( len(l)) :
        m.append (valeur(l[i])*i)
    r=0
    for p in m : 
        r=r+p
    return r
    
print ( trans ())



    
    