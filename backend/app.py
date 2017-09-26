# Flask API to serve JavaScript with Python
from flask import Flask, request, jsonify
from interact import getquestion, collectfeedback
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        question, id_q = getquestion()
        return jsonify({
            'question': question, 'id_q': id_q, "method": "GET", "message": "Get the next question."})

    elif request.method == 'POST':
        id_q = int(request.json.get('id_q'))
        new_grade = request.json.get('new_grade')
        new_notes = request.json.get('new_notes')
        collectfeedback(id_q, new_grade, new_notes)
        return jsonify({'id_q': id_q, "method": "POST", "message": "Data has been stored."})
    else:
        return jsonify({"method": "UNKNOWN", "message": "Wrong endpoint has been requested."})

if __name__ == '__main__':
    app.run()
    # print 'Done'
