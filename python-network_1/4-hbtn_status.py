#!/usr/bin/python3
"""This is just a doc"""


import requests


if __name__ == '__main__':
    myreq = requests.request('https://intranet.hbtn.io/status')
    print(myreq.text)
