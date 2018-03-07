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

  def get_device(self, pin=None):
    ''' Query the status of a specific pin (or all configured pins if pin is ommitted) '''
    url = self.base_url + '/device'
    r = requests.get(url, params = {'pin':pin}, timeout = 30)
    return r.json()

  def get_status(self):
    ''' Query the device status. Returns JSON of the device internal state '''
    url = self.base_url + '/status'
    r = requests.get(url, timeout = 30)
    return r.json()

  def put_device(self, pin, state, momentary=None, times=None, pause=None):
    ''' Actuate a device pin '''
    url = self.base_url + '/device'

    payload = {
      "pin": pin,
      "state": state
    }

    if momentary is not None:
      payload["momentary"] = momentary

    if times is not None:
      payload["times"] = times

    if pause is not None:
      payload["pause"] = pause

    r = requests.put(url, json=payload, timeout = 30)
    return r.ok

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
