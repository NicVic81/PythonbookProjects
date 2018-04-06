from name_function import get_formatted_name

print("Enter 'quit' at any time to quit.")
while True:
    first = input("\nWhat is your first name? ")
    if first.lower() == 'quit':
        break
    last = input("What is your last name? ")
    if last.lower() == 'quit':
        break
    formatted_name = get_formatted_name(first, last)
    print("\tNeatley formatted name: " + formatted_name)
