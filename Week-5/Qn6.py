import sys
import shutil
import os

def create_backup(file_name):
    """
    Creates a backup copy of a given file.

    The function takes the name of an existing file, copies its contents, 
    and saves the copy with a new name that appends '_backup' to the original file name.
    If the original file does not exist, an error message is displayed.
    
    Args:
        file_name (str): The name of the file to back up.
    
    Returns:
        None: The backup file is created on the filesystem.
    """
    if os.path.exists(file_name):
        # Define the backup file name by appending '_backup' before the file extension
        base_name, extension = os.path.splitext(file_name)
        backup_file_name = base_name + "_backup" + extension
        
        # Copy the contents of the original file to the backup file
        shutil.copy(file_name, backup_file_name)
        
        print(f"Backup created successfully: {backup_file_name}")
    else:
        print(f"Error: The file '{file_name}' does not exist.")

if __name__ == "__main__":
    """
    A program that takes the name of a file as a command-line argument and creates a backup copy of the file.
    
    The script expects a valid file name as input. It then copies the contents of the original file
    and saves it with a new name that appends '_backup' to the original file name.
    
    Usage:
        python3 create_backup.py <file_name>
    
    Example:
        python3 create_backup.py myfile.txt
    """
    
    # Check if a file name was provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python3 create_backup.py <file_name>")
    else:
        file_name = sys.argv[1]
        create_backup(file_name)


'''bash : python3 create_backup.py myfile.txt'''