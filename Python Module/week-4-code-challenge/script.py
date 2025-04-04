# python script that read the contents of input.txt
with open('input.txt', 'r') as file:
    text = file.read()

# To count the numberof text
word_count = len(text.split())

# To convert all text to uppercase
uppercase_text = text.upper()

# Writing to a new file called output.txt
with open('output.txt', 'w') as new_file:
    new_file.write(f"WORDS IN FILE: {word_count}\n{uppercase_text}")

# Print a success message
print("Success! The processed text and word count have been written to output.txt.")