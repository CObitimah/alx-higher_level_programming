#!/usr/bin/python3
"""
Script to a POST request to a given URL with an email parameter and display the response body.
"""
import requests
import sys

def main():
    """
    Main function to send a POST request with the provided email address.
    """
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}

    response = requests.post(url, data=payload)
    print(response.text)

if __name__ == '__main__':
    main()
