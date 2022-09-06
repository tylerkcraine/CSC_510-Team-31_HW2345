import args
import fileutils
import print as custom_print
import parse
def main():
    the_args = args.The()
    file_string = fileutils.read_file(the_args)
    parser_dict = parse.parser(file_string)
    print(custom_print.o(parser_dict))


if __name__ == '__main__':
    main()