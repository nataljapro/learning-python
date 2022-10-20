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

            elif p_move == 'rock':
                if computor_move_str == 'paper':
                    print('paper beats rock, i win hehe')
                    computor_points += 1
                    game_count += 1

                elif computor_move_str == 'scissors':
                    print('rock beats scissors, ' + p_name + ', you win this turn! :)')
                    p_points += 1
                    game_count += 1

            elif p_move == 'paper':
                if computor_move_str == 'rock':
                    print('paper beats rock, ' + p_name + ', you win this turn! :)')
                    p_points += 1
                    game_count += 1

                elif computor_move_str == 'scissors':
                    print('scissors beat paper, i win haha')
                    computor_points += 1
                    game_count += 1

            elif p_move == 'scissors':
                if computor_move_str == 'paper':
                    print('scissors beats paper, ' + p_name + ', you win this turn!! :)')
                    p_points += 1
                    game_count += 1

                elif computor_move_str == 'rock':
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

            elif p1_move == 'rock':
                if p2_move == 'paper':
                    print('paper beats rock, ' + p2_name + ', you win this turn! :)')
                    p2_points += 1
                    game_count += 1

                elif p2_move == 'scissors':
                    print('rock beats scissors, ' + p1_name + ', you win this turn! :)')
                    p1_points += 1
                    game_count += 1

            elif p1_move == 'paper':
                if p2_move == 'rock':
                    print('paper beats rock, ' + p1_name + ', you win this turn! :)')
                    p1_points += 1
                    game_count += 1

                elif p2_move == 'scissors':
                    print('scissors beat paper, ' + p2_name + ', you win this turn! :)')
                    p2_points += 1
                    game_count += 1

            elif p1_move == 'scissors':
                if p2_move == 'paper':
                    print('scissors beats paper, ' + p1_name + ', you win this turn!! :)')
                    p1_points += 1
                    game_count += 1

                elif p2_move == 'rock':
                    print('rock beats scissors, ' + p2_name + ', you win this turn! :)')
                    p2_points += 1
                    game_count += 1

            if p1_points == p2_points:
                print('wow, its a tie :-) congratulations to you both!!')

            elif p1_points > p2_points:
                print(p1_name + ', you win!!! congrats!!!! :3')

            elif p2_points > p1_points:
                print(p2_name + ', you win!! congrats!!!! :3')

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