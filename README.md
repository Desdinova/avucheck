# avucheck
avucheck.py is a program that gathers monitoring (status, values) information from a html website. These values are extracted with BeautifulSoup and converted to a InfluxDB string. The programm is triggered by the input.exec module of Telegraf. The data is later used for visualization and alerting in Grafana.

Preparatory work:
	
	sudo apt update
	sudo apt install python3-pip python3-bs4
	sudo pip3 install requests
	
	Be sure to give the user "telegraf" the rights to use this script. You can place the script in /home/telegraf/avucheck and chmod telegraf:telegraf avucheck.py

Telegraf configuration:

	[[inputs.exec]]
	commands = ["/home/telegraf/avucheck/avucheck.py"]
	timeout = "5s"
	name_suffix = "_avucheck"
	data_format = "influx"
