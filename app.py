from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Card model
class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(150), unique=True, nullable=False)
    ans = db.Column(db.String(250), default='')

    def __repr__(self):
        return f"{self.question} - {self.ans}"

# Route to add a new flashcard
@app.route('/ques', methods=['POST'])
def add_ques():
    data = request.json
    question = data.get('ques')
    answer = data.get('ans')
    card = Card(question=question, ans=answer)
    db.session.add(card)
    db.session.commit()
    return {'id': card.id}

# Route to read all flashcards with questions and answers
@app.route('/ques', methods=['GET'])
def read_ques():
    cards = Card.query.all()
    output = []
    for card in cards:
        card_info = {
            'id': card.id,
            'ques': card.question,
            'ans': card.ans
        }
        output.append(card_info)
    return {'flashcards': output}

# Route to update a flashcard (question and answer)
@app.route('/ques/<int:id>', methods=['PUT'])
def update_ques(id):
    card = Card.query.get_or_404(id)
    data = request.json
    if 'ques' in data:
        card.question = data['ques']
    if 'ans' in data:
        card.ans = data['ans']
    db.session.commit()
    return {
        "message": "Flashcard updated",
        "id": card.id,
        "ques": card.question,
        "ans": card.ans
    }

# Route to delete a flashcard
@app.route('/ques/<int:id>', methods=['DELETE'])
def delete_ques(id):
    card = Card.query.get_or_404(id)
    db.session.delete(card)
    db.session.commit()
    return {"message": "Flashcard deleted"}

if __name__ == "__main":
    app.run(debug=True)