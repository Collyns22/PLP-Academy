def read_write_file(filename):
    try:
        
        with open(filename, 'r') as file:
            text = file.read()

        # Converting to uppercase
        uppercase_text = text.upper()

        word_count = len(uppercase_text.split())

        # Writing word count to a new file
        with open('output.txt', 'w') as new_file:
            new_file.write(f"WORDS IN FILE: {word_count}\n{uppercase_text}")

        print("Success! The processed text and word count have been written to output.txt.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Access to the file '{filename}' is denied.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Processing complete.")
     


# user input for the filename
filename = input("Enter the filename: ").strip()

# function call.
read_write_file(filename)