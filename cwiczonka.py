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
