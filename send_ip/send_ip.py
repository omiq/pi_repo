import subprocess
import requests

# load API key from file
inFile = open('/home/pi/mailgun-api.txt', 'r')
api_key = inFile.readline().rstrip()
inFile.close()

# get host and IP
this_host = subprocess.check_output("hostname", shell=True).rstrip()
IP_line = subprocess.check_output("hostname -I", shell=True).rstrip()


# send via Mailgun
def send_message():
    return requests.post(
        "https://api.mailgun.net/v3/chrisg.mailgun.org/messages",
        auth=("api", api_key),
        data={"from": "Bot <pibot@chrisg.mailgun.org>",
              "to": ["chris@chrisg.com"],
              "subject": "MY IP: " + IP_line,
              "text": this_host + " = host and " + IP_line + " is my IP!"})

print send_message()
