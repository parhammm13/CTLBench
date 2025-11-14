import json
import random
import sys
sys.path.append(r'D:\uni\fifth semester\logic\CTL\faze2\githubcodes\Questions')


import question_type91 as q2
import question_type92 as q3
import question_type93 as q4
import question_type94 as q5
import question_type96 as q6
import Question9_6 as q7
import question_type97 as q8
import question_type98 as q9
import question_type99 as q10
import question_type910 as q11
import question_type22 as q12
import question_type23 as q13
import question_type24 as q14
import question_type25 as q15
import question_type26 as q16
import question_type27 as q17
import question_type28 as q18
import question_type29 as q19
import question_type100 as q20
import question_type101 as q21
import question_type102 as q22
import question_type103 as q23
import question_type104 as q24
import question_type105 as q25
import question_type107 as q27
import question_type108 as q28
import question_type109 as q29
import question_type1010 as q30
import question_type71 as q31
import question_type72 as q32
import question_type73 as q33
import question_type74 as q34
import question_type75 as q35
import question_type76 as q36
import question_type77 as q37
import question_type78 as q38
import question_type79 as q39
import question_type710 as q40
import question_type711 as q41
import question_type712 as q42
import question_type31 as q43
import question_type32 as q44
import question_type33 as q45
import question_type34 as q46
import question_type11 as q47
import question_type12 as q48
import question_type13 as q49
import question_type14 as q50
import question_type15 as q51
import question_type41 as q52
import question_type42 as q53
import question_type61 as q54
import question_type62 as q55
import question_type63 as q56
import question_type64 as q57
import question_type65 as q58
import question_type66 as q59
import question_type67 as q60
import question_type68 as q61
import question_type69 as q62
import question_type610 as q63
import question_type51 as q64
import question_type52 as q65
import question_type53 as q66
import question_type54 as q67
import question_type55 as q68
import question_type56 as q69
import question_type57 as q70
import question_type58 as q71
import question_type59 as q72

def generate_and_save_questions(num_questions, output_file):
    """Generate exactly n questions with distribution across different question types and save them to a JSON file."""
    error_count = 0
    total_generated = 0
    questions_data = []

    # Define a dictionary to store function names and how many times each function should execute
    functions_dict = {
        q2.generate_question_type1: 7,
        q3.generate_question_type1: 7,
        q4.generate_question_type1: 7,
        q5.generate_question_type1: 7,
        q6.generate_question_type1: 7,
        q7.generate_question_type1: 7,
        q8.generate_question_type1: 7,
        q9.generate_question_type1: 7,
        q10.generate_question_type1: 7,
        q11.generate_question_type1: 7,
        q12.generate_space_mission_question_type: 8,
        q13.generate_kingdom_defense_question_type: 8,
        q14.generate_cooking_tournament_question_type: 8,
        q15.generate_film_production_question_type: 8,
        q16.generate_question_type3: 8,
        q17.generate_question_type3: 8,
        q18.generate_question_type3: 8,
        q19.generate_question_type3: 8,
        q20.generate_question_type3: 3,
        q21.generate_question_type3: 3,
        q22.generate_question_type3: 3,
        q23.generate_question_type3: 3,
        q24.generate_question_type3: 3,
        q25.generate_question_type3: 3,
        q27.generate_question_type3: 3,
        q28.generate_question_type3: 3,
        q29.generate_question_type3: 3,
        q30.generate_question_type3: 3,
        q31.generate_question_type7: 6,
        q32.generate_space_question_type7: 6,
        q33.generate_fitness_question_type7: 6,
        q34.generate_cleaning_question_type7: 6,
        q35.generate_party_question_type7: 6,
        q36.generate_travel_question_type7: 6,
        q37.generate_circus_question_type7: 6,
        q38.generate_mission_question_type7: 6,
        q39.generate_cooking_question_type7: 6,
        q40.generate_patrol_question_type7: 6,
        q41.generate_vr_question_type7: 6,
        q42.generate_time_travel_question_type7: 6,
        q43.generate_question: 9,
        q44.generate_question: 11,
        q45.generate_question: 10,
        q46.generate_question: 10,
        q47.generate_question: 3,
        q48.generate_question: 3,
        q49.generate_question: 3,
        q50.generate_question: 3,
        q51.generate_question: 3,
        q52.generate_question: 2,
        q53.generate_question: 2,
        q54.generate_question: 2,
        q55.generate_question: 2,
        q56.generate_question: 2,
        q57.generate_question: 2,
        q58.generate_question: 2,
        q59.generate_question: 2,
        q60.generate_question: 2,
        q61.generate_question: 2,
        q62.generate_question: 2,
        q63.generate_question: 2,
        q64.generate_question: 6,
        q65.generate_question: 6,
        q66.generate_question: 6,
        q67.generate_question: 6,
        q68.generate_question: 6,
        q69.generate_question: 6,
        q70.generate_question: 6,
        q71.generate_question: 6,
        q72.generate_question: 6,
    }

    # Keep generating questions until the exact number is met
    while total_generated < num_questions:
        for func, repeat_count in functions_dict.items():
            # Generate questions for each function until we hit the target
            for _ in range(repeat_count):
                if total_generated < num_questions:
                    try:
                        # Generate a question by calling the function
                        quest, truth_label, QT1, QT2 = func()
                        questions_data.append({"question": quest, "truth_value": truth_label, "QT1": QT1, "QT2": QT2})
                        total_generated += 1
                    except Exception as e:
                        # If an error occurs, print an error message and continue with the next function
                        print(f"Error occurred while processing {func.__name__}: {e}")
                        error_count += 1
                        continue

            if total_generated >= num_questions:
                break

    # Write the generated questions and truth labels to a JSON file
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(questions_data, file, ensure_ascii=False, indent=4)

    print(f"Generated {num_questions} questions and saved to {output_file}")
    print(f"Total errors encountered: {error_count}")


# Example Usage:
num_questions_to_generate = 2500  # Total number of questions you want to generate
output_json_file = 'generated_questions.json'  # The file to save the questions and truth labels

# Generate the questions and save to JSON
generate_and_save_questions(num_questions_to_generate, output_json_file)
