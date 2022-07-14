#Julia Gordon
#6/29/2021
#Assignment 3:


legal_colors = ['R', 'G', 'B', 'Y', 'W', 'O', 'M', 'V']

def generate_color_sequence():
    import random
    random.seed()

    sequence = random.sample(range(len(legal_colors)), 4)
    return [legal_colors[i] for i in sequence]

colors = generate_color_sequence()

### # Your Code Here

print("-------------------------------------------------------------------")
print('----------------------------Mastermind-----------------------------')
print("-------------------------------------------------------------------")
print("   >  you get five tries to guess the right color combination")
print("   >  W means youve guessed the right color but it is in the wrong place")
print("   >  R means you have guessed the right color in the right pace!")
    
turn = 0
max_tries = 5

while True:
# User validation
    guess = input("Please enter your guess of length 4 using the letters RGBYWOMV: ")
    print("---------------------------------------------------------------")
    if len(guess) < len(colors) or len(guess) > len(colors):    # will tell the user if there input is not 4 colors. 
        print("ERROR - Make sure you type in only 4 colors.")
        print("---------------------------------------------------------------")
        continue
    if not guess.isupper():    # will tell user if their input is not uppercase.
        print("ERROR - Make sure you type your guess in capital letters.")
        print("---------------------------------------------------------------")
        continue 
    if guess[0]==guess[1] or guess[2]==guess[3] or guess[0]==guess[3] or guess[0]==guess[2] or guess[1]==guess[2] or guess[1]==guess[3]:   # will tell the user if they have a duplicate color in their inputprint("ERROR - Colors can not be repeated.")
        print("ERROR - colors can be repeated.")
        print("---------------------------------------------------------------")
        continue
    if guess in legal_colors:   ### will tell the user if their input contains an unknown character.
        print("ERROR- Unknown character found.")
        print("---------------------------------------------------------------")
        continue
      
    turn += 1
    peg =''
    guess_count = ("Guess " + str(turn))
    print(guess_count,":", guess)

    for i in range(4):  # this code gives the hits with the pegs to the player. 
        if (guess[i] in colors) & (guess[i] != colors[i]):
            peg = peg+ 'W'  # W = in phrase but at the wrong place
        elif guess[i] == colors[i]:
            peg = peg+ 'R'  # R = in phrase and in the right place
        else:
            peg = peg+ '_'  # - = not in phrase        
    print(peg)
    print("---------------------------------------------------------------")
         
    if peg == 'RRRR' :    # tells the player if they win.  
        print ('You Win!')
        break
    else:
        if turn>=int(max_tries):    # tells player they lose if they go over their 5 guesses.
            print('Out of tries! Better luck next time! The colors were '+ str(colors))
            break    

