from question_model import Question
from quiz_brain import  QuizBrain
from data import question_data
question_bank = []
for questions in question_data:
    question_text=questions['text']
    question_answer=questions['answer']
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)
print(question_bank)

quiz=QuizBrain(question_bank)
while quiz.still_has_questions:
    quiz.next_question()
print("you have completed the Quiz.")
print(f'Your Final Score is : {quiz.score}')
