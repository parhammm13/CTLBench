import random

def generate_vr_adventures(name):
    """Generates dynamic VR adventure games for Alex."""
    # Define possible VR adventure activities
    vr_activities = [
        "explores a mysterious dungeon", "solves a puzzle", "battles a monster",
        "collects a rare artifact", "completes the level", "removes the VR headset",
        "hacks into a futuristic city’s security system", "sneaks past enemy guards",
        "reaches the mainframe", "downloads classified data", "completes the mission",
        "pilots a spaceship through an asteroid field", "engages in a space battle",
        "docks at a space station", "unlocks a hidden chamber", "discovers ancient ruins",
        "deciphers encrypted messages", "finds a legendary weapon", "defeats a boss enemy",
        "solves a hacking challenge", "flies through a wormhole", "defends a cyber-network",
        "meets an AI character", "escapes from a digital prison", "retrieves lost treasure",
        "interacts with a virtual companion", "explores an alien planet"
    ]

    # Generate three unique VR adventure experiences
    game1 = random.sample(vr_activities, random.randint(4, 6)) + ["removes the VR headset"]
    game2 = random.sample(vr_activities, random.randint(4, 6)) + ["removes the VR headset"]
    game3 = random.sample(vr_activities, random.randint(4, 6)) + ["removes the VR headset"]

    # Create the context in natural language
    context = f"""
{name} is an avid gamer who plays different types of virtual reality adventure games, and each time he randomly selects one:
- Game 1: {', then '.join(game1)}.
- Game 2: {', then '.join(game2)}.
- Game 3: {', then '.join(game3)}.
    """

    games = {"Game 1": game1, "Game 2": game2, "Game 3": game3}
    return games, context

def random_gamer_name():
    """Generates a random gamer's name."""
    names = ["Alex", "Jordan", "Chris", "Taylor", "Morgan", "Robin", "Casey", "Jamie"]
    return random.choice(names)

def generate_vr_question(games, name):
    """Generates dynamic VR adventure-related questions."""
    question_type = random.choice([1, 2, 3, 4, 5, 6])  # Select a question type randomly
    ctl_type = ""
    question = ""
    truth_value = ""

    if question_type == 1:
        # Type 1: If X happens, will Y follow?
        game = random.choice(list(games.values()))
        if len(game) > 2:
            x, y = random.sample(game[:-1], 2)
            truth_value = game.index(x) < game.index(y)
            question = f"If {name} {x} today, will he {y} afterward?"
            ctl_type = "AX"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    elif question_type == 2:
        # Type 2: If Y happens, is there a possibility that X happened earlier?
        game = random.choice(list(games.values()))
        if len(game) > 2:
            x, y = random.sample(game[1:], 2)
            truth_value = game.index(y) > game.index(x)
            question = f"If {name} {y}, is there a possibility that he {x} earlier?"
            ctl_type = "EU"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    elif question_type == 3:
        # Type 3: Will X and Y ever happen together in the same sequence?
        game = random.choice(list(games.values()))
        if len(game) > 2:
            x, y = random.sample(game[:-1], 2)
            truth_value = game.index(x) < game.index(y)
            question = f"Will {name} ever {x} and then {y}?"
            ctl_type = "EF"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    elif question_type == 4:
        # Type 4: If X or Y happens, what are we sure will happen eventually?
        game = random.choice(list(games.values()))
        x, y = random.sample(game[:-1], 2)
        truth_value = "removes the VR headset" in game
        question = f"If {name} {x} or {y}, what are we sure he will eventually do?"
        ctl_type = "AF"
        question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
        question_type_str = "Semantic"

    elif question_type == 5:
        # Type 5: What does Alex do at the end of every VR session?
        truth_value = "removes the VR headset"
        question = f"What does {name} do at the end of every VR session?"
        ctl_type = "AG"
        question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <name the activity>}'''
        question_type_str = "Semantic"

    elif question_type == 6:
        # Type 6: Does X always follow Y?
        game = random.choice(list(games.values()))
        if len(game) > 2:
            x, y = random.sample(game[:-1], 2)
            truth_value = all(r.index(y) < r.index(x) for r in games.values() if y in r and x in r)
            question = f"Does {name} always {x} after {y}?"
            ctl_type = "AU"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    return question, truth_value, ctl_type, question_type_str

def generate_vr_question_type7():
    """Generates a dynamic question set for a VR adventure game session."""
    name = random_gamer_name()  # Generate a random gamer's name
    games, context = generate_vr_adventures(name)  # Create VR adventure experiences
    question, truth_value, ctl_type, question_type_str = generate_vr_question(games, name)  # Generate VR game-related question

    return (context + "\n" + question), truth_value, ctl_type, question_type_str

# Main Execution
question7, truth_label7, ctl_type7 , question_type_str= generate_vr_question_type7()
print(question7)
print(truth_label7)
print(ctl_type7, question_type_str)
