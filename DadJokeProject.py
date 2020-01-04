''' This program collects jokes from a website using json.
Then, gets user input for a topic. It displays how many jokes
of that topic were found. Finally, it picks a joke at random and displays
it to the user'''
from pyfiglet import figlet_format
from colorama import init
from termcolor import colored
import requests
from random import choice
init()

# intro message
msg = "Lame Dad Jokes"
title1 = figlet_format(msg)
msg1 = colored(title1, color="cyan")
print(msg1)

topic = input("What would you like to search for?: ")
url = "https://icanhazdadjoke.com/search"
response = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": topic}
    ).json()
num_jokes = response["total_jokes"]
results = response["results"]
if num_jokes > 1:
	print(f"I found {num_jokes} jokes about {topic}. heres one:")
	print(choice(results)["joke"])
elif num_jokes == 1:
	print(f"I found one joke about your topic: {topic}")
	print(results[0]["joke"])
else:
	print(f"Sorry, couldn't find a joke with that topic: {topic}")