import re


def remove_special_symbols(string):
    # Use regex to remove special symbols
    pattern = r'[^a-zA-Z0-9\s]'  # Matches any character that is not a letter, digit, or whitespace
    processed_string = re.sub(pattern, '', string)
    return processed_string


# Test the function
input_string = input("Enter a string: ")
result = remove_special_symbols(input_string)
print("Processed string:", result)
