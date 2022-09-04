import fileparser


def read_file(the):
    file_name = the['f']
    buffer_string = ""
    with open(file_name, "r") as csv_file:
        file_lines = csv_file.readlines()
    for i in file_lines:
        buffer_string = buffer_string + i
    print(buffer_string)
    fileparser.parse(buffer_string)




