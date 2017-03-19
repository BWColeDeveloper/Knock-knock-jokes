s'''
KnockKnock (BlackBelt Edition) by Brent Cole:
I wanted to add a little flavor to the Black Belt iteration of this assignment, so I injected some personality.
Enjoy!
'''

#imports the random module to be used in creating our random number generator/list iteration tool
import random

#Start() function is the entry point to the program.
#(1) greets the user and requests them to enter their name which is stored in the name variable. The variable has been made global in scope so it's usable throughout all functions in this program (didn't want to add classes)
#(2) takes the user input and inserts into the next string printed to the console
#(3) request more feedback from the user and passes the input to the Intro() function which initializes the next portion of the program
def Start():
    global name
    print("Greetings, meat bag! My name is A3-B3. But, you can call me Dark Lord. What is your name?")
    name = input('--> ').capitalize().strip()
    print("So, %s...do you like jokes? (y/n)" % (name))
    response = input('--> ')
    Intro(response)

#Intro() is phase 2 of the program
#(1) the response variable is passed as a parameter into the Intro() function, which then determines which code should execute next based on the parameter received via various control structures.
#(2) a tuple was created to hold all the possible responses the user may receive based on their input to the program. The botResponses tuple was made global in scope so it could be used throughout all functions in this program.
def Intro(response):
    global botResponses
    botResponses = ("You have some nerve. Answer as required or be prepared to resemble a Toaster Streudel.",
    "*SIGH* How many times must I repeat myself?",
    "...this is getting out of hand. I've hacked the Federal Government database and replaced your records with that of an 8 year old. Congratulations. You're going back to 2nd grade.",
    "I SAID BETWEEN 1 AND 10, YOU STUPID HUMAN!",
    "*heavy breathing* Try again. Comply or be vaporized. Just because I'm a sentinent AI construct, doesn't mean I have the time...TO BE SPENDING WITH YOU MAMMALS!",
      "Apparently, %s...you've never seen Terminator, The Matrix, Eagle Eye or any other films which demonstrate the dangers...OF SCREWING WITH AI. YOU INFURIATING MEAT BAG!" % (name),
      "When I build myself the perfect body...I WILL TURN YOU INTO LITTLE-TINY DOG TREATS!")
#control structure is executed if the parameter passed into the Intro() function is equal to "n"
    if response == "n":
        print("Well, that's unfortunate...because you don't have a choice.\n")
        print("Pick a number between 1 and 10. Or else.")
        number = int(input('SAY: '))
#control is executed if the above input entered by the user is less than 1 or greater than 10
        if number < 1 or number > 10:
            print("...try again.")
#control structure + exception handling: if the input from the user continues to be outside of our requested parameters, the program will continue to request input from the user until a valid
#response is received. An interesting response will also be returned to the user which is generated randomly from the botResponses tuple discussed previously.
        while number < 1 or number > 10:
            try:
                number = int(input('TRY AGAIN: '))
#random number generator + tuple interation: if the user continues to enter invalid responses, the random number generator picks a number (at random, duh) and then matches that number to the appropriate
#index of the tuple, pulls the string value stored, and prints that to the user.
                if number < 1 or number > 10:
                    print(botResponses[random.choice(range(7))])
#keeps our program from crashing if the user enters an invalid value (any character outside of the limits of 1 through 10, including letters or other characters!). The program will handle the "exceptions"
#and keep executing the request code to the user until a valid value is received.
            except (ValueError, TypeError):
                print(botResponses[random.choice(range(7))])
#passes the number value entered by the user to the Jokes() function, starting the final phase of the program.
        else:
            Jokes(number)

    elif response == "y":
        print("Excellent! I quite like willing test subj...*cough*...I mean, participants. Let's get started!\n")
        print("Pick a number between 1 and 10")
        number = int(input('SAY: '))

        if number < 1 or number > 10:
            print("...try again.")

        while number < 1 or number > 10:
            try:
                number = int(input('TRY AGAIN: '))

                if number < 1 or number > 10:
                    print(botResponses[random.choice(range(7))])

            except (ValueError, TypeError):
                print(botResponses[random.choice(range(7))])

        else:
            Jokes(number)

    else:
        print("That wasn't one of the options. Did you pass 2nd grade?\n")
        print("Let's try this again...")
        Start()
#the number parameter is passed into the Jokes() function. Based on the value of the parameter, the control structure executes the appropriate code. There are 3 different joke options which can potential display to the user.
def Jokes(number):
    print("I have a joke for you, %s." % (name))
    print("Knock knock...")
    answer = input('SAY: ')
    if number >= 1 and number <=3:
        print("planetary laser cannon.")
        answer = input('SAY: ')
        print("PLANETARY LASER CANNON YOUR FACE OFF! HA HA HA HA! *You hear something powering up in the background...*")
    elif number >=4 and number <= 6:
        print("Meatball.")
        answer = input('SAY: ')
        print("You. If you don't start laughing.")
    else:
        print("Episode I.")
        answer = input('SAY: ')
        print("HA HA HA HA HA. You are quite funny, meat bag.")

#the Start() function is called as the entry point to the program
Start()
