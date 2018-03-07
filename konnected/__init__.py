''' Python library for interacting with Konnected devices '''
'''            learn more at konnected.io                 '''

__author__ = 'Nate Clark, Konnected Inc <help@konnected.io>'

import requests
import json
import os

from requests.exceptions import RequestException;

class Client(object):

  def __init__(self, host, port):
    self.host = host
    self.port = port
    self.base_url = 'http://' + host + ':' + port

  def put_settings(self, sensors, actuators, auth_token, endpoint):
    ''' Sync settings to the Konnected device '''
    url = self.base_url + '/settings'

    payload = {
      "sensors": sensors,
      "actuators": actuators,
      "token": auth_token,
      "apiUrl": endpoint
    }

    r = requests.put(url, json=payload, timeout = 30)

    return r.ok
