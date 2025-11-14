import random

def generate_workout_routines(name):
    """Generates dynamic workout routines for a fitness enthusiast."""
    # Define possible workout activities
    workout_activities = [
        "does weightlifting", "does cardio", "does core exercises", "stretches",
        "cools down with a light jog", "drinks a protein shake", "warms up with jump rope",
        "does mobility drills", "performs strength training", "does HIIT training",
        "practices boxing", "finishes with yoga", "does push-ups", "performs squats",
        "runs on the treadmill", "uses resistance bands", "practices martial arts",
        "does a cycling session", "performs deadlifts", "engages in CrossFit training",
        "uses battle ropes", "does burpees", "does a plank hold", "performs kettlebell swings"
    ]

    # Generate three workout routines with unique sequences
    routine1 = random.sample(workout_activities, random.randint(4, 6)) + ["drinks a protein shake"]
    routine2 = random.sample(workout_activities, random.randint(4, 6)) + ["drinks a protein shake"]
    routine3 = random.sample(workout_activities, random.randint(4, 6)) + ["drinks a protein shake"]

    # Create the context in natural language
    context = f"""
{name} has three different workout routines, and each day they randomly follow one:
- Routine 1: {', then '.join(routine1)}.
- Routine 2: {', then '.join(routine2)}.
- Routine 3: {', then '.join(routine3)}.
    """

    routines = {"Routine 1": routine1, "Routine 2": routine2, "Routine 3": routine3}
    return routines, context

def random_fitness_name():
    """Generates a random fitness name."""
    names = ["Alex", "Jordan", "Taylor", "Chris", "Morgan", "Pat", "Casey", "Robin"]
    return random.choice(names)

def generate_fitness_question(routines, name):
    """Generates dynamic fitness-related questions."""
    question_type = random.choice([1, 2, 3, 4, 5, 6])  # Select a question type randomly
    ctl_type = ""
    question = ""
    truth_value = ""
    question_type_str = ""

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
        truth_value = "drinks a protein shake" in routine
        question = f"If {name} {x} or {y}, what are we sure they will eventually do?"
        ctl_type = "AF"
        question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
        question_type_str = "Semantic"

    elif question_type == 5:
        # Type 5: What does the person do after every workout?
        truth_value = "drinks a protein shake"
        question = f"What does {name} do after every workout?"
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

    return question, truth_value, ctl_type ,question_type_str

def generate_fitness_question_type7():
    """Generates a dynamic question set for a workout routine."""
    name = random_fitness_name()  # Generate a random fitness-related name
    routines, context = generate_workout_routines(name)  # Create workout routines
    question, truth_value, ctl_type , question_type_str = generate_fitness_question(routines, name)  # Generate fitness-related question

    return (context + "\n" + question), truth_value, ctl_type, question_type_str

# Main Execution

# for i in range(1000):
#     question7, truth_label7, ctl_type7, question_type_str = generate_fitness_question_type7()
#     print(question7)
#     print(truth_label7)
#     print(ctl_type7)
