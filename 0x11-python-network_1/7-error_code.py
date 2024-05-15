#!/usr/bin/python3
"""
Script to send a request to a URL and display the body of the response
"""
import requests
import sys


def main():
    """
    Main function to send a request to the provided URL
    """
    url = sys.argv[1]

    try:
        response = requests.get(url)
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)
    except requests.RequestException as e:
        print(f'Error: {e}')

        if __name__ == '__main__':
            main()
