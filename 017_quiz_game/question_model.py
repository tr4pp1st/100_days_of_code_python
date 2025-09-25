class Question:
    """
    Represents a single quiz question.

    Attributes:
        text (str): The question text.
        answer (str): The correct answer ("True" or "False").
    """
    def __init__(self, text: str, answer: str):
        self.text: str = text
        self.answer: str = answer
