import random
import json

# Lists of possible replacements
names1 = ["Emma", "Leo", "Serge", "Sam", "Roy"]
names2 = ["Oliver", "Carlos", "Kevin", "Gary", "Alen"]


def generate_random_times():
    drive = random.randint(2, 10)
    bus = drive + random.randint(1, 2)
    i = random.randint(0, 3)

    if i == 0:
        bike = bus
        walk = bike + random.randint(1, 2)
    elif i == 1:
        bike = drive
        walk = bike + random.randint(1, 2)
    elif i == 2:
        walk = bus
        bike = walk - random.randint(1, 1)
    else:
        walk = drive
        bike = walk - random.randint(1, 1)

    return drive, bus, bike, walk


def create_question(name1, name2, times):
    story = f"""
{name1} and {name2} are reading the same book and racing to finish it. If {name1} wears their 
reading glasses, they will finish in {drive} hours, but if they reads without them, it will 
take them {bus} hours. {name2} will finish in {bike} hours if they use their magnifying glasses 
but will take {walk} hours if they read without any aid.
"""
    return story


# Generate random values
name1 = random.choice(names1)
name2 = random.choice(names2)
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