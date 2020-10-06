import random

weapons = ['rock', 'paper', 'scissors']
counters = None
scores = {}
computer_weapon = None
player_weapon = None
player_name = None
player_score = 0


def get_name():
    global player_name
    player_name = input("Enter your name: ")
    print(f"Hello, {player_name}")
    
    
def get_scores(filename):
    score_file = open(filename, "r")
    for line in score_file:
        scores[line.split()[0]] = int(line.split()[1])
    score_file.close()
    

def get_weapons():
    global weapons
    global counters
    new_weapons = input()
    if new_weapons != "":
        weapons = new_weapons.split(",")
    print("Okay, let's start")
        
        
def get_input():
    command = input()
    if command == '!exit':
        return False
    else:
        return command
        
  
def get_winner():
    global player_score
    global counters
    counters = weapons[weapons.index(player_weapon) + 1:]
    counters += weapons[:weapons.index(player_weapon)]
    counters = counters[:len(counters) // 2]
    if computer_weapon in counters:
        print(f"Sorry, but the computer chose {computer_weapon}")
    elif player_weapon == computer_weapon:
        print(f"There is a draw ({computer_weapon})")
        player_score += 50
    else:
        print(f"Well done. The computer chose {computer_weapon} and failed")
        player_score += 100
    

get_name()
get_scores("rating.txt")
if player_name in scores:
    player_score = scores[player_name]
get_weapons()
while True:
    player_weapon = get_input()
    if player_weapon:
        if player_weapon in weapons:
            computer_weapon = random.choice(weapons)
            get_winner()
        else:
            if player_weapon == '!rating':
                print(f"Your rating: {player_score}")
            else:
                print("Invalid input")
    else:
        print("Bye!")
        break

    