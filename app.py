from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def index():
    """Return homepage"""

    #Creates list ['noun', 'verb']
    part_of_speeches= silly_story.prompts


    html = render_template("questions.html", prompts = part_of_speeches)
    print("html is: ", html)

    return html

#imports example story (ex: silly story instance)

#Create a form where the inputs the user will make are on the prompts
#taken from the silly story insance (ex:"noun")