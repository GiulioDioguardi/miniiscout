import json
import os

from flask import Flask, render_template, abort

app = Flask(__name__)
ROOT = os.path.dirname(os.path.abspath(__file__))

def read_json_file(filename):
    with open(filename) as _file:
        return json.load(_file)

@app.context_processor
def inject_debug():
    return dict(debug=app.debug)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map/<questionnumber>')
def map_page(questionnumber):
    try:
        question = read_json_file(os.path.join(ROOT, "questions.json"))[int(questionnumber) - 1]
    except (IndexError, ValueError):
        abort(404)
    return render_template('map.html', question=question, number=questionnumber)

if __name__ == "__main__":
    app.run(debug=True)
