import random

def roll_dice():

    #dice art as dictionary
    dice_art = {
        1: (
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘",
        ),
        2: (
            "┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘",
        ),
        3: (
            "┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘",
        ),
        4: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        5: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        6: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
    }


    #input from user
    roll = input("Roll the dice? [Y/N]  ")
    num = int(input("Enter the number of dice to be rolled : "))

    while roll.lower() == "y":
        #roll the dice
        dice = []
        for count in range(num):
            dice.append(random.randint(1,6))

        #printing the result
        print("The results are : ")  
        print(*dice, sep = ", ")

        #printing the simulation
        for count in range(num):
            print("\n".join(dice_art[dice[count]]))


        roll = input("Roll again? [Y/N]  ")


roll_dice()