#!/usr/bin/python3
""" Takes a URL, sends request and displays
the value of the variable X-Request-ID
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
