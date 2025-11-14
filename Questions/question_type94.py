import random

DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
Context ="""
In a universe days move in 3 ways, the days of the week follow branching timelines based on specific events. Depending on the occurrences, the flow of time can branch forward, backward, or loop.

Each day always only one event happened. 
--- 
Rules: 

1. If Event X happens, time advances 4 days forward.
2. If Event Y happens, time moves 1 day back.
3. If Event Z happens only on Friday, time skips forward to Wednesday. (This event only occurs on Friday)"""
def advance_time(current_day, event):
    jump_x = 4
    jump_y = 1
    jump_z = "Wednesday"
    index = DAYS_OF_WEEK.index(current_day)
    if event == "X":
        return DAYS_OF_WEEK[(index + jump_x) % 7]
    elif event == "Y":
        return DAYS_OF_WEEK[(index - jump_y) % 7]
    elif event == "Z" and current_day == "Friday":
        return jump_z
    return current_day


def simulate_event_sequence(start_day, events):
    current_day = start_day
    for event in events:
        current_day = advance_time(current_day, event)
    return current_day

def generate_event_sequences(length):
    events = ["X", "Y", "Z"]
    if length == 1:
        return [[e] for e in events]
    smaller_sequences = generate_event_sequences(length - 1)
    return [seq + [e] for seq in smaller_sequences for e in events]

def find_minimum_sequence(start_day, target_day):
    for length in range(1, 10):
        for sequence in generate_event_sequences(length):
            if simulate_event_sequence(start_day, sequence) == target_day:
                return sequence
    return None

def does_time_loop(start_day, sequence):
    final_day = simulate_event_sequence(start_day, sequence)
    return final_day == start_day

def get_possible_next_days(start_day):
    return [advance_time(start_day, event) for event in ["X", "Y", "Z"]]

def generate_question_type1():
    question_type = random.choice([1, 2, 3, 4, 5, 6, 7])  # Added Type 6 and 7
    QT1 = ""
    QT2 = "Arithmetic"  # Default set to Arithmetic, we will change it if necessary.

    if question_type == 1:
        start_day = random.choice(DAYS_OF_WEEK)  # Random start day
        events = random.choices(["X", "Y", "Z"], k=3)
        final_day = simulate_event_sequence(start_day, events)
        truth_value = final_day == "Friday"
        question = f'''If the current day is {start_day}, and the events {events} happen, will it be Friday after 3 days?\n 
         Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True oe False>}}'''
        QT1 = "EF"

    elif question_type == 2:
        start_day, target_day = random.sample(DAYS_OF_WEEK, 2)
        sequence = find_minimum_sequence(start_day, target_day)
        question = f'''What is the minimum sequence of events to get from {start_day} to {target_day}?
        Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <events>}}'''
        truth_value = sequence
        QT1 = "AF"

    elif question_type == 3:
        start_day = random.choice(DAYS_OF_WEEK)  # Random start day
        events = random.choices(["X", "Y", "Z"], k=3)
        final_day = simulate_event_sequence(start_day, events)
        truth_value = final_day == "Tuesday"
        question = f'''Using the events {events}, can you get from {start_day} to Tuesday?
        Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True oe False>}}'''
        QT1 = "EU"


    elif question_type == 4:
        start_day = random.choice(DAYS_OF_WEEK)
        length = random.randint(1, 6)
        sequence = random.choices(["X", "Y", "Z"], k=length)
        truth_value = does_time_loop(start_day, sequence)
        question = f'''If the current day is {start_day}, does the sequence {sequence} cause time to loop back to {start_day}?
                    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True oe False>}}'''
        QT1 = "EG"

    elif question_type == 5:
        start_day, target_day = random.sample(DAYS_OF_WEEK, 2)
        sequence = find_minimum_sequence(start_day, target_day)
        question = f'''Is it possible to reach {target_day} from {start_day} within 9 events?
           Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True oe False>}}'''
        truth_value = sequence is not None
        QT1 = "EF"

    elif question_type == 6:
        start_day, target_day = random.sample(DAYS_OF_WEEK, 2)
        sequence = find_minimum_sequence(start_day, target_day)
        question = f'''Is it possible to reach {target_day} from {start_day} after only 1 event?
           Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True oe False>}}'''
        truth_value = sequence and len(sequence) == 1
        QT1 = "EF"

    elif question_type == 7:
        start_day = random.choice(DAYS_OF_WEEK)
        possible_days = get_possible_next_days(start_day)
        question = f'''Give me the list of days possible to be after {start_day}?(if z happens we stay on that day)
           Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <list of  days >}}'''
        truth_value = possible_days
        QT1 = "EX"

    return Context + question, truth_value , QT1, QT2

question, truth_value, QT1, QT2 = generate_question_type1()
print(f"Question: {question}")
print(f"Truth Value: {truth_value}")
print(f"CTL Type (QT1): {QT1}")
print(f"Question Type (QT2): {QT2}")
