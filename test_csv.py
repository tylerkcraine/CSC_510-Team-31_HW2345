# import re
# def reader_file(file_name):
#     with open(file_name, "r") as csv_file:
#         file_lines = csv_file.readlines()
#     for i in file_lines:
#         a = i.split(the.seperator)
#         for l in a:


#     #     buffer_string = buffer_string + i
#     # return buffer_string

# a = reader_file("data/auto93.csv")
# data = a.split("")

def test_csv(the, n):
    list = []
    n = 0
     with open(the, "r") as csv_file:
        file_lines = csv_file.readlines()
        for i in file_lines:
        # a = i.split(the.seperator)
    match = re.search(data, the.seperator)
    list.append(match)
    for row in list: 
        n = n+1
        if n > 10:
            return
        else:
            oo(row)