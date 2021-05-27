import os
from os import system, name, sys

def application_path():
    """Get's the current application path

    Returns:
        string: Retruns current application path
    """
    if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
        application_path = os.path.dirname(sys.argv[0])
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
    return application_path

def clear(): 
    """Clears terminal of all data.
    """
    if name == 'nt': 
        _ = system('cls') 
    # MacOs support and Linux not likely
    else: 
        _ = system('clear')