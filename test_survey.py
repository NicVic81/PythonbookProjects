import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Test for the class AnonymousSurvey"""

    def setUp(self):
        """Create a survey and a set of responses to for all test in this test class"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.test_responses = ['english', 'spanish', 'german']

    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        self.my_survey.record_answer(self.test_responses[0])
        self.assertIn(self.test_responses[0], self.my_survey.responses)

    def test_three_responses(self):
        """Test to make sure more than one response can be stored"""
        for response in self.test_responses:
            self.my_survey.record_answer(response)

        for response in self.test_responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()
