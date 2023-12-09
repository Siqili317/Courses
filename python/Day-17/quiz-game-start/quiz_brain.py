class QuizBrian:
    def __init__(self, list) -> None:
        self.question_number =0
        self.question_list = list
        self.score = 0
    
    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list) 
         
    def next_question(self) -> str:
        # get nth object
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?: ")
        return self.check_answer(ans, current_question.answer)
    
    def check_answer(self, actual, expectation):
        if actual.lower() == expectation.lower():
            print("RIGHT")
            self.score +=1
        else:
            print("WRONG")
        print(f"The correct answer was: {expectation}. ")
        print(f"Your current score is:{self.score}/{self.question_number}")
        print("\n")

