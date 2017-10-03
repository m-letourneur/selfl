#SELFL

Lean webpage for a learning framework.

Selection of questions in pool, self-assessment of the user's level to answer the questions. Questions are selected based on previous self-assessed grades so that the user faces its weaknesses more often and work on them until he or she reaches a better grade on these questions.

Status: v1 is live.
 
> basic JavaScript + basic HTML/CSS + Flask API to run Python

## Run the local server

Ensure you run the Flask API in your virtual environment.

In Terminal:
> mkvirtualenv selfl

> pip install -r requirements.txt

Move to the repo directory

> cd selfl

Launch the API server
>  python backend/app.py runserver


## Open the page

In your browser:

> http://localhost:5000/


## Chrome extension
In Chrome Browser:

- Go to "chrome://extensions/"

- Click "Load unpacked extension..."

- Select the folder "selfl/backend/templates"



 