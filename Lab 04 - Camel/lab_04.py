import random


def main():
    print("Welcome to Hoth!")
    print("You have stolen a Tantan to make your way across the great Empire defense,")
    print("The Empire want their Tantan back and are chasing you down!")
    print("Survive your trek and outrun the Empire's forces.\n")
    # variables
    miles_Traveled = 0
    thirst = 0
    tantanFatigue = 0
    empireTraveled = -20
    canteen = 3
    done = False
    oasis = 0

    # start main loop
    while not done:
        empireBehind = miles_Traveled - empireTraveled
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
            print("Your Tantan is this tired ", tantanFatigue)
            print("The Empire is ", empireBehind, "miles behind you.")
        # rest for night
        elif userInput.lower() == "d":
            tantanFatigue *= 0
            print("Your Tantan feels refreshed and happy his fatigue is  ", tantanFatigue)
            empireTraveled += random.randrange(7, 15)
        # go all out
        elif userInput.lower() == "c":
            print("You traveled ", fullSpeed, "miles! You are as fast as a Podracer!!")
            miles_Traveled += fullSpeed
            thirst += 1
            tantanFatigue += random.randrange(1, 4)
            empireTraveled += random.randrange(7, 15)
            oasis = random.randrange(1, 21)

        # jog at moderate speed
        elif userInput.lower() == "b":
            print("You traveled ", moderateSpeed, "miles! You may want to hurry!!")
            miles_Traveled += moderateSpeed
            thirst += 1
            tantanFatigue += 1
            empireTraveled += random.randrange(7, 15)
            oasis = random.randrange(1, 21)

            # drink from canteen
        elif userInput.lower() == "a":
            if canteen == 0:
                print("You're out of water uh oh.")
            else:
                canteen -= 1
                thirst *= 0
                print("You have ", canteen, "drinks left and you are no longer thirsty yay.")

        # not done check
        if oasis == 20:
            tantanFatigue *= 0
            thirst *= 0
            canteen = 3
            print("You found an oasis! After taking a drink you filled your canteen and the Tantan is refreshed.")
        if empireBehind <= 15:
            print("The Empire is drawing near run for your life")
        if miles_Traveled >= 200 and not done:
            print("You made it across the Empire's defense, you win!")
            done = True
        if empireTraveled >= miles_Traveled:
            print("The Empire's forces shot you!!.")
            print("You're dead!")
            done = True
        if thirst > 4 and thirst <= 6 and not done:
            print("You are thirsty")
        if thirst > 6:
            print("You died of dehydration! sorry :(")
            done = True
        if tantanFatigue > 5 and tantanFatigue <= 8 and not done:
            print("Your Tantan is getting tired.")
        if tantanFatigue > 8:
            print("Your Tantan is dead.")
            done = True
main()





