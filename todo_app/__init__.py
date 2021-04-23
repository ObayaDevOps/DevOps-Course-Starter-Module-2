# Set env variables here 
import requests
import os
from dotenv import load_dotenv

host = 'https://api.trello.com'
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_TOKEN')

# boards = requests.get( host + '/1/members/me/boards?key=' + api_key + '&token=' + api_secret).json()
# board_id = boards[0]['id']

# board_lists = requests.get( host + '/1/boards/' + board_id + '/lists?key=' + api_key + '&token=' + api_secret).json()
# todo_board_list_id = board_lists[0]['id']
# doing_board_list_id = board_lists[1]['id']
# done_board_list_id = board_lists[2]['id']


# os.environ['HOST'] = host
# os.environ['BOARD_ID'] = '5fbd67b4d720701b139bc046'

# os.environ['TODO_LIST_ID'] = '5fbd67b4d720701b139bc047'
# os.environ['DOING_LIST_ID'] = '5fbd67b4d720701b139bc048'
# os.environ['DONE_LIST_ID'] = '6082e1ad687cbd1af5894322'



