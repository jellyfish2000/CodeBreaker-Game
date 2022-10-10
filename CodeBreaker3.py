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

# Removes one number from the guess and replaces it with another
# Guess is the guess in which we want to remove one number from

def next_guess(guess, available_numbers, unused):
    global x
    
    y = random.choice(available_numbers)
    available_numbers.remove(y)
    x = random.choice(unused)
    unused.remove(x)
    i = guess.index(y)
    guess[i] = x

    random.shuffle(guess)
    
    return guess


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
            l = Generate_combinations(m)
            x = random.choice(l)
            l.remove(x)
            new.append(x[0])
            new.append(x[1])

            random.shuffle(new)
            
            return new
             
            
        
        




