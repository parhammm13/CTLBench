import random

def generate_time_travel_journeys(name):
    """Generates dynamic time travel journeys for Nora."""
    # Define possible time travel activities
    time_travel_activities = [
        "arrives in Ancient Egypt", "deciphers hieroglyphs", "helps construct a pyramid",
        "gathers historical artifacts", "records her findings", "returns to the present",
        "travels to the year 3025", "explores a futuristic city", "finds an advanced AI",
        "collects data on future technology", "visits the Medieval Era", "assists a royal court",
        "learns about medieval warfare", "studies an ancient manuscript", "discovers a lost invention",
        "meets a historical figure", "witnesses a major battle", "invents a new timeline paradox",
        "documents cultural evolution", "recovers lost scrolls", "influences historical events",
        "witnesses a major historical discovery", "travels to a prehistoric era",
        "observes the construction of a historical monument", "escapes a time anomaly",
        "disguises herself as a local citizen", "finds an alternative timeline",
        "visits a legendary lost civilization"
    ]

    # Generate three unique time travel journeys
    travel1 = random.sample(time_travel_activities, random.randint(4, 6)) + ["returns to the present"]
    travel2 = random.sample(time_travel_activities, random.randint(4, 6)) + ["returns to the present"]
    travel3 = random.sample(time_travel_activities, random.randint(4, 6)) + ["returns to the present"]

    # Create the context in natural language
    context = f"""
{name} is a time traveler who has three different time periods she visits each day, and each time she randomly selects one:
- Time Travel 1: {', then '.join(travel1)}.
- Time Travel 2: {', then '.join(travel2)}.
- Time Travel 3: {', then '.join(travel3)}.
    """

    journeys = {"Time Travel 1": travel1, "Time Travel 2": travel2, "Time Travel 3": travel3}
    return journeys, context

def random_time_traveler_name():
    """Generates a random time traveler's name."""
    names = ["Nora", "Sophia", "Lillian", "Olivia", "Isla", "Eleanor", "Clara", "Amelia"]
    return random.choice(names)

def generate_time_travel_question(journeys, name):
    """Generates dynamic time-travel-related questions."""
    question_type = random.choice([1, 2, 3, 4, 5, 6])  # Select a question type randomly
    ctl_type = ""
    question = ""
    truth_value = ""

    if question_type == 1:
        # Type 1: If X happens, will Y follow?
        journey = random.choice(list(journeys.values()))
        if len(journey) > 2:
            x, y = random.sample(journey[:-1], 2)
            truth_value = journey.index(x) < journey.index(y)
            question = f"If {name} {x} today, will she {y} afterward?"
            ctl_type = "AX"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    elif question_type == 2:
        # Type 2: If Y happens, is there a possibility that X happened earlier?
        journey = random.choice(list(journeys.values()))
        if len(journey) > 2:
            x, y = random.sample(journey[1:], 2)
            truth_value = journey.index(y) > journey.index(x)
            question = f"If {name} {y}, is there a possibility that she {x} earlier?"
            ctl_type = "EU"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    elif question_type == 3:
        # Type 3: Will X and Y ever happen together in the same sequence?
        journey = random.choice(list(journeys.values()))
        if len(journey) > 2:
            x, y = random.sample(journey[:-1], 2)
            truth_value = journey.index(x) < journey.index(y)
            question = f"Will {name} ever {x} and then {y}?"
            ctl_type = "EF"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    elif question_type == 4:
        # Type 4: If X or Y happens, what are we sure will happen eventually?
        journey = random.choice(list(journeys.values()))
        x, y = random.sample(journey[:-1], 2)
        truth_value = "returns to the present" in journey
        question = f"If {name} {x} or {y}, what are we sure she will eventually do?"
        ctl_type = "AF"
        question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
        question_type_str = "Semantic"

    elif question_type == 5:
        # Type 5: What does Nora do at the end of every time travel trip?
        truth_value = "returns to the present"
        question = f"What does {name} do at the end of every time travel trip?"
        ctl_type = "AG"
        question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <name the activity>}'''
        question_type_str = "Semantic"

    elif question_type == 6:
        # Type 6: Does X always follow Y?
        journey = random.choice(list(journeys.values()))
        if len(journey) > 2:
            x, y = random.sample(journey[:-1], 2)
            truth_value = all(r.index(y) < r.index(x) for r in journeys.values() if y in r and x in r)
            question = f"Does {name} always {x} after {y}?"
            ctl_type = "AU"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    return question, truth_value, ctl_type, question_type_str

def generate_time_travel_question_type7():
    """Generates a dynamic question set for a time-traveling adventure."""
    name = random_time_traveler_name()  # Generate a random time traveler's name
    journeys, context = generate_time_travel_journeys(name)  # Create time travel journeys
    question, truth_value, ctl_type, question_type_str = generate_time_travel_question(journeys, name)  # Generate time-travel-related question

    return (context + "\n" + question), truth_value, ctl_type, question_type_str

# Main Execution
question7, truth_label7, ctl_type7, question_type_str = generate_time_travel_question_type7()
print(question7)
print(truth_label7)
print(ctl_type7, question_type_str)
