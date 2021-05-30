# FirmwareTeamsAlert
## Overview
Python script created to check the Crestron website for new firmwares.
Locates if a new firmware was found for the following device:
- NVX
- CP3, CP3N, CP4, CP4N
- AV3
- PRO3
- MC4
- RMC3

Example of the output if you do use the Microsoft Teams Alerting:
<img width="624" alt="Screen Shot 2021-01-11 at 8 21 45 AM" src="https://user-images.githubusercontent.com/63974878/104231294-bfe1dd00-541c-11eb-9443-35b46f2a7546.png">

Requirements:
a Webhook created in a Microsoft Teams Channel ,if no Microsoft Teams Webhook is in use, it will just print to the console
Instructions for integrating a webhook in Microsoft Teams can be found at this link:

https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/connectors-using#setting-up-a-custom-incoming-webhook

![TeamsWebhook](https://user-images.githubusercontent.com/63974878/104045437-8d31ad80-51ac-11eb-8959-5dee1928c00e.png)

## Installation
Python Version: 3.7
Required Libraries : Requests, lxml, BeautifulSoup4

For Mac/Linux

```shell
$ git clone https://github.com/ronpichardo/FirmwareTeamsAlert.git
$ cd FirmwareTeamsAlert
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

For Windows using Powershell

```shell
$ git clone https://github.com/ronpichardo/FirmwareTeamsAlert.git
$ cd FirmwareTeamsAlert
$ python3 -m venv venv
$ ./venv/bin/Activate.ps1
(venv) $ pip install -r requirements.txt
```

## Usage
Once you are inside your VirtualEnvironment, to confirm you're in venv, you should see (venv) in front of your shell
```shell
$ source venv/bin/activate
(venv) $ python main.py
```

You will see output to the screen notifying you of updated firmware if found, or non found.  The date will be saved in the config folder in order to track updates.
