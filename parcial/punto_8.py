def ident(n):
    if(n <= 1):
        print(n)
        return n
    elif(n > 1):
        print(n,' ',end="")
        return(ident(n-1))
        
a = int(input("ingrese: "))
ident(a)
