from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Liste des questions et réponses (à remplacer par une base de données)
questions = [
    {"question": "Quelle est la capitale de la France ?", "reponses": ["Paris", "Londres", "Berlin"], "reponse_correcte": "Paris"},
    {"question": "Combien de continents y a-t-il sur Terre ?", "reponses": ["5", "6", "7"], "reponse_correcte": "7"},
    # Ajouter d'autres questions...
]

# Route pour afficher la page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Route pour récupérer une question
@app.route('/get_question', methods=['GET'])
def get_question():
    # Obtenir une question aléatoire
    import random
    question = random.choice(questions)
    return jsonify(question)

# Route pour soumettre une réponse et vérifier si elle est correcte
@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    data = request.json
    question_id = data.get('question_id')
    user_answer = data.get('user_answer')

    # Vérifier si la réponse est correcte
    question = questions[question_id]
    correct_answer = question['reponse_correcte']
    if user_answer == correct_answer:
        response = {'correct': True}
    else:
        response = {'correct': False}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
