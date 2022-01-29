print("podaj dlugosc")
dane=input()
nowe=int(dane)
x=""
for i in range(0, nowe, 1):
    for j in range(0, i+1, 1):
        x+="x"
    print(x)
    x=""
