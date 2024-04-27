#example of code: dirscan.py wordlist.txt example.com   dirscan.py wordlist.txt 127.0.0.1
import requests
import sys

sub_list = open(sys.argv[1]).read()
directories = sub_list.splitlines()

for dir in directories:
    dir_enum = f"http://{sys.argv[2]}/{dir}.html"
    try:
        r = requests.get(dir_enum)
        if r.status_code >= 200 and r.status_code < 300:
            print("valid directory:", dir_enum)
        elif r.status_code >= 300 and r.status_code < 400:
            print("redirection:", dir_enum)
        elif r.status_code == 403:
            print("forbidden:", dir_enum)
        elif r.status_code >= 400 and r.status_code <= 500:
            pass
        elif r.status_code > 500 and r.status_code < 600: #500 code is all catch request in 99% chance is 404 error code 
            print("server error:", dir_enum)
        else:
            print("Unknown status code:", r.status_code, "for", dir_enum)
    except requests.ConnectionError:
        print(f"error here: {dir_enum}")
        pass

