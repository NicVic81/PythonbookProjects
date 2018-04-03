# This opens the entire file and store it in memory in the object file_object
# The "with" at the start of it tells python to close the file whenever we are done
# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     # if we just use the print command we will get a blank line at the end so we use rstrip to remove the blank line.
#     print(contents.rstrip())
#
# # Now we are goignto loop through the file with a for loop.
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
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))