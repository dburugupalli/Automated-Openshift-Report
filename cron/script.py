import logging
import json
import sys
import os
import urllib3
import requests
import json

token = os.environ['token']
api_url = os.environ['api_url']


headers = {
		'Authorization': 'Bearer ' + token, 
		'Accept': 'application/json', 
	  }

url = 'https://' + api_url + 'apis/route.openshift.io/v1/routes/'
print(url)

if __name__ == "__main__":

    #configuring logging files
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filemode='a')
    response = requests.get(url, headers=headers)
    print (response.json())
    json_data = json.loads(response.text)
    if response.status_code == 200:
        logging.debug(api_url + " is operational")
    else:
        logging.error(api_url + " IS NOT WORKING \n" + r.json)

