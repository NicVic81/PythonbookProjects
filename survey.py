class AnonymousSurvey:
    """A class for storing questions and getting anonymous answers"""

    def __init__(self, question):
        """Since this class just takes in one variable it only needs this initializion statement
        and here is takes in the question and stores it"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question"""
        print(self.question)

    def record_answer(self, new_response):
        """Store a single response"""
        self.responses.append(new_response)

    def show_results(self):
        """Show the list of responses"""
        print("Here are your results: ")
        for response in self.responses:
            print(response.title())

