# Napisz funkcję, liczy pole kwadrat. Następnie napisz kolejną funkcję, która
# poprosi o podanie boku kwadratu wykorzystując funkcję poprzednią
# policzy i wyświetli na konsoli odpowiedni komunikat o polu kwadratu.

#funkcja pobierająca dane o bokach kwadrata
def kwadrat_pytam_o_bok():
    bok = input('podaj długość boku kwadratu ') # ja wole wpisywanie w tej samej linijce zamiast \n tak że tak robię, ale wiem że można zrobić \n i przeskoczyć do nowej linijki
    return bok

#funkcja licząca pole kwadrat
def kwadrat_licze_pole(bok):
    return int(bok) ** 2

#funkcja oddająca pole
def kwadrat_policzylem_pole(bok):
    print('twój kwadrat o boku ' + str(bok) + ' ma pole ' + str(int(bok) ** 2) + ' :)')

#cały program boży do liczenia kwadratu pola
def pole_kwadratu():
    bok = kwadrat_pytam_o_bok()
    kwadrat_licze_pole(bok)
    kwadrat_policzylem_pole(bok)

# pole_kwadratu()

# Napisz funkcję, liczy obwód kwadrat. Następnie napisz kolejną funkcję,
# która poprosi o podanie boku kwadratu wykorzystując funkcję poprzednią
# policzy i wyświetli na konsoli odpowiedni komunikat o obwodzie kwadratu.

def kwadrat_licze_obwod(bok):
    return int(bok) * 4
    return int(bok)

def kwadrat_pytam_o_bok():
    bok = input('prosze podac dlugosc boku kwadratu ')
    return bok

def kwadrat_oddaje_obwod(bok, obwod):
    print('obwod kwadratu o boku ' + str(bok) + ' wynosi ' + str(obwod) + ' :) ')

def kwadrat_obwod():
    bok = kwadrat_pytam_o_bok()
    obwod = kwadrat_licze_obwod(bok)
    kwadrat_oddaje_obwod(bok, obwod)

# kwadrat_obwod()

# Napisz funkcję, która policzy liczbę słów w zdaniu podanym przez
# użytkownika

def prosze_o_zdanie():
    zdanie = input('witam prosze napisac zdanie a ja policze ile slow jest :) ')
    return zdanie

def licze_slowa(zdanie):
    slowa = zdanie.split()
    liczba_slow = len(slowa)
    return liczba_slow

def zwracam_liczbe_slow(liczba_slow):
    print('ilosc slow w tym zdaniu wynosi ' + str(liczba_slow) + ' :)')

def ile_slow():
    zdanie = prosze_o_zdanie()
    liczba_slow = licze_slowa(zdanie)
    zwracam_liczbe_slow(liczba_slow)

# ile_slow()

# Napisz funkcję, która policzy liczbę słów w zdaniu podanym przez
# użytkownika, ale będzie wyświetlała odpowiednie komunikaty: W zdaniu
# jest tylko jedno słowo, W zdaniu są 2/3/4 słowa, W zdaniu jest 5/6/... słów.

def prosze_o_zdanie():
    zdanie = input('witam prosze napisac zdanie a ja policze ile slow jest :) ')
    return zdanie

def licze_slowa(zdanie):
    slowa = zdanie.split()
    liczba_slow = len(slowa)
    return liczba_slow

def zwracam_liczbe_slow(liczba_slow):
    if liczba_slow == 1:
        print('w tym zdaniu jest ' + str(liczba_slow) + ' slowo')
    elif 1 < liczba_slow < 5:
        print('w tym zdaniu sa ' + str(liczba_slow) + ' slowa')
    else:
        print('w tym zdaniu jest ' + str(liczba_slow) + ' slow')

def ile_slow():
    zdanie = prosze_o_zdanie()
    liczba_slow = licze_slowa(zdanie)
    zwracam_liczbe_slow(liczba_slow)

# ile_slow()

# napisz funkcję, liczy pole prostokąta Następnie napisz kolejną funkcję,
# która poprosi o podanie boków prostokąta i wykorzystując funkcję
# poprzednią policzy i wyświetli na konsoli odpowiedni komunikat o polu
# prostokąta. Zadanie rozwiąż wysyłając oddzielne prośby o podanie długości
# boków, jak i jedną prośbę o podanie obu długości na raz rozdzielnych
# spacją TU JAKIS SPLIT MA BYC. W drugim przypadku wykorzystaj odpowiednią metodę do
# wydzielenia długości poszczególnych boków.

#opcja 1

def prosze_o_boki():
    a = int(input('długość pierwszego boku: '))
    b = int(input('długość drugiego boku: '))
    return a, b

