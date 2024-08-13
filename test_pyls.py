import os

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

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    if '-F' in args:
        files = list_files_with_suffixes()
    else:
        files = list_files()
    for file in files:
        print(file)

