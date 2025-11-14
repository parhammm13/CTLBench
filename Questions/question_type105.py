import random

def generate_dynamic_kingdom_context():
    """Generates a dynamic natural-language context for magical kingdom heir selection with varied events and durations."""
    # Define potential events and resolutions with templates
    possible_events = [
        {"name": "Great Magical War and Prophecy", "template": "A great magical war might last {war_duration} years, followed by a prophecy revealing the heir within {prophecy_duration} years."},
        {"name": "Forbidden Spell and Collapse", "template": "A forbidden spell might cause the kingdom to collapse, requiring {rebuilding_duration} years of rebuilding before a ruler is appointed."},
        {"name": "Dragon Rule and Human Reclamation", "template": "A dragon might rule for {dragon_duration} years before humans reclaim the throne."},
        {"name": "Hero’s Journey", "template": "A hero’s journey might take {hero_journey_duration} years before they retrieve the crown."},
        {"name": "Ancient Scroll Deciphering", "template": "Ancient scrolls might take {scroll_duration} years to decipher before identifying the rightful heir."}
    ]

    # Randomize durations for each scenario
    context = "Magical Kingdom Heir Selection Scenarios:\n"
    scenarios = []
    for event in possible_events:
        scenario = {}
        if "{war_duration}" in event["template"]:
            scenario["war_duration"] = random.randint(100, 400)
        if "{prophecy_duration}" in event["template"]:
            scenario["prophecy_duration"] = random.randint(1, 10)
        if "{rebuilding_duration}" in event["template"]:
            scenario["rebuilding_duration"] = random.randint(50, 200)
        if "{dragon_duration}" in event["template"]:
            scenario["dragon_duration"] = random.randint(200, 500)
        if "{hero_journey_duration}" in event["template"]:
            scenario["hero_journey_duration"] = random.randint(50, 150)
        if "{scroll_duration}" in event["template"]:
            scenario["scroll_duration"] = random.randint(100, 400)

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
        election_scenarios = [s for s in scenarios if "hero_journey_duration" in s]
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

    scenarios, context = generate_dynamic_kingdom_context()  # Create a new dynamic context
    question, truth_value, ctl_type, question_type_str = generate_dynamic_question(scenarios)  # Generate a random question

    return context + question, truth_value, ctl_type, question_type_str

# Example usage
# question_data = generate_question_type3()
question, truth_value, ctl_type, question_type_str  = generate_question_type3()
print(question,'\n', truth_value,'\n', question_type_str)