import random
import json

# Lists of possible replacements
names1 = ["Isabella", "Charlotte", "Amelia", "Jordan", "Stephen"]
names2 = ["Andy", "Alex", "Josh", "Alen", "Robert"]
places = ["coffee shop", "park", "library", "bookstore", "ice cream parlor"]


def generate_random_times():
    drive = random.randint(20, 100)
    bus = drive + random.randint(10, 25)
    i = random.randint(0, 3)

    if i == 0:
        bike = bus
        walk = bike + random.randint(10, 30)
    elif i == 1:
        bike = drive
        walk = bike + random.randint(10, 30)
    elif i == 2:
        walk = bus
        bike = walk - random.randint(10, 15)
    else:
        walk = drive
        bike = walk - random.randint(10, 15)

    return drive, bus, bike, walk


def create_question(name1, name2, times):
    story = f"""
{name1} and {name2} want to meet at a {place}. If {name1} drives to the {place}, they will arrive in {times[0]} minutes,
but if they takes the bus, they will arrive in {times[1]} minutes. {name2} will arrive in {times[2]} minutes if they rides 
their bike and will arrive in {times[3]} minutes if they walk to the {place}.
"""
    return story


# Generate random values
name1 = random.choice(names1)
name2 = random.choice(names2)
place = random.choice(places)
drive, bus, bike, walk = generate_random_times()

# Calculate maximum waiting time
maximum = abs(max(bus - bike, walk - drive))

questions = [
    f"""What is the maximum amount of time that one of them would be waiting for the other? 
Format your answer only as a JSON don't include the unit, like JSON = {{"explanation": <your step by step solution>, "answer": <number of minutes>}}
    """,
    f"""What is the minimum amount of time that one of them would be waiting for the other? 
Format your answer only as a JSON don't include the unit, like JSON = {{"explanation": <your step by step solution>, "answer": <number of minutes>}}
    """
]

answers = [
    maximum,
    0
]

arithmeticOrSemantic = [
    "arithmetic",
    "arithmetic",
]

type = [
    "complex",
    "complex"
]

# Print paragraph multiple times with questions and answers
def generate_question():
    i = random.randint(0, 1)
    question = create_question(name1, name2, [drive, bus, bike, walk])
    question = question + "\n" + questions[i]
    truth_label = answers[i]
    CTLType = type[i]
    questionType = arithmeticOrSemantic[i]
    return question, truth_label, CTLType, questionType
