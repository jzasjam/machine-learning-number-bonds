
import random
import microbit
import time

# Set the initial number bonds all to 5
bonds = [5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0]

# Set the initial score variables
human_wins = 0
machine_wins = 0
turns = 0

# Instruction Message
print('# Train a machine to learn its number bonds to 10! #')
print('====================================================')
print('> I give you a number, and you tell me what you add to it to make 10')
time.sleep(3)

# Main Loop for Training
while True:
    print() # Add a blank line 

    # Select a Random Number 0-9
    number = random.randint(0,9)  

    # Output the Chosen Number
    print('--------------------------------------------')
    print('>>> Chosen Number is ' + str(number) + ' <<<')
    print('--------------------------------------------')

    # See the 'known' bonds and watch it improve its data set
    print("> Machine Current Bonds: " + str(bonds)) 
    print() # Add a blank line 
    time.sleep(1.5)

    # Machines Guess
    print('> Machine says: The bond to 10 is ' + str(round(bonds[number])))
    if number + round(bonds[number]) == 10:
        print('Machine is: CORRECT!')
        machine_wins += 1 # Add to the machine's score
    else:
        print('Machine is: WRONG (more training needed)')
    time.sleep(1)

    # Humans Guess
    print('--------------------------------------------')
    print('> Your Turn: ' + str(number) + ' + [?] = 10')
    human_answer = input('Enter Your Answer [1-10]: ')
    if human_answer == 'quit':
        break
    elif human_answer == 'reset':
        human_wins = 0
        machine_wins = 0
        turns = 0
    elif number + int(human_answer) == 10:
        human_wins += 1 # Add to the human's score
        bonds[number] = (bonds[number] + int(human_answer)) / 2
        print('Correct! Now the machine thinks it is ' + str(round(bonds[number])))
    else:
        print('Wrong! Are you trying to mislead a poor machine?')
        

    # End and Count turn    
    turns += 1
    time.sleep(1)
    
# On Quit, show the scores
print('Human score ' + str(human_wins) + ' out of ' + str(turns))
print('Machine score ' + str(machine_wins) + ' out of ' + str(turns))
microbit.display.show('H '+str(human_wins)+' M'+str(machine_wins),wait=False,loop=True)