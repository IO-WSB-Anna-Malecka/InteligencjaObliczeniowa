def obcinaj(s):
    return s[1:-1]

def max_sum(a,b,c):
    liczby = [a,b,c]
    pierwsza = max(liczby)
    liczby.remove(pierwsza)
    druga = max(liczby)
    return pierwsza + druga

def wybierz_parzyste(x):
    d=[]
    for i in x:
        if i % 2 == 0:
            d.append(i)
    return d

def pole_trapezu(a,b,h):
    pole=(a+b)*h/2
    return pole

print(obcinaj("kwadrat prostokąt trójkąt"))
print(max_sum(15,44,54))
print(wybierz_parzyste([5,4,3,1,84]))
print(pole_trapezu(2,5,3))
