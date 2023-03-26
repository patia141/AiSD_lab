def na_bin(n):
    if n==0: return 0
    else:
        liczba = na_bin(n//2)
        reszta = n%2
        return liczba*10 + reszta