def licze_pole_prostokonta(a, b):
    return a * b

def oddaje_pole(a, b, pole):
    print('pole prostokonta o bokach dlugosci ' + str(a) + ' i ' + str(b) + ' wynosi ' + str(pole) + ' :)')

def pole_prostokonta():
    a, b = prosze_o_boki()
    pole = licze_pole_prostokonta(a, b)
    oddaje_pole(a, b, pole)

# pole_prostokonta()

# opcja 2

def prosze_o_boki_2():
    boki = input('podaj dlugosci bokow oddzielone spacjom ')
    return boki

def dziele_boki_na_dwa(boki):
    x = boki.split()
    a = int((x[0]))
    b = int((x[1]))
    return a, b

def licze_pole_prostokonta(a, b):
    return a * b

def oddaje_pole(a, b, pole):
    print('pole prostokonta o bokach dlugosci ' + str(a) + ' i ' + str(b) + ' wynosi ' + str(pole) + ' :)')

def pole_prostokonta():
    boki = prosze_o_boki_2()
    a, b = dziele_boki_na_dwa(boki)
    pole = licze_pole_prostokonta(a, b)
    oddaje_pole(a, b, pole)

# pole_prostokonta()

# Napisz funkcję, liczy obwód prostokąta Następnie napisz kolejną funkcję,
# która poprosi o podanie boków prostokąta i wykorzystując funkcję
# poprzednią policzy i wyświetli na konsoli odpowiedni komunikat o
# obwodzie prostokąta. Zadanie rozwiąż wysyłając oddzielne prośby o
# podanie długości boków, jak i jedną prośbę o podanie obu długości na raz
# rozdzielnych spacją. W drugim przypadku wykorzystaj odpowiednią
# metodę do wydzielenia długości poszczególnych boków.

# opcja 1

def prosze_o_boki_obwud():
    a = int(input('długość pierwszego boku: '))
    b = int(input('długość drugiego boku: '))
    return a, b

def licze_obwud_prostokonta(a, b):
    return a * b

def oddaje_obwud(a, b, obwud):
    print('obwud prostokonta o bokach dlugosci ' + str(a) + ' i ' + str(b) + ' wynosi ' + str(obwud) + ' :)')

def obwud_prostokonta():
    a, b = prosze_o_boki_obwud()
    obwud = licze_obwud_prostokonta(a, b)
    oddaje_obwud(a, b, obwud)

# obwud_prostokonta()

# opcja 2

def prosze_o_boki_2_obwud():
    boki = input('podaj dlugosci bokow oddzielone spacjom ')
    return boki

def dziele_boki_na_dwa_obwud(boki):
    x = boki.split()
    a = int((x[0]))
    b = int((x[1]))
    return a, b

def licze_obwud_prostokonta(a, b):
    return a * b

def oddaje_obwud(a, b, obwud):
    print('obwud prostokonta o bokach dlugosci ' + str(a) + ' i ' + str(b) + ' wynosi ' + str(obwud) + ' :)')

def obwud_prostokonta():
    boki = prosze_o_boki_2_obwud()
    a, b = dziele_boki_na_dwa_obwud(boki)
    obwud = licze_obwud_prostokonta(a, b)
    oddaje_obwud(a, b, obwud)

# obwud_prostokonta()

# Napisz funkcję, która będzie przeliczała podaną liczbę dni na wybraną
# jednostkę (godziny, minuty, sekundy). Następnie napisz kolejną funkcję,
# która będzie sprawdzała poprawność danych (wykorzystaj try i expect)
# dotyczącą liczby dni (zakładamy, że zostaną podane prawidłowe jednostki
# lub też funkcja przeliczająca zajmie się tym problemem), w zależności od
# podanych wartości wykona następujące polecenia:
# o przeliczy na wskazane jednostki (liczba dni całkowita dodatnia) i
# wyświetli wynik z odpowiednim komentarzem;
# o wyświetli komunikat, że Podałeś liczbę 0, proszę podaj liczbę dodatnią
# (liczba dni 0);
# 2
# o wyświetli komunikat, że Podałeś liczbę ujemną, nie zostanie
# wykonane przeliczenie (liczba dni ujemna);
# o wyświetli komunikat Twoje dane nie są liczbą. NIE RUJNUJ
# PROGRAMU! w przypadku błędu

def prosze_o_dni():
    dni = input('witam prosze podac liczbe dni: ')
    return dni

