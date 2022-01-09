#!/usr/bin/python3
""" login into github using API """

if __name__ == "__main__":
    import sys
    import requests
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    info = (username, password)
    req = requests.get(url, auth=info)
    try:
        print(req.json()['id'])
    except Exception:
        print('None')
