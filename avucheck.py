#!/usr/bin/env python3

import requests

avuXml = requests.get("http://212.89.102.251:8180/monitor/")
print(avuXml.text) 
