'''
Guessing Game:
'''

from random import shuffle

#Required functions:
def shuffle_list(mylist):
	shuffle(mylist)

def ask_guess():
	choice = int(input("Enter a number (0,1 or 2): "))
	
	while choice > 2:
		print("Invalid input!")
		choice = int(input("Enter a number (0,1 or 2): "))
	else:
		return choice

def check_guess(mylist,choice):
	if mylist[choice] == 'O':
		print('Correct!!!')
	else:
		print('Wrong!!!')
		print(mylist)

#Main functions:
if __name__ == '__main__':
	
	mylist = [' ',' ','O']
	game_on = True
	print("Welcome to the Game")
	
	while game_on:
		print(mylist)
		shuffle_list(mylist)
		guess = ask_guess()
		check_guess(mylist,guess)
		choice = input("Do you want to continue? Y or N: ").lower()
		if choice == 'y':
			pass
		elif choice == 'n':
			game_on = False
			print('Goodbye')
		else:
			print('Invalid input')