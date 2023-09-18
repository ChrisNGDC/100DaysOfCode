from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import random


question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))
random.shuffle(question_bank)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.ask_next_question()
    print('-'*50)
print("You completed the quiz!")
print(f'Your final score is: {quiz_brain.score}/{quiz_brain.current_question}')
