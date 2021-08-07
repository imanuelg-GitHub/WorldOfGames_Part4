from flask import Flask
from flask import render_template
from Utilities import SCORES_FILE_NAME, BAD_RETURN_CODE

# creates a Flask application, named app
app = Flask(__name__)


# a route where we will display the message via an HTML template
@app.route("/")
def score_server():
    try:
        f = open(SCORES_FILE_NAME, "r")
        SCORE = f.read()
        return render_template('show_score.html', SCORE=SCORE)
        f.close()
    except IOError:
        ERROR = "Error occurred " + SCORES_FILE_NAME + " not found. Return code: " + str(BAD_RETURN_CODE)
        return render_template('show_error.html', ERROR=ERROR)


# run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6001)

