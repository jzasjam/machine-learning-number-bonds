
import random
import time
# Use matplotlib to chart the progress of the machine
import matplotlib.pyplot as plt

# Text Colours
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Set the initial number bonds all to 5
bonds = [5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0]

# Instruction Message
print('# Train a machine to learn its number bonds to 10! #')
print('====================================================')
print('> I give you a number, and you tell me what you add to it to make 10')
time.sleep(2)

counter = 0

# Main Loop for Training
while True:
    
    print() # Add blank line

    # Select a Random Number 0-9
    number = random.randint(0,9) 

    # Output the Chosen Number
    print('--------------------------------------------')
    print(bcolors.BOLD  + '>>> Chosen Number is ' + str(number) + ' <<<' + bcolors.ENDC)
    print('--------------------------------------------')
    counter += 1
    if(counter == 1):
        # See the 'known' bonds and watch it improve its data set
        print("> Machine Current Bonds: " + str(bonds)) 
        print() # Add a blank line 

        # Chart the bonds in a line chart
        plt.plot([10,9,8.0,7.0,6.0,5.0,4.0,3.0,2.0,1.0])
        plt.plot(bonds)
        plt.ylabel('Bond to 10')
        #Show the chart 
        plt.show()
    
    if(counter == 10):
        counter = 0


    time.sleep(0.5)

    # Machines Guess
    print('> Machine says: The bond to 10 is ' + str(round(bonds[number])))
    if number + round(bonds[number]) == 10:
        print(bcolors.OKGREEN  + ' + Machine is: CORRECT!' + bcolors.ENDC)
    else:
        print(bcolors.FAIL + ' - Machine is: WRONG (more training needed)' + bcolors.ENDC)

    time.sleep(0.5)

    # Humans Guess
    print('--------------------------------------------')
    print('> Your Turn: ' + str(number) + ' + [?] = 10')
    #human_answer = input('Enter Your Answer [1-10]: ')
    human_answer = (10 - number)
    print('> Your Turn Auto Chosen: ' + str(human_answer))
    if number + int(human_answer) == 10:
        # Update the known number bonds
        bonds[number] = (bonds[number] + int(human_answer)) / 2
        print(' + Correct! Now the machine thinks it is ' + str(round(bonds[number])))
    else:
        print(' - Wrong! Are you trying to mislead a poor machine?')
      
    
    time.sleep(0.5)
	
    