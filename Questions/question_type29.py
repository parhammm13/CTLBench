import random

def generate_superhero_context():
    """Generates a dynamic context with natural language descriptions for superhero actions."""
    actions = {
        "Aerial Patrol": {"time": random.randint(3, 5), "exclusions": ["Ground Combat"]},
        "Ground Combat": {"time": random.randint(4, 6), "prerequisites": ["Intel Gathering"]},
        "Intel Gathering": {"time": random.randint(2, 4), "prerequisites": [], "exclusions": []},
        "Shield Deployment": {"time": random.randint(3, 5), "parallel": random.choice([True, False])},
        "Healing & Recovery": {"time": random.randint(1, 3), "prerequisites": ["Shield Deployment"], "exclusions": ["Aerial Patrol"]}
    }

    # Create a descriptive context in text format
    context = " Superhero Actions & Time Assignments:\n"
    for action, details in actions.items():
        context += f"- {action} takes {details['time']} units of time."
        if "prerequisites" in details and details["prerequisites"]:
            prereqs = ", ".join(details["prerequisites"])
            context += f" It must be completed after {prereqs}."
        if "exclusions" in details and details["exclusions"]:
            exclusions = ", ".join(details["exclusions"])
            context += f" It cannot be performed simultaneously with {exclusions}."
        if details.get("parallel") is not None:
            context += f" {'It can run in parallel with other tasks.' if details['parallel'] else 'It cannot run in parallel with other tasks.'}"
        context += "\n"
    return actions, context

def can_actions_run_simultaneously(action1, action2, actions):
    """Checks if two actions can run simultaneously."""
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

def can_tasks_run_simultaneously(task1, task2, tasks):
    """Checks if two tasks can run simultaneously."""
    return task1 not in tasks[task2].get("exclusions", []) and task2 not in tasks[task1].get("exclusions", [])

def find_replacement_options(running_tasks, tasks):
    """Finds which tasks can replace one of the currently running tasks."""
    possible_replacements = []
    for task in tasks.keys():
        if task not in running_tasks:  # Check only new tasks
            if any(can_tasks_run_simultaneously(task, t, tasks) for t in running_tasks):
                possible_replacements.append(task)
    return possible_replacements

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


def generate_question(tasks):
    """Randomly generates a natural-language question with dynamically changing context."""
    question_type = random.choice([1, 2, 3, 4, 6, 7, 8, 9])
    # question_type = 5
    QT1 = ""
    QT2 = "Arithmetic"  # Default set to Arithmetic, we will change it if necessary.

    if question_type == 1:
        task1, task2 = random.sample(list(tasks.keys()), 2)
        time_limit = random.randint(5, 12)
        total_time = tasks[task1]["time"] + tasks[task2]["time"]
        truth_value = total_time <= time_limit
        question = f'''Can the AI complete both {task1} and {task2} within {time_limit} time units?
                   Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}'''
        QT1 = "EF"
        QT2 = "Arithmetic"

    elif question_type == 2:
        task1, task2 = random.sample(list(tasks.keys()), 2)
        start_time_task1 = random.randint(0, 3)
        truth_value = tasks[task2]["time"] + start_time_task1 <= 10
        question = f'''If {task1} starts at T={start_time_task1}, can {task2} still be completed within 10 time units?
                   Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}'''
        QT1 = "EU"
        QT2 = "Arithmetic"

    elif question_type == 3:
        task = random.choice(list(tasks.keys()))
        prerequisites = tasks[task].get("prerequisites", [])
        truth_value = bool(prerequisites)
        question = f'''Does {task} always complete after {', '.join(prerequisites)}?" if prerequisites else f"Does {task} always depend on a prerequisite?
                   Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}'''
        QT1 = "AF"
        QT2 = "Semantic"  # This is a semantic question as it's asking about a dependency condition.

    elif question_type == 4:
        task1, task2 = random.sample(list(tasks.keys()), 2)
        truth_value = can_tasks_run_simultaneously(task1, task2, tasks)
        question = f'''Can the AI perform {task1} and {task2} simultaneously?
                   Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}'''
        QT1 = "AG"
        QT2 = "Semantic"  # This is a semantic question as it's about whether two tasks can run at the same time.

    # elif question_type == 5:
    #     task_sequence = list(tasks.keys())
    #     total_time = calculate_completion_time(task_sequence, tasks)
    #     truth_value = total_time
    #     question = f'''What is the minimum amount of time required to complete all tasks?
    #      Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <times with out including unit >}}'''
    #     QT1 = "AF"
    #     QT2 = "Arithmetic"

    elif question_type == 6:
        paused_task = random.choice(list(tasks.keys()))
        other_task = random.choice(list(tasks.keys()))
        truth_value = paused_task != other_task
        question = f'''If {paused_task} is paused, can {other_task} still be executed?
        Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}'''
        QT1 = "EU"
        QT2 = "Semantic"  # This is a semantic question as it's about task dependencies.

    elif question_type == 7:
        task = random.choice(list(tasks.keys()))
        condition = random.choice(["must follow another task", "cannot run in parallel"])
        truth_value = bool(tasks[task].get("prerequisites", [])) if condition == "must follow another task" else not tasks[task].get("parallel", True)
        question = f'''Is it always true that {task} {condition}?
        Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}'''
        QT1 = "AU"
        QT2 = "Semantic"  # This is a semantic question as it's asking about task execution conditions.

    elif question_type == 8:
        running_tasks = random.sample(list(tasks.keys()), 3)
        possible_replacements = find_replacement_options(running_tasks, tasks)
        truth_value = bool(possible_replacements)
        question = f'''If {', '.join(running_tasks)} are running, is it possible to replace one of them with another task as the next task?
        Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}'''
        QT1 = "EX"
        QT2 = "Semantic"  # This is a semantic question about task replacement.

    elif question_type == 9:
        running_tasks = random.sample(list(tasks.keys()), 2)
        possible_parallel_tasks = find_parallel_task_options(running_tasks, tasks)
        truth_value = possible_parallel_tasks
        question = f'''If {', '.join(running_tasks)} are running, what are the possible options to choose another task to run in parallel?
        Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <list of task>}}'''
        QT1 = "EX"
        QT2 = "Semantic"  # This is a semantic question as it's asking about parallel task options.

    return question, truth_value, QT1, QT2
def find_parallel_task_options(running_tasks, tasks):
    """Finds which tasks can run in parallel with the currently running tasks."""
    return [task for task in tasks.keys() if task not in running_tasks and
            all(can_tasks_run_simultaneously(task, t, tasks) for t in running_tasks)]

def generate_question_type3():
    """Generates a dynamic context and a random question."""
    tasks, context = generate_superhero_context()  # Create task context
    question, truth_value, QT1, QT2 = generate_question(tasks)  # Generate a question
    return context + question, truth_value, QT1, QT2

# Main Script
tasks, context = generate_superhero_context()  # Create a new task context in text format
question, truth_value, QT1, QT2 = generate_question(tasks)  # Generate a random question
print(f"Context:\n{context}")
print(f"Question: {question}")
print(f"Truth Value: {truth_value}")
print(f"CTL Type (QT1): {QT1}")
print(f"Question Type (QT2): {QT2}")

