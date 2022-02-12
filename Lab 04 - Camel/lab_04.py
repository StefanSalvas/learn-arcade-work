import random


def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert,")
    print("The natives want their camel back and are chasing you down!")
    print("Survive your desert trek and outrun the natives.\n")
    # variables
    miles_Traveled = 0
    thirst = 0
    camelFatigue = 0
    nativesTraveled = -20
    canteen = 3
    done = False
    oasis = 0

    # start main loop
    while not done:
        nativesBehind = miles_Traveled - nativesTraveled
        fullSpeed = random.randrange(10, 21)
        moderateSpeed = random.randrange(5, 13)
        print("""
        A. Drink from your canteen.
        B. Ahead at moderate speed.
        C. Ahead full speed.
        D. Stop for the night.
        E. Status check
        Q. Quit.""")
        print()
        userInput = input("Your choice? ")
        if userInput.lower() == "q":
            done = True

        # status
        elif userInput.lower() == "e":
            print("Miles traveled: ", miles_Traveled)
            print("Drinks in canteen: ", canteen)
            print("Your camel has ", camelFatigue, "amount of fatigue.")
            print("The natives are ", nativesBehind, "miles behind you.")
        # rest for night
        elif userInput.lower() == "d":
            camelFatigue *= 0
            print("Your camel feels refreshed and happy his fatigue is now ", camelFatigue)
            nativesTraveled += random.randrange(7, 15)
        # go all out
        elif userInput.lower() == "c":
            print("You traveled ", fullSpeed, "miles! You are as fast as Shadowfaux!!")
            miles_Traveled += fullSpeed
            thirst += 1
            camelFatigue += random.randrange(1, 4)
            nativesTraveled += random.randrange(7, 15)
            oasis = random.randrange(1, 21)

        # jog at moderate speed
        elif userInput.lower() == "b":
            print("You traveled ", moderateSpeed, "miles! You may want to hurry!!")
            miles_Traveled += moderateSpeed
            thirst += 1
            camelFatigue += 1
            nativesTraveled += random.randrange(7, 15)
            oasis = random.randrange(1, 21)

            # drink from canteen
        elif userInput.lower() == "a":
            if canteen == 0:
                print("You're out of water.")
            else:
                canteen -= 1
                thirst *= 0
                print("You have ", canteen, "drinks left and you are no longer thirsty.")

        # not done check
        if oasis == 20:
            camelFatigue *= 0
            thirst *= 0
            canteen = 3
            print("You found an oasis! After taking a drink you filled your canteen and the camel is refreshed.")
        if nativesBehind <= 15:
            print("The natives are drawing near!")
        if miles_Traveled >= 200 and not done:
            print("You made it across the desert, you win!")
            done = True
        if nativesTraveled >= miles_Traveled:
            print("The natives caught and beheaded you.")
            print("You're dead!")
            done = True
        if thirst > 4 and thirst <= 6 and not done:
            print("You are thirsty")
        if thirst > 6:
            print("You died of dehydration! sorry :(")
            done = True
        if camelFatigue > 5 and camelFatigue <= 8 and not done:
            print("Your camel is getting tired.")
        if camelFatigue > 8:
            print("Your camel is dead.")
            done = True
main()





