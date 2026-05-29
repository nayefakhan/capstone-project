from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'astrotest-secret'

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
        "text": "What is the planet besides Earth we visit the most?",
        "answers": ["Mars", "Venus", "the Sun", "Neptune"],
        "correct": "Mars"
    },
    5: {
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
    if num == 1:
        session['score'] = 0
    q = questions.get(num)
    return render_template('question.html', num=num, question=q, result=None)

@app.route('/answer')
def answer():
    num = request.args.get('num', type=int)
    chosen = request.args.get('answer')
    q = questions.get(num)
    correct = chosen == q['correct']
    if correct:
        session['score'] = session.get('score', 0) + 1
    result = 'Correct!' if correct else f'Incorrect. The correct answer is {q["correct"]}.'
    next_num = num + 1 if questions.get(num + 1) else None
    return render_template('question.html', num=num, question=q, result=result, next_num=next_num)

@app.route('/results')
def results():
    score = session.get('score', 0)
    total = len(questions)
    percentage = round((score / total) * 100)
    return render_template('results.html', score=score, total=total, percentage=percentage)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
