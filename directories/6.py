import string
import os


folder_name = "letters"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)


for letter in string.ascii_uppercase:
    file_path = os.path.join(folder_name, f"{letter}.txt")
    with open(file_path, "w") as file:
        file.write(letter)  

print("26 text files (A-Z) have been created in the 'letters' folder.")