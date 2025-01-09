import sys

def count_arguments():
    """
    Reports the number of arguments provided when running the script from the command line.
    
    The function counts the command-line arguments provided to the script, excluding the script name itself.
    The count is derived from sys.argv, where sys.argv[0] is the script name, and sys.argv[1:] contains the arguments.
    
    Prints the number of arguments supplied by the user.
    
    Args:
        None: The function uses the arguments passed to the script via the command line.
    
    Returns:
        None: The result is printed to the console.
    """
    num_arguments = len(sys.argv) - 1  # Subtract 1 to exclude the script name
    print(f"Number of arguments: {num_arguments}")

if __name__ == "__main__":
    """
    A program that reports the number of arguments provided when running the script from the command line.
    
    The program counts the command-line arguments, excluding the script name. It prints the total number of 
    arguments provided. If no arguments are provided (other than the script name), it will report zero arguments.
    
    Usage:
        python3 count_arguments.py <arg1> <arg2> <arg3> ...
    
    Example:
        python3 count_arguments.py arg1 arg2 arg3
    """
    
    print(count_arguments.__doc__)  # Print the docstring
    count_arguments()

'''bash : python3 Qn2.py arg1 arg2 arg3'''