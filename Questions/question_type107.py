import random

def generate_dynamic_space_empire_context():
    """Generates a dynamic natural-language context for space empire governance with varied events and durations."""
    # Define potential events and resolutions with templates
    possible_events = [
        {"name": "Galactic War and Stabilization", "template": "A galactic war might last {war_duration} years, followed by {stabilization_duration} years of stabilization before a ruler emerges."},
        {"name": "Cosmic Anomaly", "template": "A cosmic anomaly might cause irreversible collapse."},
        {"name": "Rogue AI Control", "template": "A rogue AI might control the empire for {ai_control_duration} years before humans reclaim power."},
        {"name": "Diplomatic Mission", "template": "A diplomatic mission might take {diplomatic_duration} years to unify the planets under one ruler."},
        {"name": "Council Governance Decision", "template": "A council might take {council_duration} years to determine a new governance structure."}
    ]

    # Randomize durations for each scenario
    context = "Space Empire Rise and Fall Scenarios:\n"
    scenarios = []
    for event in possible_events:
        scenario = {}
        if "{war_duration}" in event["template"]:
            scenario["war_duration"] = random.randint(100, 400)
        if "{stabilization_duration}" in event["template"]:
            scenario["stabilization_duration"] = random.randint(10, 100)
        if "{ai_control_duration}" in event["template"]:
            scenario["ai_control_duration"] = random.randint(200, 600)
        if "{diplomatic_duration}" in event["template"]:
            scenario["diplomatic_duration"] = random.randint(50, 200)
        if "{council_duration}" in event["template"]:
            scenario["council_duration"] = random.randint(100, 400)

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
        election_scenarios = [s for s in scenarios if "diplomatic_duration" in s]  # Check if diplomatic_duration exists
        if election_scenarios:
            min_time = min(s["total_duration"] for s in election_scenarios)
            truth_value = min_time
            question = '''What is the minimum time required to elect a new ruler?
             Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <only number of years>}}'''
        else:
            min_time = 0
            truth_value = min_time
            question = '''What is the minimum time required to elect a new ruler?
             Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <only number of years>}}'''
        ctl_type = "AF"
        question_type_str = "Arithmetic"

    elif question_type == 3:
        # Question Type 3: If a war lasts X years, will a ruler eventually be chosen?
        war_scenario = random.choice([s for s in scenarios if "war_duration" in s])
        war_duration = war_scenario["war_duration"]
        truth_value = "diplomatic_duration" in war_scenario  # Check if diplomatic_duration exists to decide if ruler is chosen
        question = f'''If a war lasts {war_duration} years, will a ruler eventually be chosen?
         Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}'''
        ctl_type = "EF"
        question_type_str = "Semantic"

    return question, truth_value, ctl_type, question_type_str


def generate_question_type3():

    scenarios, context = generate_dynamic_space_empire_context()  # Create a new dynamic context
    question, truth_value, ctl_type, question_type_str = generate_dynamic_question(scenarios)  # Generate a random question

    return context + question, truth_value, ctl_type, question_type_str

# Example usage
# question_data = generate_question_type3()
question, truth_value, ctl_type, question_type_str  = generate_question_type3()
print(question,'\n', truth_value,'\n', question_type_str)
