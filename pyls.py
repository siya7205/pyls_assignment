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
    assert isinstance(files, list), "Expected list of files"
    result = []
    for file in files:
        assert isinstance(file, str), "Expected file name to be a string"
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
    assert isinstance(files, list), "Expected list of files"
    result = []
    for file in files:
        assert isinstance(file, str), "Expected file name to be a string"
        stats = os.stat(file)
        last_modified = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stats.st_mtime))
        size = stats.st_size if not os.path.isdir(file) else 0
        result.append(f"{last_modified} {size} {file}")
    return result
