# print("question no 3")
# import pyttsx3
# engine = pyttsx3.init()
# engine.say("I am umair i am the student of software engineering recently i complete my 6th semter now i am here to learn python")
# engine.runAndWait()


# ............................os module sy content directory print krna ha

import os

def print_directory_contents(path):
    try:
        # Get the list of all files and directories
        dir_contents = os.listdir(path)
        
        # Print the contents
        for item in dir_contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory {path} does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory {path}.")

# Specify the path
directory_path = '/'  # Replace with the actual directory path

# Call the function
print_directory_contents(directory_path)
