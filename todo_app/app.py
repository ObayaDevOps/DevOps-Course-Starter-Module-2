from todo_app.view_model import ViewModel
from flask import Flask, render_template, redirect, url_for, request
from todo_app.flask_config import Config
from dotenv import load_dotenv

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():   
    item_view_model = {
        'todo' : ViewModel.show_todo_items(),
        'doing' : ViewModel.show_doing_items(),
        'done' : ViewModel.show_done_items()
    }

    return render_template('index.html', view_model = item_view_model)

@app.route('/items/new', methods=['POST'])
def add_item():
    title = request.form['title']
    ViewModel.add_item(title)

    return redirect(url_for('index'))


@app.route('/items/<id>/complete')
def complete_item(id):
    ViewModel.complete_item(id)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
