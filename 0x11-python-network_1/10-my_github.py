#!/usr/bin/python3
"""
This script takes GitHub credentials (username and personal access token) and uses the GitHub API to display the user's id.
"""

import sys
import requests

def get_github_id(username, password):
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        return response.json()['id']
    else:
        return None

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    github_id = get_github_id(username, password)
    print(github_id)
