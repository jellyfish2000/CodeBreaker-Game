# -*- coding: utf-8 -*-

'''
Code Breaker Game
Version 3: The Computer is the Code Breaker and the User is the Code Maker

1. Explain Rules
2. User Chooses Code with no duplicates
3. Computer Guesses code
    initial 5 digit code
4. User inputs Clues
4b. check clues
5. Display Previous clues and new clues
6. Using the clues enter next guess
    1. algorithm for finding the 5 numbers
    2. algoithm for finding the right places

7. Repeat Steps 2 and 6 Until the CLues are all black or 12 guesses has passed
8. End the game
'''
# -*- coding: utf-8 -*-
import random

def Guess_under_5_intial(total_guesses, maybe, total_clues, available_index, unused, correct): 
    
    global i
    global y

    
    old_clue = list(total_guesses.values())[len(total_guesses)-2]
    new_clue = list(total_guesses.values())[len(total_guesses)-1]

    old_guess = list(total_guesses.keys())[len(total_guesses)-2]
    new_guess = list(total_guesses.keys())[len(total_guesses)-1]
    
    old_check = total_clues[len(total_clues)-2][1]
    new_check = total_clues[len(total_clues)-1][1]
    
    if y:
        old_guess = list(total_guesses.keys())[len(total_guesses)-3]
        old_check = total_clues[len(total_clues)-3][1]
        old_clue = list(total_guesses.values())[len(total_guesses)-3]
        
    if len(old_clue) < len(new_clue):
        new = list(new_guess).copy()
        if new_check > old_check:
            correct[i] = new_guess[i]
        maybe = []
        available_index.remove(i)
        i = random.choice(available_index)
        x = random.choice(unused)
        new[i] = x
        unused.remove(x)
        return new
    
    elif len(old_clue) > len(new_clue):
        new = list(old_guess).copy()
        y = True
        if old_check > new_check:
            correct[i] = old_guess[i]
        if len(maybe) > 0:
            new[i] = maybe[1]
            maybe.remove(maybe[1])
            available_index.remove(i)
            i = random.choice(available_index)
            x = maybe[0]
            new[i] = x
            maybe = []
        else:
            available_index.remove(i)
            i = random.choice(available_index)
            x = random.choice(unused)
            new[i] = x
            unused.remove(x)
        return new
    
    elif len(old_clue) == len(new_clue):
        if old_clue != new_clue:  
            if new_check > old_check:
                new = list(new_guess).copy()
                correct[i] = new_guess[i]
                available_index.remove(i)
                x = i
                i = random.choice(available_index)
                new[i] = old_guess[x]
                return new
            
            elif old_check > new_check:
                new = list(old_guess).copy()
                correct[i] = old_guess[i]
                available_index.remove(i)
                x = i
                i = random.choice(available_index)
                new[i] = new_guess[x]
                return new
        elif old_clue == new_clue:
            if len(maybe) > 0:
                maybe = []
                new = list(new_guess).copy()
                x = random.choice(unused)
                new[i] = x
                unused.remove(x)
                return new
            else:
                new = list(new_guess).copy()
                maybe.append(old_guess[i])
                maybe.append(new_guess[i])
                x = random.choice(unused)
                new[i] = x
                unused.remove(x)
                return new

            
     
i = 3
total_guesses = {(1,2,3,4,5): 'o o o ● ', (1,2,3,4,6): 'o o ● ', (1,2,3,7,5): 'o o ● '}
maybe = []
y = True
total_clues = [[3,1],[2,1],[2,1]]
available_index = [0,1,2,3]
unused = [8]
h = {0: None,1: None,2: None,3: None,4: None,}
            
x = Guess_under_5_intial(total_guesses, maybe, total_clues, available_index, unused, h) 

print(x)
print(total_guesses)
print(maybe)
print(unused)
print(available_index)
print(h)

def guess_under_2(unused,old_guess):
    new = unused.copy()
    random.shuffle(new)
    x = random.sample(old_guess,2)
    new.append(x[0])
    new.append(x[1])
    return new        

old_guess = [1,2,3,4,5]
unused = [6,7,8]
x = guess_under_2(unused,old_guess)     
print(x)
                
                
def guess_intial():
    n = [1,2,3,4,5,6,7,8]
    h = random.sample(n,5)
    return h
x = guess_intial()
print(x)

def unused(intial):
    n = [1,2,3,4,5,6,7,8]
    for i in intial:
        if i in n:
            n.remove(i)
    return n


h = unused(x)

print(h)
