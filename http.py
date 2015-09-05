from flask import Flask, render_template, send_from_directory
import json
import requests

app = Flask(__name__)

# Provide username, password and the subdomain of your ZenDesk instance.
username = ""
password = ""
subdomain = ""
currentUrl = "https://" + subdomain + ".zendesk.com/api/v2/channels/voice/stats/current_queue_activity.json"
historicURL = "https://" + subdomain + ".zendesk.com/api/v2/channels/voice/stats/historical_queue_activity.json"

def callsCurrent(url,username,password):
	'''
	make call to zendesk to get current queue info and return output
	'''
	r = requests.get(url, auth=(username,password))
	if r.status_code == 200:
		#print r.text
		return r.json()
	else:
		print "Connection Failed"


def callsHistoric(url,username,password):
	'''
	make call to zendesk to get historical queue info
	'''
	r = requests.get(url, auth=(username,password))
	if r.status_code == 200:
		return r.json()
	else:
		print "Connection Failed"


@app.route("/")
def template_test():
    return render_template('content.html', currentQueue = callsCurrent(currentUrl, username, password), 
    	historicQueue = callsHistoric(historicURL, username, password))

if __name__ == "__main__":
    app.run()
