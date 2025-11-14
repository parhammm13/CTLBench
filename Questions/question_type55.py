import random
from datetime import datetime, timedelta

# Possible replacements
names = ["Luna", "Taylor", "Selene", "Nova", "Leo"]

# Select random replacements
name = random.choice(names)

# Generate observation dates
start_date = datetime(2025, 10, 3)

def random_date(start, end):
    return start + timedelta(days=random.randint(1, (end - start).days))

date1 = start_date
date3 = random_date(date1 + timedelta(days=5), date1 + timedelta(days=30))
date2 = random_date(date1 + timedelta(days=3), date3 - timedelta(days=1))
date4 = random_date(date3 + timedelta(days=3), date3 + timedelta(days=30))
date5 = random_date(date4 + timedelta(days=3), date4 + timedelta(days=30))
date6 = random_date(date5 + timedelta(days=3), date5 + timedelta(days=30))

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
    f"""How many more nights does {name} get to stargaze if the sky remains clear compared to occasional cloudy nights?
Format your answer only as a JSON don’t include the unit, like JSON = {{"explanation": <your step by step solution>, "answer": <number of days>}}
    """,
    f"""How many more nights can {name} observe if there are occasional cloudy nights compared to a mostly rainy season?"
Format your answer only as a JSON don’t include the unit, like JSON = {{"explanation": <your step by step solution>, "answer": <number of days>}}
    """,
    f"""Is there a possible scenario where {name} starts observing immediately after understanding the weather condition?
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    """,
    f"""Is there a possible scenario where {name} is required to wait for better visibility until they can observe the night sky?
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    """,
    f"""Is there a possible scenario where {name} will eventually be able to observe the night sky?
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    """,
    f"""Is there a possible scenario where {name} doesn’t get to observe the night sky?
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    """
]

# Print the paragraph multiple times, each with a different question
def generate_question():
    i = random.randint(0, 5)  # Randomly select a question index from 0 to 5
    story = f"""
    {name} is observing the night sky, but their stargazing schedule depends on the weather conditions.
    • If the sky remains clear throughout the season, they can observe the stars from {format_date(date1)} to {format_date(date2)} every night.
    • If there are occasional cloudy nights, they must wait for better visibility and can only observe from {format_date(date3)} to {format_date(date4)}.
    • If the season is mostly rainy, they will only have a brief window to stargaze from {format_date(date5)} to {format_date(date6)}.

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

    return story, truth_label, CTLType, questionType, NameType

