from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Logic to capture the user’s answers and redirect to the result page
        return redirect(url_for('result'))
    else:
        return render_template('quiz.html')  # Displays the question and options

@app.route('/result')
def result():
    # Calculate and display the user's score
    score = 1  # Example score for demonstration
    return render_template('result.html', score=score)



if __name__ == '__main__':
    app.run(debug=True)