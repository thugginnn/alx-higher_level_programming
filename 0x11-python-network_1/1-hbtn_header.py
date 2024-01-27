#!/usr/bin/python3
from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with request.urlopen(url) as response:
        if 'X-Request-Id' in response.headers:
            x_request_id = response.headers['X-Request-Id']
            print(x_request_id)
