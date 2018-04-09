from survey import AnonymousSurvey

# Define a question and return the survey results
question = "What language did you first learn to speak? "
my_survey = AnonymousSurvey(question)
# Show the question and store the results
my_survey.show_question()
print("Enter 'quit' to stop at any time. \n")
while True:
    response = input("Language: ")
    if response.lower() == 'quit':
        break
    else:
        my_survey.record_answer(response)

print("\nThanks everyone for taking the survey")
my_survey.show_results()