# # import random
# #
# # # Define the timeline and rules
# # DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# #
# # # Define the rules for events
# # def advance_time(current_day, event):
# #     """Simulates time movement based on the given event."""
# #     index = DAYS_OF_WEEK.index(current_day)
# #     if event == "X":  # Move forward by 1 day
# #         return DAYS_OF_WEEK[(index + 1) % len(DAYS_OF_WEEK)]
# #     elif event == "Y":  # Move backward by 2 days
# #         return DAYS_OF_WEEK[(index - 2) % len(DAYS_OF_WEEK)]
# #     elif event == "Z" and current_day == "Friday":  # Skip to Saturday
# #         return "Saturday"
# #     return current_day  # No time change if Z happens on a non-Friday day
# #
# # def simulate_event_sequence(start_day, events):
# #     """Simulates a sequence of events and returns the final day."""
# #     current_day = start_day
# #     for event in events:
# #         current_day = advance_time(current_day, event)
# #     return current_day
# #
# # def find_minimum_sequence_to_saturday():
# #     """Finds the minimum sequence of events to get to Saturday."""
# #     for length in range(1, 10):  # Arbitrary upper limit on sequence length
# #         for sequence in generate_event_sequences(length):
# #             if simulate_event_sequence("Wednesday", sequence) == "Saturday":
# #                 return sequence
# #     return None
# #
# # def generate_event_sequences(length):
# #     """Generates all possible sequences of events (X, Y, Z) of a given length."""
# #     events = ["X", "Y", "Z"]
# #     if length == 1:
# #         return [[e] for e in events]
# #     smaller_sequences = generate_event_sequences(length - 1)
# #     return [seq + [e] for seq in smaller_sequences for e in events]
# #
# # def does_time_loop(start_day, sequence):
# #     """Checks if a sequence causes time to loop back to the start day."""
# #     final_day = simulate_event_sequence(start_day, sequence)
# #     return final_day == start_day
# #
# # # Generate questions
# # def generate_question():
# #     """Randomly generates one of the four question types."""
# #     # question_type = random.choice([1, 2, 3, 4])  # Select a question type randomly
# #     question_type = 2
# #     if question_type == 1:
# #         # Question Type 1: After 3 days, can it be Friday?
# #         start_day = "Wednesday"
# #         events = random.choices(["X", "Y", "Z"], k=3)
# #         final_day = simulate_event_sequence(start_day, events)
# #         truth_value = final_day == "Friday"
# #         question = f"If the current day is {start_day}, and the events {events} happen, will it be Friday after 3 days?"
# #
# #     elif question_type == 2:
# #         # Question Type 2: Minimum sequence to get to Saturday
# #         sequence = find_minimum_sequence_to_saturday()
# #         truth_value = True  # By definition, this sequence gets to Saturday
# #         question = f"What is the minimum sequence of events to get from Wednesday to Saturday? Answer: {sequence}"
# #
# #     elif question_type == 3:
# #         # Question Type 3: Path to get from Monday to Tuesday
# #         start_day = "Monday"
# #         events = random.choices(["X", "Y", "Z"], k=3)
# #         final_day = simulate_event_sequence(start_day, events)
# #         truth_value = final_day == "Tuesday"
# #         question = f"Using the events {events}, can you get from {start_day} to Tuesday?"
# #
# #     else:  # Question Type 4: Time looping back to its starting day
# #         start_day = random.choice(DAYS_OF_WEEK)
# #         length = random.randint(1, 6)
# #         sequence = random.choices(["X", "Y", "Z"], k=length)
# #         truth_value = does_time_loop(start_day, sequence)
# #         question = f"If the current day is {start_day}, does the sequence {sequence} cause time to loop back to {start_day}?"
# #
# #     return question, truth_value
# #
# # # Generate and display a random question
# # question, truth_value = generate_question()
# # print(f"Question: {question}")
# # print(f"Truth Value: {truth_value}")
# import random
#
# # Define the timeline and rules
# DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#
#
# # Define the rules for events
# def advance_time(current_day, event):
#     """Simulates time movement based on the given event."""
#     index = DAYS_OF_WEEK.index(current_day)
#     if event == "X":  # Move forward by 1 day
#         return DAYS_OF_WEEK[(index + 1) % len(DAYS_OF_WEEK)]
#     elif event == "Y":  # Move backward by 2 days
#         return DAYS_OF_WEEK[(index - 2) % len(DAYS_OF_WEEK)]
#     elif event == "Z" and current_day == "Friday":  # Skip to Saturday
#         return "Saturday"
#     return current_day  # No time change if Z happens on a non-Friday day
#
#
# def simulate_event_sequence(start_day, events):
#     """Simulates a sequence of events and returns the final day."""
#     current_day = start_day
#     for event in events:
#         current_day = advance_time(current_day, event)
#     return current_day
#
#
# def generate_event_sequences(length):
#     """Generates all possible sequences of events (X, Y, Z) of a given length."""
#     events = ["X", "Y", "Z"]
#     if length == 1:
#         return [[e] for e in events]
#     smaller_sequences = generate_event_sequences(length - 1)
#     return [seq + [e] for seq in smaller_sequences for e in events]
#
#
# def find_minimum_sequence(start_day, target_day):
#     """Finds the minimum sequence of events to get from `start_day` to `target_day`."""
#     for length in range(1, 10):  # Check sequences of increasing lengths
#         for sequence in generate_event_sequences(length):
#             if simulate_event_sequence(start_day, sequence) == target_day:
#                 return sequence
#     return None  # No sequence found within the limit
#
#
# def does_time_loop(start_day, sequence):
#     """Checks if a sequence causes time to loop back to the start day."""
#     final_day = simulate_event_sequence(start_day, sequence)
#     return final_day == start_day
#
#
# # Generate questions
# def generate_question():
#     """Randomly generates one of the four question types."""
#     # question_type = random.choice([1, 2, 3, 4])
#     question_type = 2
#     if question_type == 1:
#         # Question Type 1: After 3 days, can it be Friday?
#         start_day = "Wednesday"
#         events = random.choices(["X", "Y", "Z"], k=3)
#         final_day = simulate_event_sequence(start_day, events)
#         truth_value = final_day == "Friday"
#         question = f"If the current day is {start_day}, and the events {events} happen, will it be Friday after 3 days?"
#
#     elif question_type == 2:
#         # Question Type 2: Minimum sequence to get from a random start day to a random target day
#         start_day, target_day = random.sample(DAYS_OF_WEEK, 2)
#         sequence = find_minimum_sequence(start_day, target_day)
#
#         if sequence:
#             question = f"What is the minimum sequence of events to get from {start_day} to {target_day}?"
#             truth_value = sequence
#         else:
#             question = f"Is it possible to reach {target_day} from {start_day} within 9 events?"
#             truth_value = False
#
#     elif question_type == 3:
#         # Question Type 3: Path to get from Monday to Tuesday
#         start_day = "Monday"
#         events = random.choices(["X", "Y", "Z"], k=3)
#         final_day = simulate_event_sequence(start_day, events)
#         truth_value = final_day == "Tuesday"
#         question = f"Using the events {events}, can you get from {start_day} to Tuesday?"
#
#     else:  # Question Type 4: Time looping back to its starting day
#         start_day = random.choice(DAYS_OF_WEEK)
#         length = random.randint(1, 6)
#         sequence = random.choices(["X", "Y", "Z"], k=length)
#         truth_value = does_time_loop(start_day, sequence)
#         question = f"If the current day is {start_day}, does the sequence {sequence} cause time to loop back to {start_day}?"
#
#     return question, truth_value
#
#
# # Generate and display a random question
# question, truth_value = generate_question()
# print(f"Question: {question}")
# print(f"Truth Value: {truth_value}")


