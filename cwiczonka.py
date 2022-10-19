# weight = float(input('what is your cats weight? :3 '))
# unit = input("in (k)g or (l)bs? ")
# if unit == 'k':
#   print('thats ' +  str((weight * 2.2)) + 'lbs ')
# if unit == 'l':
#   print('thats ' +  str((weight * 0.45)) + 'kg ')
#   print('oki bye')

##############################################################################
    # przejdz przez liste owockuw i jesli jest w nich japko to wyswietl mam alergie
    # jesli jest owoc na p to niech wyswietli jego nazwe
# owocki = ['japko', 'pomaranczyk', 'cebula', 'pomidor']
# for owoc in owocki:
#     if owoc == 'japko':
#         print(owoc + ' - mam alergie')
#     if owoc[0] == 'p':
#         print(owoc)

#################################################################################
# tekst = '''
# twoja stara
# '''
# print(tekst)

#################################################################################
# zarobki = int(input('ile zarabiasz pieniodzuw (w pln)?: '))
# koty = int(input('ile posiadasz kotuw (w szt)?: '))
# if zarobki >= 3000 and koty <= 3:
#     is_zdolnosc_kredytowa = True
# else:
#     is_zdolnosc_kredytowa = False
# if is_zdolnosc_kredytowa:
#     print('ok mozesz kredyt')
# else:
#     print('nie mozesz kredyt')

###############################################################################
# username = input('jakie username dasz sobie wpisz: ')
# if len(username) < 5:
#     print('za krutkie')
# elif len(username) > 20:
#     print('za dlugie')
# else:
#     print('oki super')

###############################################################################
# import random
# secret_number = random.randint(0, 10)
# guess_count = 1
# guess_limit = 3
# guess = int(input('zgaduj liczbe '))
# guess_count +=1
# while guess_count <= guess_limit:
#     if guess == secret_number:
#         print('łał zajebicho')
#         break
#     else:
#         input('dawaj jeszcze raz ')
#         guess_count += 1
# if guess_count > guess_limit:
#     print('no i chuj nie udalo sie')

#########################################################
# car game :3
# command = input('type help to see options ')
# while True:
#     if command == 'help':
#         command = input('''start - to start the car
#     stop - to stop the car
#     quit - to quit the game ''')
#     is_started = False
#     is_stopped = True
#     if command == 'start':
#         is_started = True
#         command = input('car started... ')
#     if is_started and command == 'start':
#         command = input('the car already started ')
#     if command == 'stop' and not is_stopped:
#         is_stopped = True
#         command = input('car stopped... ')
#     elif is_stopped and command == 'stop':
#         command = input('the car already stopped ')
#     elif command == 'quit':
#         print('you quit the game bye :3')
#         break
#     else:
#         command = input('i dont understand maybe try again? ')

##########################################################################
# for item in range(0, 61):
#     if item % 5 == 0:
#         print(item)

##########################################################################
# prices = [21, 37, 69]
# total = 0
# for price in prices:
#     total += price
# print('total: ' + str(total))

#########################################################################
# for x in range(6):
#     for y in range(11):
#         print(f'{x}, {y}')

##########################################################################
# numbers = [5, 2, 5, 2, 2]
# for number in numbers:
#     print(number * 'x')

########################################################################
# import random
# number = random.randint(0, 50)
# user_guess = int(input('zgadnij liczbe wylosowanom '))
# while True:
#     if user_guess > number:
#         user_guess = int(input('sekretna liczba jest mniejsza niż ' + str(user_guess) + ', dawaj jeszcze raz '))
#     elif user_guess < number:
#         user_guess = int(input('sekretna liczba jest większa niż ' + str(user_guess) + ', dawaj jeszcze raz '))
#     else:
#         print('zajebicho')
#         break

########################################################################
# name = input('whats your name ')
# birth_date = input('when were you born in format DDMMYYYY pliz answer ')
# birth_year = birth_date[4:8]
# one_century_after_year = int(birth_year) + 100
#
# print(name + ', you will be 100 years old in the year ' + str(one_century_after_year) + '!')

########################################################################
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for item in a:
#     if item < 10:
#         print(item)

########################################################################
'''create a program that asks the user for a number and then prints out a
list of all the divisors of that number. (If you don’t know what a
divisor is, it is a number that divides evenly into another number.
    For example, 13 is a divisor of 26 because 26 / 13 has no remainder.'''

# number = int(input('gimme a number '))
# for i in range(1, number):
#     if number % i == 0:
#         print(i)

########################################################################
'''write a program that returns a list that contains only the elements 
that are common between the lists (without duplicates)'''

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# for item in a:
#     if item in b:
#         print(item)

########################################################################
'''Ask the user for a string and print out whether this string is a 
palindrome or not. (A palindrome is a string that reads the same forwards 
and backwards.)'''

'''             SLICING GUIDE
a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array
a[::-1]        # spells item backwards : D
'''

# string = input('type something ')
# if string == string[::-1]:
#     print('its a palindrome - ' + string + ' - see? :)')
# else:
#     print('its not a palindrome : D')

########################################################################
