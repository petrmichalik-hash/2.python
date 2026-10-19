cislo_list = [1,2,2,4,4,4,4,5,6,7,7,7]
unitkatni_cisla = set(cislo_list)#set vymažuje duplicity

print("uniktaní čísla:", unitkatni_cisla )

print("puvodni seznam", cislo_list)

prazdna_mnoziny = set()
prazdna_mnoziny.add(150)
prazdna_mnoziny.add(90)

print("Množina po přidání prvku:", prazdna_mnoziny)

if 3 in unitkatni_cisla:
    print("Čislo 3 je v množine unikátních čísel.")

else:
    print("Čislo 3 ---NENÍ v množině uníkátních čísel.")