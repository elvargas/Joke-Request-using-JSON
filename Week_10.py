# Assignment 10
#Eric Vargas
# Description: This program will ask the user if they would like to hear a Chuck Norris joke. Depending on the users answer
# data will be requested from the URL. The program will continue to prompt the user if they'd like to hear a joke until
# the user enters "No".

import json
import requests


print("-------- Welcome --------\n")
while True:
    print("\nWould you like to hear a Chuck Norris joke?")
    user_input = input('Yes/No: ')
    if user_input == 'yes':

        # Requests joke from URL
        url = requests.get('https://api.chucknorris.io/jokes/random')
        data = json.loads(url.text)

        # Prints a joke
        print(data["value"])
    elif user_input == 'no':
        print('The program has ended')
        break # breaks the program if No is entered as response
    else:
        # If user enters any characters beside Yes or No, will be re-prompted to enter correct response.
        print("Invalid Response.....Enter Yes or No")


