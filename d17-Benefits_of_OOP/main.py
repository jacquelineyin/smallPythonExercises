from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []


def populate_question_bank(question_bank):
    for rawQuestion in question_data:
        text, answer = rawQuestion["text"], rawQuestion["answer"]
        question = Question(text, answer)
        question_bank.append(question)


populate_question_bank(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}.")
