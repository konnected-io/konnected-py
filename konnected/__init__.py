# Python library for interacting with Konnected devices
# learn more at konnected.io
import asyncio
import aiohttp
import json
import os

__author__ = 'Nate Clark, Konnected Inc <help@konnected.io>'

class Client(object):

    def __init__(self, host, port, websession):
        self.host = host
        self.port = port
        self.websession = websession
        self.base_url = 'http://' + host + ':' + port

    async def get_device(self, pin=None):
        """ Query the status of a specific pin (or all configured pins if pin is ommitted) """
        url = self.base_url + '/device'
        try:
            async with self.websession.get(url, params={'pin': pin}, timeout=10) as resp:
                return await resp.json()
        except (aiohttp.ClientError, asyncio.TimeoutError) as err:
            raise Client.ClientError(err)

    async def get_status(self):
        """ Query the device status. Returns JSON of the device internal state """
        url = self.base_url + '/status'
        try:
            async with self.websession.get(url, timeout=10) as resp:
                return await resp.json()
        except (aiohttp.ClientError, asyncio.TimeoutError) as err:
            raise Client.ClientError(err)

    async def put_device(self, pin, state, momentary=None, times=None, pause=None):
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
            async with self.websession.put(url, json=payload, timeout=10) as resp:
                return await resp.json()
        except (aiohttp.ClientError, asyncio.TimeoutError) as err:
            raise Client.ClientError(err)

    async def put_settings(self, sensors=[], actuators=[], auth_token=None,
                     endpoint=None, blink=None, discovery=None,
                     dht_sensors=[], ds18b20_sensors=[]):
        """ Sync settings to the Konnected device """
        url = self.base_url + '/settings'

        payload = {
            "sensors": sensors,
            "actuators": actuators,
            "dht_sensors": dht_sensors,
            "ds18b20_sensors": ds18b20_sensors,
            "token": auth_token,
            "apiUrl": endpoint
        }

        if blink is not None:
            payload['blink'] = blink

        if discovery is not None:
            payload['discovery'] = discovery

        try:
            async with self.websession.put(url, json=payload, timeout=10) as resp:
                return (resp.status >= 200 and resp.status < 300)
        except (aiohttp.ClientError, asyncio.TimeoutError) as err:
            raise Client.ClientError(err)

    class ClientError(Exception):
        """Generic Error."""
        pass

