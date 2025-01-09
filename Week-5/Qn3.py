import sys

def find_shortest_argument():
    """
    Takes command-line arguments and prints the shortest one.
    
    The function retrieves the arguments (excluding the script name), sorts them by length,
    and prints the shortest argument. If there are multiple arguments with the same shortest length,
    any one of them will be printed.
    
    Args:
        None: The function uses the arguments passed to the script via the command-line.
    
    Returns:
        None: The result is printed to the console.
    """
    # Get all arguments except the script name (sys.argv[1:])
    arguments = sys.argv[1:]

    if arguments:
        # Sort arguments by length and print the shortest
        shortest = sorted(arguments, key=len)[0]
        print(f"The shortest argument is: {shortest}")
    else:
        print("No arguments provided.")

if __name__ == "__main__":
    """
    A program that takes command-line arguments and finds the shortest one. 
    It prints the shortest argument from the list of arguments provided.
    
    The program expects at least one argument and will output the shortest string 
    based on length. If no arguments are provided, it will notify the user.
    
    Usage:
        python3 find_shortest_argument.py <arg1> <arg2> <arg3> ...
    
    Example:
        python3 find_shortest_argument.py apple banana kiwi pear grapes mango
    """
    print(find_shortest_argument.__doc__)  # Print the docstring
    find_shortest_argument()

'''bash : python3 Qn3.py apple banana kiwi pear grapes mango '''