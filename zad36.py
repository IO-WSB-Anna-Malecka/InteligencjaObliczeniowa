print("podaj a i b")
dane=input()
nowe=dane.split(" ")
a=int(nowe[0])
b=int(nowe[1])
if a>0 and b>0:
    print("Pole: ", a*b, " Obwód: ", a*2+b*2)
else:
    print("niepoprawne dane")