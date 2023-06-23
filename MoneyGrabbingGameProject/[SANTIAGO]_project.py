'''
James Angelo L. Santiago
January 11, 2022 2:00 AM

CMSC 12 Project: Money-Grabbing Game
'''

import random
import time

def mainmenu():
	print("[1] Start New Game")
	print("[2] View High Score")
	print("[3] Load Saved Game")
	print("[0] Exit")

def controls():
	print("[w] Up")
	print("[s] Down")
	print("[a] Left")
	print("[d] Right")
	print("[e] Save and Exit")
	print("[q] Quit without saving")

#Function: Saving the data of a game
def savegame():
	gamesaved = open("gamesaved.txt","w")
	gamesaved.write(str(playername) + ":" + str(coincollected) + ":" + str(savedtime) + ":" + str(crocX) + ":" + str(crocY) + ":" + "\n")
	gamesaved.close()
	return gamesaved

#Function: Saving the board state of a game
def saveboard():
	boardsaved = open("boardsaved.txt", "w")
	boardsaved.write(str(board))
	boardsaved.close()
	return boardsaved

#Function: Saving the scores in a file
def savescores():
	gamescores = open("gamescores.txt","a")
	gamescores.write(str(playername) + ":" + str(score) + ":" + "\n")
	gamescores.close()
	print()
	return gamescores

#Function: Loading the scores from a file into the scores list
def loadscores():
	gamescores = open("gamescores.txt","r")
	for line in gamescores:
		data = line[0:-1].split(":")
		playername = data[0]
		score = data[1]
		gamerecords[float(score)] = playername
	gamescores.close()
	return gamescores

#Variables to be used
croc = "C"
coin = "O"
board = []
crocX = 0
crocY = 0
playername = " "
coincounter = 0
coincollected = 0
score = 0
savedtime = 0
scores = []
gamerecords = {}

print("\n" + "Welcome to the Money-Grabbing Game!!!")
print("You will play as Croc, a crocodile that loves money!")

