'''
Code Breaker Game
Version 1: Computer is the Code Maker and User is the Code Maker. The Code that 
choosen has no duplicates

1. Explain Rules
2a. Computer Chooses Code No Duplicates
2b. Display previous Guess
2c. Display the possible Numbers to choose from and how to type them in and 
    guess code
3. Function to check the guess and then diplay the clues
5. Repeat Steps 3 and 4 Until the CLues are all black or 12 guesses has passed
6. End the game
'''

import random
import time

'''
1: Explain the rules
'''
def Beginning():
    print('Welcome to CODEBREAKER! \n')
    time.sleep(1)
    print('This is a game where you, the codebreaker have to guess a secret code the codebreaker, the computer has created \n')
    time.sleep(2)
    print('You have twelve guesses. The Code is always 5 digits long \n')
    time.sleep(2)
    print('After each guess, the computer will provide clues to help you break the code \n')
    time.sleep(2)
    print('o: This symbol means that you have guessed the right number but it is in the wrong position \n')
    time.sleep(2)
    print('●: This symbol means that you have guessed the right number and it is in the right position \n')
    time.sleep(2)
    print('These symbols are in a random order and do not correspond to the order of your guess \n')


'''
2a: COmputer Chooses Code
There are no duplicates in this code
The Code is a list
'''

def choose_code_no():
    Num_Total = [1,2,3,4,5,6,7,8]
    Code = random.sample(Num_Total,5)
    return Code

    # x = choose_code_no()


'''
2c: Display the possible Numbers to choose from and how to type them in

total_guesses is a dictionary, where the guesses are the key and the values 
are the clues. The key is a tuple and the clues are a string
'''

def Guess(total_guesses):
    ''' I need to add the check that they dont repeat numbers '''
    Guess = ''
    y = False
    while not(len(Guess)==5 and y):  
        print('Numbers to Choose from: ')
        print('1 2 3 4 5 6 7 8 \n')
        time.sleep(2)
        g = []
        Guess = input('Please Enter Your Guess: ')
        if len(Guess) != 5:
            print('You entered a code that is not 5 digits long')
            print('Please Try Again')
        for item in Guess:
            g.append(item)
        K_guess = tuple(g)
        if K_guess in total_guesses:
            y = False
            print('You have already guesses this Code \n')
            print('Please Try Again')
        else:
            y = True
    h = [Guess,K_guess]
    return h

#x = Guess()

#print(x)
'''
2d: Display previous Guesses

this is the format of the previous guesses

print(' 1, 2, 5, 8, 3 |  o o ● ')

The input should be a dictionary in which the guesses are the key and the 
clues are the value. The key is a tuple and the value is a sting

'''
def display_guess(guess_code):
    for thing in guess_code:
        a = " ".join(thing)
        b = guess_code[thing]
        print(a, '|', b )

#h = {( '1', '2', '3', '4', '5'):['o', 'o', '✓'], ('1', '6', '8', '9', '7'):['o', 'o', '✓','o'] }

#x = display_guess(h)

'''
3. Check the guess:

The input comes in like this '12345'

'''
def Clues_No(x,code):
    print("Take another Guess! \n")
    circle = ''
    coloured_circle = ''
    for thing in x:
        if int(thing) in code:
            if x.index(thing) == code.index(int(thing)):
                coloured_circle = coloured_circle + '● '
            else:
                circle = circle + 'o '
        else:
            continue
    clue = circle + coloured_circle
    return clue

#x = Clues_No('12345', [1,2,4,3,5])

#print(x)


'''
5. Play the Game
'''

def play_game_no():
    Beginning()
    total_guesses = {}
    print('')
    time.sleep(2)
    print("Let's get started! \n")
    time.sleep(1)
    print("Hmmm... I am thinking of a code \n")
    code = choose_code_no()
    time.sleep(2)
    print('Ok! I got one.\n')
    time.sleep(2)
    guess_num = 0
    while guess_num < 12:        
        guess = Guess(total_guesses)
        clue = Clues_No(guess[0],code)
        total_guesses[guess[1]] = clue
        guess_num += 1
        if clue == '● ● ● ● ● ':
            print('Congratulations! That was my code')
            time.sleep(2)
            display_guess(total_guesses)
            time.sleep(2)
            print('you Guessed it in ', guess_num, ' guesses!')
            break
        else:
            print("Here are your previous Guesses and clues: \n")
            display_guess(total_guesses)
            time.sleep(2)
            print('You have ', 12 - guess_num, " guesses left \n")
            time.sleep(2)
            
            continue

    if not(clue == '● ● ● ● ● '):
        print('You ran out of guesses')
        print('My code was: ', code)

x = play_game_no()
    

    
    
