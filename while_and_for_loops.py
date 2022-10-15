#           while loops

# i = 1
# while i <= 5:
#     print(i)
#     i += 1
'''tutaj ^ jest i = i + 1 ale to nie znaczy że to się tyle równa (bo to nie ==) 
    tylko że zmieniam tę wartość'''

# i = 1
# while i <= 10:
#     print(i * '*')
#     i += 1
# '''stringa do integer nie mozna dodawac ale mozna mnozyc ich'''

#           for loops

'''
for owoc in owocki JEST DEKLARACJĄ ŻE OWOC TO ITEM W OWOCKACH
'''

# owocki = ['japko', 'pomaranczyk', 'cebula']
# for owoc in owocki:
#     print(owoc)
# ''' for cośtam in zbiur dla każdego itema w tym zbiorze wykona się po kolei oddzielnie'''

#           for range()

# numerki = range(5)
# print(numerki)
'''this is gonna print range(o, 5) a my chcemy zeby pokazalo po kolei numerki wiec trzeba tak jak nizej'''
# for numerek in numerki:
#     print(numerek)

''' range(5, 10) daje 5, 6, 7, 8, 9
    range(5, 10, 2) daje 5, 7, 9 poniewaz trzecia wartosc (2) to step'''