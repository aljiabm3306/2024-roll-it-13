# Loop to check user enters yes / no
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks users enter yes (Y) or no (N)
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("You did not chose a valid response")


# main routine

print("🎲🎲🎲 Roll It 13 🎲🎲🎲")

while True:

    want_instructions = yes_no("Do you want to read the instructions? ")
    print(f"you said {want_instructions} to seeing the instructions")
