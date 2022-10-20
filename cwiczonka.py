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
'''Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 
36, 49, 64, 81, 100]. Write one line of Python that takes this list a and 
makes a new list that has only the even elements of this list in it.'''

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# c = []
# for item in a:
#     if item % 2 == 0:
#         c.append(item)
# print(c)

########################################################################

import random

print('hi this is two-players rock-paper-scissors game')
option = input('type "start" to start the game or "exit" to exit the game :) ')
game_count = 0
max_count = 3
computor_points = 0
p_points = 0
p1_points = 0
p2_points = 0
if option == 'start':
    print('do you have a friend or do you want to play with me, a computor >:D?')
    game_choice = input('type "1" if you want to play with me or "2" if you have a friend to play ')
    if game_choice == '1':
        p_name = input('whats your name? ')
        while game_count < max_count:
            p_move = input(p_name + ', its your turn - type "rock", "paper" or "scissors": ')
            print('ok now its my turn hehe....')
            computor_move = random.randint(0, 2)
            # computor moves:
            if computor_move == 0:
                computor_move_str = 'rock'
            elif computor_move == 1:
                computor_move_str = 'paper'
            elif computor_move == 2:
                computor_move_str = 'scissors'
            print('i say ' + str(computor_move_str) + '!!!!')
            if p_move == computor_move_str:
                print('its a tie!')
                game_count +=1
            if p_move == 'rock':
                if computor_move_str == 'paper':
                    print('paper beats rock, i win hehe')
                    computor_points += 1
                    game_count += 1
                if computor_move_str == 'scissors':
                    print('rock beats scissors, ' + p_name + ', you win this turn! :)')
                    p_points += 1
                    game_count += 1
            if p_move == 'paper':
                if computor_move_str == 'rock':
                    print('paper beats rock, ' + p_name + ', you win this turn! :)')
                    p_points += 1
                    game_count += 1
                if computor_move_str == 'scissors':
                    print('scissors beat paper, i win haha')
                    computor_points += 1
                    game_count += 1
            if p_move == 'scissors':
                if computor_move_str == 'paper':
                    print('scissors beats paper, ' + p_name + ', you win this turn!! :)')
                    p_points += 1
                    game_count += 1
                if computor_move_str == 'rock':
                    print('rock beats scissors, i win hehe :)')
                    computor_points += 1
                    game_count += 1
            computor_move = random.randint(0, 2)
            if game_count == 3:
                if p_points == computor_points:
                    print('wow, its a tie :-) congratulations to you and me hehehe!!')
                elif p_points > computor_points:
                    print(p_name + ', you win!!! congrats!!!! :3')
                elif computor_points > p_points:
                    print('i win congrats to me thanks hihi')
                    new_game = input('do you want to start a new game? y/n ')
                    if new_game == 'y':
                        game_count = 0
                        print('oki lets start a new game: ')
                        continue
                    else:
                        print('oki bye!!')
                        break
    if game_choice == '2':
        p1_name = input('player1 name: ')
        p2_name = input('player2 name: ')
        while game_count < max_count:
            p1_move = input(p1_name + ', its your turn - type "rock", "paper" or "scissors": ')
            p2_move = input(p2_name + ', now its your turn: ')
            if p1_move == p2_move:
                print('its a tie!')
                game_count +=1
            if p1_move == 'rock':
                if p2_move == 'paper':
                    print('paper beats rock, ' + p2_name + ', you win this turn! :)')
                    p2_points += 1
                    game_count += 1
                if p2_move == 'scissors':
                    print('rock beats scissors, ' + p1_name + ', you win this turn! :)')
                    p1_points += 1
                    game_count += 1
            if p1_move == 'paper':
                if p2_move == 'rock':
                    print('paper beats rock, ' + p1_name + ', you win this turn! :)')
                    p1_points += 1
                    game_count += 1
                if p2_move == 'scissors':
                    print('scissors beat paper, ' + p2_name + ', you win this turn! :)')
                    p2_points += 1
                    game_count += 1
            if p1_move == 'scissors':
                if p2_move == 'paper':
                    print('scissors beats paper, ' + p1_name + ', you win this turn!! :)')
                    p1_points += 1
                    game_count += 1
                if p2_move == 'rock':
                    print('rock beats scissors, ' + p2_name + ', you win this turn! :)')
                    p2_points += 1
                    game_count += 1
            if p1_points == p2_points:
                print('wow, its a tie :-) congratulations to you both!!')
                full_game = True
            elif p1_points > p2_points:
                print(p1_name + ', you win!!! congrats!!!! :3')
                full_game = True
            elif p2_points > p1_points:
                print(p2_name + ', you win!! congrats!!!! :3')
                full_game = True
            if game_count == 3:
                new_game = input('do you want to start a new game? y/n ')
                if new_game == 'y':
                    game_count = 0
                    print('oki lets start a new game: ')
                    continue
                else:
                    print('oki bye!!')
                    break
if option == 'exit':
    print('oki bye!! :3')

'''Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays 
(using input), compare them, print out a message of congratulations to the 
winner, and ask if the players want to start a new game)
Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock'''
