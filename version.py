#!/usr/bin/env/ python

import requests

print requests.__version__

# response = requests.get("http://google.com")
# print response.status_code
# print response.text

response = requests.get("https://raw.githubusercontent.com/TheAspiredOne/cmput404w17lab1/master/version.py")
print response.status_code
print response.text