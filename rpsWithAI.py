'''Best 2 out of 3 rock papers scissors against AI'''

from random import randint
computer_wins = 0
player_wins = 0

while computer_wins < 2 and player_wins < 2:
	print(f"player_wins: {player_wins} Computer wins: {computer_wins} ")
	player = input("Enter rock, paper, or scissors: ").lower()
	rand_num = randint(0,2) 
	if rand_num == 0:
		computer = "rock"
	elif rand_num == 1:
		computer = "paper"
	else:
		computer = "scissors"
	print(f"The computer picked {computer}")
	if player == computer:
		print("Its a tie")
	elif player == "rock" and computer == "scissors":
		print("player wins")
		player_wins += 1
	elif player == "scissors" and computer == "paper":
		print("player wins")
		player_wins += 1
	elif player == "paper" and computer == "rock":
		print("player wins")
		player_wins += 1
	else:
		print("computer wins")
		computer_wins += 1
print(f"final score: PLAYER: {player_wins} COMPUTER: {computer_wins}")