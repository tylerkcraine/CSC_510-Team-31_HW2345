import args
from constants import F_OPTION


def read_file(argus: args.The) -> str:
    file_name = argus.the[F_OPTION]
    buffer_string = ""
    with open(file_name, "r") as csv_file:
        file_lines = csv_file.readlines()
    for i in file_lines:
        buffer_string = buffer_string + i
    return buffer_string

