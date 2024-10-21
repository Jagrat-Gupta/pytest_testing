import requests
import unittest 
from unittest.mock import Mock, patch



def get_user_data(user_id):
    response = requests.get(f"http://userdata/myuser/{user_id}")
    return response.json()


class TestUserData(unittest.TestCase):
    
    @patch('requests.get')
    def test_get_user_data(self, mock_get):
        mock_response = Mock()
        response_dict = {'name': 'jagrat', 'email':"jagrat@example.com"}
        mock_response.json.return_value = response_dict

        mock_get.return_value = mock_response
        

        user_data = get_user_data(1)
        mock_get.assert_called_with("http://userdata/myuser/1")
        self.assertEqual(user_data, response_dict)


if __name__ == '__main__':
    unittest.main()

    







