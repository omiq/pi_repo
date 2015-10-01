import subprocess
import requests
api_key = "key-614vnkd0qgkscpq6mxon7wpfbzcb9j04"
this_host = subprocess.check_output("hostname", shell=True)
IP_line = subprocess.check_output("ifconfig | grep inet | grep -v 127.", shell=True)

def send_message():
    return requests.post(
        "https://api.mailgun.net/v3/chrisg.mailgun.org/messages",
        auth=("api", "key-614vnkd0qgkscpq6mxon7wpfbzcb9j04"),
        data={"from": "Bot <pibot@chrisg.mailgun.org>",
              "to": ["chris@chrisg.com"],
              "subject": "MY IP: " + IP_line,
              "text": this_host + " = host and " + IP_line + "is my IP!"})

print send_message()
