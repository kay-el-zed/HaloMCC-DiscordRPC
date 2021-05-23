import requests, json
from additional import clear, application_path
from datetime import datetime
from os import path, makedirs
import webbrowser
from time import sleep
CLIENT_ID = "8f9b5ee4-b4eb-40ea-a02f-c9be1f7ae7bf"
REDIRECT_URI = "https://localhost/oauth_success"

def main():
    """Making sure tokens are up to date in case any errors arrive.
    """
    current = datetime.now().isoformat(timespec='microseconds') + "9Z"
      
    if(path.exists(application_path() + "\\tokens\\token.json")):
        with open((application_path() + '\\tokens\\token.json'), 'r') as f:
            tokens = json.load(f)
    else:
        tokens = None
    if(tokens != None):        
        if(current > tokens['NotAfter']): 
            if(application_path() + "\\tokens\\accesstoken.json"):
                with open((application_path() + "\\tokens\\accesstoken.json"), 'r+') as f:
                    accesstoken = json.load(f)
                    access_token = refreshToken(accesstoken['refresh_token'])
                    user_token = userToken(access_token)
                    XToken(user_token)
            print("Generated a token.")
    else:
        url()
        authorization_code = input("Enter URL:")
        makedirs(application_path() + "\\tokens")
        clear()
        access_token = accessToken(authorization_code)
        user_token = userToken(access_token)
        XToken(user_token)
    pass
    
    
def url() -> None:
    """
    Authorize account for app and receive authorization code
    """
    url = "https://login.live.com/oauth20_authorize.srf"
    query_params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "approval_prompt": "auto",
        "scope": "Xboxlive.signin Xboxlive.offline_access",
        "redirect_uri": REDIRECT_URI,
    }

    destination_url = requests.Request("GET", url, params=query_params).prepare().url

    print("Login to your xbox account and save the url.")
    sleep(2)
    webbrowser.open(destination_url)
        
    
def accessToken(authorization_code) -> str:
    """
    Authenticate account via authorization code and receive access/refresh token
    """
    base_url = "https://login.live.com/oauth20_token.srf"
    params = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "scope": "Xboxlive.signin Xboxlive.offline_access",
        "code": authorization_code.replace("https://localhost/oauth_success?code=", ""),
        "redirect_uri": REDIRECT_URI,
    }
    
    resp = requests.post(base_url, data=params)
    if resp.status_code != 200:
        print("Failed to get access token")
        return

    access_token = resp.json()["access_token"]
    with open('tokens\\accesstoken.json', 'w+') as f:
        f.write(json.dumps(resp.json(), indent=2))
    return access_token    
        
def refreshToken(refresh_token) -> str:
    """
    Authenticate account via refresh code and receive access/refresh token
    """
    base_url = "https://login.live.com/oauth20_token.srf"
    params = {
        "grant_type": "refresh_token",
        "client_id": CLIENT_ID,
        "scope": "Xboxlive.signin Xboxlive.offline_access",
        "refresh_token": refresh_token,
        "redirect_uri": REDIRECT_URI,
    }
    
    resp = requests.post(base_url, data=params)
    if resp.status_code != 200:
        print("Failed to refresh token")
        return

    access_token = resp.json()["access_token"]
    with open('tokens\\accesstoken.json', 'w+') as f:
        f.write(json.dumps(resp.json(), indent=2))
    return access_token

def userToken(access_token) -> str:
    """
    Authenticate via access token and receive user token
    """
    url = "https://user.auth.xboxlive.com/user/authenticate"
    headers = {"x-xbl-contract-version": "1"}
    data = {
        "RelyingParty": "http://auth.xboxlive.com",
        "TokenType": "JWT",
        "Properties": {
            "AuthMethod": "RPS",
            "SiteName": "user.auth.xboxlive.com",
            "RpsTicket": "d=" + access_token,
        },
    }

    resp = requests.post(url, json=data, headers=headers)

    if resp.status_code != 200:
        print("Invalid response")
        return

    user_token = resp.json()["Token"]
    with open('tokens\\token.json', 'w+') as f:
        f.write(json.dumps(resp.json(), indent=2))
    return user_token

def XToken(user_token) -> str:
    """
    Authorize via user token and receive final X token
    """
    url = "https://xsts.auth.xboxlive.com/xsts/authorize"
    headers = {"x-xbl-contract-version": "1"}
    data = {
        "RelyingParty": "http://xboxlive.com",
        "TokenType": "JWT",
        "Properties": {
            "UserTokens": [user_token],
            "SandboxId": "RETAIL",
        },
    }

    resp = requests.post(url, json=data, headers=headers)

    if resp.status_code != 200:
        print("Invalid response")
        return

    with open('tokens\\xtoken.json', 'w+') as f:
        data = f.write(json.dumps(resp.json(), indent=2))
    return data

if __name__ == "__main__":
    main()