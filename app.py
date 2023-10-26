from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(150), unique=True, nullable=False)
    ans = db.Column(db.String(250), default='')

    def __repr__(self):
        return f"{self.question} - {self.ans}"

@app.route('/ques', methods=['POST'])
def add_ques():
    data = request.get_json()
    ques = Card(question=data.get('ques'))
    db.session.add(ques)
    db.session.commit()
    return jsonify({'id': ques.id})

@app.route('/ques', methods=['GET'])
def read_ques():
    ques = Card.query.all()
    output = []
    for q in ques:
        ques_info = {'id': q.id, "ques": q.question, "ans": q.ans}
        output.append(ques_info)
    return jsonify({"ques": output})

@app.route('/ques/<int:id>', methods=['PUT'])
def update_ques(id):
    ques = Card.query.get_or_404(id)
    data = request.get_json()
    if 'ques' in data:
        ques.question = data['ques']
    if 'ans' in data:
        ques.ans = data['ans']
    db.session.commit()
    return jsonify({"message": "Question updated", "id": ques.id, "ques": ques.question, "ans": ques.ans})

@app.route('/ques/<int:id>', methods=['DELETE'])
def delete_ques(id):
    ques = Card.query.get_or_404(id)
    db.session.delete(ques)
    db.session.commit()
    return jsonify({"message": "Question deleted"})

if __name__ == "__main":
    app.run(debug=True)
