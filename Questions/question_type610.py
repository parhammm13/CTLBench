import random
import json

# Lists of possible replacements
names1 = ["Alice", "Simon", "Jrue", "Brook", "Sal"]
names2 = ["Ben", "Tyrese", "Damian", "Brian", "Joey"]
places = ["article", "blog", "post", "book", "lecture"]


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
{name1} and {name2} are typing an {place}. If {name1} uses a mechanical keyboard, they will finish in {drive} 
minutes, but if they type on a slow, old keyboard, it will take them {bus} minutes. {name2} will finish 
in {bike} minutes if they use a laptop keyboard but will take {walk} minutes if they type on a touchscreen.
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

type = [
    "complex",
    "complex",
]

arithmeticOrSemantic = [
    "arithmetic",
    "arithmetic"
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