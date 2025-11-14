import random

import addid
import identical_finder
import deleteexplain
import json
import re
from collections import Counter


input_json_file = 'generated_questions3.json'  # The JSON file with generated questions
output_json_file = 'cleaned_questions3.json'  # Output file to save cleaned data

def addid(questions):
    # Ensure all questions have an 'id' field
    for index, question in enumerate(questions):
        question["id"] = index  # Assign ID = array index, even if it's already there

    return questions


def deletexp(data):
    for item in data:
        question = item['question']
        # Use regex to remove the "explanation" line from the example JSON
        modified_question = re.sub(r'"explanation": <your step by step solution>,\s*', '', question)
        item['question'] = modified_question
    return data

def process_and_write_cleaned_data(data):

    # Extract all questions from the data
    questions = [entry['question'] for entry in data]

    # Count occurrences of each question using Counter
    question_counts = Counter(questions)

    # Identify and count duplicate questions (those with more than 1 occurrence)
    identical_questions = {question: count for question, count in question_counts.items() if count > 1}

    if len(identical_questions) == 0:
        print("No duplicates detected. The data is already clean.")
        return  # If no duplicates, exit early as data is already clean

    # Print out how many identical questions exist, without repeating questions
    print(f"Identical questions found: {len(identical_questions)}")
    print("The identical questions and their counts are:")

    for question in identical_questions.keys():
        print(f"Question: '{question}' appears {identical_questions[question]} times.")

    # Remove duplicates from the data (keeping only unique questions)
    unique_questions = list(set(questions))  # This will get unique questions only
    cleaned_data = []

    for entry in data:
        if entry['question'] in unique_questions:
            cleaned_data.append(entry)
            unique_questions.remove(entry['question'])  # Remove after adding to prevent duplicates

    return cleaned_data

# Open the JSON file and load data
with open(input_json_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

data = process_and_write_cleaned_data(data)
data= deletexp(data)
random.shuffle(data)
data= addid(data)

with open(output_json_file, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)


print("saved and done")