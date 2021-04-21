from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

app.config['SECRET_KEY'] = 'juny0192'
debug = DebugToolbarExtension(app)

@app.route('/')
def show_form():
    prompts = story.prompts
    title = story.title
    return render_template('main.html', title = title, prompts = prompts)

@app.route('/story')
def show_story():
    title = story.title
    text = story.generate(request.args)
    return render_template('story.html', title = title, text = text)



