import os  # library to make the code get executed as in the terminal

collected_files = []  # initialized list to store the paths

# collecting files function, takes the path as its parameter
def file_collection(directory_path):
    for root, dirs, files in os.walk(directory_path):  # ls — lists all directories and files recursively
        for file in files:  # search through each file found
            if file.endswith(('.txt', '.jpg', '.docx')):  # check for specific extensions
                fullnew = os.path.join(root, file)  # get the full path to the file
                collected_files.append(fullnew)  # store the full path in the list
    return collected_files  # return the final list of collected file paths

# function to write file paths into a log file and open it
def print_files(file_collection):
    log_path = r'C:\Users\Test 1\Desktop\code'  # use raw string to avoid escape issues
    with open(os.path.join(log_path, "files.log"), 'w') as log_file:
        for i in file_collection:
            log_file.write(i + "\n")
    
    os.system(f'start "" "{log_path}"')  # open the log file
    return log_path
   
# User Code
if __name__ == "__main__":  # main function: all functions start/get provoked after it (could be removed but better for clarity and organization)
    path = input("Please Enter your directory's path:  ")  # the input is taken as a string
    files = file_collection(path)  # call file collection function with user input
    print(files)  # print the list of file paths to the console
    print_files(files)  # write to log file and open it
    
