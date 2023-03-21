tab = [1,2,3,4,5]

def odwroc(tab):
    if len(tab)==0: return []
    else: return [tab[-1]] + odwroc(tab[:-1])

print(odwroc(tab))