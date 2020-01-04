'''This project uses beautifulsoup to scrape quotes from a website
and picks one at random. Then creates a game with 4 guesses and the user
has to guess the name of the person who said the quote. After each
wrong guess the program gives a hint to the user. At the end it gives
the name of the person. Finally, it asks the user if they want to play again
'''

import requests
from bs4 import BeautifulSoup
from csv import DictReader
from random import choice

BASE_URL = "http://quotes.toscrape.com"
filename= "scraped_quotes.csv"
def read_quotes(filename):
	with open(filename, "r") as file:
		csv_reader = DictReader(file)
		return list(csv_reader)

def start_game(quotes):	
	quote = choice(quotes)
	print("Here's a quote: ")
	print(quote["text"])
	guess = ''
	remaining_guesses = 4
	while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
		guess = input(f"Who said this quote? Guesses remaining: {remaining_guesses}   ")
		if guess.lower() == quote["author"].lower():
			print("You guessed right!")
			break
		remaining_guesses -= 1
		if remaining_guesses == 3:
			res = requests.get(f"{BASE_URL}{quote['bio_link']}")
			soup = BeautifulSoup(res.text, "html.parser")
			birth_date = soup.find(class_="author-born-date").get_text()
			birth_place = soup.find(class_="author-born-location").get_text()
			print(f"Here's a hint: The author was born on {birth_date} {birth_place}")
		elif remaining_guesses == 2:
			print(f"Here's a hint: The author's first name starts with {quote['author'][0]}")
		elif remaining_guesses == 1:
			last_initial = quote["author"].split(" ")[1][0]
			print(f"Here's a hint: The author's last name starts with {last_initial}")
		else:
			print(f"You have no guesses remaining. The author was {quote['author']}")		
	
	again = ''
	while again.lower() not in ('y', 'yes', 'n', 'no'):
		again = input("Would you like to play again? (Y/N) ")
	if again.lower() in ('yes', 'y'):
		print("OK starting new game")
		return start_game(quotes)
	else:
		print("OK, Goodbye")

quotes = read_quotes("scraped_quotes.csv")
start_game(quotes)