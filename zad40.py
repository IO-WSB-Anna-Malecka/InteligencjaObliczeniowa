print("podaj dlugosc")
dane=input()
nowe=int(dane)
x=""
y=""
for i in range(nowe, 0, -1):
    for j in range(0, i, 1):
        y += " "
    for u in range(i, nowe+1, 1):
        x += "x"
    print(y + x)
    x=""
    y=""
