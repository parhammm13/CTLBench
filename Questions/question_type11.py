import random
from datetime import datetime, timedelta
def generate():
    # Possible replacements
    names = ("Luna", "Jasper", "Amara", "Finn", "Zara", "Asher", "Clara", "Dante")
    car_names = ["Tesla Model S", "Ford Mustang", "Chevrolet Camaro", "BMW 3 Series", "Audi A4"]

    # Select random replacements
    name = random.choice(names)

    car = random.choice(car_names)

    # Generate vacation dates
    start_date = datetime(2025, 1, 1)
    end_date = datetime(2025, 12, 31)

    def random_date(start, end):
        return start + timedelta(days=random.randint(0, (end - start).days))

    # Generate date1 as a random date within the year
    date1 = random_date(start_date, end_date)

    # Generate date2 to be greater than date1 and within the allowed range
    date2 = min(date1 + timedelta(days=random.randint(35, 80)), end_date)
    date3 = date2 - timedelta(days=random.randint(2, 34))

    # Format dates without the year
    format_date = lambda dt: dt.strftime("%B %d")

    # Generate questions
    Questions = [
        f"""How many more days can {name} rent {car} if {name} has a good driving record?
    Format your answer only as a JSON dont include the unit, like JSON = {{"explanation": <your step by step solution>, "answer":<number of days>}}
    Truth Label: {((date2 - date1).days)-((date3 - date1).days)}
    CTL type: Complex
    Question Type: Arithmatic""",
        f"""will {name} always get a rental car at one point?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}""",
        f"""Can {name} not rent a car if {name} has traffic violations?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}"""]


    # Print the paragraph and questions
    story = f"""
    {name} is a driver looking to rent a {car}. If he has no traffic violations, {name} can rent {car} from {format_date(date1)}, to {format_date(date2)} , However, if {name} has one or more violations, he can only rent a car from {format_date(date1)}, to {format_date(date3)}.
    """

    Truth_label = [f"{((date2 - date1).days)-((date3 - date1).days)}", "True", "False"]
    CTL_Type = ["Complex", "AF", "EF"]
    Question_Type = ["Arithmatic", "Semantic", "Semantic"]
    return Truth_label, CTL_Type, Question_Type, Questions, story


def generate_question():
    Truth_label, CTL_Type, Question_Type, Questions, story = generate()
    i = random.randint(0, 2)
    question = story + "\n" + Questions[i]
    truth_label = Truth_label[i]
    ctl_type = CTL_Type[i]
    question_type = Question_Type[i]
    name = 'question_type15' + '_'
    return question , truth_label , ctl_type , question_type

