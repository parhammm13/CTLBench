# import random

# def generate_context():
#     """Generates a dynamic natural-language context for land succession scenarios."""
#     scenarios = [
#         {
#             "name": "Long War and Stability",
#             "description": "A war might last 400 years, then it would take 20 years for the land to stabilize, and afterward, a new ruler would be elected within a year.",
#             "duration": 400 + 20 + 1,
#             "war_duration": 400,
#         },
#         {
#             "name": "Total Destruction",
#             "description": "A 100-year war might result in the complete destruction of the land.",
#             "duration": 100,
#             "war_duration": 100,
#         },
#         {
#             "name": "Coup",
#             "description": "A coup might occur, lasting 100 years.",
#             "duration": 100,
#             "war_duration": None,
#         },
#         {
#             "name": "Short War and Stability",
#             "description": "A 20-year war might lead to stability, followed by the election of a new ruler within a year.",
#             "duration": 20 + 1,
#             "war_duration": 20,
#         },
#         {
#             "name": "Council Debate",
#             "description": "A council might debate succession for 221 years, after which the ruler would immediately ascend to the throne.",
#             "duration": 221,
#             "war_duration": None,
#         },
#     ]

#     # Build the context text dynamically
#     context = "Land Succession Scenarios:\n"
#     for scenario in scenarios:
#         context += f"- {scenario['description']}\n"

#     return scenarios, context

# def generate_question(scenarios):
#     """Generates a natural-language question based on the scenarios."""
#     question_type = random.choice([1, 2, 3])  # Choose a question type randomly

#     if question_type == 1:
#         # Question Type 1: If it takes X years, is it possible that a war occurred?
#         duration = random.choice([s["duration"] for s in scenarios])
#         war_scenarios = [s for s in scenarios if s["war_duration"] is not None]
#         truth_value = any(s["duration"] == duration and s["war_duration"] is not None for s in war_scenarios)
#         question = f"If it takes {duration} years, is it possible that a war occurred?"

#     elif question_type == 2:
#         # Question Type 2: What is the minimum time required to elect a new ruler?
#         election_scenarios = [s for s in scenarios if "elected" in s["description"]]
#         min_time = min(s["duration"] for s in election_scenarios)
#         truth_value = min_time
#         question = "What is the minimum time required to elect a new ruler?"

#     elif question_type == 3:
#         # Question Type 3: If a war lasts X years, will a ruler eventually be chosen?
#         war_scenario = random.choice([s for s in scenarios if s["war_duration"] is not None])
#         war_duration = war_scenario["war_duration"]
#         truth_value = "elected" in war_scenario["description"]
#         question = f"If a war lasts {war_duration} years, will a ruler eventually be chosen?"

#     return question, truth_value

# # Main Script
# scenarios, context = generate_context()  # Create a new context
# question, truth_value = generate_question(scenarios)  # Generate a random question
# print(f"Context:\n{context}")
# print(f"Question: {question}")
# print(f"Truth Value: {truth_value}")
import random

def generate_dynamic_context():
    """Generates a dynamic natural-language context with varied events and durations."""
    # Define potential events and resolutions with templates
    possible_events = [
        {"name": "Long War and Stabilization", "template": "A war might last {war_duration} years, then it would take {stabilization_duration} years for the land to stabilize, and afterward, a new ruler would be elected within {election_duration} year(s)."},
        {"name": "Complete Destruction", "template": "A war lasting {war_duration} years might result in the complete destruction of the land."},
        {"name": "Civil Coup", "template": "A coup might occur, lasting {coup_duration} years."},
        {"name": "Short Conflict and Election", "template": "A brief conflict lasting {war_duration} years might lead to stability, followed by the election of a new ruler within {election_duration} year(s)."},
        {"name": "Council Debate", "template": "A council might debate succession for {debate_duration} years, after which the ruler would immediately ascend to the throne."},
        {"name": "Natural Succession", "template": "Peaceful discussions might occur over {debate_duration} years, leading to a natural succession without war."}
    ]

    # Randomize durations for each scenario
    context = "Land Succession Scenarios:\n"
    scenarios = []
    for event in possible_events:
        scenario = {}
        if "{war_duration}" in event["template"]:
            scenario["war_duration"] = random.randint(20, 500)
        if "{stabilization_duration}" in event["template"]:
            scenario["stabilization_duration"] = random.randint(10, 50)
        if "{election_duration}" in event["template"]:
            scenario["election_duration"] = random.randint(1, 5)
        if "{coup_duration}" in event["template"]:
            scenario["coup_duration"] = random.randint(50, 150)
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

    scenarios, context = generate_dynamic_context()  # Create a new dynamic context
    question, truth_value, ctl_type, question_type_str = generate_dynamic_question(scenarios)  # Generate a random question

    return context + question, truth_value, ctl_type, question_type_str

# Example usage
# question_data = generate_question_type3()
question, truth_value, ctl_type, question_type_str  = generate_question_type3()
print(question,'\n', truth_value,'\n', question_type_str)
# print(question_data)

# # Main Script
# scenarios, context = generate_dynamic_context()  # Create a new dynamic context
# question, truth_value = generate_dynamic_question(scenarios)  # Generate a random question
# print(f"Context:\n{context}")
# print(f"Question: {question}")
# print(f"Truth Value: {truth_value}")
