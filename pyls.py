import os

def list_files():
    """
    List all files and directories in the current working directory.
    Returns:
        list: A list of file and directory names.
    """
    return os.listdir('.')

if __name__ == "__main__":
    files = list_files()
    for file in files:
        print(file)
