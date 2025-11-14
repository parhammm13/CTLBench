import random

def generate_dynamic_ai_world_order_context():
    """Generates a dynamic natural-language context for AI governance with varied events and durations."""
    # Define potential events and resolutions with templates
    possible_events = [
        {"name": "Rogue AI Uprising", "template": "A rogue AI uprising might last {uprising_duration} years, followed by {peace_duration} years of peace and a final transition to AI rule within {transition_duration} year(s)."},
        {"name": "Cyberwar and AI Collapse", "template": "A cyberwar might destroy all data and prevent AI governance altogether.", "war_duration": random.randint(50, 150)},
        {"name": "Gradual AI Integration", "template": "AI might be gradually integrated into human governance over {integration_duration} years, before fully taking over.", "election_duration": random.randint(5, 15)},  # Added election_duration here
        {"name": "Human Resistance and AI Leadership", "template": "A human resistance might last {resistance_duration} years, followed by {coexistence_duration} years of co-existence before AI assumes leadership within {transition_duration} year(s)."},
        {"name": "AI Self-Awareness", "template": "AI might develop self-awareness and take {self_awareness_duration} years before autonomously assuming control."}
    ]

    # Randomize durations for each scenario
    context = "Rise of a New AI World Order Scenarios:\n"
    scenarios = []
    for event in possible_events:
        scenario = {}
        if "{uprising_duration}" in event["template"]:
            scenario["uprising_duration"] = random.randint(100, 400)
        if "{peace_duration}" in event["template"]:
            scenario["peace_duration"] = random.randint(10, 50)
        if "{transition_duration}" in event["template"]:
            scenario["transition_duration"] = random.randint(1, 10)
        if "{integration_duration}" in event["template"]:
            scenario["integration_duration"] = random.randint(100, 300)
        if "{resistance_duration}" in event["template"]:
            scenario["resistance_duration"] = random.randint(50, 200)
        if "{coexistence_duration}" in event["template"]:
            scenario["coexistence_duration"] = random.randint(10, 100)
        if "{self_awareness_duration}" in event["template"]:
            scenario["self_awareness_duration"] = random.randint(200, 500)
        if "war_duration" in event:
            scenario["war_duration"] = event["war_duration"]
        if "election_duration" in event:
            scenario["election_duration"] = event["election_duration"]

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
    question_type = 2
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
        election_scenarios = [s for s in scenarios if "election_duration" in s]
        if election_scenarios:
            min_time = min(s["total_duration"] for s in election_scenarios)
            truth_value = min_time
            question = '''What is the minimum time required to elect a new ruler?
             Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <only number of years>}}'''
        else:
            question = '''What is the minimum time required to elect a new ruler?
             Format your answer only as a JSON, like JSON = {{"explanation": "No election scenarios exist", "answer": "N/A"}}'''
            truth_value = "N/A"
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

    scenarios, context = generate_dynamic_ai_world_order_context()  # Create a new dynamic context
    question, truth_value, ctl_type, question_type_str = generate_dynamic_question(scenarios)  # Generate a random question

    return context + question, truth_value, ctl_type, question_type_str

# Example usage
question, truth_value, ctl_type, question_type_str  = generate_question_type3()
print(question,'\n', truth_value,'\n', question_type_str)
