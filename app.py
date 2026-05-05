from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    "You’re at a social gathering. What are you doing?",
    "What draws you most in a story?",
    "Your ideal writing style is:",
    "What inspires you most?",
    "How do you approach conflict?"
]

options = [
    ['a', 'b', 'c', 'd'],
    ['a', 'b', 'c', 'd'],
    ['a', 'b', 'c', 'd'],
    ['a', 'b', 'c', 'd'],
    ['a', 'b', 'c', 'd']
]

user_figure = ['Hamlet', 'Helena', 'Juliet', 'Petruchio']
user_figure_mbti = ['INFJ', 'INFP', 'ENFP', 'ENTP']

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/result', methods=['POST'])
def result():
    guesses = []

    for i in range(len(questions)):
        answer = request.form.get(f'answer{i}')
        guesses.append(answer)

    count_a = guesses.count('a')
    count_b = guesses.count('b')
    count_c = guesses.count('c')
    count_d = guesses.count('d')

    total = len(guesses)

    percentages = [
        int(count_a / total * 100),
        int(count_b / total * 100),
        int(count_c / total * 100),
        int(count_d / total * 100)
    ]

    max_index = percentages.index(max(percentages))

    return render_template(
        'result.html',
        percentages=percentages,
        figures=user_figure,
        mbti=user_figure_mbti,
        winner=user_figure[max_index],
        winner_mbti=user_figure_mbti[max_index]
    )

if __name__ == '__main__':
    app.run(debug=True)