from animals import animals

user_input = input("Please enter the number of the habitat you would like to view: ")
habitat_number = int(user_input)

if 0 <= habitat_number < len(animals):
    print(animals[habitat_number])

print("---\nYou've reached the end of the program. To check another habitat, please restart the watcher.")
