import random
from datetime import datetime, timedelta

# Possible replacements
names = ["Sarah", "John", "Osman", "Jeffrey", "Nia"]
activities_tests = {
    "theater performance": "acting evaluation",
    "musical recital": "vocal assessment",
    "dance showcase": "choreography review",
    "film production": "screen test",
    "opera": "singing audition"
}
workshops = {
    "theater performance": "acting workshops",
    "musical recital": "singing lessons",
    "dance showcase": "dance rehearsals",
    "film production": "script reading sessions",
    "opera": "stage combat training"
}

name = random.choice(names)
activity, test_name = random.choice(list(activities_tests.items()))
workshop = workshops[activity]

# Generate rehearsal dates
start_date = datetime(2025, 3, 5)

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
# Format dates without the year
format_date = lambda dt: dt.strftime("%B %d")

# List of questions
questions = [
    f"""How many more days does {name} get to rehearse if they earn the lead role compared to a supporting role?
Format your answer only as a JSON don’t include the unit, like JSON = {{"explanation": <your step by step solution>, "answer": <number of days>}}
    """,
    f"""How many more days can {name} rehearse if they are in a supporting role compared to a minor role?
Format your answer only as a JSON don’t include the unit, like JSON = {{"explanation": <your step by step solution>, "answer": <number of days>}}
    """,
    f"""Is there a possible scenario where {name} starts rehearsing immediately after receiving their {test_name}?
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    """,
    f"""Is there a possible scenario where {name} is required to attend {workshop} until they are allowed to rehearse for the {activity}?
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    """,
    f"""Is there a possible scenario where {name} will eventually be allowed to rehearse for the {activity}?
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    """,
    f"""Is there a possible scenario where {name} never gets to rehearse?
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    """
]

def generate_question():
    i = random.randint(0, 5)  # Randomly select a question index from 0 to 5
    story = f"""
    {name} is rehearsing for a {activity}, but their rehearsal schedule depends on their {test_name} results.
    • If {name} earns the lead role, they can rehearse from {format_date(date1)} to {format_date(date2)} every day.
    • If they are cast in a supporting role, they must attend {workshop} from {format_date(date3)} to {format_date(date4)} and can only rehearse from {format_date(date5)} to {format_date(date6)}.
    • If they are given a minor role, they will not be allowed to perform in the main show and can only rehearse from {format_date(date7)} to {format_date(date8)}.

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


