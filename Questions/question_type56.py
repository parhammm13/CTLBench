import random
from datetime import datetime, timedelta

# Possible replacements
names = ["Max", "Ethan", "Lucas", "Nathan", "Owen"]
places_professions = {
    "ancient temple": "archaeologist",
    "sunken shipwreck": "marine historian",
    "lost city ruins": "explorer",
    "prehistoric cave": "paleontologist",
    "forgotten fortress": "historian"
}

# Select random replacements
name = random.choice(names)
place, profession = random.choice(list(places_professions.items()))

# Generate exploration dates
start_date = datetime(2025, 9, 4)

def random_date(start, end):
    return start + timedelta(days=random.randint(1, (end - start).days))

date1 = start_date
date3 = random_date(date1 + timedelta(days=5), date1 + timedelta(days=30))
date2 = random_date(date1 + timedelta(days=3), date3 - timedelta(days=1))
date4 = random_date(date3 + timedelta(days=3), date3 + timedelta(days=30))
date5 = random_date(date4 + timedelta(days=3), date4 + timedelta(days=30))
date6 = random_date(date5 + timedelta(days=3), date5 + timedelta(days=20))

while (date2 - date1).days <= (date4 - date3).days:
    date4 = date4 - timedelta(days=1)

while (date4 - date3).days <= (date6 - date5).days:
    date6 = date6 - timedelta(days=1)


training_days_A = (date2 - date1).days
training_days_B = (date4 - date3).days
training_days_below_B = (date6 - date5).days
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
    f"""How many more days does {name} get to explore if full access is granted compared to restricted access?
Format your answer only as a JSON don’t include the unit, like JSON = {{"explanation": <your step by step solution>, "answer": <number of days>}}
    """,
    f"""How many more days can {name} explore if access is restricted compared to the site being deemed too fragile?
Format your answer only as a JSON don’t include the unit, like JSON = {{"explanation": <your step by step solution>, "answer": <number of days>}}
    """,
    f"""Is there a possible scenario where {name} starts exploring immediately after receiving the schedule?
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    """,
    f"""Is there a possible scenario where {name} is required to wait until they are allowed to explore the {place}?
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    """,
    f"""Is there a possible scenario where {name} will eventually be allowed to explore the {place}?
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    """,
    f"""Is there a possible scenario where {name} never gets to explore the {place}?
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    """
]

# Print the paragraph multiple times, each with a different question
def generate_question():
    i = random.randint(0, 5)  # Randomly select a question index from 0 to 5
    story = f"""
    {name} is exploring a {place}, but their access depends on the {profession}s' schedule.
    • If the excavation team grants full access, they can explore from {format_date(date1)} to {format_date(date2)} every day.
    • If the team restricts access for preservation work, they must wait until {format_date(date3)}, and can only explore from then until {format_date(date4)}.
    • If the site is deemed too fragile, they will only be allowed limited access from {format_date(date5)} to {format_date(date6)}.

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

