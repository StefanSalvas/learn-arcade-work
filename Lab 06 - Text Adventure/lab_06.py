while True:
    answer = input("Would you like to explore the small dungeon?\n(yes/no)")

    if answer.lower().strip() == "yes":

        answer = input("You wake up in a dark room there are two rooms would you like to go north or east.\n Where would you like to go?").lower().strip()
        if answer == "east":
            answer = input("You have entered a very bright room, there are two other doors one leads north and the other goes east.\n Which one do you choose?")

            if answer == "east":
                print("You notice a massive creature you get eaten alive oh no!!.")

        if answer == "north":
            answer == input("You have entered a highly decorated bedroom.\n There is a single door leading east go through?").lower().strip()
            if answer == "east":
                answer == input("This room has a single door leading north you wonder what it may lead to. Your body feels exhausted you better hurry!!")
            elif answer == "north":
                answer == input("You have discovered the alter of Gods and have gained total enlightenment!!\n You have completed the game congratulations hero")
            else:
                print("Not an option you are killed")
        elif answer == "south":
            print("You walk into the wall and knock yourself out.")
        else:
            print("Not an option, you died!!")

    else:
        print("Maybe another time.")
    break