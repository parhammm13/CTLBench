import random

def generate_travel_routines(name):
    """Generates dynamic summer travel routines for Liam."""
    # Define possible travel activities
    travel_activities = [
        "visits a tropical beach", "goes snorkeling", "explores a nearby island", "tries local seafood",
        "takes a sunset boat ride", "relaxes in a hammock", "takes a road trip to the mountains",
        "hikes to a scenic viewpoint", "sets up a campsite", "enjoys a bonfire",
        "explores a historic city", "visits museums", "takes a guided cultural tour",
        "tries street food", "takes travel photos", "buys souvenirs", "goes kayaking",
        "visits an ancient temple", "watches a traditional performance", "takes a scenic train ride",
        "goes on a wildlife safari", "swims in a waterfall", "learns a local dance",
        "tries an adventure sport", "visits a national park", "rides a bicycle around the city",
        "watches the sunset from a cliff", "does a wine tasting tour", "enjoys a relaxing spa day"
    ]

    # Generate three unique travel plans
    trip1 = random.sample(travel_activities, random.randint(4, 6)) + ["relaxes in a hammock"]
    trip2 = random.sample(travel_activities, random.randint(4, 6)) + ["relaxes in a hammock"]
    trip3 = random.sample(travel_activities, random.randint(4, 6)) + ["relaxes in a hammock"]

    # Create the context in natural language
    context = f"""
{name} has three different summer travel plans, and each year he randomly follows one:
- Trip 1: {', then '.join(trip1)}.
- Trip 2: {', then '.join(trip2)}.
- Trip 3: {', then '.join(trip3)}.
    """

    routines = {"Trip 1": trip1, "Trip 2": trip2, "Trip 3": trip3}
    return routines, context

def random_travel_name():
    """Generates a random traveler's name."""
    names = ["Liam", "Noah", "Oliver", "Elijah", "James", "Benjamin", "Henry", "Alexander"]
    return random.choice(names)

def generate_travel_question(routines, name):
    """Generates dynamic travel-related questions."""
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
            question = f"If {name} {x} today, will he {y} afterward?"
            ctl_type = "AX"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    elif question_type == 2:
        # Type 2: If Y happens, is there a possibility that X happened earlier?
        routine = random.choice(list(routines.values()))
        if len(routine) > 2:
            x, y = random.sample(routine[1:], 2)
            truth_value = routine.index(y) > routine.index(x)
            question = f"If {name} {y}, is there a possibility that he {x} earlier?"
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
        truth_value = "relaxes in a hammock" in routine
        question = f"If {name} {x} or {y}, what are we sure he will eventually do?"
        ctl_type = "AF"
        question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
        question_type_str = "Semantic"

    elif question_type == 5:
        # Type 5: What does Liam do on every summer trip?
        truth_value = "relaxes in a hammock"
        question = f"What does {name} do on every summer trip?"
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

def generate_travel_question_type7():
    """Generates a dynamic question set for a summer travel routine."""
    name = random_travel_name()  # Generate a random traveler's name
    routines, context = generate_travel_routines(name)  # Create travel routines
    question, truth_value, ctl_type, question_type_str = generate_travel_question(routines, name)  # Generate travel-related question

    return (context + "\n" + question), truth_value, ctl_type, question_type_str

# Main Execution
question7, truth_label7, ctl_type7, question_type_str = generate_travel_question_type7()
print(question7)
print(truth_label7)
print(ctl_type7, question_type_str)
