body = 80
chemce_ho = True

if body >= 80:
    if chemce_ho:
        print("jo cheme ho")
        print("ma dost bodu")
    else:
        print("ma dost bodu")
        print("necheme ho")
else:
    print("nema dost bodu")




cislo = 5

if cislo % 2 == 0:
    print("Číslo je sudé")
else:
    print("Cislo je liche.")


print(7 % 2)




nakupni_kosik = []
if nakupni_kosik:
    print("kosik neni prazdny")
else:
    print("Kosik je prazdny")

povolene_ovoce = ["jablko","banán","pomeranc"]
moje_ovoce = "jablko"

if moje_ovoce in povolene_ovoce:
    print(f"{moje_ovoce.capitalize()} je povolene ovoce")
else:
    print(f"{moje_ovoce.capitalize()} není na seznamu povoleného ovoce.")
