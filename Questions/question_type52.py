import random
from datetime import datetime, timedelta

# Possible replacements
names = ["Jake", "Ethan", "Liam", "Noah", "Mason"]
activities_classes = {
    "marathon": "stamina assessment",
    "cycling competition": "physical endurance test",
    "swimming competition": "athletic evaluation",
    "tennis competition": "performance benchmark",
    "basketball competition": "cardio fitness check"
}
extra_classes = {
    "stamina assessment": "conditioning class",
    "physical endurance test": "strength training",
    "athletic evaluation": "endurance training",
    "performance benchmark": "flexibility session",
    "cardio fitness check": "speed drills"
}

# Select random replacements
name = random.choice(names)
activity, test_name = random.choice(list(activities_classes.items()))
class_name = extra_classes[test_name]

# Generate training dates
start_date = datetime(2025, 3, 1)


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

# Compute extra training days
training_days_A = (date2 - date1).days
training_days_B = (date6 - date5).days
training_days_below_B = (date8 - date7).days
extra_days_A_vs_B = training_days_A - training_days_B
extra_days_B_vs_below_B = training_days_B - training_days_below_B

# List of questions
questions = [
    f"""How many more days does {name} get to train if they score an excellent result compared to a moderate result?
    Format your answer only as a JSON don’t include the unit, like JSON = {{"explanation": <your step by step solution>, "answer": <number of days>}}
    """,
    f"""How many more days can {name} train if they score a moderate result compared to scoring below the required level?
    Format your answer only as a JSON don’t include the unit, like JSON = {{"explanation": <your step by step solution>, "answer": <number of days>}}
    """,
    f"""Is there a possible scenario where {name} starts training immediately after receiving their score?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    """,
    f"""Is there a possible scenario where {name} is required to attend {class_name} until they are allowed to train for the {activity}?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    """,
    f"""Is there a possible scenario where {name} will eventually be allowed to train for the {activity}?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    """,
    f"""Is there a possible scenario where {name} never gets to train?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    """
]

# Format dates without the year
format_date = lambda dt: dt.strftime("%B %d")


def generate_question():
    i = random.randint(0, 5)  # Randomly select a question index from 0 to 5
    story = f"""
{name} is preparing for their {activity}, but their practice schedule depends on their school grades.
If {name} scores an A in their {class_name}, they can practice from {format_date(date1)} to 
{format_date(date2)} every day. However, if they score a B, they must attend {extra_classes} from 
{format_date(date3)} to {format_date(date4)} and can only practice {activity} from {format_date(date5)}
to {format_date(date6)}. If they score below a B, they will not be allowed to participate in the 
{activity} and can only practice from {format_date(date7)} to {format_date(date8)}.

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

