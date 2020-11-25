import requests
from bs4 import BeautifulSoup as soup
import os, json, sys

from classes.Teams import Teams

main_url = 'https://www.crestron.com/Support/Search-Results?c=4'
my_devices = ['NVX', 'CP3', 'CP3N', 'RMC3', 'PRO3', 'AV3', 'CP4', 'CP4N', 'MC4']

s = requests.Session()

# Open the configuration file to then copy the teamsUri and check last updated date
with open('config.json') as json_data:
  config = json.load(json_data)

  todays_date = config['lastUpdated']
  teamUri = config['teamsUri']

# print(todays_date)
alertTeam = Teams(teamUri)

init_request = s.get(main_url)
fwsource = soup(init_request.text, 'lxml')
devices = fwsource.findAll('div', 'search-result')

device_firmwares = []
firmware_date = devices[0].find('p', 'resource-search-date').text.strip()

# We check that if our last date is not equal to the latest update on the website
# it will save the new date from the website.  If the dates are the same, we do nothing
# and simply exit the script and print no new updates found to the console
if config['lastUpdated'] != firmware_date:
  # Changes the lastUpdated feild in the config file to the new date found on the website
  config['lastUpdated'] = firmware_date

  # Re-open the file so that we can write our previous file with the new updated firmware date
  updateFile = open('config.json', 'w')
  updateFile.write(json.dumps(config, indent=4))
  updateFile.close()

else:
  print('No new updates found')
  sys.exit(0)

updated_devices = []
send_to_teams = []

# The response we get back from parsing Crestron is a list, so we need to create a for loop
# and then find the tags necessary for our finds.
for device in devices:
  # Example output of device_name is 'DM‐NVX‐D80‐IOAV 4.1.4472.00024_r381143'
  device_name = device.find('div', 'resource-search-name').text.strip()
  fwDate = device.find('p', 'resource-search-date').text.strip()

  # save the results to another list with just the device names from the 
  # resource-search-name tag
  updated_devices.append(device_name)

# Loop through each of our devices to check against the recently found updates
for owned in my_devices:
  # Loop through the updates that were found
  for updated in updated_devices:

    # There are Home devices which include a '-R' in the name, ex CP4-R
    # Enterprises dont utilize Home devices, so we ignore those updates
    if owned in updated:
      if '-R' in updated:
        pass
      else:
        # At the moment, we will add the found devices to a list
        # This can be output to a file with the device/firmware version to view
        # locally
        send_to_teams.append(owned)
        # We also print out to the console the updates that was found
        print('Update found: ' + updated)


# if we found devices that matched what we are searching for
# a Notification will be sent to the channel that the Microsoft Teams Webhook was added to
if len(send_to_teams) > 0 and teamUri != "":
  alertResult = alertTeam.sendNotification(len(send_to_teams))
  print(alertResult)