import random

def generate_dynamic_ai_context():
    """Generates a dynamic natural-language context for AI governance evolution with varied events and durations."""
    # Define potential events and resolutions with templates
    possible_events = [
        {"name": "AI Wars and Restructuring", "template": "AI wars might last {war_duration} years, followed by {restructuring_duration} years of restructuring, and then AI assumes governance within {transition_duration} year(s)."},
        {"name": "Human Resistance Movement", "template": "A human resistance movement might lead to AI being banned permanently."},
        {"name": "Quantum Computing Breakthrough", "template": "A quantum computing breakthrough might allow AI governance after {breakthrough_duration} years."},
        {"name": "AI Malfunction and Hybrid Government", "template": "AI might malfunction, causing {chaos_duration} years of chaos before a hybrid government is formed in {hybrid_duration} years."},
        {"name": "Negotiations for AI Governance", "template": "Negotiations might last {negotiation_duration} years before AI fully takes over."}
    ]

    # Randomize durations for each scenario
    context = "Artificial Intelligence Evolution Scenarios:\n"
    scenarios = []
    for event in possible_events:
        scenario = {}
        if "{war_duration}" in event["template"]:
            scenario["war_duration"] = random.randint(100, 200)
        if "{restructuring_duration}" in event["template"]:
            scenario["restructuring_duration"] = random.randint(20, 80)
        if "{transition_duration}" in event["template"]:
            scenario["transition_duration"] = random.randint(1, 5)
        if "{breakthrough_duration}" in event["template"]:
            scenario["breakthrough_duration"] = random.randint(200, 500)
        if "{chaos_duration}" in event["template"]:
            scenario["chaos_duration"] = random.randint(50, 100)
        if "{hybrid_duration}" in event["template"]:
            scenario["hybrid_duration"] = random.randint(5, 20)
        if "{negotiation_duration}" in event["template"]:
            scenario["negotiation_duration"] = random.randint(200, 400)

        # Populate template with durations
        scenario["description"] = event["template"].format(**scenario)
        scenario["total_duration"] = sum(v for k, v in scenario.items() if k.endswith("_duration"))
        scenario["name"] = event["name"]
        scenarios.append(scenario)

        # Append scenario description to context
        context += f"- {scenario['description']}\n"

    return scenarios, context


def generate_dynamic_question(scenarios):
    """Generates a natural-language question based on dynamically created scenarios."""
    question_type = random.choice([1, 2, 3])  # Choose a question type randomly
    question_type = 2  # Fixed to question type 3 for this case

    if question_type == 1:
        # Question Type 1: If it takes X years, is it possible that a war occurred?
        duration = random.choice([s["total_duration"] for s in scenarios])
        war_scenarios = [s for s in scenarios if "war_duration" in s]
        truth_value = any(s["total_duration"] == duration and "war_duration" in s for s in war_scenarios)
        question = f'''If it takes {duration} years, is it possible that a war occurred?
         Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}'''
        ctl_type = "EU"
        question_type_str = "Arithmetic"

    elif question_type == 2:
        # Question Type 2: What is the minimum time required to elect a new ruler?
        election_scenarios = [s for s in scenarios if "hybrid_duration" in s]
        if election_scenarios:
            min_time = min(s["total_duration"] for s in election_scenarios)
            truth_value = min_time
            question = '''What is the minimum time required to elect a new ruler?
             Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <only number of years>}}'''
        else:
            truth_value = None
            question = '''No election scenarios found. Can a ruler be elected?'''

        ctl_type = "AF"
        question_type_str = "Arithmetic"

    elif question_type == 3:
        # Question Type 3: If a war lasts X years, will a ruler eventually be chosen?
        war_scenario = random.choice([s for s in scenarios if "war_duration" in s])
        war_duration = war_scenario["war_duration"]
        truth_value = "election_duration" in war_scenario
        question = f'''If a war lasts {war_duration} years, will a ruler eventually be chosen?
         Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}'''
        ctl_type = "EF"
        question_type_str = "Semantic"

    return question, truth_value, ctl_type, question_type_str


def generate_question_type3():
    scenarios, context = generate_dynamic_ai_context()  # Create a new dynamic context
    question, truth_value, ctl_type, question_type_str = generate_dynamic_question(scenarios)  # Generate a random question

    return context + question, truth_value, ctl_type, question_type_str

# Example usage
# question_data = generate_question_type3()
question, truth_value, ctl_type, question_type_str  = generate_question_type3()
print(question, '\n', truth_value, '\n', question_type_str)
