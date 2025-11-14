import random

def generate_routines(random_name):
    """Generates dynamic nightly routines for a random person."""
    # Define possible activities
    activities = [
        "plays video games", "watches a movie", "studies", "goes for a run",
        "boils water", "watches a documentary", "makes tea", "reads a book",
        "plays football", "listens to music", "does yoga", "writes in his journal",
        "paints", "cooks dinner", "writes poetry", "takes a walk", "does meditation",
        "plays chess", "calls a friend", "takes a nap", "organizes their desk", "cleans the house",
        "plays basketball", "practices guitar", "goes cycling", "learns a new language",
        "bakes cookies", "builds a puzzle", "takes a shower", "does stretching exercises",
        "practices drawing", "sketches in a notebook", "does a home workout", "reads news articles",
        "watches a TV show", "writes a letter", "calls family members", "listens to a podcast",
        "takes photos", "does laundry", "reads a magazine", "plans the week ahead", "watches a sports game",
        "does a DIY project", "attends a virtual meeting", "does gardening", "plays a musical instrument",
        "visits a museum", "practices meditation", "studies a subject online", "plays board games"
    ]

    # Randomize three routines with unique sequences of activities
    routine1 = random.sample(activities, random.randint(4, 6)) + ["sleeps"]
    routine2 = random.sample(activities, random.randint(4, 6)) + ["sleeps"]
    routine3 = random.sample(activities, random.randint(4, 6)) + ["sleeps"]

    # Create the context in natural language
    context = f"""
{random_name} has three nightly routines, and each night they randomly choose one:
- Routine 1: {', then '.join(routine1)}.
- Routine 2: {', then '.join(routine2)}.
- Routine 3: {', then '.join(routine3)}.
    """

    routines = {"Routine 1": routine1, "Routine 2": routine2, "Routine 3": routine3}
    return routines, context

def random_name():
    """Generates a random name."""
    names = ["Alex", "Jordan", "Taylor", "Chris", "Morgan", "Pat", "Casey", "Robin"]
    return random.choice(names)

def generate_question(routines, name):
    """Generates dynamic questions based on nightly routines."""
    question_type = random.choice([1, 2, 3, 4, 5, 6])  # Select a question type randomly
    ctl_type = ""
    question = ""
    truth_value = ""
    if question_type == 1:
        # Question Type 1: If X, will Y happen afterward?
        routine = random.choice(list(routines.values()))
        if len(routine) > 2:
            x, y = random.sample(routine[:-1], 2)
            truth_value = routine.index(x) < routine.index(y)
            question = f'''If {name} {x} tonight, will they {y} afterward?
              Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}'''
            ctl_type = "AX"
            question_type_str = "Semantic"

    elif question_type == 2:
        # Question Type 2: If X, is it possible they did Y earlier?
        routine = random.choice(list(routines.values()))
        if len(routine) > 2:
            x, y = random.sample(routine[1:], 2)
            truth_value = routine.index(y) < routine.index(x)
            question = f'''If {name} {x}, is there a possibility that they {y} earlier?
              Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}'''
            ctl_type = "EU"
            question_type_str = "Semantic"

    elif question_type == 3:
        # Question Type 3: Will they ever do X and then Y?
        routine = random.choice(list(routines.values()))
        if len(routine) > 2:
            x, y = random.sample(routine[:-1], 2)
            truth_value = routine.index(x) < routine.index(y)
            question = f'''Will {name} ever {x} and then {y}?
              Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}'''
            ctl_type = "EF"
            question_type_str = "Semantic"

    elif question_type == 4:
        # Question Type 4: If X or Y, what will they definitely do?
        routine = random.choice(list(routines.values()))
        x, y = random.sample(routine[:-1], 2)
        truth_value = "sleeps" in routine
        question = f'''If {name} {x} or {y}, what are we sure they will eventually do?
          Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}'''
        ctl_type = "AF"
        question_type_str = "Semantic"

    elif question_type == 5:
        # Question Type 5: What does they do every night?
        truth_value = "sleep"
        question = f'''What does {name} do every night?
          Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <name the activity>}}'''
        ctl_type = "AG"
        question_type_str = "Semantic"

    elif question_type == 6:
        # Question Type 6: Does they always do X after Y?
        routine = random.choice(list(routines.values()))
        if len(routine) > 2:
            x, y = random.sample(routine[:-1], 2)
            truth_value = all(r.index(y) < r.index(x) for r in routines.values() if y in r and x in r)
            question = f'''Does {name} always {x} after {y}?
              Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}'''
            ctl_type = "AU"
            question_type_str = "Semantic"

    return question, truth_value, ctl_type, question_type_str


def generate_question_type7():

    name = random_name()  # Generate a random name once
    routines, context = generate_routines(name)  # Create a new dynamic context with the name
    question, truth_value, ctl_type, question_type_str = generate_question(routines, name)  # Generate a random question with the name

    return (context + question), truth_value, ctl_type, question_type_str

# Example usage
question, truth_value, ctl_type, question_type_str  = generate_question_type7()
print(question, '\n', truth_value, '\n', ctl_type, '\n', question_type_str)
