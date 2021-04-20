from board_item import Board_item
from flask import Flask, render_template, redirect, url_for, request

from todo_app.flask_config import Config
from todo_app.data import session_items as session

import requests
import os
from dotenv import load_dotenv
import json

app = Flask(__name__)
app.config.from_object(Config)

load_dotenv()
host =  os.getenv('HOST')
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_TOKEN')
board_id = os.getenv('BOARD_ID')
todo_board_list_id = os.getenv('TODO_LIST_ID')
done_list_id = os.getenv('DONE_LIST_ID')


@app.route('/')
def index():        
    cards = requests.get( host + '/1/lists/' + todo_board_list_id + '/cards?key=' + api_key + '&token=' + api_secret).json()

    display_cards = []
    id_counter = 0
    for card in cards:
        name = card['name']
        id = card['id']
        status = card['dueComplete']
        if status != True:
            status = "NotStarted"
        else:
            status = "Completed"

        new_card = Board_item(id, status, name)
        display_cards.append(new_card)
        id_counter += 1

    return render_template('index.html', items = display_cards)

@app.route('/items/new', methods=['POST'])
def add_item():
    response = requests.post( host + '/1/cards?key=' + api_key + '&token=' + api_secret + '&idList=' + todo_board_list_id ).json()
    new_card_id = response['id']

    title = request.form['title']
    requests.put(host + '/1/cards/' + new_card_id + '?key=' + api_key + '&token=' + api_secret + '&name=' + title )     

    return redirect(url_for('index'))


@app.route('/items/<id>/complete')
def complete_item(id):
    requests.put(host + '/1/cards/' + id + '?key=' + api_key + '&token=' + api_secret + '&dueComplete=true' )     
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
