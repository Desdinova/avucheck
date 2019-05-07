#!/usr/bin/env python3
# Florian Novy (2019)

from bs4 import BeautifulSoup
from collections import Counter
import requests

url = "http://212.89.102.251:8180/monitor/"
getXml = requests.get(url)
avuXml = getXml.text
soup = BeautifulSoup(avuXml, "lxml")


# parse the webpage for htmlTitle and count the number of true and false. return influx DB string
def countTrueFalse(htmlTitle):
	findTitles = soup.find_all(title=htmlTitle)
	trueFalseList = []
	for title in findTitles:
		trueFalseList.extend(title.find_all(text="true"))
		trueFalseList.extend(title.find_all(text="false"))
	counts = Counter(trueFalseList)
	numberTrue = counts["true"]
	numberFalse = counts["false"]
	print("EDI,query=" + url + ",tag=" + htmlTitle + " " + htmlTitle + "true=" + str(numberTrue) + "," + htmlTitle + "false=" + str(numberFalse))


# parse the webpage for htmlTitle extract the values
def getProcessCounters(htmlTitle):
	findTitles = soup.find_all(title=htmlTitle)
	counterList = []
	for title in findTitles:
		counterList.extend(title.string)
	maxError = max(counterList)
	print("EDI,query=" + url + ",tag=" + htmlTitle + " " + htmlTitle + "=" + str(maxError))

if getXml.ok == True:
	# process.started (true, false)
	countTrueFalse("process.started")
	# process.alert
	countTrueFalse("process.alert")
	# trigger.alert
	countTrueFalse("trigger.alert")
	#  process.count.error
	getProcessCounters("process.count.error")
	# process.count.ongoing
	getProcessCounters("process.count.ongoing")