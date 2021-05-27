import os, time, sys

def main():
    xbox_token = os.getenv('LOCALAPPDATA') + "\\OpenXbox\\xbox\\tokens.json"
    remove = str(input("Do you want to remove your authenticate token? (Recommended for a Shared Computer) Y/N: "))
    if (remove == "y" or remove == "Y"):
        try:
            os.remove(xbox_token)
            print("Your Token Has Been Removed.")
            time.sleep(3)
        except OSError:
            print("You never had a Xbox Live Token. If you did then this might be an error.")
            time.sleep(3)
            pass
    elif(remove == "n" or remove == "N"):
        print("I would recommend you do.")
        time.sleep(3)
    else:
        print("Your Live token is stored in Open Xbox or maybe Not.")
        time.sleep(3)
def removeExisting():
    xbox_token = (os.getenv('LOCALAPPDATA') + "\\OpenXbox\\xbox\\tokens.json")
    if(os.path.isfile(xbox_token) == True):
        os.remove(xbox_token)
        print("Removed Token")
def createToken():
    xbox_token = os.getenv('LOCALAPPDATA') + "\\OpenXbox\\xbox\\tokens.json"
    remove = str(input("Do you want to Create a new Token?: "))
    if (remove == "y" or remove == "Y"):
        try:
            os.remove(xbox_token)
            print("Your Token Has Been Removed.")
            time.sleep(3)
        except OSError:
            print("You never had a Xbox Live Token. Try Creating one.")
    elif(remove == "n" or remove == "N"):
        print("Loading Token.")
        time.sleep(3)