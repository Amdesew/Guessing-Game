# Guessing Game Code
# a guessing game that have problem in return function
# have problem in line 17
def Guessing_Game(guess):
    #Secret number of Guessing_Game
    secret_number = 5
    guess_count = 0
    #It's Count Is 0
    guess_limit = 3
    #The Guess Can Ask The User 3 Times
    while guess_count < guess_limit:
        guess_count += 1
        #The Guess Counted 1 or less than one
        if guess == secret_number:
            print('You Have Won The Guess...')
            #After the user guessed it correctly the programm doesn't ask it to do more guess
            break
        return 
        #I Don't Understand To What I Return I will Do it after i learned Return Statement Well
        #in which part will return insert it if you know
    else:
        print('You Have Failed The Guess...')
        #If the user try's 3 times and don't get the guess the programm will anounce hi's failed
try:
    # if the user try's to distrube the programm it will be prevent by this code under this
    guess = int(input('Guess: '))
    #the main guess input
    print(Guessing_Game(guess))
except ValueError:
    #if the user enter alphabetical words the programm will tell him it determine as error 
    print('Invalid Error')


    