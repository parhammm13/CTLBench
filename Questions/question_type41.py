import random

names = ["Lila", "Harrison", "Oscar", "Ivy", "Grayson", "Clara", "Sky", "Hunter", "Joe", "Lily"]
activities = ["art", "painting", "photographing", "sculpting", "drawing", "sketching", "animating", "woodworking", "glass art"]
courses = ["algebra", "music", "physics", "geometry", "English", "chemistry", "Spanish", "biology", "science", "calculus"]


name = random.choice(names)
activity = random.choice(activities)
course =random.choice(courses)

story = f"""{name} is preparing for a major life decision involving their passion for {activity} and their 
career in teaching {course}. If they win the prestigious {activity} fellowship, they'll dedicate the 
next year to traveling and working on their {activity} projects, aiming to hold their first solo exhibition 
by the end of the year. If they don't win the fellowship, they plan to return to teaching {course} 
full-time at their local high school."""

Questions = [
    f"""If {name} is holding their first solo exhibition, did they win the fellowship? 
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
""",
    f""". If {name} wins the art fellowship, will she start teaching? 
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
""",
    f"""If {name} wins the {activity} fellowship, must she start traveling and working on their {activity} projects next? 
Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
""",
    f""". If {name} returns to teaching full-time at their local high school, did they win the fellowship? 
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

def generate_question():
    i = random.randint(0, 1)
    question = story
    question = question + "\n" + Questions[i]
    truth_label = answers[i]
    CTLType = type[i]
    questionType = arithmeticOrSemantic[i]
    return question, truth_label, CTLType, questionType

