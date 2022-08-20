#GAME JOKENPÔ.
from time import sleep
from random import randint
import os

#Colors Bold High Intensity
Black='\033[1;90m'
Red='\033[1;91m'
Green='\033[1;92m'
Yellow='\033[1;93m'
Blue='\033[1;94m'
Purple='\033[1;95m'
Cyan='\033[1;96m'
White='\033[1;97m'
BBlack='\033[1;30m'
BWhite = "\033[1;97;1m"
RESET = "\033[0;0m"

print('\033[1;30;107m* \033[m'*30)
print('{:^73}'.format('\033[1;32;40;1m ROCK PAPER SCISSORS\033[m '))
print('\033[1;30;107m* \033[m'*30)

counter = defeats = victories = draws = 0
defeats2 = Purple +'COMPUTER  WON'+ RESET
victories2 = Purple +'YOU WON'+ RESET
rounds = ' '
rounds = int(input('\nNº OF ROUNDS: '))
rounds +=1
draw = Red +'DRAW'+RESET
draw2 = Cyan +'THE ROUND ENDED IN A DRAW'+RESET

while rounds != 1:
	itens = [Cyan+'ROCK'+RESET, Cyan+'PAPER'+RESET, Cyan+'SCISSORS'+RESET]
	pc = randint(0,2)
	counter += 1
	rounds -= 1
	print('REMAINING ROUNDS: %i'%rounds)
	print(Green + '=='*30 + RESET)
	print(BBlack +'''YOUR OPTIONS:
[0] Rock
[1] Paper
[2] Scissors'''+RESET)
	player = int(input(BWhite +'Whats your move? ' + RESET))
	os.system('cls||clear')

	while player > 2:
		sleep(0.5)
		print(Red + '\nInvalid Option, TRY AGAIN!' + RESET)
		print(Cyan + '=='*30 + RESET)
		print(BBlack +'''\nYOUR OPTIONS:
[0] Rock
[1] Paper
[2] Scissors'''+RESET)
		player = int(input(BWhite+'Whats your move? '+ RESET))
	os.system('cls||clear')

	print('\033[1;30;107m* \033[m'*30)
	print('{:^73}'.format('\033[1;32;40;1m ROCK PAPER SCISSORS\033[m '))
	print('\033[1;30;107m* \033[m'*30)
	print('')
	print (Yellow +'          #########    ####')
	print('              ##     ##    ##')
	print('              ##     ##    ##')
	print('              ##     ##    ##')
	print('              ##     ##    ##')
	print('         ##   ##     ##    ##')
	print('         ##   ##     ##    ##')
	print('           ###         ####' + RESET)
	sleep(1)

	print ("")
	print ("")

	print(Red+'    ##   ##    ########    ###     ##')
	print('    ## ##      ##          ###     ##')
	print('    ###        ###         ## #    ##')
	print('    ##         ######      ##  #   ##')
	print('    ###        ###         ##   #  ##')
	print('    ## ##      ##          ##    # ##')
	print('    ##   ##    ########    ##     ###'+RESET)
	sleep(1)

	print ("")
	print ("")

	print(Cyan+'         ######         ####      ##')
	print('         ##    ##     ##    ##    ##')
	print('         ##     ##    ##    ##    ##')
	print('         ##    ##     ##    ##    ##')
	print('         ######       ##    ##    ##')
	print('         ##           ##    ##    ##')
	print('         ##           ##    ##')
	print('         ##             ####      ##'+RESET)
	sleep(1)
	
	os.system('cls||clear')
	print('\033[1;30;107m* \033[m'*30)
	print('{:^73}'.format('\033[1;32;40;1m ROCK PAPER SCISSORS\033[m '))
	print('\033[1;30;107m* \033[m'*30)
	print(Green + '=='*30 + RESET)
	print(f'COMPUTER Played: {itens[pc]}')
	print(f'YOU Played: {itens[player]}')
	if pc == 0:
		if player == 0:
			draws += 1
			print(draw)
		elif player == 1:
			victories += 1
			print(victories2)
			print('paper covers the stone')
			print(Green + '=='*30 + RESET)
		elif player == 2:
			defeats += 1
			print ("")
			print(defeats2)
			print('stone break scissors')
			print(Green + '=='*30 + RESET)
	elif pc == 1:
		if player == 1:
			draws += 1
			print(draw)
		elif player == 0:
			defeats += 1
			print ("")
			print(defeats2)
			print('paper covers the stone')
			print(Green + '=='*30 + RESET)
		elif player == 2:
			victories += 1
			print ("")
			print(victories2)
			print('scissors cut paper')
			print(Green + '=='*30 + RESET)
	elif pc == 2:
		if player == 2:
			draws += 1
			print(draw)
		elif player == 0:
			victories += 1
			print ("")
			print(victories2)
			print('stone break scissors')
			print(Green + '=='*30 + RESET)
		elif player == 1:
			defeats += 1
			print ("")
			print(defeats2)
			print('scissors cut paper')
			print(Green + '=='*30 + RESET)
		
if victories > defeats:
	print(' ')
	print(Yellow + '=='*30 + RESET)
	print(Blue + 'YOU WON THE ROUND...' + RESET)
	print('TIMES PLAYED: %i'%counter)
	print(Yellow + '=='*30 + RESET)
elif victories == defeats:
	print(f'\n{draw2}')
else:
	print(' ')
	print(Yellow + '=='*30 + RESET)
	print(Blue + 'THE COMPUTER WON THE ROUND...' + RESET)
	print('TIMES PLAYED: %i'%counter)
	print(Yellow + '=='*30 + RESET)

print('\nFINAL SCORE:')
print('\nCOMPUTER: %i'%defeats)
print('YOU: %i'%victories)
print('DRAWS: %i'%draws)
print(f'\n{" END GAME ":=^60}')