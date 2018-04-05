"""File for storing the function for counting words in a file"""
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # if you remove this and just put in 'pass' it would not report an error and would just keep going
        msg = "Sorry the file " + filename + " was not found."
        print(msg)
    else:
        # Count the approximate number of words in a file
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about "  + str(num_words) + " words in it")

