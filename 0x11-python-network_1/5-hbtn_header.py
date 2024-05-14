#!/usr/bin/python3
"""
Script to send a request to a URL and display the value of the variable X-Request-Id in the response header.
"""

import requests
if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    data = response.text
    data_type = type(data)
    print(f'Body response:\n\t- type: {data_type}\n\t- content: {data}')
