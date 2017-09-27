# Static page
http://127.0.0.1:5000/

# Request next question
curl -X GET http://127.0.0.1:5000/req

# Request a hint
curl -X GET http://127.0.0.1:5000/hint/<int:id_q>

# Store the notes and the grade based on self-assessment
curl -X POST -H 'Content-Type: application/json' -d '{"id_q":"0", "new_grade":"6", "new_notes":"ahaha"}' localhost:5000/req
