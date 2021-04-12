import random
import os

lines = open("./words.txt").read()
line = lines[0:]
words = line.split()

hWord = random.choice(words)
faults = 0


def status(guessDict, faults, guessedLetters):
	print("\n\n-----------------------\n\n")

	position = 1
	gGuessCount = 0

	if faults == 6:
		print("You have lost")
		print("\nThe word was:", hWord)
		exit()

	for letter in hWord:
		if guessDict[position] == "guessed":
			print(letter, end="")
			gGuessCount += 1
		else:
			print("_", end="")

		position += 1

	if gGuessCount == len(hWord):
		print("\n\nYou have won")
		exit()
	else:
		print("\n\nLetters: ", len(hWord))
		print("\nYou have", faults, "faults.", (6 - faults), "guesses remain.")
		print("\n\nGuessed letters: ", end="")
		for letter in "abcdefghijklmnopqrstuvwxyz":
			if guessedLetters[letter] == "yes":
				print(letter, end=", ")



def guess(faults, guessDict, guessedLetters):
	gLetter = input("\n\n\nGuess a letter: ")
	position = 1
	goodGuess = False

	if len(gLetter) != 1:
		print("\n\nGuess must be 1 letter")
		status(guessDict, faults, guessedLetters)
		return guess(faults, guessDict, guessedLetters)

	if gLetter == "" or gLetter == " ":
		print("\n\nCan't take empty guess")
		status(guessDict, faults, guessedLetters)
		return guess(faults, guessDict, guessedLetters)

	if guessedLetters[gLetter] == "yes":
		print("\n\nYou already guessed this letter")
		status(guessDict, faults, guessedLetters)
		return guess(faults, guessDict, guessedLetters)

	for letter in hWord:
		if letter == gLetter:
			guessDict[position] = "guessed"
			goodGuess = True

		position += 1
		
	if goodGuess == False:
			faults += 1

	guessedLetters[gLetter] = "yes"
	
	status(guessDict, faults, guessedLetters)
	guess(faults, guessDict, guessedLetters)

	# Output for testing
	# print(faults)
	# print(guessDict)


def gameStart():
	faults = 0
	guessDict = {}
	position = 1
	guessedLetters = {}

	for letter in "abcdefghijklmnopqrstuvwxyz":
		guessedLetters[letter] = "no"

	for letter in hWord:
		print("_", end="")
		guessDict[position] = "hidden"
		position += 1
	print("\n\nLetters: ", len(hWord))

	guess(faults, guessDict, guessedLetters)


gameStart()