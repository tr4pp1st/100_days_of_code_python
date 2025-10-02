class QuizBrain:
    """
    Handles the logic of the quiz game.

    Attributes:
        question_list (list[Question]): List of Question objects.
        question_number (int): Tracks the current question index.
        score (int): Tracks the user's current score.
    """

    def __init__(self, question_list: list) -> None:
        self.question_list: list = question_list
        self.question_number: int = 0
        self.score: int = 0

    def still_has_questions(self) -> bool:
        """
        Checks if there are more questions left in the quiz.

        Returns:
            bool: True if there are remaining questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer: str, correct_answer: str) -> None:
        """
       Checks the user's answer against the correct answer and updates the score.

       Args:
           user_answer (str): The answer provided by the user.
           correct_answer (str): The correct answer for the question.
       """
        if user_answer.strip().lower() == correct_answer.strip().lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

    def next_question(self) -> None:
        """
        Presents the next question to the user, prompts for input, and checks the answer.
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def show_final_score(self) -> None:
        """
        Prints the final score after the quiz is completed.
        """
        print("Quiz Completed!")
        print(f"Your final score: {self.score}/{self.question_number}")
