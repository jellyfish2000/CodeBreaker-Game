# -*- coding: utf-8 -*-


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
    n = [1,2,3,4,5,6,7,8]
    h = random.sample(n,5)
    return h

'''
4: Input clues
'''
total_clues = []
def clues(total_clues):
    x = input('Enter the number of numbers which are correct but not in the right spot:')
    y = input('Enter the number of numbers which are correct and in the correct spot')
    total_clues.append([x,y])

'''
5. Computer makes a new guess: Three correct numbers
'''

def three_num_correct(total_guesses, maybe, total_clues, available_index, unused, correct, no): 
    
    global i
    global y
    
    
    old_clue = list(total_guesses.values())[-2]
    new_clue = list(total_guesses.values())[-1]

    old_guess = list(total_guesses.keys())[-2]
    new_guess = list(total_guesses.keys())[-1]
    
    old_check = total_clues[-2][1]
    new_check = total_clues[-1][1]
    
    if y == 1:
        old_guess = list(total_guesses.keys())[-3]
        old_check = total_clues[-3][1]
        old_clue = list(total_guesses.values())[-3]
    if y == 2:
        old_guess = list(total_guesses.keys())[-4]
        old_check = total_clues[-4][1]
        old_clue = list(total_guesses.values())[-4]
        
    if len(old_clue) < len(new_clue):
        new = list(new_guess).copy()
        if new_check > old_check:
            correct[i] = new_guess[i]
        else:
            no.append(new_guess[i])]
        maybe = []
        available_index.remove(i)
        i = random.choice(available_index)
        x = random.choice(unused)
        new[i] = x
        unused.remove(x)
        return new
    
    elif len(old_clue) > len(new_clue):
        new = list(old_guess).copy()
        y += 1
        if old_check > new_check:
            correct[i] = old_guess[i]
        else:
            no.append(old_guess[i])
        if len(maybe) > 0:
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
        if len(unused) == 0:
            if new_check > old_check:
                correct[i] = new_guess[i]
            elif old_check > new_check:
                correct[i] = old_guess[i]
            else:
                no.append(new_guess[i])
                no.append(old_guess[i])
            new = old_guess.copy()
            available_index.remove(i)
            x = new_guess[i]
            i = random.choice(available_index)
            new[i] = x
            return new
        
        elif old_clue != new_clue:  
            if new_check > old_check:
                no.append(old_guess[i])
                new = new_guess.copy()
                correct[i] = new_guess[i]
                available_index.remove(i)
                x = i
                i = random.choice(available_index)
                new[i] = old_guess[x]
                return new
            
            elif old_check > new_check:
                no.append(new_guess[i])
                new = old_guess.copy()
                correct[i] = old_guess[i]
                available_index.remove(i)
                x = new_guess[i]
                i = random.choice(available_index)
                new[i] = x
                return new
            
        elif old_clue == new_clue:
            no.append(old_guess[i])
            no.append(new_guess[i])
            if len(new_clue) == 8 and len(maybe) >= 2:
                new  = new_guess.copy()
                x = random.choice(unused)
                unused.remove(x)
                new[i] = x
                maybe = []
                return new
            
            elif new_guess[i] in maybe:
                new = new_guess.copy()
                maybe.append(old_guess[i])
                x = old_guess[i]
                available_index.remove(i)
                i = random.choice(available_index)
                new[i] = x
                return new
            
            elif len(maybe) >= 2:
                maybe.append(new_guess[i])
                new = list(new_guess).copy()
                x = random.choice(unused)
                new[i] = x
                unused.remove(x)
                return new
            
            elif len(unused) == 0:
                new = new_guess.copy()
                x = new_guess[i]
                i = random.choice(available_index)
                new[i] = x
            
            else:
                new = list(new_guess).copy()
                maybe.append(old_guess[i])
                maybe.append(new_guess[i])
                x = random.choice(unused)
                new[i] = x
                unused.remove(x)
                return new


'''
5: Computer makes a guess: 4 intially right numbers
'''

