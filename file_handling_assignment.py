try:
    # File Creation
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Another line with text and numbers: 42\n")

    # File Reading and Display
    print("Contents of my_file.txt:")
    with open("my_file.txt", "r") as file:
        file_content = file.read()
        print(file_content)

    # File Appending
    with open("my_file.txt", "a") as file:
        file.write("Appending line 1\n")
        file.write("Appending line 2\n")
        file.write("Appending line 3\n")

except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to open the file.")
finally:
    print("Execution completed.")
