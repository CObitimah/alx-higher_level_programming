#!/usr/bin/python3
"""
This script sends a request to a epecified URL and displays the body of the response, decoded in utf-8. Incase of an HTTP error, it prints the error code.
"""

import urllib.request
import urllib.error
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            response_body = respose.read().decode('utf-8')
            print(response_body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
