import requests
import os
import json

# Get HUD API key
HUD_API_KEY = os.getenv('HUD_API_KEY')
HUD_AUTH_HEADER = {"Authorization": "Bearer {}".format(HUD_API_KEY)}
HUD_BASE_URL = "https://www.huduser.gov/hudapi/public/"

# Get list of states from HUD
response = requests.get("{}fmr/data/4843999999?year=2018".format(HUD_BASE_URL),
                 headers=HUD_AUTH_HEADER)
json_object = json.dumps(response.json(), indent=4)

if response.status_code == 200:
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)
else:
    print("Couldn't complete request. Status code: {}".format(response.status_code))
