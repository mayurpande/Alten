import unittest
import requests
import json


class TestRestApi(unittest.TestCase):

    """Test case to handle asserting response code is 200 and printing to console"""

    def setUp(self):

        # GET request to the API server and store response
        self.response = requests.get('https://api.covid19api.com/total/country/germany')

    def test_response_status_code_is_equal_200(self):

        # Assert response status code is 200
        self.assertEqual(self.response.status_code, 200)

    def test_response_status_code_not_equal_303(self):

        # Assert response status code fails if 303
        self.assertNotEqual(self.response.status_code, 303)

    def test_response_status_code_not_equal_404(self):

        # Assert response status code fails if 404
        self.assertNotEqual(self.response.status_code, 404)

    def test_prints_data_to_console(self):

        # Convert response.text to json, print results to console
        json_data = json.loads(self.response.text)
        for data in json_data:
            print("Fecha: " + data['Date'] + ", Num. Casos Activos: " + str(data['Active']))


if __name__ == '__main__':
    unittest.main()
