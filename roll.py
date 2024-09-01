#user to roll the dice
#add score until one
import random


def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll
while True:

    players=input("enter the number of players(1-4):")
    if players.isdigit():
        players=int(players)
        if 1<=players<=4:
            break
        else:
            print("must be between 2 to 4 players")
    else:
        print("INVALID")
max_score=50
player_scores=[0 for _ in range(players)]

while max(player_scores)<max_score:
    for player_idx in range(players):
        print(' player number',player_idx+1,"turn has just started!/n")
        current_score=0
        should_roll=input("would you like to roll(y)?")
        if should_roll.lower()!="y":
            break
        value=roll()
        if value==1:
            print("you rolles a 1 turn down")
            current_score=1
        else:
            current_score+=value
            print("you rolles a:",value)
        print("your score is:",current_score)
player_scores[player_idx]+=current_score
print("Your total score is:",player_scores[player_idx])
    