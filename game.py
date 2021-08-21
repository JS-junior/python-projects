import math
import time
import  random

def main(user_move, comp_move):
	if user_move == comp_move:
		print('Its a tie')
	elif user_move == 'r':
		if comp_move == 's':
			print('You won the game!')
		elif comp_move == 'p':
			print('Computer won the game!')
	elif user_move == 'p':
			if comp_move == 'r':
				print('You won the game!')
			elif comp_move == 's':
				print('Computer won the game')
	elif user_move == 's':
			if comp_move == 'p':
				print('You won the game')
			elif comp_move == 'r':
				print('Computer won the game')
				
	time.sleep(0.5)
	print('--------------------------')
	cmd = input('Type quit to exit and start to restart\n')
	if cmd == 'quit':
			print('')
	elif cmd == 'start':
			rps_game()
			
def rps_game():
	time.sleep(1)
	print('-------------------------')
	print('Welcome to the game!')
	print('-------------------------')
	time.sleep(1)
	print('okay so lets begin')
	time.sleep(1)
	print('-------------------------')
	choice = input('Type r for rock, p for paper, s for scissor \n')
	outcomes = ['r', 'p', 's']
	comp_choice = random.choice(outcomes)
	print(f'You choosed {choice}')
	time.sleep(1)
	print(f'computer choosed {comp_choice}')
	time.sleep(1)
	main(choice, comp_choice)
	
if __name__ == '__main__':
	rps_game()