def four_num_correct(total_guesses, maybe, total_clues, available_index, unused, correct,no):
    global i
    global y
    
    old_clue = list(total_guesses.values())[-2]
    new_clue = list(total_guesses.values())[-1]

    old_guess = list(total_guesses.keys())[-2]
    new_guess = list(total_guesses.keys())[-1]
    
    old_check = total_clues[len(total_clues)-2][1]
    new_check = total_clues[len(total_clues)-1][1]
    
    if y == 1:
        old_guess = list(total_guesses.keys())[-3]
        old_check = total_clues[-3][1]
        old_clue = list(total_guesses.values())[-3]
    
    if y == 2:
        old_guess = list(total_guesses.keys())[-4]
        old_check = total_clues[-4][1]
        old_clue = list(total_guesses.values())[-4]
        
    if len(unused) == 0:
        if new_check > old_check:
            correct[i] = new_guess[i]
            no.append(old_guess[i])
        if old_check > new_check:
            correct[i] = old_guess[i]
            no.append(new_guess[i])
        new = old_guess.copy()
        available_index.remove(i)
        x = new_guess[i]
        i = random.choice(available_index)
        new[i] = x
        return new
    
    elif len(old_clue) < len(new_clue):
        if new_check > old_check:
            correct[i] = new_guess[i]
        else:
            no.append(new_guess[i])
            
    elif len(old_clue) > len(new_clue):
        new = old_guess.copy()
        y += 1
        if old_check > new_check:
            correct[i] = old_guess[i]
        else:
            no.append(old_guess[i])
        x = random.choice(unused)
        unused.remove(x)
        available_index.remove(i)
        i = random.choice(available_index)
        new[i] = x
        return new
    
    elif len(old_clue) == len(new_clue):
        x = random.choice(unused)
        unused.remove(x)
        new[i] = x
        return new
    
'''
5: Computer Guesses: 2 inital correct numbers
'''

def guess_under_2(unused,initial):
    new = unused.copy()
    x = random.sample(initial,2)
    new.append(x[0])
    new.append(x[1])
    random.shuffle(new)
    return new

'''
FInd the indexes
'''
def find_indexes(correct):
    n = []
    for i in correct:
        if correct[i] == None:
            n.append(i)
    return n


'''
Swap 2 random indexes
'''
def swap_two_rand(indexes, guess):
    global i
    i = random.sample(indexes, 2)
    guess[i[0]],guess[i[1]] = guess[i[1]],guess[i[0]]
    #new = ''.join(h)
    return guess
'''
Swap two specific indexes
'''
def swap_not_rand(guess):
    global i
    guess[i[0]],guess[i[1]] = guess[i[1]],guess[i[0]]
    return guess

'''
Pattern with three numbers with correct placement, two known and one not known
'''
def three_correct_maybe(possible,indexes,total_clues, total_guesses):
    global i
    
    if total_clues[-1][1] == 3:
        last = list(total_guesses.keys())[-1]
        x = random.choice(possible[-1])
        i = [last.index(x),indexes[0]]
        last[i[0]],last[i[1]] = last[i[1]],last[i[0]]
        possible[-1].remove(x)
        return last
    if total_clues[-1][1] == 2:
        new = list(total_guesses.keys())[-2]
        h = (possible[-1][0])
        i = [new.index(h),indexes[0]]
        new[i[0]],new[i[1]] = new[i[1]],new[i[0]]
        return new

'''
Trying to find the placement in which all the correct ones are known

gotta change no to the indexes not the numbers

'''

def placement_intial(no,indexes,maybe,total_guess,total_clues,nope,swapped):
    
    global i
    global y
    global u
    
    old_check = total_clues[-2][1]
    new_check = total_clues[-1][1]
    
    new_guess = list(total_guesses.keys())[-1]
    old_guess = list(total_guesses.keys())[-2]
    
    new = new_guess.copy()
    
    
    if new_check == 3:
        i = indexes
        x = swap_not_rand(new)
        return x
    
    elif new_check == 2:
        x = swap_two_rand(indexes, new)
        return x
    
    elif new_check == 1:
        if len(no) == 1:
            indexes.remove(no[0])
            i = [no[0], randome.choice(indexes)]
        elif len(no) == 2:
            swapped.append(no)
            indexes.remove(no[0])
            indexes.remove(no[1])
            swapped.append(indexes)
            i=[]
            new[no[0]],new[indexes[0]] = new[indexes[0]],new[no[0]]
            new[no[1]],new[indexes[1]] = new[no[1]],new[indexes[1]]
            return new
        
        else:
            x = swap_two_rand(indexes, new)
            return x

    elif new_check == 0:
        if len(no) == 1:
            indexes.remove(no[0])
            i = [no[0], randome.choice(indexes)]
        elif len(no) == 2:
            swapped.append(no)
            indexes.remove(no[0])
            indexes.remove(no[1])
            i = random.sample(indexes, 2)
            swapped.append(i)
            new[no[0]],new[i[0]] = new[i[0]],new[no[0]]
            new[no[1]],new[i[1]] = new[i[1]],new[no[1]]
            return new
        elif len(no) == 3:
            l = random.sample(no,2)
            indexes.remove(l[0])
            indexes.remove(l[1])
            h = random.sample(indexes,2)
            swapped.append(l)
            swapped.appened(h)
            new[l[0]],new[h[0]] = new[h[0]],new[l[0]]
            new[l[1]],new[h[1]] = new[h[1]],new[l[1]]
            return new
            
        else:
            x = swap_two_rand(indexes, new)
            return x
        
            
        
            
    
    
    
    
