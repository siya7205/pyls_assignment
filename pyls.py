import os
import time

def list_files():
    """
    List all files and directories in the current working directory.
    Returns:
        list: A list of file and directory names.
    """
    return os.listdir('.')

def list_files_with_suffixes():
    """
    List all files and directories in the current working directory with suffixes.
    Suffix '/' is added to directories and '*' is added to executable files.
    Returns:
        list: A list of file and directory names with appropriate suffixes.
    """
    files = os.listdir('.')
    result = []
    for file in files:
        if os.path.isdir(file):
            result.append(file + '/')
        elif os.access(file, os.X_OK):
            result.append(file + '*')
        else:
            result.append(file)
    return result

def list_files_with_details():
    """
    List all files and directories in the current working directory with details.
    Details include last modified date, size, and name.
    Returns:
        list: A list of file and directory details.
    """
    files = os.listdir('.')
    result = []
    for file in files:
        stats = os.stat(file)
        last_modified = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stats.st_mtime))
        size = stats.st_size if not os.path.isdir(file) else 0
        result.append(f"{last_modified} {size} {file}")
    return result

def list_files_with_details_and_suffixes():
    """
    List all files and directories in the current working directory with details and suffixes.
    Details include last modified date, size, and name.
    Suffix '/' is added to directories and '*' is added to executable files.
    Returns:
        list: A list of file and directory details with appropriate suffixes.
    """
    files = os.listdir('.')
    result = []
    for file in files:
        stats = os.stat(file)
        last_modified = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stats.st_mtime))
        size = stats.st_size if not os.path.isdir(file) else 0
        suffix = '/' if os.path.isdir(file) else '*' if os.access(file, os.X_OK) else ''
        result.append(f"{last_modified} {size} {file}{suffix}")
    return result

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
