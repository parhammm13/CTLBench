import random

def generate_mission_protocols(ship_name):
    """Generates dynamic mission protocols for a spaceship."""
    # Define possible space activities
    space_activities = [
        "conducts a planetary scan", "collects asteroid samples", "transmits data to Earth",
        "calibrates the navigation system", "performs an engine check", "activates the fuel thrusters",
        "monitors space anomalies", "adjusts trajectory", "runs a deep-space analysis", "deploys a satellite",
        "performs a gravity assist maneuver", "analyzes cosmic radiation", "launches a probe",
        "scans for alien signals", "tests communication systems", "studies a black hole",
        "performs emergency maneuvers", "gathers atmospheric data", "runs diagnostic tests",
        "maps an unknown planet", "performs a spacewalk", "examines meteor debris"
    ]

    # Randomly generate three unique mission protocols with 4-6 steps
    protocol1 = random.sample(space_activities, random.randint(4, 6)) + ["enters sleep mode"]
    protocol2 = random.sample(space_activities, random.randint(4, 6)) + ["enters sleep mode"]
    protocol3 = random.sample(space_activities, random.randint(4, 6)) + ["enters sleep mode"]

    # Create the mission context
    context = f"""
The {ship_name} spaceship has three different mission protocols, and each time the crew randomly follows one:
- Protocol 1: {', then '.join(protocol1)}.
- Protocol 2: {', then '.join(protocol2)}.
- Protocol 3: {', then '.join(protocol3)}.
    """

    protocols = {"Protocol 1": protocol1, "Protocol 2": protocol2, "Protocol 3": protocol3}
    return protocols, context

def random_ship_name():
    """Generates a random spaceship name."""
    ship_names = ["Odyssey-7", "Nebula Explorer", "Starhawk-9", "Cosmic Voyager", "Apollo-X", "Galactic Pioneer"]
    return random.choice(ship_names)

def generate_space_question(protocols, ship_name):
    """Generates dynamic space mission questions."""
    question_type = random.choice([1, 2, 3, 4, 5, 6])  # Select a random question type
    ctl_type = ""
    question = ""
    truth_value = ""

    if question_type == 1:
        # Type 1: If X happens, will Y follow?
        protocol = random.choice(list(protocols.values()))
        if len(protocol) > 2:
            x, y = random.sample(protocol[:-1], 2)
            truth_value = protocol.index(x) < protocol.index(y)
            question = f"If the crew {x} today, will they {y} afterward?\n"
            ctl_type = "AX"
            question += '''Format your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    elif question_type == 2:
        # Type 2: If Y happens, is there a possibility that X happened earlier?
        protocol = random.choice(list(protocols.values()))
        if len(protocol) > 2:
            x, y = random.sample(protocol[1:], 2)
            truth_value = protocol.index(y) > protocol.index(x)
            question = f"If the crew {y}, is there a possibility that they {x} earlier?\n"
            ctl_type = "EU"
            question += '''Format your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    elif question_type == 3:
        # Type 3: Will X and Y ever happen together in the same sequence?
        protocol = random.choice(list(protocols.values()))
        if len(protocol) > 2:
            x, y = random.sample(protocol[:-1], 2)
            truth_value = protocol.index(x) < protocol.index(y)
            question = f"Will the crew ever {x} and then {y}?\n"
            ctl_type = "EF"
            question += '''Format your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    elif question_type == 4:
        # Type 4: If X or Y happens, what are we sure will happen eventually?
        protocol = random.choice(list(protocols.values()))
        x, y = random.sample(protocol[:-1], 2)
        truth_value = "enters sleep mode" in protocol
        question = f"If the crew {x} or {y}, what are we sure they will eventually do?\n"
        ctl_type = "AF"
        question += '''Format your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
        question_type_str = "Semantic"

    elif question_type == 5:
        # Type 5: What does the crew do on every mission?
        truth_value = "enters sleep mode"
        question = f"What does the crew do on every mission?\n"
        ctl_type = "AG"
        question += '''Format your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <name the activity>}'''
        question_type_str = "Semantic"

    elif question_type == 6:
        # Type 6: Does X always follow Y?
        protocol = random.choice(list(protocols.values()))
        if len(protocol) > 2:
            x, y = random.sample(protocol[:-1], 2)
            truth_value = all(r.index(y) < r.index(x) for r in protocols.values() if y in r and x in r)
            question = f"Does the crew always {x} after {y}?\n"
            ctl_type = "AU"
            question += '''Format your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    return question, truth_value, ctl_type, question_type_str

def generate_space_question_type7():
    """Generates a dynamic question set with a spaceship theme."""
    ship_name = random_ship_name()  # Generate a random spaceship name
    protocols, context = generate_mission_protocols(ship_name)  # Create a new dynamic mission context
    question, truth_value, ctl_type, question_type_str = generate_space_question(protocols, ship_name)  # Generate a random space mission question

    return (context + "\n" + question), truth_value, ctl_type, question_type_str

# Main Execution
question7, truth_label7, ctl_type7, question_type_str7 = generate_space_question_type7()
print(question7)
print(truth_label7)
print(ctl_type7)
print(question_type_str7)
