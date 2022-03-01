import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

def read_json_file(filename):
    with open(filename, "rb") as _file:
        return json.load(_file)

def get_questions():
    questions = read_json_file(os.path.join(ROOT, "questions.json"))
    n_questions = []
    for question in questions:
        question["encoded_title"] = question["title"].encode('utf-8')
        n_questions.append(question)
    return n_questions
