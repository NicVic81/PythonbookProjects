# Exercise 10-1 Learning Python
# Reading the entire file at once
# learning_python = 'learning_python.txt'
#
# with open(learning_python) as learn_python:
#     whole_file = learn_python.read()
#
# print(whole_file.rstrip())
# Reading each line
# learning_python = 'learning_python.txt'
#
# with open(learning_python) as learn_python:
#     for line in learn_python:
#         print(line.rstrip())
#
# learning_python = 'learning_python.txt'
#
# with open(learning_python) as learn_python:
#     python_line = learn_python.readlines()
#
# for line in python_line:
#     print(line.rstrip())

# Exercise 10-2 Learning C
#
# learning_python = 'learning_python.txt'
#
# with open(learning_python) as learn_python:
#     for line in learn_python:
#         print(line.replace('Python', 'Ruby on Rails').rstrip())

# Exercise 10-4 Guest Book
# print("Please enter your name below")
# print("Enter 'stop' at any time to exit")
# user_list = 'user_list.txt'
# name = ''
# while name.lower() != 'stop':
#     name = input("Name: ")
#     if name.lower() != 'stop':
#         print("Hello " + name.title() + " ,it is nice to meet you!")
#         with open(user_list, 'a') as visitors:
#             visitors.write(name.title() + " has visited the site\n")
#     else:
#         print("Goodbye")
#         Just wanted to do it another way that might look a little cleaner
# user_list = 'user_list.txt'
# print("Please enter your name below")
# print("Enter 'stop' at any time to exit")
#
# while True:
#     name = input("Name: ")
#
#     if name.lower() == 'stop':
#         print("Goodbye")
#         break
#     else:
#         print("Hello " + name.title() + " ,it is nice to meet you!")
#         with open(user_list, 'a') as visitors:
#             visitors.write(name.title() + " has visited the site\n")

#  Exercise 10-5 Programming Poll
# This one was the same as 10-4 excpet it was goign to ask why you liked programming so I am not doing it just to cut
# and paste code here

#  Starting to use error handlers or try-except block as they call them in Python

# print("Give me two numbers and I'll divide them.")
# print("Enter 'quit' to stop the program")
#
# while True:
#     first_number = input("\nFirst Number: ")
#     if first_number.lower() == 'quit':
#         break
#     second_number = input("Second Number: ")
#     if second_number.lower() == 'quit':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0, you dumb cunt")
#     else:
#         print(answer)
# Now handling the file not found error
#
# filename = 'alice.txt'
#
# try:
#     with open(filename) as f_object:
#         contents = f_object.read()
# except FileNotFoundError:
#     print("I am sorry the file " + filename + " was not found.")

# Now to import the contents of a text file and count the number of words while uisng a try-except block.

book_file = 'OnlineResources/chapter_10/alice.txt'

try:
    with open(book_file) as book:
        contents = book.read()
except FileNotFoundError:
    msg = "I am sorry the file " + book_file + " is not found"
    print(msg)
else:
    # Count the approximate number of words in the book
    word_list = contents.split()
    num_words = len(word_list)
    print("The file " + book_file + " has about " + str(num_words) + " words in it.")

