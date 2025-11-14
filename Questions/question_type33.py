import random
import numpy

def generate():
    Veridia = random.choice(["Zephyria", "Nandor", "Lunaria", "Drakonis", "Aetheria", "Veridia"])
    Dornia = random.choice(["Cylindria", "Glimmerfell", "Vortexia", "Mystara", "Eldoria", "Dornia"])
    tech_prod, luxury_prod, raw_material, agricultural_prod = random.sample(
        ["high-tech products", "luxury goods", "essential raw materials",
         "agricultural products", "energy resources",
         "pharmaceuticals", "automotive parts", "machinery",
         "chemical products", "construction materials",
         "metals and minerals", "consumer electronics"], 4)
    farming, manufacturing = random.sample([
        "domestic farming efforts", "manufacturing",
        "renewable energy projects", "infrastructure development",
        "water resource management", "technological innovation programs"], 2)

    story = f"""{Veridia} and {Dornia} have a trade agreement with specific import and export rules.
     If {Veridia} allows {tech_prod} to be exported, it can import {luxury_prod} from {Dornia}.
      Otherwise, it must focus on importing {raw_material}. If {Dornia} restricts agricultural 
      exports, {Veridia} will need to increase {farming}. However, if the exports of {agricultural_prod}
       are permitted, {Veridia} can reduce it's investments on {farming} and focus on {manufacturing}."""

    Questions = [
        f"""If {Veridia} is importing {luxury_prod}, is it exporting {tech_prod}?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    Truth Label: True
    CTL Type: AG
    Question Type: Semantic""",
        f"""If {Veridia} is increasing {farming}, is {Dornia} restricting {agricultural_prod} exports?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    Truth Label: True
    CTL Type: AG
    Question Type: Semantic""",
        f"""If {Veridia} is focusing on {manufacturing}, have they been increasing their investments on {farming}?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    Truth Label: False
    CTL Type: AG
    Question Type: Semantic""",
        f"""If {Veridia} does not export {tech_prod}, have they been importing {raw_material}?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    Truth Label: True
    CTL Type: EG
    Question Type: Semantic""",
        f"""If {Veridia} exports {tech_prod}, does it import {luxury_prod} next?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    Truth Label: True
    CTL Type: EX
    Question Type: Semantic""",
        f"""Is there a scenario where {Veridia} increases {farming}?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    Truth Label: True
    CTL Type: EF
    Question Type: Semantic""",
        f"""Will {Veridia} always focus on {farming} if {Dornia} restricts the exports of {agricultural_prod}?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    Truth Label: True
    CTL Type: EG
    Question Type: Semantic""",
        f"""If {Dornia} restricts the exports of {agricultural_prod}, does {Veridia} always increase {farming} next?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    Truth Label: True
    CTL Type: AX
    Question Type: Semantic""",
        f"""Will {Veridia} always import {luxury_prod} at some point if it exports {tech_prod}?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    Truth Label: True
    CTL Type: AX
    Question Type: Semantic""",
        f"""Can {Veridia} import {luxury_prod} from {Dornia} and reduce investments on {farming} at the same time ?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}
    Truth Label: True
    CTL Type: Complex
    Question Type: Semantic"""
    ]
    Truth_label = ["True", "True", "False", "True", "True", "True", "True", "True", "True", "True"]
    CTL_Type = ["AG", "AG","AG", "EG", "EX", "EF", "EG", "AX", "AX", "Complex" ]
    Question_Type = ["Semantic", "Semantic", "Semantic", "Semantic", "Semantic", "Semantic", "Semantic", "Semantic", "Semantic", "Semantic"]
    return Truth_label, CTL_Type, Question_Type, Questions, story

def generate_question():
    Truth_label, CTL_Type, Question_Type, Questions, story = generate()
    i = random.randint(0,9)
    question = story + "\n" + Questions[i]
    truth_label = Truth_label[i]
    ctl_type = CTL_Type[i]
    question_type = Question_Type[i]
    return question , truth_label , ctl_type , question_type
print(generate_question())