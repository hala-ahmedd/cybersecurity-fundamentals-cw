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
    with open("file.log", 'w') as log_file:  # open log file in write mode
        for i in file_collection:  # use the passed argument (list of file paths)
            log_file.write(i + "\n")  # write each path followed by a newline

    os.system("start file.log")  # On Windows: automatically open the log file using default program
    return "file.log"  # return the name of the log file

# User Code
if __name__ == "__main__":  # main function: all functions start/get provoked after it (could be removed but better for clarity and organization)
    path = input("Please Enter your directory's path:  ")  # the input is taken as a string
    files = file_collection(path)  # call file collection function with user input
    print(files)  # print the list of file paths to the console
    print_files(files)  # write to log file and open it
