import random

names = ["Elizabeth", "Alice", "Thomas", "Nicole", "George"]
sports = ["basketball", "baseball", "football", "volleyball", "handball", "water polo", "table tennis", "racing", "horse racing", "swimming"]
jobs = ["mechanic", "therapist", "construction worker", "mailman", "delivery person", "electrical engineer", "lawyer", "doctor", "psychologist", "sailor", "store owner"]

name = random.choice(names)
sport = random.choice(sports)
job =random.choice(jobs)

story = f"""{name} is at a crossroads in their {sport} career. They have been training for years 
to qualify for the national {sport} team, but they also has a stable job as a {job}. 
If they qualify for the team, they will spend the next year traveling and competing professionally, 
with the goal of securing a sponsorship deal by the end of the season. If they don't qualify, 
they plan to focus on their career as a {job}.."""

Questions = [
    f"""If {name} secures a sponsorship deal, did they qualify for the national {sport} team? 
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
""",
    f""". If {name} qualifies for the national {sport} team, will they start working?
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
""",
    f"""If {name} qualifies for the national {sport} team, must they start traveling and competing professionally next? 
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
""",
    f""". If {name} returns to working full-time, did they qualify for the team? 
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
""",
]

answers = [
    "True",
    "False",
    "True",
    "False"
]

type = [
    "AG",
    "AX",
    "AX",
    "AG"
]

arithmeticOrSemantic = [
    "semantic",
    "semantic",
    "semantic",
    "semantic"
]

# for i in range(len(Questions)):
#     print("\n=== Question {} ===".format(i + 1))
#     print(story)
#     print("Question:")
#     print(Questions[i])
#     print("answer: " + str(answers[i]))
#     print(arithmeticOrSemantic[i])
#     print("type: " + type[i])

def generate_question():
    i = random.randint(0, 1)
    question = story
    question = question + "\n" + Questions[i]
    truth_label = answers[i]
    CTLType = type[i]
    questionType = arithmeticOrSemantic[i]
    return question, truth_label, CTLType, questionType







