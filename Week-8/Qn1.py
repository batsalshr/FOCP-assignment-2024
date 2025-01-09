import sys

def nl_command(file_name):
    """
    Simulates the Unix 'nl' command by printing the lines of a file with line numbers.

    The function takes a file name, reads the file, and outputs each line prefixed with its line number.
    
    Args:
        file_name (str): The name of the text file to read and number the lines.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    try:
        with open(file_name, 'r') as file:
            # Read and print each line with a line number
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number}\t{line}", end="")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")

if __name__ == "__main__":
    # Check if a filename is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python nl_command.py <filename>")
    else:
        file_name = sys.argv[1]
        nl_command(file_name)
