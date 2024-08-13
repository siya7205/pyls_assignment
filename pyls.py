import os
import time

def list_files():
    """
    List all files and directories in the current working directory.
    Returns:
        list: A list of file and directory names.
    """
    return os.listdir('.')


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

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    if '-l' in args:
        files = list_files_with_details()
    elif '-F' in args:
        files = list_files_with_suffixes()
    else:
        files = list_files()
    for file in files:
        print(file)
