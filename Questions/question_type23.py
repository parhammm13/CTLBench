import random

def generate_kingdom_defense_context():
    """Generates a dynamic context with natural language descriptions for war strategies."""
    actions = {
        "Castle Fortification": {"time": random.randint(3, 5), "exclusions": ["Weapon Production"]},
        "Weapon Production": {"time": random.randint(4, 6), "prerequisites": ["Resource Gathering"]},
        "Resource Gathering": {"time": random.randint(2, 4), "prerequisites": [], "exclusions": []},
        "Scout Enemy Movement": {"time": random.randint(3, 5), "parallel": random.choice([True, False])},
        "Magic Barrier Activation": {"time": random.randint(1, 3), "prerequisites": ["Scout Enemy Movement"], "exclusions": ["Castle Fortification"]}
    }

    # Create a descriptive context in text format
    context = " Defense Actions & Time Assignments:\n"
    for action, details in actions.items():
        context += f"- {action} takes {details['time']} units of time."
        if "prerequisites" in details and details["prerequisites"]:
            prereqs = ", ".join(details["prerequisites"])
            context += f" It must be completed after {prereqs}."
        if "exclusions" in details and details["exclusions"]:
            exclusions = ", ".join(details["exclusions"])
            context += f" It cannot be executed simultaneously with {exclusions}."
        if details.get("parallel") is not None:
            context += f" {'It can run in parallel with other actions.' if details['parallel'] else 'It cannot run in parallel with other actions.'}"
        context += "\n"
    return actions, context

def can_actions_run_simultaneously(action1, action2, actions):
    """Checks if two actions can be executed simultaneously."""
    return action1 not in actions[action2].get("exclusions", []) and action2 not in actions[action1].get("exclusions", [])

def calculate_completion_time(action_sequence, actions):
    """Calculates the total time needed to complete a sequence of actions."""
    time = 0
    completed_actions = set()
    for action in action_sequence:
        prerequisites = actions[action].get("prerequisites", [])
        if all(pre in completed_actions for pre in prerequisites):
            time += actions[action]["time"]
            completed_actions.add(action)
        else:
            return float('inf')  # Invalid sequence due to unmet prerequisites
    return time

def find_replacement_options(running_actions, actions):
    """Finds which actions can replace one of the currently running actions."""
    possible_replacements = []
    for action in actions.keys():
        if action not in running_actions:  # Check only new actions
            if any(can_actions_run_simultaneously(action, a, actions) for a in running_actions):
                possible_replacements.append(action)
    return possible_replacements

def find_parallel_action_options(running_actions, actions):
    """Finds which actions can run in parallel with the currently running actions."""
    return [action for action in actions.keys() if action not in running_actions and 
            all(can_actions_run_simultaneously(action, a, actions) for a in running_actions)]

def generate_kingdom_defense_question(actions):
    """Randomly generates a natural-language question with dynamically changing context."""
    question_type = random.choice([1, 2, 3, 4, 6, 7, 8, 9])
    QT1 = ""
    QT2 = "Arithmetic"  # Default set to Arithmetic, we will change it if necessary.

    if question_type == 1:
        action1, action2 = random.sample(list(actions.keys()), 2)
        time_limit = random.randint(5, 12)
        total_time = actions[action1]["time"] + actions[action2]["time"]
        truth_value = total_time <= time_limit
        question = f"Can the kingdom complete both {action1} and {action2} within {time_limit} time units?"
        QT1 = "EF"
        QT2 = "Arithmetic"

    elif question_type == 2:
        action1, action2 = random.sample(list(actions.keys()), 2)
        start_time_action1 = random.randint(0, 3)
        truth_value = actions[action2]["time"] + start_time_action1 <= 10
        question = f"If {action1} starts at T={start_time_action1}, can {action2} still be completed within 10 time units?"
        QT1 = "EU"
        QT2 = "Arithmetic"
    elif question_type == 3:
        action = random.choice(list(actions.keys()))
        prerequisites = actions[action].get("prerequisites", [])
        truth_value = bool(prerequisites)
        question = f"Does {action} always complete after {', '.join(prerequisites)}?" if prerequisites else f"Does {action} always depend on a prerequisite?"
        QT1 = "AF"
        QT2 = "Semantic"
    elif question_type == 4:
        action1, action2 = random.sample(list(actions.keys()), 2)
        truth_value = can_actions_run_simultaneously(action1, action2, actions)
        question = f"Can the kingdom execute {action1} and {action2} simultaneously?"
        QT1 = "AG"
        QT2 = "Semantic"
    # elif question_type == 5:
    #     action_sequence = list(actions.keys())
    #     total_time = calculate_completion_time(action_sequence, actions)
    #     truth_value = total_time
    #     question = f"What is the minimum amount of time required to complete all defense strategies?"
    #     QT1 = "AF"
    #     QT2 = "Arithmetic"
    elif question_type == 6:
        paused_action = random.choice(list(actions.keys()))
        other_action = random.choice(list(actions.keys()))
        truth_value = paused_action != other_action
        question = f"If {paused_action} is paused, can {other_action} still proceed?"
        QT1 = "EU"
        QT2 = "Semantic"
    elif question_type == 7:
        action = random.choice(list(actions.keys()))
        condition = random.choice(["must follow another action", "cannot run in parallel"])
        truth_value = bool(actions[action].get("prerequisites", [])) if condition == "must follow another action" else not actions[action].get("parallel", True)
        question = f"Is it always true that {action} {condition}?"
        QT1 = "AU"
        QT2 = "Semantic"
    elif question_type == 8:
        running_actions = random.sample(list(actions.keys()), 3)
        possible_replacements = find_replacement_options(running_actions, actions)
        truth_value = bool(possible_replacements)
        question = f"If {', '.join(running_actions)} are active, is it possible to replace one of them with another action as the next move?"
        QT1 = "EX"
        QT2 = "Semantic"
    elif question_type == 9:
        running_actions = random.sample(list(actions.keys()), 2)
        possible_parallel_actions = find_parallel_action_options(running_actions, actions)
        truth_value = possible_parallel_actions
        question = f"If {', '.join(running_actions)} are active, what are the possible options to choose another action to execute in parallel?"
        QT1 = "EX"
        QT2 = "Semantic"
    return question, truth_value, QT1, QT2

def generate_kingdom_defense_question_type():
    """Generates a dynamic war strategy context and a random question."""
    actions, context = generate_kingdom_defense_context()  # Create defense strategy context
    question, truth_value, QT1, QT2 = generate_kingdom_defense_question(actions)  # Generate a question
    return context + question, truth_value, QT1, QT2

# Run the script to generate a random war strategy question
print(generate_kingdom_defense_question_type())
