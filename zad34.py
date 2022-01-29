waga = 75
wzrost = 180
#sposob przez format
s = "Jan Kowalski (waga {}, wzrost {})"
s = s.format(waga, wzrost)
print(s)
#sposob przez konwersje liczby na string
wagatxt = str(waga)
wzrosttxt = str(wzrost)
s = "Jan Kowalski (waga: " + wagatxt + ", wzrost, " + wzrosttxt + ")"
print(s)
