# Name: Jordyn Pendergrass 
# Date: 4-16-2026
# Quiz game website app

from flask import Flask, render_template, request, redirect, url_for, make_response
import random
import json

app = Flask(__name__)

# Load questions from JSON file
def load_questions():
    with open('questions.json', 'r') as f:
        questions = json.load(f)
    random.shuffle(questions)
    for q in questions:
        random.shuffle(q['options'])
    return questions

# Load leaderborad scores from JSON file
def load_leaderboard():
    try:
        with open('scores.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
# Save leaderboard scores to JSON file
def save_scores(name, score, total):
    scores = load_leaderboard()
    scores.append({'name': name, 'score': score, 'total': total})
    scores.sort(key=lambda x: x['score'], reverse=True)
    with open('scores.json', 'w') as f:
        json.dump(scores, f)

@app.route('/')
# Check if user has used browser before
# Return none if they have not
# STore users score history as JSON in cookie

def index():
    username = request.cookies.get('username')
    score_history = request.cookies.get('score_history')
    if score_history:
        score_history = json.loads(score_history)
    else:
        score_history = []
    return render_template('index.html', username=username, score_history=score_history)


@app.route('/start', methods=['POST'])
# Save user cookies and start quiz
def start():
    name = request.form.get('username', "").strip()
    if not name:
        return render_template('index.html', error="Please enter your name!")
    response = redirect(url_for('quiz'))
    response.set_cookie('username', name)

    return response

@app.route('/quiz')
# Load and display quiz page
def quiz():
    questions = load_questions()
    response = make_response(                                  # make_response() wraps the string
        render_template('quiz.html', questions=questions,
                        username=request.cookies.get('username'))
    )
    response.set_cookie('questions', json.dumps(questions))   # now this works
    return response

@app.route('/submit', methods=['POST'])
# Grde quiz and save score to leaderboard
def submit():
    questions_raw = request.cookies.get('questions')
    if not questions_raw:
        return redirect(url_for('quiz'))
    questions = json.loads(questions_raw)
    score = 0
    for i, q in enumerate(questions):
        user_answer = request.form.get(f'q{i}')
        if user_answer == q['correct']:
            score += 1
    
    total = len(questions)

    # Add new score to leaderboard and cookie history
    score_history = request.cookies.get('score_history')
    history = json.loads(score_history) if score_history else []
    history.append({'score': score, 'total': total, 'percentage': round(score / total * 100, 1)})

    save_scores(request.cookies.get('username', 'Anonymous'), score, total)
    response = make_response(
        render_template('result.html', score=score, total=total,
                        percentage=round(score / total * 100, 1))
    )
    response.set_cookie('score_history', json.dumps(history))
    return response

@app.route('/results')
# Show final score and leaderboard
def results():
    score = request.args.get('score', 0, type=int)
    total = request.args.get('total', 5, type=int)
    leaderboard = load_leaderboard()[:10]
    return render_template('result.html', score=score, total=total, leaderboard=leaderboard, username=request.cookies.get('username'))

@app.route('/api/questions')
# API endpoint to get questions as JSON
def api_questions():
    return json.dumps(load_questions())

@app.route('/api/leaderboard')
# API endpoint to get leaderboard scores as JSON
def api_leaderboard():
    return json.dumps(load_leaderboard())


# Run the app
if __name__ == '__main__':
    app.run(debug=True)