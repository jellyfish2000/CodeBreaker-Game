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
import random


'''
2.
'''
'''
def Code():
    print('Numbers to choose from: 1 2 3 4 5 6 7 8')
    y = False
    Code = ''
    while not(len(Code)==5 and y):
        Code = input('Please enter your code:')
        if len(Code) != 5:
            print('You entered a code that is not 5 digits long')
            print('Please Try Again')
        else:
            for thing in Code:
                if Code.count(thing) > 1:
                    print('This code has Duplicates please try again')
                    y = False
                    break
                else:
                    y = True
    return Code


x = Code()

print(x)
'''
'''
intial Guess
'''

def Intial():
    Num_total = '12345678'
    Intial = int(''.join(random.sample(Num_total, 5)))
    return Intial
'''    
x = Intial()
print(x)
'''

'''
3. Computer Guesses Code

h = {( '1', '2', '3', '4', '5'): 'o o ✓ ', ('1', '6', '8', '9', '7'):'o o ✓ ' }

    last_clue = list(total_guesses.values())[len(total_guesses)-1]
    
    
    if len(last_clue) >= 6 and len(last_clue) < 10:
'''

def replace_1_num(new_guess,available,avail_index):
    #new_guess = list(list(total_guesses.keys())[len(total_guesses)-1])
    index_guess = random.sample(avail_index, 1)
    index_ava = random.randint(0,len(available)-1)
    new_guess [index_guess[0]] = available[index_ava]
    return new_guess
'''
h = [1,2,3,4,5] 

num_not = [6,7,8]
x = replace_1_num(h,num_not,[0,1,2,3,4])
print(x)
'''
def replace_2_num(last_guess,available):
    #last_guess = list(list(total_guesses.keys())[len(total_guesses)-1])
    num = [0, 1, 2, 3, 4]
    i = random.sample(num, 2)
    new_guess = available.copy()
    new_guess.append(last_guess[i[0]])
    new_guess.append(last_guess[i[1]])
    return new_guess
'''
h = [1,2,3,4,5]
unused = [6,7,8]
x = replace_2_num(h, unused)

print(x)
'''
'''
Old guess to new guess increases by one
'''

def increase_one(guess_old, guess_new, numbers):
    for item in guess_new:
        if item not in guess_old:
            numbers['yes'].append(item)
            i = guess_new.index(item)
            numbers['no'].append(guess_old[i])
            break
    return i
'''
guess_old = [1,2,3,4,5]
guess_new = [1,2,3,4,6]
number = {'yes':[],'no':[]}
x = increase_one(guess_old, guess_new, number)

print(x)
print(number)
'''
def increase_one_black(guess_old, guess_new, numbers, place, unused):
    for item in guess_new:
        if item not in guess_old:
            numbers['yes'].append(item)
            i = guess_new.index(item)
            numbers['no'].append(guess_old[i])
            place[item] = i
            unused.remove(item)
            break
    return i

'''
guess_old = [1,2,3,4,5]
guess_new = [1,2,3,4,6]
number = {'yes':[],'no':[]}
place = {1:-1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 7: -1, 8: -1}
x = increase_one_black(guess_old, guess_new, number, place)

print(x)

print(place)
print(number)

'''
def decrease_one(guess_old, guess_new, numbers, unused):
    for item in guess_new:
        if item not in guess_old:
            numbers['no'].append(item)
            i = guess_new.index(item)
            numbers['yes'].append(guess_old[i])
            unused.remove(item)
            break
    return i
'''       
guess_old = [1,2,3,4,6]
guess_new = [1,7,3,4,6]
number = {'yes':[],'no':[]}

x = decrease_one(guess_old, guess_new, number)

print(number)
'''

def decrease_one_black(guess_old, guess_new, numbers, place, unused):
    for item in guess_new:
        if item not in guess_old:
            numbers['no'].append(item)
            i = guess_new.index(item)
            numbers['yes'].append(guess_old[i])
            place[guess_old[i]] = i
            unused.remove(item)
            break
    return i
