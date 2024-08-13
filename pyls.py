import os
import time

def list_files():
    """
    List all files and directories in the current working directory.
    Returns:
        list: A list of file and directory names.
    """
    return os.listdir('.')

def print_help():
    """
    Print the help information for the pyls command.
    """
    help_text = """
    pyls - A limited version of the ls command

    Usage:
      pyls [options]

    Options:
      -F    Add suffixes to directories (/) and executable files (*)
      -l    Show details including last modified date, size, and name
      -h, --help  Show this help message and exit
    """
    print(help_text)

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    if '-h' in args or '--help' in args:
        print_help()
    elif '-l' in args and '-F' in args:
        files = list_files_with_details_and_suffixes()
    elif '-l' in args:
        files = list_files_with_details()
    elif '-F' in args:
        files = list_files_with_suffixes()
    else:
        files = list_files()
    for file in files:
        print(file)
