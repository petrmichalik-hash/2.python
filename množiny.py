python_devs = {"Nelča" , "Petr" ,"Barča" ,"Marshalek"}
java_devs = {"Romana" , "Karel" , "Adam" , "Petr"}

vsichni_devs = python_devs | java_devs
print("všichni vývojaři (sjednocení):",vsichni_devs)
print(20*"=")
#operace průniku (A)
polyglot_devs = python_devs & java_devs
print("vyvojaři, kteři ovládají oba jazyky ( průnik):" , polyglot_devs)

#rozdil
vsichni_devs = python_devs - java_devs
print("Všíchni vvývojaři (rozdíl):", vsichni_devs)
