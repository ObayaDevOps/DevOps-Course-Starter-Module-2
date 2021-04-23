# from flask.globals import request
# import pytest
# from requests.models import Response
# from todo_app import app
# from dotenv import find_dotenv, load_dotenv
# from unittest.mock import patch, Mock

# @pytest.fixture
# def client():
#     file_path = find_dotenv('.env.test')
#     load_dotenv(file_path, override=True)

#     test_app = app.create_app()
#     with test_app.test_client() as client:
#         yield client 

# @patch('requests.get')
# def test_index_page(mock_get_requests, client):
#     mock_get_requests.side_effect = mock_get_lists
# #  get html: response.data.decode() - string returned - make assertions
#     response = client.get('/')


# def mock_get_lists(url):
# #  Put some real data in Mock and assert - l21

#     response = Mock() 
#     response.json.return_value = []

#     return response