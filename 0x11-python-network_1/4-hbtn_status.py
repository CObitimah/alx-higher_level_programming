#!/usr/bin/python3
"""
Script to fetch and display information from https://alx-intranet.hbtn.io/status using the requests package.

Usage:
    ./4-hbtn_status.py

Requirements:
    - requests package
"""

import requests
def main():
    """
    Fetches the URL https://alx-intranet.hbtn.io/status and displays information about the response body.
    """
    url = 'https://alx-intranet.hbtn.io/status'
    response = request.get(url)
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
if __name__ == "__main__":
    main()
