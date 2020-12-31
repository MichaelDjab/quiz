from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Create an empty list of question objects
questions = []

# Convert question dictionaries from the given data to question objects and add them to the list
for question in question_data:
    questions.append(Question(question["text"], question["answer"]))

my_quiz = QuizBrain(questions)

my_quiz.next_question()