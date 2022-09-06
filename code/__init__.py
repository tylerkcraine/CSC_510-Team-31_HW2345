import args
import fileutils
import print as custom_print
from parse_function import parse

def main():
    the_args = args.The()
    file_string = fileutils.read_file(the_args)
    parser_dict = parse(file_string)
    custom_print.o(parser_dict)

if __name__ == '__main__':
    main()