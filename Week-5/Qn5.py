import sys

def process_temperatures():
    """
    Takes temperature readings from command-line arguments and calculates the maximum, minimum, and mean.
    
    The program expects the temperature readings to be passed as command-line arguments. 
    It calculates and prints the maximum, minimum, and mean temperatures.
    
    If no arguments are provided, it prints an error message.
    
    If any argument is not a valid number, it will catch the exception and print an error message.
    """
    # Check if command-line arguments are provided (excluding the script name)
    if len(sys.argv) < 2:
        print("No temperature readings provided. Please enter temperature values as command-line arguments.")
        return
    
    try:
        # Convert the command-line arguments to a list of floats (temperature readings)
        temperatures = [float(arg) for arg in sys.argv[1:]]
        
        # Calculate the max, min, and mean
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        mean_temp = sum(temperatures) / len(temperatures)
        
        # Print the results
        print(f"Maximum Temperature: {max_temp}")
        print(f"Minimum Temperature: {min_temp}")
        print(f"Mean Temperature: {mean_temp:.2f}")
    
    except ValueError:
        print("Invalid temperature readings. Please enter valid numbers as arguments.")

if __name__ == "__main__":
    print(process_temperatures.__doc__)  # Print the docstring
    process_temperatures()

'''bash : python3 Qn5.py 32 45 60 78 56 23'''