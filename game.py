import math
import pyqrcode
import time
import string
from forex_python.converter import  CurrencyRates
from colorama import Fore, Back
from gtts import gTTS
from colorama import Back, Fore
import  random
import  jwt

master_key = "SECRET"
price_list = []
c = CurrencyRates()

hangman_words = ['python', 'mathematics', 'vectors', 'matrices', 'javascript', 'react', 'netflix']

def main():
	inp = input('Choose what to do \n 1) Rock, paper, scissor \n 2) Password manager  \n 3) Qr code \n 4) Hangman \n 5) Text to audio \n 6) Expense tracker \n Type your choice : ')
	
	if inp == '1':
		rps_game()
	elif inp == '2':
		pass_manage()
	elif inp == '3':
		genqr()
	elif inp == '4':
		hangman()
	elif inp == '5':
		txt_audio()
	elif inp == '6':
		expense()
	else:
			print('Restarting program')
			time.sleep(1)
			print('.......')
			time.sleep(1)
			print('..............')
			time.sleep(1)
			main()
			

def expense():
	print(Fore.BLACK + Back.YELLOW + "--------------Expense tracker------------- \n")
	inp = input(Fore.GREEN + Back.BLACK + " 1) Add to list \n 2) View list \n 3) Find total \n choose your input: ")
	if inp == '1':
		name = input('name: ')
		price = input('price: ')
		currency = input('currency: ')
		with open('expense.txt', 'a') as f:
			f.write(name + '|' + str(price) + '|' + currency + '\n')
		main()
			
	elif inp == '2':
		with open('expense.txt', 'r') as f:
			for line in f.readlines():
				data = line.rstrip()
				name, price, currency = data.split('|')
				print(name, ':', str(price))
				r = c.convert(currency, "USD", int(price))
				price_list.append(int(r))
			
		total = sum(price_list)
		print("\n Your total expense is $",total, '\n')
		main()
				
	elif inp == '3':
		with open('expense.txt', 'r') as f:
			for line in f.readlines():
				data = line.rstrip()
				name, price, currency = data.split('|')
				print(name, ':', str(price))
				r = c.convert(currency, "USD", int(price))
				price_list.append(int(r))
			
		total = sum(price_list)
		print("\n Your total expense is $",total,'\n')
		
		line_num = input('Type the line to delete: ')
		with open("expense.txt", "r") as infile:
		  lines = infile.readlines()
		  
		  with open("expense.txt", "w") as outfile:
		          	for pos, line in enumerate(lines):
		          		print(pos)
		          		if pos != line_num:
		          			outfile.write(line)
		          			expense()


def genqr():
		data = input('Put some data')
		qr = pyqrcode.create(data)
		qr.svg('qr_code.svg', scale = 8)
		print(qr)
		main()
		
def txt_audio():
		audio = "hello.mp3"
		sp = gTTS(text="Hello world",lang="en", slow=False)
		sp.save(audio)
		
		
def hangman():
		print('------------Hangman---------------')
		time.sleep(1)
		print('ready?')
		time.sleep(1)
		for i in range(3):
			print(str(i+1) + '\n')
			time.sleep(1)
		print('Go!')
		word = random.choice(hangman_words)
		word_letters = set(word)
		used_letters = set()
		while len(word_letters)> 0:
			print('used letters: ' + ' '.join(used_letters))
			word_list = [letter if letter in used_letters else  '_'  for letter in word]
			print('Current word : ', ' '.join(word_list))
			user_letter = input('guess the word : ').lower()
			if user_letter not in used_letters:
				used_letters.add(user_letter)
				if user_letter in word_letters:
					word_letters.remove(user_letter)
			elif user_letter in used_letters:
				print('You have already used that character')
				
		print(f'You nailed it man, Your word was {word}')
		
		
		
def pass_manage():
	print('-------------------------------')
	print('----password-manager-----')
	print('-------------------------------')
	time.sleep(1)
	mas_key = input('login as root user: ')
	if mas_key == master_key:
		print("welcome back chief")
	else:
		print("something went wrong, try again")
	time.sleep(1)
	inp = input('1) View all password \n2) add new one\n3) delete account :')
	if inp == '1':
		view_all_pass()
	elif inp == '2':
		add_pass()
	elif inp == '3':
		delete_pass()
	else:
		order = input('Type quit to exit and start to restart')
		if order == 'quit':
			print('')
		elif order == 'start':
			main()
		else:
			print('Restarting program')
			time.sleep(1)
			print('.......')
			time.sleep(1)
			print('..............')
			time.sleep(1)
			main()
			

def view_all_pass():
	with open('password.txt', 'r') as f:
		for line in f.readlines():
			data = line.rstrip()
			acc, pwd = data.split('|')
			name = jwt.decode(acc, master_key, algorithms=["HS256"])
			pswd = jwt.decode(pwd, master_key, algorithms=["HS256"])
			print(name, pswd)
			print(name, ':', pswd)
			pass_manage()
	
def add_pass():
	name = input('what is your account name: ')
	pwd = input('password: ')
	
	acc = jwt.encode({"name": name }, master_key, algorithm="HS256")
	
	pswd = jwt.encode({"name": pwd }, master_key, algorithm="HS256")
	print(acc, pswd)
	with open('password.txt', 'w') as f:
		f.write(acc + '|' + pswd + '\n')
		print('password saved successfully')
		pass_manage()
	
def delete_pass():
	return
	
	
def rps(user_move, comp_move):
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
	cmd = input('Type quit to exit and start to restart or back to menu \n')
	if cmd == 'quit':
			print('')
	elif cmd == 'start':
			rps_game()
	elif cmd == 'back':
			main()
	else:
			print('Restarting program')
			time.sleep(1)
			print('.......')
			time.sleep(1)
			print('..............')
			main()
			
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
	rps(choice, comp_choice)
	
if __name__ == '__main__':
	print(Fore.GREEN + 'python projects')
	
	main()
