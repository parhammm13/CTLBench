import random
from datetime import datetime, timedelta

# Possible replacements
names = ["Sophia", "Olivia", "Emma", "Ava", "Mia"]
classes = {
    "ballet class": "dance performance",
    "painting class": "art exhibition",
    "drama class": "theater play",
    "physics class": "science fair",
    "chess strategy class": "chess tournament"
}
extra_classes = {
    "advanced choreography": "dance performance",
    "art history": "art exhibition",
    "acting techniques": "theater play",
    "mathematical modeling": "science fair",
    "grandmaster training": "chess tournament"
}

# Select random replacements
name = random.choice(names)
class_name, activity = random.choice(list(classes.items()))
extra_class = [key for key, value in extra_classes.items() if value == activity][0]

# Generate dates with conditions
start_date = datetime(2025, 6, 1)


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

# Ensure condition: (date2 - date1) > (date6 - date5)
while (date2 - date1).days <= (date6 - date5).days:
    date6 = date6 - timedelta(days=1)

while (date6 - date5).days <= (date8 - date7).days:
    date8 = date8 - timedelta(days=1)

# Compute extra lesson days if class is passed
practice_days_A = (date2 - date1).days
practice_days_B = (date6 - date5).days
practice_days_below_B = (date8 - date7).days
extra_days_A_vs_B = practice_days_A - practice_days_B
extra_days_B_vs_below_B = practice_days_B - practice_days_below_B

# List of questions
questions = [
    f"""How many more days does {name} get to practice {activity} if they score an A compared to a B?
Format your answer only as a JSON don't include the unit, like JSON = {{"explanation": <your step by step solution>, "answer": <number of days>}}
    """,
    f"""How many more days can {name} practice {activity} if they score a B compared to scoring below a B?
Format your answer only as a JSON don't include the unit, like JSON = {{"explanation": <your step by step solution>, "answer": <number of days>}}
    """,
    f"""Is there a possible scenario where {name} starts practicing {activity} immediately after receiving their grade?"
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    """,
    f"""Is there a possible scenario where {name} is required to attend {extra_class} until they are allowed to practice {activity}?"
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    """,
    f"""Is there a possible scenario where {name} will eventually be allowed to practice {activity}?
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    """,
    f"""Is there a possible scenario where {name} never gets to practice {activity}?
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
{format_date(date2)} every day. However, if they score a B, they must attend {extra_class} from 
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

