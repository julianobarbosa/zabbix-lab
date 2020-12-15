import json
import logging
import random
import sys
from importlib import import_module
from time import sleep

import requests
from faker import Faker

# Logging setting for docker containers
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger('glpi-provisioning')

# Install pyzabbix with pip module
# try:
#     import_module('Faker')
# except ImportError:
#     import pip
#     pip.main(['install', 'Faker'])
# finally:
#     globals()['faker'] = import_module('Faker')


# Zabbix default credentials
GLPI_URL = "http://zabbix-lab.docker.internal:8082/apirest.php"
GLPI_USERNAME = 'zabbix-api'
GLPI_PASSWORD = 'jM&H25T%girH7pce5P*E'
GLPI_API_TOKEN = 'MIBN9JQoI10q6KTF2sP33DD0rKDFl54fvbFyKshW'
GLPI_APP_TOKEN = 'N8Xl0hHs6XLIHqyz0Nr0lJsA8n5C0sxR60hZTNG4'
GLPI_PERSONAL_TOKEN = '9X7Ewyhp8qU5i6L67aygpi27SRW0UYZS0QchLkGN'
GLPI_AUTH = (f'{GLPI_USERNAME}', f'{GLPI_PASSWORD}')

URL_ENTITY = GLPI_URL + '/Entity/'
URL_INIT = GLPI_URL + '/initSession/'
URL_TICKET = GLPI_URL + '/Ticket/'
URL_COMPUTER = GLPI_URL + '/Computer/'
URL_CONTRACT = GLPI_URL + '/Contract/'
URL_CONTRACT_TYPE = GLPI_URL + '/ContractType/'


def do_create_entity():
    payload = {}
    for _ in range(100):
        payload = {
            "input": {
                "name": f"{faker.company()}",
                "address": f"{faker.address()}",
                "comments": f"{faker.text()}",
                "phonenumber": f"{faker.phone_number()}",
                "fax": f"{faker.phone_number()}",
                "url": f"{faker.url()}",
                "email": f"{faker.email()}",
                "postcode": f"{faker.postcode()}",
                "state": f"{faker.state_abbr()}",
                "town": f"{faker.city()}"
            }
        }

        response = requests.post(URL_ENTITY, headers=headers, json=payload)
        print(response)


def do_create_computer():
    payload = {}
    for _ in range(100):
        payload = {
            "input": {
                "name": f"{faker.name()}",
                "entities_id": f"{random.randint(1,100)}"
            }
        }

        response = requests.post(URL_COMPUTER, headers=headers, json=payload)
        print(response)


# Wait for zabbix-frontend container to be available
frontend_available = False
while frontend_available is False:
    try:
        logger.info('Trying to connect to glpi-frontend')
        headers = {
            "App-Token": f"{GLPI_APP_TOKEN}",
            "Content-Type": "application/json"
        }
        login = requests.get(URL_INIT, auth=GLPI_AUTH, headers=headers)
        data = login.json()
        SESSION_TOKEN = data["session_token"]
        frontend_available = True

        logger.info("Connected to glpi-frontend")
    except Exception:
        logger.info('Waiting 5 secs for glpi-frontend to be available')
        sleep(5)

# Insert Entities
headers = {
    "Session-Token": SESSION_TOKEN,
    "App-Token": GLPI_APP_TOKEN,
    "Content-Type": "application/json"
}

faker = Faker('pt_BR')
logger.info('Create Entity')
# do_create_entity()

logger.info('Create Computer')
do_create_computer()
exit(0)


