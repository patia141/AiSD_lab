def fibonacci(n):
    fib=[]
    for i in range(n):
        if i==0:
            fib.append(i)
        elif i==1:
            fib.append(i)
        else:
            fib.append(fib[i-1]+fib[i-2])
    return(fib)

n=int(input("podaj ilość wyrazów ciągu - n: "))
print(fibonacci(n))