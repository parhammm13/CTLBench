import random
from datetime import datetime, timedelta

# Possible replacements
names = ["Liam", "Ethan", "Noah", "James", "Oliver"]
activities_extra_classes = {
    "chess tournament": "strategy workshops",
    "math olympiad": "advanced problem-solving",
    "science fair": "research methodology",
    "robotics competition": "coding bootcamp",
    "debate championship": "public speaking training"
}

# Select random replacements
name = random.choice(names)
activity, extra_class = random.choice(list(activities_extra_classes.items()))

# Generate training dates
start_date = datetime(2025, 4, 3)

def random_date(start, end):
    return start + timedelta(days=random.randint(1, (end - start).days))

date1 = start_date
date3 = random_date(date1 + timedelta(days=5), date1 + timedelta(days=30))
date2 = random_date(date1 + timedelta(days=3), date3 - timedelta(days=1))
date4 = random_date(date3 + timedelta(days=3), date3 + timedelta(days=30))
date5 = random_date(date4 + timedelta(days=3), date4 + timedelta(days=30))
date6 = random_date(date5 + timedelta(days=3), date5 + timedelta(days=20))
date7 = random_date(date5 + timedelta(days=3), date5 + timedelta(days=20))
date8 = random_date(date7 + timedelta(days=3), date7 + timedelta(days=20))

while (date2 - date1).days <= (date6 - date5).days:
    date6 = date6 - timedelta(days=1)

while (date6 - date5).days <= (date8 - date7).days:
    date8 = date8 - timedelta(days=1)

training_days_A = (date2 - date1).days
training_days_B = (date6 - date5).days
training_days_below_B = (date8 - date7).days
extra_days_A_vs_B = training_days_A - training_days_B
extra_days_B_vs_below_B = training_days_B - training_days_below_B

# Ensure condition: (date2 - date1) > (date6 - date5)
max_attempts = 100  # Prevent infinite loop
attempts = 0
while (date2 - date1).days <= (date6 - date5).days and attempts < max_attempts:
    date6 = random_date(date5 + timedelta(days=3), date5 + timedelta(days=20))
    attempts += 1

if attempts == max_attempts:
    print("Warning: Max attempts reached while adjusting date6!")

# Format dates without the year
format_date = lambda dt: dt.strftime("%B %d")

# List of questions
questions = [
    f"""How many more days does {name} get to train if they rank in the top tier compared to the middle tier?
Format your answer only as a JSON don’t include the unit, like JSON = {{"explanation": <your step by step solution>, "answer": <number of days>}}
    """,
    f"""How many more days can {name} train if they rank in the middle tier compared to ranking below the middle tier?
Format your answer only as a JSON don’t include the unit, like JSON = {{"explanation": <your step by step solution>, "answer": <number of days>}}
    """,
    f"""Is there a possible scenario where {name} starts practicing immediately after receiving their result?
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    """,
    f"""Is there a possible scenario where {name} is required to attend {extra_class} until they are allowed to practice?
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    """,
    f"""Is there a possible scenario where {name} will eventually be allowed to practice for the {activity}?
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    """,
    f"""Is there a possible scenario where {name} never gets to practice?
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    """
]

# Print the paragraph multiple times, each with a different question
def generate_question():
    i = random.randint(0, 5)  # Randomly select a question index from 0 to 5
    story = f"""
    {name} is practicing for a {activity}, but their training schedule depends on their ranking in the qualifying rounds.
    • If {name} ranks in the top tier, they can train from {format_date(date1)} to {format_date(date2)} every day.
    • If they rank in the middle tier, they must attend {extra_class} from {format_date(date3)} to {format_date(date4)} and can only train from {format_date(date5)} to {format_date(date6)}.
    • If they rank below the middle tier, they will not be allowed to participate in the tournament and can only train from {format_date(date7)} to {format_date(date8)}..

Question: {questions[i]}
"""

    # Determine the answer based on question index
    if i < 2:
        truth_label = extra_days_A_vs_B if i == 0 else extra_days_B_vs_below_B
    elif i == 2:
        truth_label = "True"
    elif i == 3:
        truth_label = "True"
    elif i == 4:
        truth_label = "True"
    else:
        truth_label = "False"

    # Determine the type based on the question index
    if i < 2:
        CTLType = "EF"
    elif i == 2:
        CTLType = "EX"
    elif i == 3:
        CTLType = "EU"
    elif i == 4:
        CTLType = "AF"
    else:
        CTLType = "EG"

    # Determine if it's arithmetic or semantic
    questionType = "arithmetic" if i < 4 else "semantic"

    return story, truth_label, CTLType, questionType
