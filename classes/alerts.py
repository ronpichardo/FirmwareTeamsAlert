import requests
import json
from time import strftime, localtime

class Teams:

  def __init__(self, baseUrl):
    self._baseUrl = baseUrl

  def send_notification(self, numOfUpdates):
    payload = {
      "@type": "MessageCard",
      "@context": "http://schema.org/extensions",
      "themeColor": "0076D7",
      "summary": "New Crestron Firmware",
      "sections": [{
        "activityTitle": "Crestron Firmware",
        "activitySubtitle": "New Firmware Available",
        "facts": [{
            "name": "Updates found",
            "value": numOfUpdates
        },{
            "name": "Time of alert",
            "value": strftime("%a, %d %b %Y %H:%M:%S", localtime())
        },{
            "name": "Status",
            "value": "New"
        }],
        "markdown": True
      }]
    }

    postMessage = requests.post(self._baseUrl, json=payload, headers={ 'Content-Type': 'application/json' })

    if postMessage.status_code != 200:
      print('Error posting message')
      return 'Exited with message num: %s' % postMessage.text

    if int(postMessage.text) != 1:
      return 'Message exited before posting with errorCode: %s' % postMessage.text

    return 'Message successfully posted!'