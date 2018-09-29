# Python library for interacting with Konnected devices
# learn more at konnected.io

import requests
import json
import os

from requests.exceptions import RequestException;

__author__ = 'Nate Clark, Konnected Inc <help@konnected.io>'


class Client(object):

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.base_url = 'http://' + host + ':' + port

    def get_device(self, pin=None):
        """ Query the status of a specific pin (or all configured pins if pin is ommitted) """
        url = self.base_url + '/device'
        try:
            r = requests.get(url, params={'pin': pin}, timeout=10)
            return r.json()
        except RequestException as err:
            raise Client.ClientError(err)

    def get_status(self):
        """ Query the device status. Returns JSON of the device internal state """
        url = self.base_url + '/status'
        try:
            r = requests.get(url, timeout=10)
            return r.json()
        except RequestException as err:
            raise Client.ClientError(err)

    def put_device(self, pin, state, momentary=None, times=None, pause=None):
        """ Actuate a device pin """
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

        try:
            r = requests.put(url, json=payload, timeout=10)
            return r.json()
        except RequestException as err:
            raise Client.ClientError(err)

    def put_settings(self, sensors, actuators, auth_token, endpoint,
                     blink=None, discovery=None):
        """ Sync settings to the Konnected device """
        url = self.base_url + '/settings'

        payload = {
            "sensors": sensors,
            "actuators": actuators,
            "token": auth_token,
            "apiUrl": endpoint
        }

        if blink is not None:
            payload['blink'] = blink

        if discovery is not None:
            payload['discovery'] = discovery

        try:
            r = requests.put(url, json=payload, timeout=10)
            return r.ok
        except RequestException as err:
            raise Client.ClientError(err)

    class ClientError(Exception):
        """Generic Error."""
        pass

