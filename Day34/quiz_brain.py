from question_model import Question


class QuizBrain:

    def __init__(self, questions: [Question]):
        self.questions = questions
        self.current_question = 0
        self.score = 0

    def still_has_questions(self) -> bool:
        return self.current_question != len(self.questions)

    def check_answer(self, user_answer: str):
        if self.questions[self.current_question - 1].answer == user_answer:
            self.score += 1
            return True
        return False

    def next_question(self) -> Question:
        question_to_ask = self.questions[self.current_question]
        self.current_question += 1
        return question_to_ask
