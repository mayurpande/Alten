import unittest
import requests


class TestRestApi(unittest.TestCase):

    def setUp(self):

        # GET request to the API server and store response
        self.response = requests.get('https://api.covid19api.com/total/country/germany')

    def test_response_status_code_is_200(self):

        # Assert response status code is 200
        self.assertEqual(self.response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
