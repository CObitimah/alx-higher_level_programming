#!/usr/bin/python3
"""
Script to a POST request to a given URL with an email paramete.
"""
import requests
import sys


def main():
    """
    Main function to send a POST request with the provided email address.
    """
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}

    response = requests.post(url, data=payload)
    print(response.text)


if __name__ == '__main__':
    main()
