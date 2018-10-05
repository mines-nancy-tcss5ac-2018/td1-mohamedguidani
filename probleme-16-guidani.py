def somme_chiffres (n) : 
    s=0
    while n>0 :
        a=n%(10)
        n=n//(10)
        s=s+a
    return s    
assert somme_chiffres(2**15)==26
print( somme_chiffres (2**1000))