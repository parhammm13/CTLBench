import random

def generate_cooking_strategies(name):
    """Generates dynamic cooking strategies for Mia."""
    # Define possible cooking activities
    cooking_activities = [
        "chops ingredients", "sautés vegetables", "prepares the sauce", "plates the dish",
        "garnishes the dish", "presents it to the judges", "prepares the dough",
        "preheats the oven", "kneads the dough", "bakes it to perfection",
        "fillets a fish", "sears it on a hot pan", "prepares a side dish",
        "whisks eggs", "grills a steak", "makes a dessert", "melts chocolate",
        "folds pastry", "seasons the dish", "blends a smoothie",
        "boils pasta", "creates a signature dish", "cooks rice perfectly",
        "makes a soup", "plates a gourmet meal", "practices presentation skills"
    ]

    # Generate three unique cooking strategies
    strategy1 = random.sample(cooking_activities, random.randint(4, 6)) + ["presents it to the judges"]
    strategy2 = random.sample(cooking_activities, random.randint(4, 6)) + ["presents it to the judges"]
    strategy3 = random.sample(cooking_activities, random.randint(4, 6)) + ["presents it to the judges"]

    # Create the context in natural language
    context = f"""
{name} is a contestant on a high-stakes cooking show, and each round she randomly follows one of three different cooking strategies:
- Strategy 1: {', then '.join(strategy1)}.
- Strategy 2: {', then '.join(strategy2)}.
- Strategy 3: {', then '.join(strategy3)}.
    """

    strategies = {"Strategy 1": strategy1, "Strategy 2": strategy2, "Strategy 3": strategy3}
    return strategies, context

def random_chef_name():
    """Generates a random chef's name."""
    names = ["Mia", "Sophia", "Isabella", "Olivia", "Charlotte", "Amelia", "Emma", "Ava"]
    return random.choice(names)

def generate_cooking_question(strategies, name):
    """Generates dynamic cooking show-related questions."""
    question_type = random.choice([1, 2, 3, 4, 5, 6])  # Select a question type randomly
    ctl_type = ""
    question = ""
    truth_value = ""

    if question_type == 1:
        # Type 1: If X happens, will Y follow?
        strategy = random.choice(list(strategies.values()))
        if len(strategy) > 2:
            x, y = random.sample(strategy[:-1], 2)
            truth_value = strategy.index(x) < strategy.index(y)
            question = f"If {name} {x} today, will she {y} afterward?"
            ctl_type = "AX"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"
    elif question_type == 2:
        # Type 2: If Y happens, is there a possibility that X happened earlier?
        strategy = random.choice(list(strategies.values()))
        if len(strategy) > 2:
            x, y = random.sample(strategy[1:], 2)
            truth_value = strategy.index(y) > strategy.index(x)
            question = f"If {name} {y}, is there a possibility that she {x} earlier?"
            ctl_type = "EU"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    elif question_type == 3:
        # Type 3: Will X and Y ever happen together in the same sequence?
        strategy = random.choice(list(strategies.values()))
        if len(strategy) > 2:
            x, y = random.sample(strategy[:-1], 2)
            truth_value = strategy.index(x) < strategy.index(y)
            question = f"Will {name} ever {x} and then {y}?"
            ctl_type = "EF"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    elif question_type == 4:
        # Type 4: If X or Y happens, what are we sure will happen eventually?
        strategy = random.choice(list(strategies.values()))
        x, y = random.sample(strategy[:-1], 2)
        truth_value = "presents it to the judges" in strategy
        question = f"If {name} {x} or {y}, what are we sure she will eventually do?"
        ctl_type = "AF"
        question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
        question_type_str = "Semantic"

    elif question_type == 5:
        # Type 5: What does Mia do at the end of every cooking round?
        truth_value = "presents it to the judges"
        question = f"What does {name} do at the end of every cooking round?"
        ctl_type = "AG"
        question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <name the activity>}'''
        question_type_str = "Semantic"

    elif question_type == 6:
        # Type 6: Does X always follow Y?
        strategy = random.choice(list(strategies.values()))
        if len(strategy) > 2:
            x, y = random.sample(strategy[:-1], 2)
            truth_value = all(r.index(y) < r.index(x) for r in strategies.values() if y in r and x in r)
            question = f"Does {name} always {x} after {y}?"
            ctl_type = "AU"
            question += '''\nFormat your answer only as a JSON, like JSON = {"explanation": <your step by step solution>, "answer": <true or false>}'''
            question_type_str = "Semantic"

    return question, truth_value, ctl_type, question_type_str

def generate_cooking_question_type7():
    """Generates a dynamic question set for a cooking show competition."""
    name = random_chef_name()  # Generate a random chef's name
    strategies, context = generate_cooking_strategies(name)  # Create cooking strategies
    question, truth_value, ctl_type , question_type_str= generate_cooking_question(strategies, name)  # Generate cooking-related question

    return (context + "\n" + question), truth_value, ctl_type, question_type_str

# Main Execution
question7, truth_label7, ctl_type7 , question_type_str= generate_cooking_question_type7()
print(question7)
print(truth_label7)
print(ctl_type7, question_type_str)
