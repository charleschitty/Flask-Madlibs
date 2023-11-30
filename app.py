from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def index():
    """Return homepage"""

    # stories = [
    #     stories.silly_story, stories.excited_story, stories.horror_story
    # ]

    # return render_template("base.html", stories = stories)

    # Creates list ['noun', 'verb']
    prompts = stories.silly_story.prompts

    return render_template("questions.html", prompts = prompts)

@app.get("/results")
def get_madlibs():
    """Gets form results and return story madlib"""

    text = stories.silly_story.get_result_text(request.args)

    return render_template("results.html", story_text=text)


@app.get("/template")
def get_templates():
    """Shows story templates to pick from"""

    story_templates = [
        stories.silly_story, stories.excited_story, stories.horror_story
        ]

    return render_template("storytemplates.html", stories = story_templates)