'''
guess_old = [1,2,3,4,6]
guess_new = [1,7,3,4,6]
number = {'yes':[],'no':[]}
place = {1:-1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 7: -1, 8: -1}
x = decrease_one_black(guess_old, guess_new, number, place)

print(number)
print(place)
'''
def same_black_get(guess_old, guess_new, numbers, place, unused):
    for item in guess_new:
        if item not in guess_old:
            numbers['yes'].append(item)
            i = guess_new.index(item)
            numbers['yes'].append(guess_old[i])
            place[item] = i
            unused.remove(item)
            break
    return i
'''
guess_old = [1,2,3,4,6]
guess_new = [1,7,3,4,6]
number = {'yes':[],'no':[]}
place = {1:-1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 7: -1, 8: -1}
x = same_black_get(guess_old, guess_new, number, place)

print(number)
print(place)

'''
def same_black_lose(guess_old, guess_new, numbers, place, unused):
    for item in guess_new:
        if item not in guess_old:
            numbers['yes'].append(item)
            i = guess_new.index(item)
            numbers['yes'].append(guess_old[i])
            place[guess_old[i]] = i
            unused.remove(item)
            break
    return i

'''
guess_old = [1,2,3,4,6]
guess_new = [1,2,3,7,6]
number = {'yes':[],'no':[]}
place = {1:-1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 7: -1, 8: -1}
x = same_black_lose(guess_old, guess_new, number, place)

print(number)
print(place)
'''
'''
this next function is for guesses in which are less then 5 correct and we have 
made at least two guesses so far
this function returns a new guess depending on the clues
'''

def Guess_under_5_intial(total_guesses, numbers, place, total_clues, available_index, unused): 
    

    old_clue = list(total_guesses.values())[len(total_guesses)-2]
    new_clue = list(total_guesses.values())[len(total_guesses)-1]

    old_guess = list(total_guesses.keys())[len(total_guesses)-2]
    new_guess = list(total_guesses.keys())[len(total_guesses)-1]


    old_circle = total_clues[len(total_clues)-2][0]
    new_circle = total_clues[len(total_clues)-1][0]
    old_check = total_clues[len(total_clues)-2][1]
    new_check = total_clues[len(total_clues)-1][1]
    
    
    
    
    
    if len(old_clue) < len(new_clue):
        new = list(new_guess).copy()
        if new_check > old_check:
            x = increase_one_black(old_guess, new_guess, numbers, place)
            available_index.remove(x)
            replace_1_num(new,unused,available_index)
            #remember to update unused
            return new
        elif new_circle > old_circle:
            x = increase_one(old_guess, new_guess, numbers)
            available_index.remove(x)
            replace_1_num(new,unused,available_index)
            return new
        # produce a new guess
    elif len(old_clue) > len(new_clue):
        new = list(old_guess).copy()
        if old_circle > new_circle:
            x = decrease_one(old_guess, new_guess, numbers)
            available_index.remove(x)
            replace_1_num(new,unused,available_index)
            return new
        elif old_check > new_check:
            x = decrease_one_black(old_guess, new_guess, numbers, place)
            available_index.remove(x)
            replace_1_num(new,unused,available_index)
            return new
    elif len(old_clue) == len(new_clue):
        if old_clue == new_clue:
            #how to make new guess
            print('hi')
        elif old_clue != new_clue:
            if new_check > old_check:
                x = same_black_get(old_guess, new_guess,numbers,place)
                available_index.remove(x)
                i = random.choice(available_index)
                new[i] = old_guess[x]
                return new
            elif old_check > new_check:
                x = same_black_lose(old_guess, new_guess, numbers, place)
                available_index.remove(x)
                i = random.choice(available_index)
                new = list(old_guess).copy()
                new[i] = new_guess[x]
                return new
                


   

 
h = {(1,2,3,4,5): 'o o o ', (1,2,3,4,6): 'o o ● '}
numbers = {'yes':[], 'no':[]}
place = {1:-1 , 2:-1, 3:-1, 4:-1, 5:-1, 6:-1, 7:-1, 8:-1}
k = [[3,0],[2,1]]
available_index = [0,1,2,3,4]



y = Guess_under_5_intial(h, numbers, place, k, available_index)

print(numbers)
print(place)
print(available_index)
print(y)
'''
this next function is for guesses in which we have our intial guess and nothing 
else.
'''
