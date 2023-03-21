def silnia(n):
    if n==0: return 1
    else: return n*silnia(n-1)

a = int(input('podaj a: '))
b = int(input('podaj b: '))

#I wersja
def nwdIter(a,b):
    while a!=b:
        if a>b: a=a-b
        else: b=b-a
    return a

def nwdRek(a,b):
    if a!=b:
        if a>b: return nwdRek(a-b,b) #a=a-b
        else: return nwdRek(a,b-a) #b=b-a
    return a

#II wersja
def nwdIterII(a,b):
    while b!=0:
        temp = b
        b = a % b
        a = temp
    return a

def nwdRekII(a,b):
    if b!=0:
        return nwdRekII(b,a%b)
    return a

print(nwdIterII(a,b))