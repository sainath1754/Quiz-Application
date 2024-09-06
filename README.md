# Terminal Quiz App

This is a simple terminal-based quiz application written in Python. It reads questions from a text file, converts them to a JSON-like structure, and then presents them to the user in an interactive quiz format.

## Features

- Read quiz questions from a simple text file format
- Convert text file to JSON structure for easy processing
- Interactive command-line interface
- Score tracking and final score display
- Easy to add, remove, or modify questions

## Requirements

- Python 3.6+
- No external libraries required

## Installation

1. Clone this repository or download the `quiz_app.py` file.
2. Ensure you have Python 3.6 or higher installed on your system.

## Usage

1. Create a text file named `quiz_questions.txt` in the same directory as `quiz_app.py`. Format your questions as follows:

   ```
   Q. What is the capital of France?
   a. London
   b. Berlin
   c. Paris
   d. Madrid
   correct: c

   Q. What is 2 + 2?
   a. 3
   b. 4
   c. 5
   d. 6
   correct: b
   ```

2. Run the script using Python:

   ```
   python quiz_app.py
   ```

3. The quiz will start in your terminal. Answer each question by typing the letter corresponding to your choice (a, b, c, or d) and pressing Enter.

4. After answering all questions, your final score will be displayed.

## Customization

You can easily customize the quiz by editing the `quiz_questions.txt` file. Add, remove, or modify questions following the format shown above. The app will automatically adapt to the number of questions in the file.

## How it Works

1. The `parse_questions()` function reads the text file and converts it to a structured format.
2. The `run_quiz()` function presents questions to the user and tracks the score.
3. The script optionally saves the structured data as a JSON file for inspection or future use.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
