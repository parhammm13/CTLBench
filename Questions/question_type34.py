import random

import numpy
import pandas


def generate():
    crimes = ["bank robbery", "cyber attack", "drug trafficking",  "kidnapping", "fraud", "human trafficking", "homicide"]
    actions1 = {
        "bank robbery": "apprehend the robbers",
        "cyber attack": "track the hackers ",
        "drug trafficking": "seize the illegal substances",
        "homicide": "identify the perpetrator",
        "human trafficking": "rescue the victims",
        "fraud": "expose the scam",
        "kidnapping": "rescue the hostage"
    }
    actions2 = {
        "bank robbery": "recover the stolen money",
        "cyber attack": "secure the compromised systems",
        "drug trafficking": "dismantle the cartel",
        "homicide": "deliver justice for the victim",
        "human trafficking": "prosecute the traffickers",
        "fraud": "compensate the defrauded individuals",
        "kidnapping": "ensure their safe return"
    }
    name = random.choice(["Isabelle", "Willow", "Aurora", "Scarlett", "Hazel"])
    crime = random.choice(crimes)
    action1 = actions1[crime]
    action2 = actions2[crime]


    story = f"""
    Detective {name} is investigating a high-profile {crime}. If she finds solid evidence linking the prime suspect 
    to the crime, she will proceed with an arrest and close the case. Otherwise, she will expand the investigation 
    to other potential suspects. If the prime suspect is arrested and confesses, {name} will {action1} and {action2}. 
    However, if the suspect denies involvement, {name} will need to gather more evidence and request a court trial.
    """
    Questions = [
        f"""If {name} is expanding the investigation, did she find solid evidence against the prime suspect?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    Truth Label: False
    CTL Type: AG
    Question Type: Semantic""",
        f"""If {name} has {action1},has the suspect denied involvement?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    Truth Label: False
    CTL Type: AG
    Question Type: Semantic""",
        f"""If {name} is preparing for a court trial,has the suspect confessed?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    Truth Label: False
    CTL Type: AG
    Question Type: Semantic""",
        f"""If {name} is preparing for a court trial,has the suspect denied involvement?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    Truth Label: True
    CTL Type: EG
    Question Type: Semantic""",
        f"""If {name} finds solid evidence, does she arrest the prime suspect next?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    Truth Label: True
    CTL Type: EX
    Question Type: Semantic""",
        f"""Is there a scenario where {name} expands the investigation?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    Truth Label: True
    CTL Type: EF
    Question Type: Semantic""",
        f"""Will {name} always keep investigating if she finds solid evidence?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    Truth Label: False
    CTL Type: EG
    Question Type: Semantic""",
        f"""If {name} arrests the prime suspect, does the suspect always confess next?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    Truth Label: False
    CTL Type: AX
    Question Type: Semantic""",
        f"""Will {name} always {action1} at some point if the suspect confesses?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    Truth Label: True
    CTL Type: AF
    Question Type: Semantic""",
        f"""Can {name} {action1} and request a court trial at the same time?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    Truth Label: False
    CTL Type: Complex
    Question Type: Semantic"""
    ]

    Truth_label = ["False", "False", "False", "True", "True", "True", "False", "False", "True", "False"]
    CTL_Type = ["AG", "AG","AG", "EG", "EX","EF", "EG", "AX", "AF", "Complex" ]
    Question_Type = ["Semantic", "Semantic", "Semantic", "Semantic", "Semantic", "Semantic", "Semantic", "Semantic", "Semantic" , "Semantic"]
    return Truth_label, CTL_Type, Question_Type, Questions, story

def generate_question():
    Truth_label, CTL_Type, Question_Type, Questions,story = generate()
    i = random.randint(0,9)
    question = story + "\n" + Questions[i]
    truth_label = Truth_label[i]
    ctl_type = CTL_Type[i]
    question_type = Question_Type[i]
    return question , truth_label , ctl_type , question_type
