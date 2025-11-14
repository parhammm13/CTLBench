import random
from datetime import datetime, timedelta
def generate():
    # Possible replacements
    names = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
    fields = ["technology", "finance", "healthcare", "automotive", "pharmaceutical"]
    companies = ["company", "corporation", "enterprise", "startup", "firm"]
    seasons = ["Spring", "Summer", "Fall", "Winter"]

    # Select random replacements
    name = random.choice(names)
    field = random.choice(fields)
    company_type = random.choice(companies)
    company = f"{field} {company_type}"
    season1, season2 = random.sample(seasons, 2)

    # Generate vacation dates
    start_date = datetime(2025, 1, 1)
    end_date = datetime(2025, 12, 31)

    def random_date(start, end):
        return start + timedelta(days=random.randint(0, (end - start).days))

    # Generate date1 as a random date within the year
    date1 = random_date(start_date, end_date)

    # Set the maximum date2 by adding 20 days to date1, while ensuring it does not exceed end_date
    max_date2 = min(date1 + timedelta(days=20), end_date)
    while(max_date2 == end_date):
        date1 = date1 - timedelta(days=1)
        max_date2 = min(date1 + timedelta(days=20), end_date)
    # Generate date2 to be greater than date1 and within the allowed range
    date2 = random_date(date1 + timedelta(days=1), max_date2)

    # Random increase between 2 and 10 days
    vacation_increase = random.randint(2, 10)

    format_date = lambda dt: dt.strftime("%B %d")
    answer_date = lambda dt: dt.strftime("%m/%d")

    Questions = [
        f"""If {name}'s work performance was positive in {season1} and {season2}, when should they plan their vacation next year?
    Format your answer only as a JSON dont include the unit, like JSON = {{"explanation": <your step by step solution>, "answer": <date1:MM/DD to date2: MM/DD>}}
    Truth Label: {answer_date(date1)} to {answer_date(date2 + timedelta(days=vacation_increase*2))}
    CTL type: Complex
    Question Type: Arithmatic""",
        f"""Will {name} always have vacation days at one point?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    Truth Label: True
    CTL type: AF
    Question Type: Semantic""",
        f"""Will {name} not get vacation days if they didn't get positive work performance reviews any season of the year?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    Truth Label: False
    CTL type: EF
    Question Type: Semantic"""]

    story = f"""
    {name} works in a {company} where the employees can take vacation days from {format_date(date1)} to {format_date(date2)}, but depending on whether their work performance was positive in each season, they gain a {vacation_increase}-day increase in their vacation days for the next year.
    """

    Truth_label = [f"{answer_date(date1)} to {answer_date(date2 + timedelta(days=vacation_increase*2))}", "True", "False"]
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



