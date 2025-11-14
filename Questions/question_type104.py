import random

def generate_dynamic_ocean_context():
    """Generates a dynamic natural-language context for underwater civilization governance with varied events and durations."""
    # Define potential events and resolutions with templates
    possible_events = [
        {"name": "Deep-Sea War and Negotiation", "template": "A deep-sea war might last {war_duration} years, followed by {negotiation_duration} years of negotiation before a government is formed in {election_duration} year(s)."},
        {"name": "Seismic Catastrophe", "template": "A catastrophic seismic event might cause the destruction of {destruction_percentage}% of settlements."},
        {"name": "Scientific Alliance", "template": "A peaceful scientific alliance might allow for governance after {scientific_duration} years."},
        {"name": "Rebellion Against the Mer-King", "template": "A rebellion against the mer-king might last {rebellion_duration} years, and order is restored in {peace_duration} years before governance is chosen in {election_duration} year(s)."},
        {"name": "Scholar Council Decision", "template": "Ocean scholars might take {debate_duration} years to determine the best system of government before appointing a ruler."}
    ]

    # Randomize durations for each scenario
    context = "Ocean Civilization Development Scenarios:\n"
    scenarios = []
    for event in possible_events:
        scenario = {}
        if "{war_duration}" in event["template"]:
            scenario["war_duration"] = random.randint(100, 500)
        if "{negotiation_duration}" in event["template"]:
            scenario["negotiation_duration"] = random.randint(10, 100)
        if "{election_duration}" in event["template"]:
            scenario["election_duration"] = random.randint(1, 5)
        if "{destruction_percentage}" in event["template"]:
            scenario["destruction_percentage"] = random.randint(50, 100)
        if "{scientific_duration}" in event["template"]:
            scenario["scientific_duration"] = random.randint(100, 300)
        if "{rebellion_duration}" in event["template"]:
            scenario["rebellion_duration"] = random.randint(50, 200)
        if "{peace_duration}" in event["template"]:
            scenario["peace_duration"] = random.randint(10, 50)
        if "{debate_duration}" in event["template"]:
            scenario["debate_duration"] = random.randint(100, 400)

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
        min_time = min(s["total_duration"] for s in election_scenarios)
        truth_value = min_time
        question = '''What is the minimum time required to elect a new ruler?
         Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <only number of years>}}'''
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

    scenarios, context = generate_dynamic_ocean_context()  # Create a new dynamic context
    question, truth_value, ctl_type, question_type_str = generate_dynamic_question(scenarios)  # Generate a random question

    return context + question, truth_value, ctl_type, question_type_str

# Example usage
# question_data = generate_question_type3()
question, truth_value, ctl_type, question_type_str  = generate_question_type3()
print(question,'\n', truth_value,'\n', question_type_str)