while True:
	mainmenu()
	command = input("Please enter one of the above options: ")
	print()

	if command == "1":
		board = [["-" for x in range(0,20)] for y in range(0,10)]
		crocX = random.randint(0,19)
		crocY = random.randint(0,9)
		board[crocY][crocX] = croc
		coincounter = 0
		coincollected = 0 

		playername = input("Please enter your name: ")
		start = time.perf_counter()

		while coincounter < 10:
			coinX = random.randint(0,19)
			coinY = random.randint(0,9)
			if board[coinY][coinX] != croc:
				if board[coinY][coinX] != coin:
					board[coinY][coinX] = coin
					coincounter = coincounter + 1

		while coincollected < 10:
			print("Player:",playername)
			print("=== Coins Collected:",coincollected,"===")
			for i in board:
				print(*i, sep = " ") 

			controls()
			command = input("Please enter one of the above options: ")
			print()

			if command == "w":
				board[crocY][crocX] = "-"
				crocY = crocY - 1
				if board[crocY][crocX] == coin:
					coincollected = coincollected + 1
				board[crocY][crocX] = "C"
			elif command == "s":
				board[crocY][crocX] = "-"
				crocY = crocY + 1
				if board[crocY][crocX] == coin:
					coincollected = coincollected + 1
				board[crocY][crocX] = "C"
			elif command == "a":
				board[crocY][crocX] = "-"
				crocX = crocX - 1
				if board[crocY][crocX] == coin:
					coincollected = coincollected + 1
				board[crocY][crocX] = "C"
			elif command == "d":
				board[crocY][crocX] = "-"
				crocX = crocX + 1
				if board[crocY][crocX] == coin:
					coincollected = coincollected + 1
				board[crocY][crocX] = "C"
			elif command == "q":
				break
			elif command == "e":
				end = time.perf_counter()
				savedtime = round(float(end - start),2)
				print("Time:",savedtime,"seconds")
				print("All data have been saved!" + "\n")
				saveboard()
				savegame()
				break
			else:
				print("Invalid input!" + "\n")
				continue
			print()

		if coincollected == 10:
			print("=== Coins Collected:",coincollected,"===")
			for i in board:
				print(*i, sep = " ") 
			end = time.perf_counter()
			score = round(float(end - start),2)
			print("Time:",score,"sec/s")
			scores.append(score)
			savescores()

	elif command == "2":
		loadscores()
		if len(gamerecords) == 0:						#checking if there are scores that are recorded
			print("There are no scores yet!" + "\n")
			continue
		else:
			scores.clear()
			for keys in gamerecords:
				scores.append(float(keys))
				scores.sort()

			n = 1
			print("Highscores:")
			for i in scores[0:10]:
				print("Rank",n,":",gamerecords[i],"(",i,"sec/s )")
				n = n + 1
			print()

	elif command == "3":
		boardsaved = open("boardsaved.txt","r")
		board = boardsaved.read()							#checking if there is a saved game/board state
		boardsaved.close()
		if len(board) == 0:
			print("There is no saved game to load!" + "\n")
		else:
			boardsaved = open("boardsaved.txt","r")
			board = eval(boardsaved.read()) 		#used eval() function to load the list and preserve/convert it into the original list used for the board.
			boardsaved.close()
			gamesaved = open("gamesaved.txt","r")
			for line in gamesaved:
				gamedata = line[0:-1].split(":")
				playername = gamedata[0]
				coincollected = int(gamedata[1])
				savedtime = float(gamedata[2])
				crocX = int(gamedata[3])
				crocY = int(gamedata[4])
				board[crocY][crocX] = croc
			gamesaved.close()

			start = time.perf_counter()
			while coincollected < 10:
				print("Player:",playername)
				print("=== Coins Collected:",coincollected,"===")
				for i in board:
					print(*i, sep = " ") 

				controls()
				command = input("Please enter one of the above options: ")
				print()

				if command == "w":
					board[crocY][crocX] = "-"
					crocY = crocY - 1
					if board[crocY][crocX] == coin:
						coincollected = coincollected + 1
					board[crocY][crocX] = "C"
				elif command == "s":
					board[crocY][crocX] = "-"
					crocY = crocY + 1
					if board[crocY][crocX] == coin:
						coincollected = coincollected + 1
					board[crocY][crocX] = "C"
				elif command == "a":
					board[crocY][crocX] = "-"
					crocX = crocX - 1
					if board[crocY][crocX] == coin:
						coincollected = coincollected + 1
					board[crocY][crocX] = "C"
				elif command == "d":
					board[crocY][crocX] = "-"
					crocX = crocX + 1
					if board[crocY][crocX] == coin:
						coincollected = coincollected + 1
					board[crocY][crocX] = "C"
				elif command == "q":
					break
				elif command == "e":
					end = time.perf_counter()
					savedtime = round(float((end - start) + savedtime),2)
					print("Time:",savedtime,"seconds")
					print("All data have been saved!" + "\n")
					savegame()
					saveboard()
					break
				else:
					print("Invalid input!" + "\n")
					continue

			if coincollected == 10:
				print("=== Coins Collected:",coincollected,"===")
				for i in board:
					print(*i, sep = " ") 
				end = time.perf_counter()
				score = round(float((end - start) + savedtime),2) 
				print("Time:",score,"sec/s")
				scores.append(score)
				savescores()
				gamesaved = open("gamesaved.txt","w")
				gamesaved.truncate(0)
				gamesaved.close()
				boardsaved = open("boardsaved.txt","w")
				boardsaved.truncate(0)
				boardsaved.close()

	elif command == "0":
		print("Thank you for playing! Have a nice day!" + "\n")
		break			

	else:
		print("Invalid input!" + "\n")
	
'''
References:
For the board, it was inspired from C0nti's youtube tutorial video.
	link: https://www.youtube.com/watch?v=JnujQxAqAIM

For better understanding of Python File methods such as truncate(), I read at:
	links: https://www.w3schools.com/python/python_ref_file.asp
		  https://www.w3schools.com/python/ref_file_truncate.asp

For better understanding of the time module, specifically time.perf_counter(), I read at:
	link: https://www.geeksforgeeks.org/time-perf_counter-function-in-python/

For better understanding of the random module, I read at:
	link: https://www.w3schools.com/python/ref_random_randint.asp

For better understanding of the eval() function, I read at:
	links: https://www.geeksforgeeks.org/eval-in-python/
		   https://realpython.com/python-eval-function/

For printing a list without the brackets, I learned at:
	link: https://www.kite.com/python/answers/how-to-print-a-list-without-brackets-in-python

For rounding of a float to certain decimal places, I learned at:
	link: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
'''