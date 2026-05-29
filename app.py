from flask import Flask, render_template, request

app = Flask(__name__)

questions = {
    1: {
        "text": "Which is the largest planet in the Solar System?",
        "answers": ["Saturn", "Neptune", "Earth", "Jupiter"],
        "correct": "Jupiter"
    },
    2: {
        "text": "How many moons does Mars have?",
        "answers": ["0", "4", "2", "1"],
        "correct": "2"
    },
    3: {
        "text": "What is the closest planet to the Sun?",
        "answers": ["Mercury", "Venus", "Earth", "Mars"],
        "correct": "Mercury"
    },
    4: {
        "text": "How many planets are in the Solar System?",
        "answers": ["9", "8", "3", "6"],
        "correct": "8"
    }
}

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/question/<int:num>')
def question(num):
    q = questions.get(num)
    return render_template('question.html', num=num, question=q, result=None)

@app.route('/answer')
def answer():
    num = request.args.get('num', type=int)
    chosen = request.args.get('answer')
    q = questions.get(num)
    result = 'Correct!' if chosen == q['correct'] else f'Incorrect. The correct answer is {q["correct"]}.'
    next_num = num + 1 if questions.get(num + 1) else None
    return render_template('question.html', num=num, question=q, result=result, next_num=next_num)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
