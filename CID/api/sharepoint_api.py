import getpass
import json
import requests

from requests.auth import HTTPBasicAuth

class SharepointAPI():

    def __init__(self):

        with open("CID/creds.json", "r+") as f:
            self.creds = json.load(f)

    def retrieve_token(self):
        """
        Retrieves a Authentication Bearer token to connect to the a Sharepoint
        api.
        """

        url = "https://login.microsoftonline.us/8c2412cb-5fcb-4910-ab96-4dd622885917/oauth2/v2.0/token"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        payload = {
            "grant_type": "client_credentials",
            "client_id": self.creds["credentials"]["sharepoint"]["client_id"],
            "client_secret": self.creds["credentials"]["sharepoint"]["client_secret"],
            "scope": self.creds["credentials"]["sharepoint"]["scope"]
        }

        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching token: {response.status_code}")
            print(f"Response {response.text}")
            return None
