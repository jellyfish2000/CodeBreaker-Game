# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 21:11:01 2022

@author: preet
"""
import random


# User Decides the Code
# The code is going to be a list of string numbers :
# Like this : ['1','2']
    
def Code():
    x = input("Enter a 5 number code with no Dublicates:")
    list(x)
    return x

#The computer makes and inital guess
# The guess will be n the form of: a list of strings ['1','2']

def guess_initial():
    n = ['1','2','3','4','5','6','7','8']
    h = random.sample(n,5)
    return h

#The user inputs the clues
#This will be in the form of a list in a list.

def clues(total_clues):
    x = input('Enter the number of numbers which are correct but not in the right spot:')
    y = input('Enter the number of numbers which are correct and in the correct spot: ')
    total_clues.append([x,y]) 
    #the first term will be the number of numbers which are in the wrong place
    # the second term will be the number of numbers which are in the right place
    
    
    
# Diplays clues:
#diplays the guess and associates the guess with the clue
    
def display_guess(total_guesses,total_clues, guess):
    x = int(total_clues[-1][0])
    h = x * 'o '
    y = int(total_clues[-1][1])
    h = h + '● ' * y
    total_guesses[''.join(guess)] = h
    for thing in total_guesses:
        b = total_guesses[thing]
        print(thing, '|', b )


# Generates combinations of two with a given list
# Needed for when we know there are three number in the code for sure
 
def Generate_combinations(l_ist):
    combinations = []
    for thing in l_ist:
        for item in l_ist:
            if l_ist.index(thing) < l_ist.index(item):
                combinations.append([thing,item])
    return combinations


def make_unused(guess):
    m = ['1','2','3','4','5','6','7','8']
    for thing in guess:
        if thing in m:
            m.remove(thing)
            
    return m


        

# Removes one number from the guess and replaces it with another
# Guess is the guess in which we want to remove one number from

def next_guess(guess, available_numbers, unused):
    global x
    
    lemons = guess.copy()
    
    m = random.choice(available_numbers)
    available_numbers.remove(m)
    x = random.choice(unused)
    unused.remove(x)
    lemons.remove(m)
    lemons.append(x)

    random.shuffle(lemons)
    
    return lemons


# Compares the guesses and outputs the new one when there are 
# no more than three numbers known

def compare(total_guesses, available_numbers, unused, maybe, n):
    global x
    global y
    global l
    
    old_clue = list(total_guesses.values())[-2]
    new_clue = list(total_guesses.values())[-1]

    old_guess = list(list(total_guesses.keys())[-2])
    new_guess = list(list(total_guesses.keys())[-1])
    
    if y > 0:
        old_guess = list(total_guesses.keys())[-1*(y+2)]
        old_clue = list(total_guesses.values())[-1*(y+2)]
        
    
    
    if len(old_clue) + 2 == len(new_clue):
        
        if len(maybe) > 2:
            maybe = []
        
        new = new_guess.copy()
        next_guess(new,available_numbers, unused)
        
        return new
    
    elif len(old_clue) - 2 == len(new_clue):
        
        if len(new_clue) == 6:
            new = old_guess.copy()
            y += 1
            next_guess(new,available_numbers, unused)
            return new
        
        elif len(new_clue) == 4 and len(unused) == 2:
            new = []
            new.append(unused[0])
            new.append(unused[1])
            for thing in old_guess:
                if thing not in new_guess:
                    new.append(thing)
                    
            m = ['1','2','3','4','5','6','7','8']
            m.remove(new[0])
            m.remove(new[1])
            m.remove(new[2])
            l = Generate_combinations(m)
            x = random.choice(l)
            l.remove(x)
            new.append(x[0])
            new.append(x[1])

            random.shuffle(new)
            
            return new
        
        elif len(new_clue) == 4 and len(unused) == 1:
            new = []
            new.append(unused[0])
            
            old_old = list(list(total_guesses.keys())[-3])
            
            for thing in old_guess:
                if thing not in new_guess:
                    new.append(thing)
                    
            for item in old_old:
                if item not in new_guess:
                    new.append(item)
                    
            
            m = ['1','2','3','4','5','6','7','8']
            m.remove(new[0])
            m.remove(new[1])
            m.remove(new[2])
            l = Generate_combinations(m)
            x = random.choice(l)
            l.remove(x)
            new.append(x[0])
            new.append(x[1])

            random.shuffle(new)
            
            return new
        
    elif len(new_clue) == len(old_clue):
            
        if len(new_clue) == 8:
            new = new_guess.copy()
            new.remove(x)
            new.append(unused[0])
            
        elif len(old_clue) == 6 and len(maybe) == 0:
            maybe.append(x)
            for thing in old_guess:
                if thing not in new_guess:
                    maybe.append(thing)
                     
            new = new_guess.copy()
            new.remove(x)
            x = random.choice(unused)
            new.append(x)
            random.shuffle(new)
                
            return new
        
        elif len(old_clue) == 6 and len(maybe) > 0:
            new = maybe.copy()
            new.append(x)
            
            m = ['1','2','3','4','5','6','7','8']
            m.remove(new[0])
            m.remove(new[1])
            m.remove(new[2])
            m.remove(unused[0])
            l = Generate_combinations(m)
            x = random.choice(l)
            l.remove(x)
            new.append(x[0])
            new.append(x[1])

            random.shuffle(new)
            
            return new
             
            
# After the combinations are picked
# the fuction that chooses what happens next

def after_three_known(total_guesses, interm, unused):
    
    global l
    global x
    global h
    
    try:
        old_clue = list(total_guesses.values())[-2]
        new_clue = list(total_guesses.values())[-1]

        old_guess = list(list(total_guesses.keys())[-2])
        new_guess = list(list(total_guesses.keys())[-1])
    
    except:
        new = unused
        old_guess = list(list(total_guesses.keys())[-1])
        l = Generate_combinations(old_guess)
        x = random.choice(l)
        new.append(x[1])
        new.append(x[0])
        
        random.shuffle(new)
        
        return new
        
    if len(old_clue) == len(new_clue):
        
        new = new_guess.copy()
        interm = x
        new.remove(x[0])
        new.remove(x[1])
        
        for thing in l:
            for item in thing:
                if item in x:
                    l.remove(thing)
                    break
        x = random.choice(l)
        new.append(x[0])
        new.append(x[1])
        
        
        random.shuffle(new)
        
        return new
    
    elif len(old_clue) + 1 == len(new_clue):
        
        if h == 1:
            # need to compare x = [1,4] and interm(the previous x [1,2])
            # You should out put two outcomes: [2,4] and [1,3]
            
            new = new.remove(x[1])
            new = new.append(x[0])
            
            b = []
            h = []
            
            for thing in interm:
                if thing not in x:
                    b.append(thing)
                else:
                    h.append(thing)
            for item in x:
                if item not in interm:
                    b.append(item)
            
            for it in l:
                for lemon in it:
                    if lemon in h:
                        l.remove(it)
                        break
            
            x = b
            new.append(x[0])
            new.append(x[1])
            
            random.shuffle(new)
            return new
        
        else:
            
            h += 1
            interm = x
            
            new = new_guess.copy()
            new.remove(x[0])
            new.remove(x[1])
            
            for thing in l:
                for item in thing:
                    if item not in x:
                        l.remove(thing)
                        break
            x = random.choice(l)
            new.append(x[0])
            new.append(x[1])
            
            random.shuffle(new)
            return new                
            
        
def play_game():
    
    global x
    global y
    global l
    global h  
    
    total_clues = []
    total_guesses= {}
    x = None
    interm = None
    y = 0
    l = []
    h = None
    interm = None
    n = None
    maybe = []
    
    # 1. the User picks the Code:
    code = Code()
    
    # 2. Intial guess from the computer
    guess = guess_initial()
    print(guess)
    unused = make_unused(guess)
    
    # 3. User writes in the clues
    clues(total_clues)
    
    # 4. Display the guess and the clue
    display_guess(total_guesses,total_clues, guess)
    
    # 5. Compare the guess and the clue:
        # if there are only two numbers that are right we have to deploy:
            # after_three_known(total_guesses, interm):
        # if not guess a ranomd one
    available_numbers = guess
    
    print(total_clues[0][1] + total_clues[0][0])
        
    if total_clues[0][1] + total_clues[0][0] == 2:
        while total_clues[-1][1] + total_clues[-1][0] != 5:
            
            new_one = after_three_known(total_guesses, interm, unused)
            print(new_one)
            
            clues(total_clues)
            display_guess(total_guesses,total_clues, new_one)
        
    else:
        new_one = next_guess(guess, available_numbers, unused)
        print(new_one)
        clues(total_clues)
        display_guess(total_guesses,total_clues, new_one)
        
        while total_clues[-1][1] + total_clues[-1][0] != 5:
            
            if len(l) == 0:
            
                new_one = compare(total_guesses, available_numbers, unused, maybe, n)
                print(new_one)
                
                clues(total_clues)
                display_guess(total_guesses,total_clues, new_one)
                
            elif len(l) != 0:
                new_one = after_three_known(total_guesses, interm, unused)
                print(new_one)
                
                clues(total_clues)
                display_guess(total_guesses,total_clues, new_one)
                
                
            
            
            
        


play_game()