import random

DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def advance_time(current_day, event):
    index = DAYS_OF_WEEK.index(current_day)
    if event == "X":
        return DAYS_OF_WEEK[(index + 1) % 7]
    elif event == "Y":
        return DAYS_OF_WEEK[(index - 2) % 7]
    elif event == "Z" and current_day == "Friday":
        return "Saturday"
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


def generate_question_type1():
    question_type = random.choice([1, 2, 3, 4, 5])  # Added Type 5
    if question_type == 1:
        start_day = "Wednesday"
        events = random.choices(["X", "Y", "Z"], k=3)
        final_day = simulate_event_sequence(start_day, events)
        truth_value = final_day == "Friday"
        question = f"If the current day is {start_day}, and the events {events} happen, will it be Friday after 3 days?"

    elif question_type == 2:
        start_day, target_day = random.sample(DAYS_OF_WEEK, 2)
        sequence = find_minimum_sequence(start_day, target_day)
        question = f"What is the minimum sequence of events to get from {start_day} to {target_day}?"
        truth_value = sequence

    elif question_type == 3:
        start_day = "Monday"
        events = random.choices(["X", "Y", "Z"], k=3)
        final_day = simulate_event_sequence(start_day, events)
        truth_value = final_day == "Tuesday"
        question = f"Using the events {events}, can you get from {start_day} to Tuesday?"

    elif question_type == 4:
        start_day = random.choice(DAYS_OF_WEEK)
        length = random.randint(1, 6)
        sequence = random.choices(["X", "Y", "Z"], k=length)
        truth_value = does_time_loop(start_day, sequence)
        question = f"If the current day is {start_day}, does the sequence {sequence} cause time to loop back to {start_day}?"

    elif question_type == 5:
        start_day, target_day = random.sample(DAYS_OF_WEEK, 2)
        sequence = find_minimum_sequence(start_day, target_day)
        question = f"Is it possible to reach {target_day} from {start_day} within 9 events?"
        truth_value = sequence is not None

    return  question, truth_value


question, truth_value = generate_question_type1()

print(f"Question: {question}")
print(f"Truth Value: {truth_value}")