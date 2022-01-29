a = 2
b = 2
c = 3

if a == b:
    if a == c:
        print("wszystkie sa rowne")
    else:
        print("a jest równe b")
elif a == c:
    print("a jest równe c")
elif b == c:
    print("b jest rowne c")
else:
    print("brak rownych liczb")