def sprawdzam_dane(dni):
    try:
        dni = int(dni)
    except:
        print('nie podales to nie ma obliczania nara')
        return False, 0
    if dni < 0:
        print('podales liczbe ujemna, nie zostanie wykonane przeliczenie.')
        return False, 0
    elif dni == str:
        print('twoje dane nie są liczbą - nie rujnuj programu :-(')
        return False, 0
    return True, dni

def prosze_o_jednostke():
    return input('na co mam przeliczyć? wpisz \n (g) - godziny \n (m) - minuty \n (s) - sekundy ')

def przeliczam_dane(dni, jednostka):
    while True:
        if jednostka == 'g':
            godziny = dni * 24
            if godziny == 1:
                print(str(dni) + ' dni to ' + str(godziny) + ' godzina')
                return
            elif 1 < godziny < 5:
                print(str(dni) + ' dni to ' + str(godziny) + ' godziny')
                return
            else:
                print(str(dni) + ' dni to ' + str(godziny) + ' godzin')
                return

        elif jednostka == 'm':
            minuty = dni * 24 * 60
            if minuty == 1:
                print(str(dni) + ' dni to ' + str(minuty) + ' minuta')
                return
            elif 1 < minuty < 5:
                print(str(dni) + ' dni to ' + str(minuty) + ' minuty')
                return
            else:
                print(str(dni) + ' dni to ' + str(minuty) + ' minut')
                return

        elif jednostka == 's':
            sekundy = dni * 24 * 60 * 60
            if sekundy == 1:
                print(str(dni) + ' dni to ' + str(sekundy) + ' sekunda')
                return
            elif 1 < sekundy < 5:
                print(str(dni) + ' dni to ' + str(sekundy) + ' sekundy')
                return
            else:
                print(str(dni) + ' dni to ' + str(sekundy) + ' sekund')
                return

        else:
            print('proszę podać jednostkę! ')
            jednostka = input('jednostka: ')

def przelicznik():
    dni = prosze_o_dni()
    check, dni = sprawdzam_dane(dni)
    if check:
        jednostka = prosze_o_jednostke()
        przeliczam_dane(dni, jednostka)

# przelicznik()

# Na koniec napisz funkcję, która wykorzysta napisane przez Ciebie funkcje
# poprosi o dane rozdzielone dwukropkiem i wyświetli komunikat. Funkcja
# ma prosić o dane dopóki nie zostanie napisane słowo exit.

def prosze_o_dane():
    dane = input('witam prosze podac liczbe dni oraz jednostkę \n (g) - godziny \n (m) - minuty \n (s) - sekundy \n rozdzielone znakiem ":" ')
    return dane

def rozdzielam_dane(dane):
    dane = dane.split(':')
    dni = dane[0]
    jednostka = dane[1]
    return dni, jednostka

def przelicznik_2():
    dane = prosze_o_dane()
    dni, jednostka = rozdzielam_dane(dane)
    check, dni = sprawdzam_dane(dni)
    if check:
        przeliczam_dane(dni, jednostka)

# przelicznik_2()

# Napisz funkcję, która poprosi użytkownika o dowolne zdanie i dowolną
# literę i wyznaczy ile razy litera wystąpiła w zdaniu. Zaprezentuj
# rozwiązanie, które zarówno nie uwzględnia, jak i uwzględnia wielkość liter.


def prosze_o_dane():
    print('witam jak dasz zdanie i literke to powiem ile razy litera wystepuje w zdaniu :-)')
    zdanie = input('prosze napisac zdanie: ')
    litera = input('prosze wybrac literke: ')
    return zdanie, litera

def uwzgledniam_wielkosc_liter(zdanie):
    zdanie2 = zdanie.lower()
    return zdanie2

def licze_litery(zdanie2, litera):
    ilosc = zdanie2.count(litera)
    return ilosc

def odpowiadam(ilosc, zdanie, litera):
    if int(ilosc) == 1:
        print('w zdaniu "' + zdanie + '" litera "' + litera + '" wystepuje ' + str(ilosc) + ' raz.')
    else:
        print('w zdaniu "' + zdanie + '" litera "' + litera + '" wystepuje ' + str(ilosc) + ' razy.')

def licze_i_uwzgledniam_wielkosc_liter():
    zdanie, litera = prosze_o_dane()
    zdanie2 = uwzgledniam_wielkosc_liter(zdanie)
    ilosc = licze_litery(zdanie2, litera)
    odpowiadam(ilosc, zdanie, litera)

def licze_po_prostu():
    zdanie, litera = prosze_o_dane()
    ilosc = licze_litery(zdanie, litera)
    odpowiadam(ilosc, zdanie, litera)

licze_i_uwzgledniam_wielkosc_liter()

# licze_po_prostu()