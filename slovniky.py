# slvník
kontakty = {
    "jmeno": "Petr",
    "Prijmeni": "Michalik",
    "vek" : 15,
    "telefon": 123456789
}

#promeny

print(f"puvodni kontakty: {kontakty}")

#vypsaní jedne proměnne

print(f"Jmeno: {kontakty['jmeno']}")

kontakty["vek"]= 69
print(kontakty["vek"])

kontakty["mesto"] = "Třinec" # dodavaní klíču
print(kontakty)

telefon = kontakty.get("telefon")
print("telovni cislo:", telefon)

