#!/usr/bin/python3
"""
This script sends a POST request to a specified URL with an email parameter
"""

import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data=data) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)
