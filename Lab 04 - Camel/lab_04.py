import random

def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.\n")

    # define variables
    done = False
    miles_traveled = 0
    thirst= 0
    camel_tiredness = 0
    natives_traveled = -20
    canteen = 3

    while done==False:
        print("""        A. Drink from your canteen.
        B. Ahead moderate speed.
        C. Ahead full speed.
        D. Stop for the night.
        E. Status check.
        Q. Quit.\n""")

        user_choice = input("What is your choice? ")

        # game logic

        if user_choice.upper() == "Q":
            print("You have quit the game.")
            break
        elif user_choice == "E":
            print("\nYou have traveled " + str(miles_traveled) + " miles.")
            print("You have " + str(canteen) + " drinks left.")
            print("The natives are " + str(miles_traveled - natives_traveled) + " miles behind you.\n")
        elif user_choice == "D":
            print("\nYou have stopped for the night to rest.")
            print("Your camel is rested and happy!")
            natives_traveled=natives_traveled+random.randrange(7, 14)
            print("The natives are " + str(miles_traveled - natives_traveled) + " miles behind you.\n")
        elif user_choice == "C":
            print("\nYour camel runs like shadowfaux!.")
            miles_traveled=miles_traveled+random.randrange(10, 20)
            camel_tiredness=camel_tiredness+random.randrange(1,3)
            natives_traveled=natives_traveled+random.randrange(7, 14)
            print("The natives are " + str(miles_traveled - natives_traveled) + " miles behind you.\n")
        elif user_choice == "B":
            print("\nYour camel takes a stroll.")
            miles_traveled=miles_traveled+random.randrange(5, 12)
            camel_tiredness=camel_tiredness+1
            natives_traveled=natives_traveled+random.randrange(7, 14)
            print("The natives are " + str(miles_traveled - natives_traveled) + " miles behind you.\n")
        elif user_choice.upper() == "A":
            if canteen>0:
                thirst=0
                canteen=canteen-1
                print("\nTastes great!")
        else:
            print("\nYou have no more drinks!!\n")






main()
