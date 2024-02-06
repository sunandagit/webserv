# test_app.py
import unittest
from service import app
from flask import jsonify

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def requestEndpoint(self, endpoint, expected_code, expected_data, isSuccess):
        response = self.app.get(endpoint)
        self.assertEqual(response.status_code, expected_code)
        if isSuccess:
            self.assertEqual(response.json, expected_data)
        else:
            self.assertNotEqual(response.json, expected_data)
    
    
    def test_v1_success(self):
        self.requestEndpoint('/reply/teststring', 200, {"message":"teststring"}, True)
        
    def test_v2_success_1(self):
        self.requestEndpoint('/v2/reply/11-teststringforv2', 200, {"message":"teststringforv2"}, True)
    
    def test_v2_success_2(self):
        self.requestEndpoint('/v2/reply/12-teststringforv2', 200, {"message":"a0d09c100eb91767e3f873f5e94c617c"}, True)
    
    def test_v2_success_3(self):
        self.requestEndpoint('/v2/reply/21-teststringforv2', 200, {"message":"88f9599885cb57f3098711e70dd70816"}, True)
    
    def test_v2_success_4(self):
        self.requestEndpoint('/v2/reply/22-teststringforv2', 200, {"message":"33468bbab0c9d2667d8137220d6663d5"}, True)

    def test_v2_invalid_input_failure_1(self):
        self.requestEndpoint('/v2/reply/222-teststringforv2', 400, {"message":"Invalid input"}, True)
    def test_v2_invalid_input_failure_2(self):
        with self.assertRaises(AssertionError):
            self.requestEndpoint('/v2/reply/-teststringforv2', 400, {"message":"Invalid input"}, True)
    def test_v2_invalid_input_failure_3(self):
        self.requestEndpoint('/v2/reply/45-teststringforv2', 400, {"message":"Invalid input"}, True)
if __name__ == '__main__':
    unittest.main()