# lab 1

# typy proste
# 1.
# print("i like python. i don't like python")

# print('i like python. i don\'t like python')

# 2.
# print("i like python. \n i \t \t \t don't like python")

# 3.
# print("""i like python \n i don't like python""")

# print("\t \t \t \t \t \n \t \t \t \t")

# typy złożone zmiennych
# 1.1
# MojaLista = [20, 7/24, "Natalka"]
# print(MojaLista)

# 1.2
# print(MojaLista[0])

# 1.3
# print(MojaLista[2])
# print(MojaLista[-1])

# 1.4
# print(MojaLista[1])
# print(MojaLista[-2])

# 1.5
# print(MojaLista + ["Prokopiuk"])
# MojaLista += ["Prokopiuk"]

# 1.7
# print(MojaLista.insert(1, 30 - MojaLista[0])

# 1.8
# MojaListaOld = MojaLista.copy()

#1.9
# na podstawie wartość w moja lista old:
# MojaListaOld.remove(7/24)
# print(MojaListaOld)

# na podstawie pozycji w moja lista:
# MojaLista.pop(1)
# print(MojaLista)

# 1.10
# MojaLista[0] += 1
# print(MojaLista)
# x +=1 to skrót od x = x + 1 czyli wartość x powiększona o 1

# MojaLista[0] = 21
# print(MojaLista)

# 1.11
# MojaLista[1] = 100
# print(MojaLista)

# 1.12
# MojaLista.reverse()
# print(MojaLista)

# krotki
# 2.1
# MojaKrotka = (20, 7/24, "Natalka")
# print(MojaKrotka)
# print(type(MojaKrotka))

# 2.2
# MojaKrotka = 20, 7/24, 'Natalka'
# print(MojaKrotka)
'''parentheses are optional in a tuple (without em its tuple packing)'''

# 2.3
# MojaKrotka1 = ("Natalka")
# print(type(MojaKrotka1))

# 2.4
# print(MojaKrotka[0])

# 2.5
# MojaKrotka[0] = 666
# print(MojaKrotka)
'''elements of a tuple cannot be changed once they have been assigned'''

# 2.6
# listek = [1, 2]
# listatuplowa = list(MojaKrotka)
# MojaKrotka2 = (listatuplowa, listek)
# print(MojaKrotka2)

# 2.7
# MojaKrotka2[1][0] = 9
# print(MojaKrotka2)
''' w tuple mozna obejsc niemoznosc zmieniania rzeczy poprzez wsadzenie ich w liste xd'''
