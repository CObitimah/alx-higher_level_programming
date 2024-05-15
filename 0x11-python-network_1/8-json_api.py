#!/usr/bin/python3
"""
Script to send a POST request
"""
import requests
import sys


def main():
    """
    Main function to send a POST request with a letter as a parameter
    """
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}

    try:
        response = requests.post(url, data=payload)
        data = response.json()

        if isinstance(data, dict) and data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        elif isinstance(data, list) and not data:
            print("No result")
        else:
            print("Not a valid JSON")
    except ValueError:
        print("Not a valid JSON")
    except requests.RequestException as e:
        print("Error:", e)

    if __name__ == '__main__':
        main()
