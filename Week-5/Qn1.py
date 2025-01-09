import sys

def report_platform():
    """
    Reports the operating system platform being used.

    This function checks the platform using sys.platform and prints the platform name.
    It handles common platforms such as Linux, macOS, and Windows, and prints
    an identifier for any other platform that may not be explicitly recognized.

    It uses the sys.platform attribute, which returns a string representing
    the platform on which the Python script is being executed:
    - 'linux' or 'linux2' for Linux-based systems
    - 'darwin' for macOS
    - 'win32' for Windows
    - Other values for unidentified or less common platforms.
    """
    platform = sys.platform
    
    if platform == "linux" or platform == "linux2":
        print("Operating System: Linux")
    elif platform == "darwin":
        print("Operating System: macOS")
    elif platform == "win32":
        print("Operating System: Windows")
    else:
        print(f"Operating System: {platform} (Unidentified)")

if __name__ == "__main__":
    print(report_platform.__doc__)  # Print the docstring
    report_platform()


'''bash : python3 Qn1.py'''