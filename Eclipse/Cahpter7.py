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
# # not then go to the print funtion and then continue the while loop 
#     if current_number % 2 ==0:
#         continue
#     print(current_number)

# exercise 7-4
directions_prompt ="Tell me the toppings you want on your pizza.\n"
directions_prompt +="Enter quit to stop entering toppings"
topping_prompt = "Enter your pizza topping: "
print(directions_prompt)

while True:
    topping=input(topping_prompt)
    
    if topping.lower()=='quit':
        break
    else:
        print("I will add "+topping.lower()+" to your pizza\n")

    