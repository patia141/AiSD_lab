import math
a = float(input('podaj a '))
b = float(input('podaj b '))
c = float(input('podaj c '))

if a!=0:
    delta = (b*b)-(4*a*c)
    if delta>0:
        x1 = ((b *(-1)) - math.sqrt(delta)) / (2 * a)
        x2 = ((b *(-1)) + math.sqrt(delta)) / (2 * a)
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    else:
        if delta==0:
            x1 = (b * (-1)) / (2 * a)
            print(f'x1 = {x1}')
        else:
            print('Brak rozwiązań rzeczywsitych')
else:
    print("To nie jest równanie kwadratowe")
