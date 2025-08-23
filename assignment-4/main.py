
# Open and read 'gospel.txt'
file = open("assignment-4/gospel.txt", 'r')
text = file.read()
file.close()

# Modify the content (example: convert to uppercase)
upper_case_text = text.upper()
print("Uppercase content of gospel.txt:\n")
print(upper_case_text)

# Ask the user for a filename
fileName = input("Enter the filename: ")

try:
    # Try to open the user-specified file
    with open('assignment-4/' + fileName, 'r') as user_file:
        user_text = user_file.read()
        print("\nFile content of", fileName, ":\n")
        print(user_text)
except FileNotFoundError:
    print(f"Error: The file '{fileName}' does not exist.")
except PermissionError:
    print(f"Error: You do not have permission to read '{fileName}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
