import random
def generate():
    names = ["Sophia", "Alex", "Jordan", "Taylor", "Chris", "Morgan", "Pat", "Casey"]
    name = random.choice(names)
    tech_job_title = random.choice(
        ["software developer", "data engineer", "product manager", "UX designer", "web developer"])
    research_field = random.choice(
        ["artificial intelligence", "quantum computing", "machine learning", "biotechnology", "neuroscience"])
    freelance_option = random.choice(
        ["freelance work", "part-time work", "consulting jobs", "remote work", "freelance writing"])
    paper_goal = random.choice(
        ["publish a paper", "present at a conference", "write a thesis", "develop a research project", "submit a patent"])

    story = f"""
    {name} sat down with their journal to map out their plans. If {name} gets the job offer from the tech company, 
    {name} will plan to move to the city and start their career as a {tech_job_title}; otherwise, {name} will focus on their 
    graduate studies in {research_field}.If {name} pursue graduate school and secure a scholarship, {name} will accept 
    and dedicate themselves fully to research, aiming to {paper_goal} by the end of the year.Alternatively, if no 
    scholarship materializes, {name} will apply for {freelance_option} to fund their studies.
    """
    Questions = [
        f"""Question: If {name} is aiming to {paper_goal}, has {name} gotten a scholarship?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}""",
        f"""Question: If {name} is exploring {freelance_option} opportunities, has {name} gotten the job offer?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}""",
        f"""Question: If {name} is exploring {freelance_option} opportunities, did {name} like the job?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}""",
        f"""Question: If {name} gets the job offer, what will their career be?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <name of profession>}}""",
        f"""Question: If {name} moves to the city , should {name} start a career in {tech_job_title}?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}""",
        f"""Question: Is there a scenario where sophie does {freelance_option} ? 
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}""",
        f"""Question: will {name} always  remain doing {freelance_option} if {name} gets a job offer? 
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}""",
        f"""Question: if {name} pursues graduate school, does {name} always get a scholarship next ?
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}""",
        f"""Question: will {name} always {paper_goal} at some point if {name} gets a scholarship? 
    Format your answer only as a JSON, like JSON = {{"explanation": <your step by step solution>, "answer": <True or False>}}"""
    ]

    Truth_label = ["True", "False", "False", f"{tech_job_title}", "True", "True", "False", "False", "True"]
    CTL_Type = ["AG", "AG", "AG", "EG", "EX", "EF", "EG", "AX", "AF"]
    Question_Type = ["Semantic", "Semantic", "Semantic", "Semantic", "Semantic", "Semantic", "Semantic", "Semantic", "Semantic"]
    return Truth_label , CTL_Type , Question_Type , Questions, story

def generate_question():
    Truth_label, CTL_Type, Question_Type, Questions, story = generate()
    i = random.randint(0, 8)  # Change the range from (0, 9) to (0, 8) to prevent index out of range
    question = story + "\n" + Question_Type[i]
    truth_label = Truth_label[i]
    ctl_type = CTL_Type[i]
    question_type = Question_Type[i]
    return question, truth_label, ctl_type, question_type
