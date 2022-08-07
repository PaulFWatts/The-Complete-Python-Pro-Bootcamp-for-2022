from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

print("\033[2J\033[1;1H")  # clear screen

# Create a QuizBrain object with the question_data list
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)  # initialise the QuizBrain class

while quiz.still_has_questions():  # while there are still questions left to ask
    quiz.next_question()  # ask the next question

print("You've finished the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
