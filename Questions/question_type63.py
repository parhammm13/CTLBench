import random
import json

# Lists of possible replacements
names1 = ["hiker", "goose", "bear"]
names2 = ["mountain goat", "dear", "tiger"]
places = ["water spring", "mountain peak", "large tree", "cave", "cabin"]


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
A {name1} and a {name2} are heading to a {place}. If the {name1} takes the direct trail, they 
will reach the spring in {drive} minutes, but if they follow the safer, winding path, it will take {bus} minutes. 
The {name2} will arrive in {bike} minutes if it climbs directly but will take {walk} minutes if it follows a 
gentler slope.
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
    "arithmetic"
]

type = [
    "complex",
    "complex",
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