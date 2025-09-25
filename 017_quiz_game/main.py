# 100 Days of Code: Python
# Day 17 Project: Quiz Game

import html

from data import QUESTION_DATA, QUESTION_DATA_FROM_OPEN_TRIVIA_DB
from question_model import Question
from quiz_brain import QuizBrain

# --- Build question bank ---
question_bank = []

# Option 1: Local hardcoded questions
# for question in QUESTION_DATA:
#     question_text = question["text"]
#     question_answer = question["answer"]
#     question_bank.append(Question(question_text, question_answer))

# Option 2: Questions from Open Trivia DB
for question in QUESTION_DATA_FROM_OPEN_TRIVIA_DB:
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

# --- Quiz Game Loop ---
while quiz_brain.still_has_questions():
    quiz_brain.next_question()

# --- Game finished ---
quiz_brain.show_final_score()
