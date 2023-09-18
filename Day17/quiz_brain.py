class QuizBrain:

    def __init__(self, questions):
        self.questions = questions
        self.current_question = 0
        self.score = 0

    def still_has_questions(self):
        return self.current_question != len(self.questions)

    def ask_next_question(self):
        question_to_ask = self.questions[self.current_question]
        self.current_question += 1
        while True:
            user_answer = input(f'Q.{self.current_question}: {question_to_ask.text} ("True" or "False")?: ').lower()
            if user_answer in ["true", "false"]:
                break
            print('Answer only with "True" or "False".')
        self.check_answer(question_to_ask, user_answer)

    def check_answer(self, question, user_answer):
        if question.is_correct(user_answer):
            self.score += 1
            print("You got it right.")
        else:
            print(f"That's wrong.")
        print(f'The correct answer was: {question.answer.capitalize()}')
        print(f'Current Score: {self.score}/{self.current_question}')


