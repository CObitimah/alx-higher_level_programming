#!/usr/bin/python3
"""
Script to fetch and display information from https://alx-intranet.hbtn.io/status using the requests package.

Usage:
    ./4-hbtn_status.py

Requirements:
    - requests package
"""

import requests
if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    response = request.get(url)
    data = response.text
    data_type = type(data)
    print(f'Body response:\n\t- type: {data_type}\n\t- content: {data}')
