import random

def numberGuessing():

	print("Welcome to number guessing game")

	print("Random generation of number between 1 and 100")

	sysNumber = random.randint(1,100)
	attempts = 0
	maxAttempts = 5

	
	while attempts < maxAttempts:
		guessedNumber = int(input("Enter your guess!"))

		attempts += 1 
		#attempts = attempts+1, both incrementals are same

		if(sysNumber == guessedNumber):
			print("Congratulation you guessed the number correctly",sysNumber)
			return

		elif guessedNumber < sysNumber:
			print("Too low, try again")
			print(f"Attempt remaining: {maxAttempts - attempts}")

		else:
			print("Too high, try again")
			print(f"Attempt remaining: {maxAttempts - attempts}")
			

	print(f"Attempt remaining: {maxAttempts - attempts}")

	print("Game over! System number was: ",sysNumber)


numberGuessing()

playAgain = input("Would you like to play again? (y/n)").lower()
while True:
	if (playAgain == 'y'):
		numberGuessing()
	elif (playAgain == 'n'):
		print("Thanks for playing!")
		break
	else:
		print("Please enter y or n.")