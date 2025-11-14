import random

def generate_circus_performances(name):
    """Generates dynamic circus performance routines for Leo."""
    # Define possible circus activities
    circus_activities = [
        "juggles flaming torches", "balances on a tightrope", "performs acrobatics",
        "interacts with the audience", "takes a final leap", "takes a bow on stage",
        "dresses as a clown", "entertains children", "performs a comedy act",
        "puts on a dazzling magic show", "saws a box in half", "performs a grand illusion",
        "does a fire-breathing trick", "tames a lion", "performs a human cannonball stunt",
        "rides a unicycle", "performs aerial silk acrobatics", "plays a funny prank on the audience",
        "does an elaborate mime act", "performs a dangerous knife-throwing trick",
        "balances on a rolling barrel", "swings on a trapeze", "controls a puppet show",
        "performs a shadow theater act", "jumps through a flaming hoop",
        "makes balloon animals", "plays a clown trumpet gag"
    ]

    # Generate three unique circus performances
    performance1 = random.sample(circus_activities, random.randint(4, 6)) + ["takes a bow on stage"]
    performance2 = random.sample(circus_activities, random.randint(4, 6)) + ["takes a bow on stage"]
    performance3 = random.sample(circus_activities, random.randint(4, 6)) + ["takes a bow on stage"]

    # Create the context in natural language
    context = f"""
{name} is a circus performer who has three different acts he can perform each night, and each time he randomly selects one:
- Performance 1: {', then '.join(performance1)}.
- Performance 2: {', then '.join(performance2)}.
- Performance 3: {', then '.join(performance3)}.
    """

    performances = {"Performance 1": performance1, "Performance 2": performance2, "Performance 3": performance3}
    return performances, context

def random_performer_name():
    """Generates a random circus performer's name."""
    names = ["Leo", "Felix", "Maximus", "Arlo", "Dante", "Lorenzo", "Remy", "Silas"]
    return random.choice(names)

def generate_circus_question(performances, name):
    """Generates dynamic circus-related questions."""
    question_type = random.choice([1, 2, 3, 4, 5, 6])  # Select a question type randomly
    ctl_type = ""
    question = ""
    truth_value = ""

    if question_type == 1:
        # Type 1: If X happens, will Y follow?
        performance = random.choice(list(performances.values()))
        if len(performance) > 2:
            x, y = random.sample(performance[:-1], 2)
            truth_value = performance.index(x) < performance.index(y)
            question = f"If {name} {x} tonight, will he {y} afterward?"
            ctl_type = "AX"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    elif question_type == 2:
        # Type 2: If Y happens, is there a possibility that X happened earlier?
        performance = random.choice(list(performances.values()))
        if len(performance) > 2:
            x, y = random.sample(performance[1:], 2)
            truth_value = performance.index(y) > performance.index(x)
            question = f"If {name} {y}, is there a possibility that he {x} earlier?"
            ctl_type = "EU"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    elif question_type == 3:
        # Type 3: Will X and Y ever happen together in the same sequence?
        performance = random.choice(list(performances.values()))
        if len(performance) > 2:
            x, y = random.sample(performance[:-1], 2)
            truth_value = performance.index(x) < performance.index(y)
            question = f"Will {name} ever {x} and then {y}?"
            ctl_type = "EF"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    elif question_type == 4:
        # Type 4: If X or Y happens, what are we sure will happen eventually?
        performance = random.choice(list(performances.values()))
        x, y = random.sample(performance[:-1], 2)
        truth_value = "takes a bow on stage" in performance
        question = f"If {name} {x} or {y}, what are we sure he will eventually do?"
        ctl_type = "AF"
        question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
        question_type_str = "Semantic"

    elif question_type == 5:
        # Type 5: What does Leo do at the end of every performance?
        truth_value = "takes a bow on stage"
        question = f"What does {name} do at the end of every performance?"
        ctl_type = "AG"
        question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <name the activity>}'''
        question_type_str = "Semantic"

    elif question_type == 6:
        # Type 6: Does X always follow Y?
        performance = random.choice(list(performances.values()))
        if len(performance) > 2:
            x, y = random.sample(performance[:-1], 2)
            truth_value = all(r.index(y) < r.index(x) for r in performances.values() if y in r and x in r)
            question = f"Does {name} always {x} after {y}?"
            ctl_type = "AU"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    return question, truth_value, ctl_type, question_type_str

def generate_circus_question_type7():
    """Generates a dynamic question set for a circus performance."""
    name = random_performer_name()  # Generate a random circus performer's name
    performances, context = generate_circus_performances(name)  # Create circus performances
    question, truth_value, ctl_type, question_type_str = generate_circus_question(performances, name)  # Generate circus-related question

    return (context + "\n" + question), truth_value, ctl_type, question_type_str

# Main Execution
question7, truth_label7, ctl_type7, question_type_str = generate_circus_question_type7()
print(question7)
print(truth_label7)
print(ctl_type7, question_type_str)
