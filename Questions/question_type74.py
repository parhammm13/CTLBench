import random

def generate_cleaning_routines(name):
    """Generates dynamic house cleaning routines for a person."""
    # Define possible cleaning activities
    cleaning_activities = [
        "vacuums the living room", "mops the floors", "dusts the furniture", "cleans the kitchen",
        "takes out the trash", "relaxes with a cup of tea", "soaks the dishes in the sink",
        "organizes the pantry", "washes the dishes", "scrubs the bathroom", "changes the bed sheets",
        "wipes down windows", "sweeps the hallway", "cleans the refrigerator", "organizes the closet",
        "wipes down the counters", "tidies up the living room", "cleans the mirrors",
        "disinfects door handles", "washes the laundry", "folds and puts away clothes",
        "cleans under the furniture", "vacuum cleans the carpet"
    ]

    # Generate three unique cleaning routines
    routine1 = random.sample(cleaning_activities, random.randint(4, 6)) + ["relaxes with a cup of tea"]
    routine2 = random.sample(cleaning_activities, random.randint(4, 6)) + ["relaxes with a cup of tea"]
    routine3 = random.sample(cleaning_activities, random.randint(4, 6)) + ["relaxes with a cup of tea"]

    # Create the context in natural language
    context = f"""
{name} has three different house cleaning routines, and each day they randomly follow one:
- Routine 1: {', then '.join(routine1)}.
- Routine 2: {', then '.join(routine2)}.
- Routine 3: {', then '.join(routine3)}.
    """

    routines = {"Routine 1": routine1, "Routine 2": routine2, "Routine 3": routine3}
    return routines, context

def random_cleaning_name():
    """Generates a random name for the cleaning routine."""
    names = ["Emma", "Sophia", "Olivia", "Ava", "Mia", "Lily", "Zoe", "Grace"]
    return random.choice(names)

def generate_cleaning_question(routines, name):
    """Generates dynamic house cleaning-related questions."""
    question_type = random.choice([1, 2, 3, 4, 5, 6])  # Select a question type randomly
    ctl_type = ""
    question = ""
    truth_value = ""

    if question_type == 1:
        # Type 1: If X happens, will Y follow?
        routine = random.choice(list(routines.values()))
        if len(routine) > 2:
            x, y = random.sample(routine[:-1], 2)
            truth_value = routine.index(x) < routine.index(y)
            question = f"If {name} {x} today, will they {y} afterward?"
            ctl_type = "AX"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    elif question_type == 2:
        # Type 2: If Y happens, is there a possibility that X happened earlier?
        routine = random.choice(list(routines.values()))
        if len(routine) > 2:
            x, y = random.sample(routine[1:], 2)
            truth_value = routine.index(y) > routine.index(x)
            question = f"If {name} {y}, is there a possibility that they {x} earlier?"
            ctl_type = "EU"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    elif question_type == 3:
        # Type 3: Will X and Y ever happen together in the same sequence?
        routine = random.choice(list(routines.values()))
        if len(routine) > 2:
            x, y = random.sample(routine[:-1], 2)
            truth_value = routine.index(x) < routine.index(y)
            question = f"Will {name} ever {x} and then {y}?"
            ctl_type = "EF"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    elif question_type == 4:
        # Type 4: If X or Y happens, what are we sure will happen eventually?
        routine = random.choice(list(routines.values()))
        x, y = random.sample(routine[:-1], 2)
        truth_value = "relaxes with a cup of tea" in routine
        question = f"If {name} {x} or {y}, what are we sure they will eventually do?"
        ctl_type = "AF"
        question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
        question_type_str = "Semantic"

    elif question_type == 5:
        # Type 5: What does the person do after every cleaning session?
        truth_value = "relaxes with a cup of tea"
        question = f"What does {name} do after every cleaning session?"
        ctl_type = "AG"
        question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <name the activity>}'''
        question_type_str = "Semantic"

    elif question_type == 6:
        # Type 6: Does X always follow Y?
        routine = random.choice(list(routines.values()))
        if len(routine) > 2:
            x, y = random.sample(routine[:-1], 2)
            truth_value = all(r.index(y) < r.index(x) for r in routines.values() if y in r and x in r)
            question = f"Does {name} always {x} after {y}?"
            ctl_type = "AU"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    return question, truth_value, ctl_type, question_type_str

def generate_cleaning_question_type7():
    """Generates a dynamic question set for a house cleaning routine."""
    name = random_cleaning_name()  # Generate a random cleaning-related name
    routines, context = generate_cleaning_routines(name)  # Create cleaning routines
    question, truth_value, ctl_type, question_type_str = generate_cleaning_question(routines, name)  # Generate cleaning-related question

    return (context + "\n" + question), truth_value, ctl_type, question_type_str

# Main Execution
question7, truth_label7, ctl_type7, question_type_str = generate_cleaning_question_type7()
print(question7)
print(truth_label7)
print(ctl_type7)
print( question_type_str)
