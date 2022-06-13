#William Williams
import random
import time
def fatal_flaw():
    if your_choice.lower() == 'rock':
        robot_choice = 'scissors'
    elif your_choice.lower() == 'paper':
        robot_choice = 'rock'
    else:
        robot_choice = 'paper'
    time.sleep(1)
    print('The Robot Chooses', robot_choice.upper())
    time.sleep(1)
    print('You chose', your_choice.upper())
    time.sleep(2)
    print('You Win!')
    print('You Win!')
    print('You Win!')
    
options_list = ['rock', 'paper', 'scissors']
print('Welcome to the Unbeatable Rock,Paper, Scissors Robot!')
time.sleep(1)
print('If you think you have a chance, go ahead and enter rock, paper, or scissors in the prompt below.')
time.sleep(1)
your_choice = input('Enter Rock, Paper, or Scissors HERE:>> ')
time.sleep(1)
while your_choice not in options_list:
    print('Sorry! You have to enter rock, paper, or scissors.')
    time.sleep(1)
    print('Our system will not accept any other values.')
    time.sleep(1)
    your_choice = input('Enter rock, paper, or scissors HERE:>> ')
if your_choice.lower() in options_list:
    robot_choice = random.choice(options_list)
    fatal_flaw()

    



    
    
    
    
    


