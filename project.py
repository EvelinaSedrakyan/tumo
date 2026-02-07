import random

print("Welcome to Mad Libs!!")

while True:
    print("\nChoose a story template:")
    print("1 - Hospital")
    print("2 - Camping")
    print("3 - Fantasy Letter")

    template = input("Enter 1, 2 or 3: ")

    if template in ("1", "2", "3"):
        break
    else:
        print("Invalid choice. Try again.")

print("\nYour lucky number today is:", random.randint(1, 10))

def safe_input(text):
    value = input(text)
    while value.strip() == "":
        print("Input cannot be empty.")
        value = input(text)
    return value

def safe_int(text):
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Please enter a valid number.")

if template == "1":
    number = safe_int("Type number: ")
    time = safe_input("Type measure of time: ")
    transport = safe_input("Type mode of transportation: ")
    adjective1 = safe_input("Type adjective: ")
    adjective2 = safe_input("Type another adjective: ")
    noun1 = safe_input("Type noun: ")

    print("\nHere's your story:\n")
    print("It was about", number, time, "ago when I arrived at the hospital in a", transport + ".")
    print("The hospital is a/an", adjective1, "place with many", adjective2, noun1 + ".")

elif template == "2":
    name = safe_input("Type a person’s name: ")
    noun = safe_input("Type a noun: ")
    adjective = safe_input("Type an adjective: ")
    verb = safe_input("Type a verb: ")

    print("\nHere's your story:\n")
    print("This weekend I am going camping with", name + ".")
    print("I packed my bag with", noun + ".")
    print("I am very", adjective, "to", verb, "in the woods.")

else:
    name = safe_input("Type a person’s name: ")
    adjective = safe_input("Type an adjective: ")
    animal = safe_input("Type an animal: ")
    place = safe_input("Type a place: ")

    print("\nHere's your story:\n")
    print("Dear", name + ",")
    print("I am writing from a", adjective, "land.")
    print("I arrived here riding a", animal, "through", place + ".")
