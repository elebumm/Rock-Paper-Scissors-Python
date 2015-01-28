import time
import random

hands = ['rock', 'paper', 'scissors']


def gamePhase():
	selection = True
	while selection == True:
		userInput = raw_input("Rock, Paper or Scissors? ")
		if userInput.lower() == "rock" or userInput.lower() == "paper" or userInput .lower() == "scissors":
			print("good job!")
			computerChoice = random.choice(hands)
			print("Results in 3...")
			time.sleep(1)
			print("Results in 2...")
			time.sleep(1)
			print("Results in 1...")
			time.sleep(1)
			if userInput.lower() == computerChoice:
				print("It's a tie game! Your choice: " + userInput + " The Computers choice: " + computerChoice)
				time.sleep(3)
				ask = raw_input("Would you like to play again? y/n")
				if ask == 'y':
					gamePhase()
				elif ask == 'n':
					selection = False
			elif userInput.lower() == 'rock' and computerChoice == 'scissors':
				print("You win! Your choice: " + userInput + " The Computers choice: " + computerChoice)
				time.sleep(3)
				ask = raw_input("Would you like to play again? y/n")
				if ask == 'y':
					gamePhase()
				elif ask == 'n':
					selection = False
			elif userInput.lower() == 'rock' and computerChoice == 'paper':
				print("You lose! Your choice: " + userInput + " The Computers choice: " + computerChoice)
				time.sleep(3)
				ask = raw_input("Would you like to play again? y/n")
				if ask == 'y':
					gamePhase()
				elif ask == 'n':
					selection = False
			elif userInput.lower() == 'paper' and computerChoice == 'rock':
				print("You win! Your choice: " + userInput + " The Computers choice: " + computerChoice)
				time.sleep(3)
				ask = raw_input("Would you like to play again? y/n")
				if ask == 'y':
					gamePhase()
				elif ask == 'n':
					selection = False
			elif userInput.lower() == 'paper' and computerChoice == 'scissors':
				print("You lose! Your choice: " + userInput + " The Computers choice: " + computerChoice)
				time.sleep(3)
				ask = raw_input("Would you like to play again? y/n")
				if ask == 'y':
					gamePhase()
				elif ask == 'n':
					selection = False
			elif userInput.lower() == 'scissors' and computerChoice == 'rock':
				print("You lose! Your choice: " + userInput + " The Computers choice: " + computerChoice)
				time.sleep(3)
				ask = raw_input("Would you like to play again? y/n")
				if ask == 'y':
					gamePhase()
				elif ask == 'n':
					selection = False
			elif userInput.lower() == 'scissors' and computerChoice == 'paper':
				print("You win! Your choice: " + userInput + " The Computers choice: " + computerChoice)
				time.sleep(3)
				ask = raw_input("Would you like to play again? y/n")
				if ask == 'y':
					gamePhase()
				elif ask == 'n':
					selection = False



gamePhase()










