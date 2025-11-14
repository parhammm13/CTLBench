import random

def generate():
    name = random.choice(["Liam", "Noah", "Ethan", "Mason", "Lucas", "Aiden", "Carter", "Grayson"])
    advanced_knowledge = random.choice(
        ["gather advanced knowledge", "acquire future insights", "obtain cutting-edge information",
         "learn about future advancements", "collect progressive wisdom"])
    fixing_paradoxes = random.choice([
        "fixing paradoxes",
        "resolving inconsistencies",
        "correcting time conflicts",
        "amending anomalies",
        "rectifying contradictions"])

    story = f"""
    {name} is a time traveler with limited energy for his device. If he chooses to travel to the future, he can {advanced_knowledge} but risks running out of energy for a return trip. If he travels to the past, he must be careful 
    not to alter history, or he will have to spend extra energy {fixing_paradoxes}. If Noah conserves energy, he can 
    make multiple short trips instead of one long journey.
    """

    Questions = [
        f"""If {name} is stuck in the future, does he have enough energy for a return trip?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}""",
        f"""If {name} is {fixing_paradoxes}, did he travel to the future?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}""",
        f"""If {name} is {fixing_paradoxes}, where did he travel?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <Future or Past>}}""",
        f"""If {name} makes multiple short trips,has the conserved energy?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}""",
        f"""If {name} wants {advanced_knowledge}, where should he travel?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <Future or Past>}}""",
        f"""If {name} travels to the future, does he gather {advanced_knowledge} next?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}""",
        f"""Is there a scenario where {name} makes multiple short trips?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}""",
        f"""Will {name} always be limited to short trips if he conserves energy?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}""",
        f"""If {name} travels to the past, does he always have to be {fixing_paradoxes} next?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}""",
        f"""Will {name} always be able to be {fixing_paradoxes} if he spends extra energy?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}""",
        f"""Can {name} be {fixing_paradoxes} and gathering {advanced_knowledge} at the same time?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}"""
    ]

    Truth_label = ["False", "False", "Past", "True", "Future", "True", "True", "False", "False", "True", "False"]
    CTL_Type = ["AG", "AG", "EG","AG","EG", "AX", "EF", "EG", "AX", "AF" , "Complex"]
    Question_Type = ["Semantic", "Semantic", "Semantic", "Semantic", "Semantic", "Semantic", "Semantic", "Semantic", "Semantic", "Semantic", "Semantic"]
    return Truth_label, CTL_Type, Question_Type, Questions, story


def generate_question():
    Truth_label, CTL_Type, Question_Type, Questions, story = generate()
    i = random.randint(0,10)
    question = story + "\n" + Questions[i]
    truth_label = Truth_label[i]
    ctl_type = CTL_Type[i]
    question_type = Question_Type[i]
    return question , truth_label , ctl_type , question_type
