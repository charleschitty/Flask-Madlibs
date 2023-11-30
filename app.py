from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def index():
    """Return homepage"""

    # Creates list ['noun', 'verb']
    prompts = silly_story.prompts

    return render_template("questions.html", prompts = prompts)

@app.get("/results")
def get_madlibs():
    """Gets form results and return story madlib"""

    text = silly_story.get_result_text(request.args)

    return render_template("results.html", story_text=text)



# old comments for reference:
# imports example story (ex: silly story instance)

# Create a form where the inputs the user will make are on the prompts
# taken from the silly story insance (ex:"noun")