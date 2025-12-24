def get_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(" Input cannot be empty. Try again.")

def get_number(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return value
        print(" Please enter a valid number.")

# Template choice with validation
while True:
    print("\nChoose a story template:")
    print("1 - Hospital")
    print("2 - Camping")
    print("3 - Fantasy Letter")
    template = input("Enter 1, 2 or 3: ")

    if template in ("1", "2", "3"):
        break
    print("Invalid choice. Please choose 1, 2, or 3.")

# ---------------- TEMPLATE 1 ----------------
if template == "1":
    number = get_number("Type number: ")
    time = get_text("Type measure of time: ")
    transport = get_text("Type mode of transportation: ")
    adjective1 = get_text("Type adjective: ")
    adjective2 = get_text("Type another adjective: ")
    noun1 = get_text("Type noun: ")
    color = get_text("Type color: ")
    body_part1 = get_text("Type part of the body: ")
    verb1 = get_text("Type verb: ")
    number2 = get_number("Type another number: ")
    noun2 = get_text("Type another noun: ")
    noun3 = get_text("Type another noun: ")
    body_part2 = get_text("Type another part of the body: ")
    verb2 = get_text("Type another verb: ")
    noun4 = get_text("Type another noun: ")
    adjective3 = get_text("Type one more adjective: ")
    silly_word = get_text("Type silly word: ")
    noun5 = get_text("Type final noun: ")

    print("\nHere's your story:\n")
    print(f"It was about {number} {time} ago when I arrived at the hospital in a {transport}.")
    print(f"The hospital is a/an {adjective1} place, there are a lot of {adjective2} {noun1} here.")
    print(f"There are nurses here who have {color} {body_part1}.")
    print(f"If someone wants to come into my room I told them that they have to {verb1} first.")
    print(f"I’ve decorated my room with {number2} {noun2}.")
    print(f"Today I talked to a doctor and they were wearing a {noun3} on their {body_part2}.")
    print(f"I heard that all doctors {verb2} {noun4} every day for breakfast.")
    print(f"The most {adjective3} thing about being in the hospital is the {silly_word} {noun5}!")

# ---------------- TEMPLATE 2 ----------------
elif template == "2":
    name = get_text("Type a person’s name: ")
    noun1 = get_text("Type a noun: ")
    adjective1 = get_text("Type an adjective (feeling): ")
    verb1 = get_text("Type a verb: ")
    adjective2 = get_text("Type another adjective (feeling): ")
    animal1 = get_text("Type an animal: ")
    verb2 = get_text("Type another verb: ")
    color = get_text("Type a color: ")
    verb_ing = get_text("Type a verb ending in 'ing': ")
    adverb = get_text("Type an adverb ending in 'ly': ")
    number = get_number("Type a number: ")
    time = get_text("Type a measure of time: ")
    color2 = get_text("Type another color: ")
    animal2 = get_text("Type another animal: ")
    number2 = get_number("Type another number: ")
    silly_word = get_text("Type a silly word: ")
    noun2 = get_text("Type another noun: ")

    print("\nHere's your story:\n")
    print(f"This weekend I am going camping with {name}.")
    print(f"I packed my lantern, sleeping bag, and {noun1}.")
    print(f"I am so {adjective1} to {verb1} in a tent.")
    print(f"I am {adjective2} we might see a(n) {animal1}.")
    print(f"While we’re camping, we are going to hike, fish, and {verb2}.")
    print(f"I have heard that the {color} lake is great for {verb_ing}.")
    print(f"Then we will {adverb} hike through the forest for {number} {time}.")
    print(f"If I see a {color2} {animal2}, I am going to bring it home as a pet!")
    print(f"At night we will tell {number2} {silly_word} stories and roast {noun2} around the campfire!")

# ---------------- TEMPLATE 3 ----------------
else:
    name = get_text("Type a person’s name: ")
    adjective1 = get_text("Type an adjective: ")
    color = get_text("Type a color: ")
    animal = get_text("Type an animal: ")
    place = get_text("Type a place: ")
    adjective2 = get_text("Type another adjective: ")
    creature1 = get_text("Type magical creature (plural): ")
    adjective3 = get_text("Type another adjective: ")
    creature2 = get_text("Type another magical creature (plural): ")
    room = get_text("Type a room in a house: ")
    noun1 = get_text("Type a noun: ")
    noun2 = get_text("Type another noun: ")
    plural_noun1 = get_text("Type plural noun: ")
    adjective4 = get_text("Type another adjective: ")
    plural_noun2 = get_text("Type plural noun: ")
    number = get_number("Type number: ")
    time = get_text("Type measure of time: ")
    verb_ing = get_text("Type verb ending in 'ing': ")
    adjective5 = get_text("Type another adjective: ")
    noun3 = get_text("Type another noun: ")

    print("\nHere's your story:\n")
    print(f"Dear {name},")
    print(f"I am writing to you from a {adjective1} castle in an enchanted forest.")
    print(f"I found myself here after riding a {color} {animal} in {place}.")
    print(f"There are {adjective2} {creature1} and {adjective3} {creature2} here!")
    print(f"In the {room} there is a pool full of {noun1}.")
    print(f"I sleep on a {noun2} of {plural_noun1} and dream of {adjective4} {plural_noun2}.")
    print(f"It feels like I have lived here for {number} {time}.")
    print(f"The only way to get here is {verb_ing} on a {adjective5} {noun3}!")

