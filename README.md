A small flask application to monitor the Voice Queue in Zendesk CRM

Edit the http.py to add your ZD username,password, and subdomain before launching.
You can also update the layout.html to add your logo to the top left.
img src="LOGO IMAGE URL"

There is also a meta-refresh tag in the layout.html that can be used to control 
the refresh rate of the page.  Each time the page is refreshed the script pulls
fresh data from the ZenDesk API.