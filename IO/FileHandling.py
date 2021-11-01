
file_name = "dogbreeds"
path = f"TestFiles\{file_name}.txt"


# Read a text file using open
# with open as - ensures that the file will be closed
with open(path, 'r') as file_reader:
    # print and read the whole file
    print(file_reader.read())


# read the lines in a file and return as a list

with open(path, 'r') as file_reader_list:
    file_list = file_reader_list.readlines()
    print(file_list)

for line in file_list:
    print(line)
