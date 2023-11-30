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
    # TODO: part_of_speeches can be prompts
    part_of_speeches = silly_story.prompts

    # TODO: can just return here
    html = render_template("questions.html", prompts = part_of_speeches) # TODO: can be prompts = prompts

    print("html is: ", html)

    return html

@app.get("/results")
def get_madlibs():
    """Gets form results and return story madlib"""

    prompts = silly_story.prompts
    answers = {prompt:request.args[f"{prompt}"] for prompt in prompts}
    print(request.args)

    print('This is prompts', prompts)

    # TODO: can just pass in request.args here
    text = silly_story.get_result_text(request.args)
    # text = silly_story.get_result_text(answers)

    # TODO: rename to just text or story_text, not a template anymore
    return render_template("results.html", template=text)



# old comments for reference:
# imports example story (ex: silly story instance)

# Create a form where the inputs the user will make are on the prompts
# taken from the silly story insance (ex:"noun")