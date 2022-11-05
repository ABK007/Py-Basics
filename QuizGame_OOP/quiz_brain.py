class QuizBrain:
    
    # Defining a constructor
    def __init__(self, question_list):
        """ Defining the constructors
        """
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        
    # Defining a method 
    def next_question (self):
        """ displays next question, checks user answer and gives user a score"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.question} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
     
     # Defining a method    
    def still_has_question (self):
        """ Checks if the questions are finished in the question list"""
        return self.question_number < len(self.question_list)
    
    # Defining a method 
    def check_answer(self, user_answer, correct_answer):
        """ Checks the answer of the user and gives a score"""
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("you got it wrong!")
            
        print(f"The correct answer was: {correct_answer}")
        print(f" Your current score is {self.score}/{self.question_number}.")
        print("\n")    
        
        
    
    