import random

def generate_dynamic_colony_context():
    """Generates a dynamic natural-language context for space colony evolution with varied events and durations."""
    # Define potential events and resolutions with templates
    possible_events = [
        {"name": "Asteroid Impact Recovery", "template": "A catastrophic asteroid impact might take {recovery_duration} years to recover, followed by {rebuilding_duration} years of rebuilding, and then a leader is elected within {election_duration} year(s)."},
        {"name": "Political Dispute", "template": "A political dispute might lead to a {instability_duration}-year period of instability, after which the colony is dissolved."},
        {"name": "Technological Breakthrough", "template": "A technological breakthrough might allow for automated leadership, lasting {breakthrough_duration} years before human governance is reinstated."},
        {"name": "Civil War and Peace", "template": "A civil war might last {war_duration} years, then peace is restored over {peace_duration} years, and a leader is chosen within {election_duration} year(s)."},
        {"name": "Council Debate", "template": "A leadership council could debate for {debate_duration} years before electing a new leader."}
    ]

    # Randomize durations for each scenario
    context = "Space Colony Evolution Scenarios:\n"
    scenarios = []
    for event in possible_events:
        scenario = {}
        if "{recovery_duration}" in event["template"]:
            scenario["recovery_duration"] = random.randint(100, 500)
        if "{rebuilding_duration}" in event["template"]:
            scenario["rebuilding_duration"] = random.randint(5, 50)
        if "{election_duration}" in event["template"]:
            scenario["election_duration"] = random.randint(1, 5)
        if "{instability_duration}" in event["template"]:
            scenario["instability_duration"] = random.randint(50, 300)
        if "{breakthrough_duration}" in event["template"]:
            scenario["breakthrough_duration"] = random.randint(200, 500)
        if "{war_duration}" in event["template"]:
            scenario["war_duration"] = random.randint(10, 100)
        if "{peace_duration}" in event["template"]:
            scenario["peace_duration"] = random.randint(10, 50)
        if "{debate_duration}" in event["template"]:
            scenario["debate_duration"] = random.randint(50, 300)

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
        if election_scenarios:  # Only proceed if there are scenarios with election_duration
            min_time = min(s["total_duration"] for s in election_scenarios)
            truth_value = min_time
            question = '''What is the minimum time required to elect a new ruler?
             Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <only number of years>}}'''
        else:
            # Handle the case where no election scenarios exist
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

    scenarios, context = generate_dynamic_colony_context()  # Create a new dynamic context
    question, truth_value, ctl_type, question_type_str = generate_dynamic_question(scenarios)  # Generate a random question

    return context + question, truth_value, ctl_type, question_type_str

question, truth_value, ctl_type, question_type_str  = generate_question_type3()
print(question,'\n', truth_value,'\n', question_type_str)