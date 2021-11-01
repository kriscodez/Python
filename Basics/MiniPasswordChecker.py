'''
Author: Kresteanna
Date: 07/25/2021

Purpose: practicing conditionals by creating a little program that checks passwords
'''

password = "blue"
guess_correct = False

while not guess_correct:
    user_guess = input("Please enter the password: ")
    if user_guess == password:
        print("you guessed correctly")
        guess_correct = True
    else:
        print("Please try again")
