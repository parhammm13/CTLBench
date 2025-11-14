import random

def generate_patrol_routines(name):
    """Generates dynamic superhero patrol routines for Blaze."""
    # Define possible superhero activities
    superhero_activities = [
        "stops a bank robbery", "chases a getaway car", "rescues hostages",
        "secures the crime scene", "checks for any remaining threats", "returns to headquarters",
        "scans the city from the rooftops", "monitors police radio", "intervenes in a street fight",
        "foils a villain’s plan", "saves civilians from danger", "helps repair property damage",
        "stops a mugging", "prevents a cyber attack", "fights off a supervillain",
        "helps the police with an investigation", "breaks up a gang operation",
        "shuts down an illegal weapons deal", "rescues people from a burning building",
        "stops a speeding car", "saves someone from falling off a building",
        "tracks a wanted criminal", "neutralizes a hostage situation",
        "helps an injured pedestrian", "safeguards a VIP escort mission",
        "disables a ticking bomb", "detects a hidden enemy trap"
    ]

    # Generate three unique superhero patrol routines
    patrol1 = random.sample(superhero_activities, random.randint(4, 6)) + ["returns to headquarters"]
    patrol2 = random.sample(superhero_activities, random.randint(4, 6)) + ["returns to headquarters"]
    patrol3 = random.sample(superhero_activities, random.randint(4, 6)) + ["returns to headquarters"]

    # Create the context in natural language
    context = f"""
{name} is a superhero who has three different patrol routines each night, and he randomly follows one:
- Patrol 1: {', then '.join(patrol1)}.
- Patrol 2: {', then '.join(patrol2)}.
- Patrol 3: {', then '.join(patrol3)}.
    """

    routines = {"Patrol 1": patrol1, "Patrol 2": patrol2, "Patrol 3": patrol3}
    return routines, context

def random_superhero_name():
    """Generates a random superhero name."""
    names = ["Blaze", "Shadow Knight", "Steel Sentinel", "Phoenix Guardian", "Night Stalker", "Storm Bringer"]
    return random.choice(names)

def generate_patrol_question(routines, name):
    """Generates dynamic superhero patrol-related questions."""
    question_type = random.choice([1, 2, 3, 4, 5, 6])  # Select a question type randomly
    ctl_type = ""
    question = ""
    truth_value = ""

    if question_type == 1:
        # Type 1: If X happens, will Y follow?
        patrol = random.choice(list(routines.values()))
        if len(patrol) > 2:
            x, y = random.sample(patrol[:-1], 2)
            truth_value = patrol.index(x) < patrol.index(y)
            question = f"If {name} {x} tonight, will he {y} afterward?"
            ctl_type = "AX"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    elif question_type == 2:
        # Type 2: If Y happens, is there a possibility that X happened earlier?
        patrol = random.choice(list(routines.values()))
        if len(patrol) > 2:
            x, y = random.sample(patrol[1:], 2)
            truth_value = patrol.index(y) > patrol.index(x)
            question = f"If {name} {y}, is there a possibility that he {x} earlier?"
            ctl_type = "EU"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    elif question_type == 3:
        # Type 3: Will X and Y ever happen together in the same sequence?
        patrol = random.choice(list(routines.values()))
        if len(patrol) > 2:
            x, y = random.sample(patrol[:-1], 2)
            truth_value = patrol.index(x) < patrol.index(y)
            question = f"Will {name} ever {x} and then {y}?"
            ctl_type = "EF"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    elif question_type == 4:
        # Type 4: If X or Y happens, what are we sure will happen eventually?
        patrol = random.choice(list(routines.values()))
        x, y = random.sample(patrol[:-1], 2)
        truth_value = "returns to headquarters" in patrol
        question = f"If {name} {x} or {y}, what are we sure he will eventually do?"
        ctl_type = "AF"
        question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
        question_type_str = "Semantic"

    elif question_type == 5:
        # Type 5: What does Blaze do at the end of every patrol?
        truth_value = "returns to headquarters"
        question = f"What does {name} do at the end of every patrol?"
        ctl_type = "AG"
        question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <name the activity>}'''
        question_type_str = "Semantic"

    elif question_type == 6:
        # Type 6: Does X always follow Y?
        patrol = random.choice(list(routines.values()))
        if len(patrol) > 2:
            x, y = random.sample(patrol[:-1], 2)
            truth_value = all(r.index(y) < r.index(x) for r in routines.values() if y in r and x in r)
            question = f"Does {name} always {x} after {y}?"
            ctl_type = "AU"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    return question, truth_value, ctl_type, question_type_str

def generate_patrol_question_type7():
    """Generates a dynamic question set for a superhero night patrol."""
    name = random_superhero_name()  # Generate a random superhero's name
    routines, context = generate_patrol_routines(name)  # Create superhero patrol routines
    question, truth_value, ctl_type , question_type_str= generate_patrol_question(routines, name)  # Generate patrol-related question

    return (context + "\n" + question), truth_value, ctl_type, question_type_str

# Main Execution
question7, truth_label7, ctl_type7 , question_type_str= generate_patrol_question_type7()
print(question7)
print(truth_label7)
print(ctl_type7, question_type_str)
