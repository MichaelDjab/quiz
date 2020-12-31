class QuizBrain:

    def __init__(self, question_list):
        self.question_num = 0
        self.question_list = question_list

    def next_question(self):
        question = self.question_list[self.question_num].text
        answer = self.question_list[self.question_num].answer
        num = self.question_num+1

        user_reply = input(f"Q.{num}: {question} (True/False): ")

        print("You got it right!") if user_reply == answer else print("That's wrong.")
        print(f"The correct answer was: {answer}.")








