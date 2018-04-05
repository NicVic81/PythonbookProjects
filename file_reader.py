# This opens the entire file and store it in memory in the object file_object
# The "with" at the start of it tells python to close the file whenever we are done
# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     # if we just use the print command we will get a blank line at the end so we use rstrip to remove the blank line.
#     print(contents.rstrip())
#
# # Now we are going to loop through the file with a for loop.
#
# filename = "pi_digits.txt"
#
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# With both these examples you can only use the file inside the "with" statement so now we are going to store
# the information in a list so we can use it later
#
# filename = 'pi_digits.txt'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# for line in lines:
#     print(line.rstrip())

# Now we are going to try and take all the info in the file and store it in one string
# filename = 'pi_digits.txt'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
#
# print(pi_string)
# print(len(pi_string))

# Showing that you can do a million digits
# filename = 'OnlineResources/chapter_10/pi_million_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
#     pi_string = ''
# for line in lines:
#     pi_string += line.strip()
# print(pi_string[:52] + "...")
# print(len(pi_string))

# Seeing if my birthday is in the pi string

filename = 'OnlineResources/chapter_10/pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
