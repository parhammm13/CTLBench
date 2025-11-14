import random

def generate_mission_protocols(name):
    """Generates dynamic secret agent mission protocols for Ethan."""
    # Define possible espionage activities
    espionage_activities = [
        "infiltrates a high-security building", "disables the security system", "gathers intel from enemy files",
        "plants a tracking device", "evades the guards", "escapes to the safehouse", "poses as a diplomat",
        "distracts the target", "copies confidential documents", "sends a secret message to headquarters",
        "evades a tailing enemy agent", "engages in a rooftop chase", "neutralizes an enemy spy",
        "retrieves a stolen microchip", "hacks into a classified database", "intercepts an encrypted message",
        "takes down a secret facility", "surveils a top-secret location", "rescues an informant",
        "plants an explosive charge", "steals blueprints for a prototype weapon", "disguises as an enemy operative",
        "listens in on a confidential meeting", "meets a double agent", "detonates a remote-controlled EMP",
        "secures an escape route", "extracts a captured ally"
    ]

    # Generate three unique mission protocols
    mission1 = random.sample(espionage_activities, random.randint(4, 6)) + ["escapes to the safehouse"]
    mission2 = random.sample(espionage_activities, random.randint(4, 6)) + ["escapes to the safehouse"]
    mission3 = random.sample(espionage_activities, random.randint(4, 6)) + ["escapes to the safehouse"]

    # Create the context in natural language
    context = f"""
{name} is a secret agent who has three different mission protocols, and each time he randomly follows one:
- Mission 1: {', then '.join(mission1)}.
- Mission 2: {', then '.join(mission2)}.
- Mission 3: {', then '.join(mission3)}.
    """

    protocols = {"Mission 1": mission1, "Mission 2": mission2, "Mission 3": mission3}
    return protocols, context

def random_agent_name():
    """Generates a random secret agent's name."""
    names = ["Ethan", "James", "Jason", "Gabriel", "Lucas", "Nolan", "Xavier", "Damian"]
    return random.choice(names)

def generate_mission_question(protocols, name):
    """Generates dynamic espionage-related questions."""
    question_type = random.choice([1, 2, 3, 4, 5, 6])  # Select a question type randomly
    ctl_type = ""
    question = ""
    truth_value = ""
    question_type_str = ""
    if question_type == 1:
        # Type 1: If X happens, will Y follow?
        protocol = random.choice(list(protocols.values()))
        if len(protocol) > 2:
            x, y = random.sample(protocol[:-1], 2)
            truth_value = protocol.index(x) < protocol.index(y)
            question = f"If {name} {x} today, will he {y} afterward?"
            ctl_type = "AX"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    elif question_type == 2:
        # Type 2: If Y happens, is there a possibility that X happened earlier?
        protocol = random.choice(list(protocols.values()))
        if len(protocol) > 2:
            x, y = random.sample(protocol[1:], 2)
            truth_value = protocol.index(y) > protocol.index(x)
            question = f"If {name} {y}, is there a possibility that he {x} earlier?"
            ctl_type = "EU"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    elif question_type == 3:
        # Type 3: Will X and Y ever happen together in the same sequence?
        protocol = random.choice(list(protocols.values()))
        if len(protocol) > 2:
            x, y = random.sample(protocol[:-1], 2)
            truth_value = protocol.index(x) < protocol.index(y)
            question = f"Will {name} ever {x} and then {y}?"
            ctl_type = "EF"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    elif question_type == 4:
        # Type 4: If X or Y happens, what are we sure will happen eventually?
        protocol = random.choice(list(protocols.values()))
        x, y = random.sample(protocol[:-1], 2)
        truth_value = "escapes to the safehouse" in protocol
        question = f"If {name} {x} or {y}, what are we sure he will eventually do?"
        ctl_type = "AF"
        question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
        question_type_str = "Semantic"

    elif question_type == 5:
        # Type 5: What does Ethan do after every mission?
        truth_value = "escapes to the safehouse"
        question = f"What does {name} do after every mission?"
        ctl_type = "AG"
        question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <name the activity>}'''
        question_type_str = "Semantic"

    elif question_type == 6:
        # Type 6: Does X always follow Y?
        protocol = random.choice(list(protocols.values()))
        if len(protocol) > 2:
            x, y = random.sample(protocol[:-1], 2)
            truth_value = all(r.index(y) < r.index(x) for r in protocols.values() if y in r and x in r)
            question = f"Does {name} always {x} after {y}?"
            ctl_type = "AU"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    return question, truth_value, ctl_type, question_type_str

def generate_mission_question_type7():
    """Generates a dynamic question set for a secret agent mission."""
    name = random_agent_name()  # Generate a random secret agent's name
    protocols, context = generate_mission_protocols(name)  # Create mission protocols
    question, truth_value, ctl_type , question_type_str= generate_mission_question(protocols, name)  # Generate espionage-related question

    return (context + "\n" + question), truth_value, ctl_type, question_type_str

# Main Execution
question7, truth_label7, ctl_type7 , question_type_str= generate_mission_question_type7()
print(question7)
print(truth_label7)
print(ctl_type7, question_type_str)
