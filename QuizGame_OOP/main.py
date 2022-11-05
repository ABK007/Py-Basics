from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = [] 

# Adding the questions in the question_banl list
for question in question_data:
    question_text  = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
# initializing the quiz brain object
quiz = QuizBrain(question_bank) # Initializing the quizbrain object
quiz.next_question() # Calls a quizBrain class method

while quiz.still_has_question(): # Calls a quizBrain class method
    quiz.next_question() # Calls a quizBrain class method
    
    

print("you have completed the quiz.")
print(f"your final score is {quiz.score}/{len(quiz.question_list)}")
        
        
