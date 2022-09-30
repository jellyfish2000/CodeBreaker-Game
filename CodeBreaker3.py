# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 22:35:25 2022

@author: preet
"""

import random

'''
1: Explain the rules
'''

def Beginning():
    print('Welcome to CODEBREAKER! \n')

    print('This is a game where you, the codebreaker have to guess a secret code the codebreaker, the computer has created \n')

    print('You have twelve guesses. The Code is always 5 digits long \n')

    print('After each guess, the computer will provide clues to help you break the code \n')

    print('o: This symbol means that you have guessed the right number but it is in the wrong position \n')

    print('●: This symbol means that you have guessed the right number and it is in the right position \n')

    print('These symbols are in a random order and do not correspond to the order of your guess \n')




'''
2: User picks a code
'''

def Code():
    x = input("Enter a 5 number code with no Dublicates:")
    return x


'''
3: First Guess
'''

def guess_initial():
    n = ['1','2','3','4','5','6','7','8']
    h = random.sample(n,5)
    return h

x = guess_initial()

print(x)

'''
4: Input clues
'''

def clues(total_clues):
    x = input('Enter the number of numbers which are correct but not in the right spot:')
    y = input('Enter the number of numbers which are correct and in the correct spot: ')
    total_clues.append([x,y]) 
    
    
'''
5. display guesses and update gusses
'''

def display_guess(total_guesses,total_clues, guess):
    x = int(total_clues[-1][0])
    h = x * 'o '
    y = int(total_clues[-1][1])
    h = h + '● ' * y
    total_guesses[''.join(guess)] = h
    for thing in total_guesses:
        b = total_guesses[thing]
        print(thing, '|', b )

'''
COmputer makes next guess:
    
    1. if increased circle
        remove from available_numbers
        choose another one
    2. if decreased circle
        old guess for new guess
        remove a different number 
        and in the future compare it to the 3 last guess
    3. if stayed the same
        replace the added number with an unused number
    4. if no more unused numbers and no repeats
        replace the added number in other spots
    5. if no more unused numbers and has some repeats:
        all the numbers which were replaces are in the code
'''




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


guess = [1,2,3,4,5]
avilable_numbers = [1,2,3,4,5]
unused = [6,7,8]

x = next_guess(guess, avilable_numbers, unused)


print(x)

def two_intial(total_guesses, available_numbers, unused, maybe):
    global x
    
    new_guess = list(list(total_guesses.keys())[-1])
    
    new = unused.copy()
    m = random.sample(new_guess,2)
    new.append(m[0])
    new.append(m[1])
    return new





def compare(total_guesses, available_numbers, unused, maybe, n):
    global y
    global x
    
    old_clue = list(total_guesses.values())[-2]
    new_clue = list(total_guesses.values())[-1]

    old_guess = list(list(total_guesses.keys())[-2])
    new_guess = list(list(total_guesses.keys())[-1])
    
    
    if y > 0:
        old_guess = list(total_guesses.keys())[-1*(y+2)]
        old_clue = list(total_guesses.values())[-1*(y+2)]
        
    
    if len(unused) == 0:
        
        if len(maybe) == 2 and len(old_clue) == len(new_clue) and len(new_clue) == 6:
            maybe.append(x)
            new = maybe.copy()
            m = [1,2,3,4,5,6,7,8]
            m.remove(maybe[0])
            m.remove(maybe[1])
            m.remove(maybe[2])
            available_numbers = m
            
            l = random.sample(available_numbers,2)
            new.append(l[0])
            new.append(l[1])
            available_numbers.remove(l[0])
            available_numbers.remove(l[1])
            x = l
            random.shuffle(new)
            return new
        
        elif len(old_clue) == len(new_clue) and len(new_clue) == 8:
            y += 1
            new = old_guess.copy()
            l = random.choice(available_numbers)
            i = new.index(l)
            available_numbers.remove(l)
            new[i] = x
            random.shuffle(new)
            return new
        
        elif len(old_clue) == len(new_clue) and len(new_clue) == 6:
            
            new = new_guess.copy()
            new.remove(x[1])
            new.remove(x[0])
            
            l = random.sample(available_numbers,2)
            new.append(l[0])
            new.append(l[1])
            available_numbers.remove(l[0])
            available_numbers.remove(l[1])
            x = l
            random.shuffle(new)
            return new
        
        elif len(old_clue) + 1 == len(new_clue) and len(new_clue) == 4:
            new = new_guess.copy()
            new.index(x[0])
            available_numbers
        #helohelohelohelo
            
    
    elif len(unused) == 0 and len(maybe) > 0 and len(old_clue) == len(new_clue):
        maybe.append(x)
        h = old_guess.copy()
        for n in old_guess:
            if n in new:
                h.remove(n)
        if h[0] not in maybe:
            maybe.append(h[0])
        
        if len(maybe) == 3 :
            new = maybe.copy()
            unused = [1,2,3,4,5,6,7,8]
            
            unused.remove[maybe[0]]
            unused.remove[maybe[1]]
            unused.remove[maybe[2]]
            
            l = random.sample(unused,2)
            available_numbers = unused.copy()
            available_numbers.remove(l[0])
            available_numbers.remove(l[1])
            
            new.append(l[0])
            new.append(l[1])            
            
            x = l[0]
            
            random.shuffle(new)

            return new
        
        elif len(maybe) == 2:
            new_guess = list(total_guesses.keys())[-1]
            new = new_guess.copy()
            x = maybe[0]
            l = random.choice(new_guess)
            i = new.index(l)
            
            new[i] = x
            return new
        
    
    
    elif len(old_clue) + 2 == len(new_clue):
        if len(maybe) > 2:
            maybe = []
        new = new_guess.copy()
        
        next_guess(new,available_numbers, unused)
        return new
        
    
    elif len(old_clue) - 2 == len(new_clue):
        if len(maybe) > 0:
            new = old_guess.copy()
            y = random.choice(available_numbers)
            available_numbers.remove(y)
            x = maybe[0]
            i = new.index(y)
            new[i] = x
            random.shuffle(new)
            maybe = []
            return new
        else: 
            new = old_guess.copy()
            y += 1
            next_guess(new,available_numbers, unused)
            return new
    
    
    elif len(old_clue) == len(new_clue):
        if len(maybe) > 0:
            new = maybe.copy()
            new.append(x)
            interm = new_guess.copy()
            interm.remove(x)
            l = random.sample(interm, 2)
            # ths is not right
        
        new = new_guess.copy()
        maybe.append(x)
        
        h = old_guess.copy()
        for n in old_guess:
            if n in new:
                h.remove(n)
        if h[0] not in maybe:
            maybe.append(h[0])
        
        i = new.index(x)
        m = random.choice(unused)
        new[i] = m
        unused.remove(m)
        random.shuffle(new)
        
        return new

        

total_guesses = {'12345': 'o o o ● ', '12346': 'o o ● '}
available_numbers = ['1','2','3','4']
unused = ['7','8']
maybe =[]
y = 0
x = 6


x = compare(total_guesses, available_numbers, unused, maybe)

print(x)
print(avilable_numbers)
print(unused)

def generate_combinations(l_ist):
    new = []
    new.append([l_ist[0],l_ist[1]])
    new.append([l_ist[0],l_ist[2]])
    new.append([l_ist[0],l_ist[3]])
    new.append([l_ist[0],l_ist[4]])
                
    new.append([l_ist[1],l_ist[2]])
    new.append([l_ist[1],l_ist[3]])
    new.append([l_ist[1],l_ist[4]])
    
    new.append([l_ist[2],l_ist[3]])
    new.append([l_ist[2],l_ist[4]])
    
    new.append([l_ist[3],l_ist[4]])
    return new

def no_unused(total_guesses,maybe, available_numbers):
    global y
    global x
    
    #old_clue = list(total_guesses.values())[-2]
    #new_clue = list(total_guesses.values())[-1]

    #old_guess = list(total_guesses.keys())[-2]
    new_guess = list(total_guesses.keys())[-1]

    
    if len(maybe) == 0:
        new = new_guess.copy()
        #available_numbers.remove(x)
        j = random.choice(available_numbers)
        l = new.index(j)
        new[l] = x
        available_numbers.remove(j)
        random.shuffle(new)
        return new
    
    
    
def no_unused_and_maybe(total_guesses,maybe, available_numbers, unused):
    
    global y
    global x
        
    if len(maybe) == 3 :
        new = maybe
        m = [1,2,3,4,5,6,7,8]
        m.remove(maybe[0])
        m.remove(maybe[1])
        m.remove(maybe[2])
        n = generate_combinations(m)
        h = random.choice(n)
        n.remove(h)
        new.append(h[0])
        new.append(h[1])
        unused = n
        random.shuffle(new)
        return new
    elif len(maybe) == 2:
        new_guess = list(total_guesses.keys())[-1]
        new = new_guess.copy()
        x = maybe[0]
        l = random.choice(new_guess)
        i = new.index(l)
        
        new[i] = x
        return new
        
        
        
def play_game():
    Beginning()
    total_guesses = {}
    total_clues = []
    maybe = []
    y = 0
    x = None

    print("Ok! Let's get started")
    x = Code() #enter code
    y = guess_initial()#enter guess
    print("I guess: ", ''.join(y))
    available_numbers = y.copy()
    unused = ['1','2','3','4','5','6','7','8']
    
    for thing in y:
        if thing in unused:
            unused.remove(thing)
        
    
    clues(total_clues) # enter clues
    display_guess(total_guesses,total_clues,y) #display guess
    print('Ok! Now I will guess another')
    
    
    
    if len(list(total_guesses.values())[-1]) != 10:
        guess = list(list(total_guesses.keys())[-1])
        next_guess(guess, available_numbers, unused)# Gusses the next guess
        print(' I guess: ', ''.join(guess))
        clues(total_clues)
        display_guess(total_guesses,total_clues,guess)
        
        
    
        while len(list(total_guesses.values())[-1]) != 10:
            print('Ok! Now I will guess another clue')
            guess = compare(total_guesses, available_numbers, unused, maybe)
            print(' I guess: ', ''.join(guess))
            clues(total_clues)
            display_guess(total_guesses, total_clues, guess)
    print('done')


play_game()
            
            
        
        
        
    

    
    
        
        
        
        
        
    
    
        
        


    
    
    
    
    
    
    
    
    
    
    
    
