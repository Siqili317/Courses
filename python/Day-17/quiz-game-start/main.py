from question_model import Question
from data import question_data
from quiz_brain import QuizBrian

question_bank = []
for items in question_data:
    question_bank.append(Question(items['text'], items['answer']))


quiz = QuizBrian(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!!!!!")
print(f"You final score was: {quiz.score}/{len(question_bank)}")