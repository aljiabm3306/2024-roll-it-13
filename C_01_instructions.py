print("🎲🎲🎲 Roll It 13 🎲🎲🎲")


# loop for testing purposes

while True:
    want_insturctions = input("Do you want to read the instructions? "). lower()

    # checks users enter yes (Y) or no (N)
    if want_insturctions == "yes":
        print("You chose yes")
    elif want_insturctions =="y":
        print("you chose yes")
    elif want_insturctions == "no":
        print("You chose no")
    elif want_insturctions == "n":
        print("you chose no")
    else:
        print("You did not chose a valid response")

