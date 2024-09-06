import json


def parse_questions(file_path):
    questions = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        question_data = {}
        options = []
        for line in lines:
            line = line.strip()
            if line.startswith('Q.'):
                if question_data:
                    question_data['options'] = options
                    questions.append(question_data)
                    question_data = {}
                    options = []
                question_data['question'] = line[3:]
            elif line.startswith(('a.', 'b.', 'c.', 'd.')):
                option, value = line.split('. ', 1)
                options.append({option: value})
            elif line.startswith('correct:'):
                question_data['correct_option'] = line.split(': ')[1]

    if question_data:
        question_data['options'] = options
        questions.append(question_data)

    return {'questions': questions}


def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def load_quiz_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def run_quiz(quiz_data):
    score = 0
    total_questions = len(quiz_data['questions'])

    for question in quiz_data['questions']:
        print(f"\nQ. {question['question']}")
        for option in question['options']:
            for key, value in option.items():
                print(f"{key}. {value}")

        user_answer = input("Your answer (a/b/c/d): ").lower()

        if user_answer == question['correct_option']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer was {question['correct_option']}.")

    print(f"\nQuiz completed! Your score: {score}/{total_questions}")


if __name__ == "__main__":
    text_file_path = 'quiz_questions.txt'
    json_file_path = 'quiz_data.json'
    quiz_data = parse_questions(text_file_path)
    save_json(quiz_data, json_file_path)
    run_quiz(quiz_data)