from animals import animals

exit_program = False

while not exit_program:
    user_input = input("Please enter the number of the habitat you would like to view: ")

    if user_input.lower() == "exit":
        print("See you later!")
        exit_program = True
    else:
        habitat_number = int(user_input)

        if 0 <= habitat_number < len(animals):
            print(animals[habitat_number])
