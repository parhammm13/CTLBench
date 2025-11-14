#nick

import random
from datetime import datetime, timedelta

def generate():
# Possible replacements
    names = ["Alex", "Chris", "Jordan", "Taylor", "Morgan"]
    sports = ["basketball player", "tennis player", "soccer player", "runner", "gymnast"]
    activities = {"basketball player": "playing basketball", "tennis player": "playing tennis", "soccer player": "playing soccer", "runner": "running", "gymnast": "doing gymnastics"}
    courses = ["physics", "calculus", "history", "biology", "programming"]


    # Select random replacements
    name = random.choice(names)
    sport = random.choice(sports)
    activity = activities[sport]
    course = random.choice(courses)


    # Generate vacation dates
    start_date = datetime(2025, 1, 1)
    end_date = datetime(2025, 12, 31)

    def random_date(start, end):
       return start + timedelta(days=random.randint(0, (end - start).days))


    date1 = random_date(start_date, end_date)
    while(end_date == min(date1 + timedelta(days=50) , end_date)):
        date1 = date1 - timedelta(days=1)
    date3 = random_date(date1 + timedelta(days=5), date1 + timedelta(days=50))
    date2 = random_date(date1 + timedelta(days=3), date3 - timedelta(days=1))
    date4 = random_date(date3 + timedelta(days=3), date3 + timedelta(days=30))
    date5 = random_date(date4 + timedelta(days=3), date4 + timedelta(days=30))
    date6 = random_date(date5 + timedelta(days=3), date5 + timedelta(days=20))

    # Ensure condition: (date2 - date1) > (date6 - date5)
    max_attempts = 100  # Prevent infinite loop
    attempts = 0
    while (date2 - date1).days <= (date6 - date5).days and attempts < max_attempts:
       date6 = random_date(date5 + timedelta(days=3), date5 + timedelta(days=20))
       attempts += 1


    if attempts == max_attempts:
       print("Warning: Max attempts reached while adjusting date6!")


    # Compute extra lesson days if course is passed
    lesson_days_pass = (date2 - date1).days
    lesson_days_fail = (date6 - date5).days
    extra_days = lesson_days_pass - lesson_days_fail


    # Check if the person will always have a lesson
    always_has_lessons = lesson_days_pass > 0 or lesson_days_fail > 0


    # Check if no lessons are possible on failure
    no_lessons_if_fail = lesson_days_fail == 0


    # Format dates without the year
    format_date = lambda dt: dt.strftime("%B %d")

    date1 = format_date(date1)
    date2 = format_date(date2)
    date3 = format_date(date3)
    date4 = format_date(date4)
    date5 = format_date(date5)
    date6 = format_date(date6)



    # Formulate final story
    story = f"""
    {name} is a professional {sport} in high school and has a {course} course this semester.
    If {name} passes {course}, they can continue {activity} from {date1} till {date2}.
    But if they have to retake {course} from {date3} till {date4}, they can only continue {activity} from {date5} till {date6}.
    """

    q1 = f"""How many more days can {name} continue {activity} if they pass {course}?
    Format your answer only as a JSON dont include the unit, like JSON = {{"explanation": <your step by step solution>, "answer": <number of days>}}"""
    q2 = f"""Will {name} always be able to continue {activity} at some point?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True oe False>}}"""
    q3 = f"""Can {name} not continue {activity} if they didn't pass {course}?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True oe False>}}"""

    Questions = [q1, q2, q3]

    Truth_label = [f"{extra_days}", "True", "False"]
    CTL_Type = ["Complex", "AF", "EF"]
    Question_Type = ["Arithmatic", "Semantic", "Semantic"]
    return Truth_label, CTL_Type, Question_Type, Questions, story


def generate_question():
    Truth_label, CTL_Type, Question_Type, Questions , story= generate()
    i = random.randint(0, 2)
    question = story + "\n" + Questions[i]
    truth_label = Truth_label[i]
    ctl_type = CTL_Type[i]
    question_type = Question_Type[i]
    return question, truth_label, ctl_type, question_type


