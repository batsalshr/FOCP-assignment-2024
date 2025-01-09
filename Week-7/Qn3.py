"""
    Question 3 : 
    Write a program that manages a list of countries and their capital cities. It should prompt the user to enter the name of a country. 
    If the program already "knows" the name of the capital city, it should display it. Otherwise it should ask the user to enter it. 
    This should carry on until the user terminates the program (how this happens is up to you).
    
"""
def manage_countries_and_capitals():
    """
    Manages a list of countries and their capital cities.
    Prompts the user to enter a country name. If the program knows the capital, it displays it.
    Otherwise, it asks the user to provide the capital city.
    The program continues until the user decides to exit by typing 'exit'.
    """
    countries_and_capitals = {}  # Dictionary to store countries and their capitals

    while True:
        # Prompt the user for a country
        user_input = input("Enter the name of a country (or type 'exit' to quit): ").strip()
        
        # Check for exit condition
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Normalize the country name to handle case-insensitivity
        country = user_input.lower()

        # Check if the country is already known
        if country in countries_and_capitals:
            capital = countries_and_capitals[country]
            print(f"The capital of {user_input.capitalize()} is {capital}.")
        else:
            # Ask for the capital city if it's not known
            capital = input(f"What is the capital city of {user_input.capitalize()}? ").strip()
            countries_and_capitals[country] = capital
            print(f"Thank you! I've added {user_input.capitalize()} and its capital {capital} to the database.")

# Display the program's documentation using __doc__
print("Program Documentation:")
print(manage_countries_and_capitals.__doc__)

# Run the program
manage_countries_and_capitals()
