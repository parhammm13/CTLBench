import random

def generate_party_routines(name):
    """Generates dynamic college party routines for Jake."""
    # Define possible party activities
    party_activities = [
        "plays beer pong", "dances", "chats with friends", "grabs a late-night snack",
        "walks around the party", "crashes on the couch", "mixes drinks",
        "plays a card game", "takes a group photo", "joins a karaoke session",
        "takes part in a drinking challenge", "helps clean up", "sings along to music",
        "tells a funny story", "does a party trick", "meets new people",
        "tries a new cocktail", "challenges someone to a dance-off",
        "plays a round of flip cup", "takes selfies with friends", "starts a game of charades",
        "takes a break on the balcony", "discusses favorite movies", "tries to convince people to do a prank"
    ]

    # Generate three unique party routines
    routine1 = random.sample(party_activities, random.randint(4, 6)) + ["crashes on the couch"]
    routine2 = random.sample(party_activities, random.randint(4, 6)) + ["crashes on the couch"]
    routine3 = random.sample(party_activities, random.randint(4, 6)) + ["crashes on the couch"]

    # Create the context in natural language
    context = f"""
{name} has three different ways he enjoys a college party, and each night he randomly follows one:
- Party Style 1: {', then '.join(routine1)}.
- Party Style 2: {', then '.join(routine2)}.
- Party Style 3: {', then '.join(routine3)}.
    """

    routines = {"Party Style 1": routine1, "Party Style 2": routine2, "Party Style 3": routine3}
    return routines, context

def random_party_name():
    """Generates a random partygoer name."""
    names = ["Jake", "Ryan", "Brandon", "Tyler", "Ethan", "Lucas", "Nathan", "Kyle"]
    return random.choice(names)

def generate_party_question(routines, name):
    """Generates dynamic party-related questions."""
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
            question = f"If {name} {x} tonight, will he {y} afterward?"
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
        truth_value = "crashes on the couch" in routine
        question = f"If {name} {x} or {y}, what are we sure he will eventually do?"
        ctl_type = "AF"
        question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
        question_type_str = "Semantic"

    elif question_type == 5:
        # Type 5: What does Jake do at every party?
        truth_value = "crashes on the couch"
        question = f"What does {name} do at every party?"
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

def generate_party_question_type7():
    """Generates a dynamic question set for a college party routine."""
    name = random_party_name()  # Generate a random partygoer name
    routines, context = generate_party_routines(name)  # Create party routines
    question, truth_value, ctl_type , question_type_str= generate_party_question(routines, name)  # Generate party-related question

    return (context + "\n" + question), truth_value, ctl_type, question_type_str

# Main Execution
question7, truth_label7, ctl_type7 , question_type_str= generate_party_question_type7()
print(question7)
print(truth_label7)
print(ctl_type7)
