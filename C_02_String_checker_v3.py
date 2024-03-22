# Check that users have entered a valid
# option based on a lis
def string_checker(question, valid_ans):

    error = f"Please enter a valid option from the following list: {valid_ans}\n"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        print(error)


yes_no = ("yes", "no")
rps_options = ("rock", "paper", "scissors", "xxx")

want_instructions = string_checker("Do you want to see the instructions? ",
                                   yes_no)
print(f"You chose {want_instructions}")

user_choice = string_checker("R / P / S ? ",
                                   rps_options)
print(f"You chose {user_choice}")