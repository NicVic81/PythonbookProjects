# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)
#
# name = input("Please enter your name: ")
# print("Hello, "+name.title()+"!")


#user_promt = 'If you tell us your name we can personalize the message for you.'
#user_promt += '\nWhat is your name?'

#name = input(user_promt)
#print("Hello, "+name.title()+"!")
##using int() to convert strings to intergers
#age = input("How old are you? ")
#age=int(age)

#height = input("How tall are you in inches? ")
#height=int(height)

#if height >= 36:
#    print("\nYou're tall enough to ride DIS DICK!")
#else:
#     print("\nYou'll be able to ride DIS DICK when you are "+str((36-height))+" inches taller!")

# using % to divide and show the remainder and use to tell if it is odd or even
# number = input("Enter a number and I will tell you if it is even or odd: ")
# number = int(number)
#
# if number % 2 == 0:
#     print("\nThe number "+str(number)+" is even.")
# else:
#     print("\nThe number "+str(number)+" is odd")
#
## while loop to count up to 5
# current_number =1
# while current_number <= 5:
#     print(current_number)
## #The += operator is shorthand for current_number =current_number + 1
#     current_number +=1
# prompt = "\nTell me something, and I will repeat it back to you. "
# prompt += "\nEnter 'quit' to end the program. : "
#
# message=""
# while message.lower() != 'quit':
#     message = input(prompt)
#     print(message)

##trying to refine the code above on my own
# first_message = "\nTell me something, and I will repeat it back to you. "
# first_message += "\nEnter 'quit' to end the program.\n"
# print(first_message)
# prompt="Your call holy man: "
# message=""
# while message.lower() != 'quit':
#     message = input(prompt)
# # Adding an if satement to not print if the word is quit
#     if message.lower() != 'quit':
#         print(message+"\n")
#
# now using a variable to see if the program should keep running
# first_message = "\nTell me something, and I will repeat it back to you. "
# first_message += "\nEnter 'quit' to end the program.\n"
# print(first_message)
# prompt="Your call holy man: "
# message=""
# active = True
# while active:
#     message = input(prompt)
# # Adding an if satement to not print if the word is quit
#     if message.lower() == 'quit':
#         active = False
#     else:
#         print(message+"\n")

# #now using a while true statement because it just runs until a break condition is met
# direction_prompt = "Please tell me all the cities you have been and I will "
# direction_prompt += "make you a list"
# direction_prompt += "\nEnter 'quit' any time you want to stop.\n"
# print(direction_prompt)
# prompt = "City"
# city_number = 1
# city_list = []
# while True:
#     city = input(prompt + ' '+str(city_number)+':')
#     city_list.append(city)
#     city_number += 1
#
#     if city.lower() == 'quit':
#         break
#     else:
#         print('Next city please.\n')
# del city_list [-1]
# print('You have been to '+str(len(city_list))+' cities.')
# print('The cities are:')
# # sort this list
# for city_print in sorted(city_list):
#     print(city_print.title())
#
# using a continue in a while loop

# current_number = 0
# while current_number < 10:
#     current_number += 1
# # this says if the number is an even number than continue the while loop and if
# # not then go to the print function and then continue the while loop
#     if current_number % 2 ==0:
#         continue
#     print(current_number)

# exercise 7-4
# directions_prompt = "Tell me the toppings you want on your pizza.\n"
# directions_prompt += "Enter quit to stop entering toppings"
# topping_prompt = "Enter your pizza topping: "
#
# print(directions_prompt)
#
# while True:
#     topping = input(topping_prompt)
#
#     if topping.lower() == 'quit':
#         break
#     else:
#         print("I will add "+topping.lower()+" to your pizza\n")

#  exercise 7-5

# age_prompt = "Please tell me your age and I will tell you the price of the ticket"
# age_prompt += "\nEnter quit at any time to exit the program\n"
# age_enter = "Age: "
# print(age_prompt)
# while True:
#     user_age = input(age_enter)
#
#     if user_age.lower() == 'quit':
#         break
#     elif int(user_age) < 3:
#         print("Your ticket is free.\n")
#     elif int(user_age) < 12:
#         print("Your ticket is 10 dollars.\n")
#     else:
#         print("Your ticket is 12 dollars\n")

# exercise 7-6.1
# This exits on a conditional statement
# age_prompt = "Please tell me your age and I will tell you the price of the ticket"
# age_prompt += "\nEnter quit at any time to exit the program\n"
# age_enter = "Age: "
# print(age_prompt)
# user_age = ""
# while str(user_age.lower()) != "quit":
#     user_age = input(age_enter)
#     # Would not work without this first if statement because while it is in the loop it first checks it the interger is
#     # less than three and would error since it is a string
#     if str(user_age.lower()) == "quit":
#         print(user_age)
#     elif int(user_age) < 3:
#         print("Your ticket is free.\n")
#     elif int(user_age) < 12:
#         print("Your ticket is 10 dollars.\n")
#     else :
#         print("Your ticket is 12 dollars\n")
# Exercise 7-6.2
# This exits using an active variable
# age_prompt = "Please tell me your age and I will tell you the price of the ticket"
# age_prompt += "\nEnter quit at any time to exit the program\n"
# print(age_prompt)
# age_enter = "Age: "
# keep_running = "True"
# while keep_running:
#     user_age = input(age_enter)
#     if str(user_age.lower()) == "quit":
#         print(user_age)
#         keep_running = False
#     elif int(user_age) < 3:
#         print("Your ticket is free.\n")
#     elif int(user_age) < 12:
#         print("Your ticket is 10 dollars.\n")
#     else :
#         print("Your ticket is 12 dollars\n")
# Exercise 7-6.3
# This uses a break to exit
# age_prompt = "Please tell me your age and I will tell you the price of the ticket"
# age_prompt += "\nEnter quit at any time to exit the program\n"
# age_enter = "Age: "
# print(age_prompt)
# while True:
#     user_age = input(age_enter)
#
#     if user_age.lower() == 'quit':
#         break
#     elif int(user_age) < 3:
#         print("Your ticket is free.\n")
#     elif int(user_age) < 12:
#         print("Your ticket is 10 dollars.\n")
#     else:
#         print("Your ticket is 12 dollars\n")

# Start with users that need to be verified
#  and an empty list to hold confirmed users
# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []
#
# # verify each user until there are no more unconfirmed users
# # move each verified user into the list of confirmed users
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#
#     print("Verifying user: " + current_user.title())
#     confirmed_users.append(current_user)
#
# #Display all confirmed users
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())
##Showing how to remove all instance of a value in a list
# pets = ['dog','cat','dog','godlfish','cat','rabbit','cat']
# print(pets)
#
# while 'cat' in pets:
#     pets.remove('cat')
#
# print(pets)
##Filling a dictionary with user input
responses = {}
#Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    #Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    #Store the response in the dictionary
    #This means the the dictionary entry for that name gets that response
    responses[name] = response

    #Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat.lower() == 'no':
        polling_active = False

#Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in sorted(responses.items()):
    print(name.title() + " would like to climb " + response.title() + ".")



