class QuizBrain:

    def __init__(self, question_list):
        self.question_num = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        question = self.question_list[self.question_num].text
        answer = self.question_list[self.question_num].answer
        self.question_num += 1
        user_reply = input(f"Q.{self.question_num}: {question} (True/False): ")

        if user_reply == answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {answer}.")
        print(f"Your current score is: {self.score}/{self.question_num}\n")

    def play_quiz(self):
        while self.question_num < len(self.question_list):
            self.next_question()

        print(f"\nYou've completed the quiz\nYour final score was: {self.score}/{self.question_num}")




