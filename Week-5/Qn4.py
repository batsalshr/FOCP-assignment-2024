import sys
import requests

def check_website(url):
    """
    Takes a URL as input and checks whether a website is working at that address.
    
    The function sends a GET request to the URL and checks the HTTP status code.
    If the status code is in the range of 200-299, the website is considered working.
    If the status code is outside this range, the website is considered unavailable.
    
    Args:
        url (str): The URL to check.
    
    Returns:
        None
    """
    try:
        response = requests.get(url)
        # Check if the response code is in the 200-299 range (indicating success)
        if 200 <= response.status_code < 300:
            print(f"The website at {url} is working!")
        else:
            print(f"The website at {url} returned status code {response.status_code}. It may not be working.")
    except requests.exceptions.RequestException as e:
        print(f"This webiste {url} does not exis.t")

if __name__ == "__main__":
    """
    A program that checks whether a website is working by sending a GET request to a URL provided as a 
    command-line argument.
    
    The program expects exactly one argument: the URL of the website. It sends a GET request to this URL 
    and checks the HTTP status code. If the code is between 200 and 299, the website is considered working. 
    Otherwise, it will indicate the status code and that the website might not be working.
    
    Usage:
        python3 check_website.py <URL>
    
    Example:
        python3 check_website.py https://www.youtube.com
    """
    
    # Ensure a URL argument is provided
    if len(sys.argv) != 2:
        print("Usage: python3 check_website.py <URL>")
    else:
        url = sys.argv[1]
        check_website(url)

'''bash : python3 Qn4.py https://www.youtube.com '''