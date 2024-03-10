#1
import os
def list_directories_files(path):
    try:
        entries = os.listdir(path)
        directories = [entry for entry in entries 
                       if os.path.isdir(os.path.join(path, entry))]
        files = [entry for entry in entries 
                 if os.path.isfile(os.path.join(path, entry))]
        return directories, files
    except FileNotFoundError:
        return None, None
specified_path = input("path: ")
directories, files = list_directories_files(specified_path)
if directories is not None and files is not None:
    print(f"Directories in the specified path: {directories}")
    print(f"Files in the specified path: {files}")
else:
    print("Specified path not found.")
print()


#2
def check_path_access(path):
    try:
        exists = os.path.exists(path)
        readable = os.access(path, os.R_OK)
        writable = os.access(path, os.W_OK)
        executable = os.access(path, os.X_OK)
        return exists, readable, writable, executable
    except Exception as e:
        return None, None, None, None
specified_path = input("path: ")
exists, readable, writable, executable = check_path_access(specified_path)
if exists is not None and readable is not None and writable is not None and executable is not None:
    print(f"Path exists: {exists}")
    print(f"Path is readable: {readable}")
    print(f"Path is writable: {writable}")
    print(f"Path is executable: {executable}")
else:
    print("Error checking access for the specified path.")
print()


#3
def analyze_path(path):
    try:
        if os.path.exists(path):
            filename = os.path.basename(path)
            directory = os.path.dirname(path)
            return True, filename, directory
        else:
            return False, None, None
    except Exception as e:
        return False, None, None
specified_path = input("path: ")
exists, filename, directory = analyze_path(specified_path)
if exists:
    print(f"Path exists: {exists}")
    print(f"Filename: {filename}")
    print(f"Directory: {directory}")
else:
    print("Path does not exist.")
print()


#4
file_path = input("path: ")
try:
    with open(file_path, 'r') as file:
        line_count = sum(1 for line in file)
    print(f"The number of lines in the file is {line_count}")
except FileNotFoundError:
    print(f"File not found")
print()


#5
my_list = [1, 2, 3, 4, 5]
output_file_path = "output.txt"
with open(output_file_path, 'w') as output_file:
    for item in my_list:
        output_file.write(str(item) + "\n")
print(f"The list has been written to {output_file_path}")
print()


#6
import string
for letter in string.ascii_uppercase:
    file_name = f"{letter}.txt"
    with open(file_name, 'w') as file:
        file.write(f"This is file {letter}")
print("26 text files have been generated.")
print()


#7
source_path = input("path of the source file: ")
destination_path = input("path of the destination file: ")
try:
    with open(source_path, 'r') as source_file:
        content = source_file.read()
        with open(destination_path, 'w') as destination_file:
            destination_file.write(content)
    print("File copied successfully.")
except FileNotFoundError:
    print("Source file not found.")
except Exception as e:
    print(f"An error occurred: {e}")
print()


#8
import os
file_path_to_delete = input("path of the file to delete: ")
if os.path.exists(file_path_to_delete):
    try:
        os.remove(file_path_to_delete)
        print(f"The file at {file_path_to_delete} has been deleted.")
    except PermissionError:
        print("Permission error. Unable to delete the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("The specified file path does not exist.")