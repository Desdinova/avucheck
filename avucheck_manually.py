#!/usr/bin/env python3
# Florian Novy (2019)

from bs4 import BeautifulSoup
import requests

getXml = requests.get("http://212.89.102.251:8180/monitor/")
avuXml = getXml.text

soup = BeautifulSoup(avuXml, "lxml")

# print(soup.prettify())

print(soup.title.string)
print(soup.td.string)


# process.started
print("process.started")
procStarted = soup.find_all(title="process.started")

for proc in procStarted:
	print(proc.string)


#  process.count.error
print("process.count.error")
procCountErr = soup.find_all(title="process.count.error")

for count in procCountErr:
	print(count.string)


# process.count.ongoing
print("process.count.ongoing")
procCountOngoing = soup.find_all(title="process.count.ongoing")

for oncount in procCountOngoing:
	print(oncount.string)


# process.alert
print("process.alert")
procAlert = soup.find_all(title="process.alert")

for alert in procAlert:
	print(alert.string)


# trigger.alert
print("trigger.alert")
triggerAlert = soup.find_all(title="trigger.alert")

for trigalert in triggerAlert:
	print(trigalert.string)