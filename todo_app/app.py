from flask import Flask, render_template, redirect, url_for, request

from todo_app.flask_config import Config
from todo_app.data import session_items as session

import requests
import os
from dotenv import load_dotenv
import json

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    # Get stuff from env - should be global
    load_dotenv()
    host = 'https://api.trello.com'
    api_key = os.getenv('API_KEY')
    api_secret = os.getenv('API_TOKEN')
        
    boards = requests.get( host + '/1/members/me/boards?key=' + api_key + '&token=' + api_secret).json()
    board_id = boards[0]['id']

    board_lists = requests.get( host + '/1/boards/' + board_id + '/lists?key=' + api_key + '&token=' + api_secret).json()
    todo_board_list_id = board_lists[0]['id']

    # Now we have the board id, we can get the cards
    cards = requests.get( host + '/1/lists/' + todo_board_list_id + '/cards?key=' + api_key + '&token=' + api_secret).json()

    display_cards = []
    id_counter = 0
    for card in cards:
        name = card['name']
        print(name)
        new_card = {
            'id': id_counter,
            'status': 'Not Started',
            'title': name
        }
        display_cards.append(new_card)
        id_counter += 1


    items = session.get_items()
    return render_template('index.html', items = display_cards)


@app.route('/items/new', methods=['POST'])
def add_item():
    title = request.form['title']
    session.add_item(title)
    return redirect(url_for('index'))


@app.route('/items/<id>/complete')
def complete_item(id):
    session.complete_item(id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
