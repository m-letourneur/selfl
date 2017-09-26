# Flask API serving JavaScript with Python
from flask import Flask, request, jsonify, render_template, url_for
from interact import getquestion, collectfeedback
app = Flask(__name__)



@app.route('/req', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        question, id_q = getquestion()
        return jsonify({
            'question': question, 'id_q': id_q, "method": "GET", "message": "Get the next question."})

    elif request.method == 'POST':
        # print request
        # print request is None
        # print request.args
        print request.json
        print "wtf"
        id_q = int(request.json.get('id_q'))
        print id_q
        new_grade = request.json.get('new_grade')
        print new_grade
        new_notes = request.json.get('new_notes')
        print new_notes
        collectfeedback(id_q, new_grade, new_notes)
        return jsonify({'id_q': id_q, "method": "POST", "message": "Data has been stored.", 'new_notes': new_notes, 'new_grade': new_grade})
    else:
        return jsonify({"method": "UNKNOWN", "message": "Wrong endpoint has been requested."})

@app.route('/')
def root():
    return render_template('front.html')



if __name__ == '__main__':
    app.run()
    url_for('static', filename='css/style.css')
    url_for('static', filename='main.js')
