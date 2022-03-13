
answer = input("Would you like to play/ (yes/no)")

if answer.lower().strip() == "yes":

    answer = input("You wake up in a dark room there are two rooms would you like to go north or east. Where would you like to go?").lower().strip()
    if answer == "east":
        answer = input("You have entered a very bright room, there are two other doors one leads north and the other goes east. Which one do you choose?")

        if answer == "east":
            print("You notice a massive creature and you die.")
    elif answer == "north":
        answer == input("You have entered a very highly decorated bedroom. There is a single door leading east go through?").lower().strip()
        if answer =="east":
            answer == input("This room has a single door leading north you wonder what it may lead to. Your body feels exhausted you better hurry!!")
    else:
        print("Not an option, you died!!")

else:
    print("Maybe another time.")