print("podaj imiona")
dane=input()
nowe=dane.split(",")
for i in nowe:
    if i[-1] == "a":
        print(i)