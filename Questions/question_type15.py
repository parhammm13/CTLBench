import random
from datetime import datetime, timedelta

def generate():
    names = ("Emily", "Michael", "Sophia", "James", "Olivia", "William", "Ava", "Ethan", "Isabella", "Alexander")
    weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
    weekend_days = ("Saturday", "Sunday")
    chores = (
        "washes the dishes",
        "cleans the room",
        "dusts the shelves",
        "vacuum the floor",
        "mops the kitchen",
        "takes out the trash",
        "does the laundry",
        "cleans the windows",
        "organizes the closet",
        "feeds the pets"
    )
    # Select random replacements
    name = random.choice(names)
    weekday = random.choice(weekdays)
    weekend = random.choice(weekend_days)
    chore1 , chore2 , chore3, chore4= random.sample(chores , 4)
    screentime = random.randint(2, 7)
    extra_minutes = random.randint(10, 90)

    # Generate questions
    Questions = [
        f"""How much screen time does {name} have on {weekend} in minutes, if {name} {chore1} and {chore2} and {chore3}?
    Format your answer only as a JSON dont include the unit, like JSON = {{"explanation": <your step by step solution>, "answer": <number of minutes>}}
    Truth Label: {((screentime+1) * 60)+(extra_minutes*3)}
    CTL type: Complex
    Question Type: Arithmatic""",
        f"""How much screen time does {name}  have on {weekday} in minutes, if {name} {chore4}?
    Format your answer only as a JSON dont include the unit, like JSON = {{"explanation": <your step by step solution>, "answer": <number of minutes>}}
    Truth Label: {(screentime * 60)+extra_minutes}
    CTL type: Complex
    Question Type: Arithmatic""",
        f"""will {name} always have daily screen time at one point?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    Truth Label: True
    CTL type: AF
    Question Type: Semantic""",
        f"""will {name} not get screen time if {name} didn't do any house chores?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    Truth Label: False
    CTL type: EF
    Question Type: Semantic"""
    ]


    # Print the paragraph and questions
    story = f"""
    {name} has a daily screen time of {screentime} hours on weekdays and {screentime + 1} hours on the weekend, but {name}'s father has a rule that for each house chore he does he gets {extra_minutes} more minutes of screen time. 
    """

    Truth_label = [f"{((screentime+1) * 60)+(extra_minutes*3)}",f"{(screentime * 60)+extra_minutes}", "True", "False"]
    CTL_Type = ["Complex","Complex", "AF", "EF"]
    Question_Type = ["Arithmatic","Arithmatic", "Semantic", "Semantic"]
    return Truth_label, CTL_Type, Question_Type, Questions, story


def generate_question():
    Truth_label, CTL_Type, Question_Type, Questions , story= generate()
    i = random.randint(0, 2)
    question =story + "\n" + Questions[i]
    truth_label = Truth_label[i]
    ctl_type = CTL_Type[i]
    question_type = Question_Type[i]
    return question, truth_label, ctl_type, question_type



