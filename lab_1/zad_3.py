a = int(input('podaj wartość '))
n = 5 #rozmiar tablicy
tab = []
x = int(input("Podaj szukaną wartość "))
for i in range(n):
    b = int(input(f"Podaj t[{i}] "))
    tab[i] = b
    if tab[i]==x:
        print("Szukana wartość występuje w tablicy")
        break
print("Szukana wartość nie występuje w tablicy")