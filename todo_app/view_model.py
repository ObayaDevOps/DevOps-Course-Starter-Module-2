#  This should contain all the information that the HTML needs in a single class
from todo_app.board_item import Board_item
import requests
import os
from dotenv import load_dotenv

load_dotenv()
host =  os.getenv('HOST')
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_TOKEN')
board_id = os.getenv('BOARD_ID')
todo_list_id = os.getenv('TODO_LIST_ID')
doing_list_id = os.getenv('DOING_LIST_ID')
done_list_id = os.getenv('DONE_LIST_ID')

def json_response_to_view_model(cards, listType):
    display_cards = []
    for card in cards:
        name = card['name']
        id = card['id']
        status = listType 

        new_card = Board_item(id, status, name)
        display_cards.append(new_card)

    return ViewModel(display_cards)

class ViewModel:
    def __init__(self, items):
        self._items = items
 
    @property
    def items(self):
        return self._items

    def show_todo_items():
        todo_cards = requests.get( host + '/1/lists/' + todo_list_id + '/cards?key=' + api_key + '&token=' + api_secret).json()
        return json_response_to_view_model(todo_cards, 'To Do')

    def show_doing_items():
        doing_cards = requests.get( host + '/1/lists/' + doing_list_id + '/cards?key=' + api_key + '&token=' + api_secret).json()
        return json_response_to_view_model(doing_cards, 'Doing')

    def show_done_items():
        done_cards = requests.get( host + '/1/lists/' + done_list_id + '/cards?key=' + api_key + '&token=' + api_secret).json()
        return json_response_to_view_model(done_cards, 'Completed')

    def add_item(title):
        response = requests.post( host + '/1/cards?key=' + api_key + '&token=' + api_secret + '&idList=' + todo_list_id ).json()
        new_card_id = response['id']
        print(new_card_id)

        requests.put(host + '/1/cards/' + new_card_id + '?key=' + api_key + '&token=' + api_secret + '&name=' + title )     

    def complete_item(id):
        requests.put(host + '/1/cards/' + id + '?key=' + api_key + '&token=' + api_secret + '&idList=' )     


