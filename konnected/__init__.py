"""Python library for interacting with Konnected devices."""
import asyncio
import aiohttp


__author__ = "Nate Clark, Konnected Inc <help@konnected.io>"


class Client:
    """API wrapper for Konnected Alarm Panels."""

    def __init__(self, host, port, websession):
        """Initialize the client connection."""
        self.throttle = asyncio.Semaphore(3)  # allow for 3 simultaneous reqs
        self.host = host
        self.port = port
        self.websession = websession
        self.base_url = "http://" + host + ":" + port

    async def get_status(self, retries=2):
        """Query the device status."""
        url = self.base_url + "/status"
        try:
            async with self.throttle:
                async with self.websession.get(url, timeout=3) as resp:
                    return await resp.json()
        except (aiohttp.ClientError, asyncio.TimeoutError) as err:
            if retries > 0:
                return await self.get_status(retries - 1)
            else:
                raise Client.ClientError(err)

    async def get_device(self, pin=None, retries=2):
        """Query the status of a specific pin (or all configured pins if pin is ommitted)."""
        url = self.base_url + "/device"
        try:
            async with self.throttle:
                async with self.websession.get(
                    url, params={"pin": pin}, timeout=3
                ) as resp:
                    return await resp.json()
        except (aiohttp.ClientError, asyncio.TimeoutError) as err:
            if retries > 0:
                return await self.get_device(pin, retries - 1)
            else:
                raise Client.ClientError(err)

    async def put_device(
        self, pin, state, momentary=None, times=None, pause=None, retries=2
    ):
        """Actuate a device pin."""
        url = self.base_url + "/device"

        payload = {"pin": pin, "state": state}

        if momentary is not None:
            payload["momentary"] = momentary

        if times is not None:
            payload["times"] = times

        if pause is not None:
            payload["pause"] = pause

        try:
            async with self.throttle:
                async with self.websession.put(url, json=payload, timeout=3) as resp:
                    return await resp.json()
        except (aiohttp.ClientError, asyncio.TimeoutError) as err:
            if retries > 0:
                return await self.put_device(
                    pin, state, momentary, times, pause, retries - 1
                )
            else:
                raise Client.ClientError(err)

    async def get_zone(self, zone=None, retries=2):
        """Query the status of a specific zone (or all configured zones if zones is ommitted)."""
        url = self.base_url + "/zone"
        try:
            async with self.throttle:
                async with self.websession.get(
                    url, params={"zone": zone}, timeout=3
                ) as resp:
                    return await resp.json()
        except (aiohttp.ClientError, asyncio.TimeoutError) as err:
            if retries > 0:
                return await self.get_zone(zone, retries - 1)
            else:
                raise Client.ClientError(err)

    async def put_zone(
        self, zone, state, momentary=None, times=None, pause=None, retries=2
    ):
        """Actuate a device zone."""
        url = self.base_url + "/zone"

        payload = {"zone": zone, "state": state}

        if momentary is not None:
            payload["momentary"] = momentary

        if times is not None:
            payload["times"] = times

        if pause is not None:
            payload["pause"] = pause

        try:
            async with self.throttle:
                async with self.websession.put(url, json=payload, timeout=3) as resp:
                    return await resp.json()
        except (aiohttp.ClientError, asyncio.TimeoutError) as err:
            if retries > 0:
                return await self.put_zone(
                    zone, state, momentary, times, pause, retries - 1
                )
            else:
                raise Client.ClientError(err)

    async def put_settings(
        self,
        sensors=[],
        actuators=[],
        auth_token=None,
        endpoint=None,
        blink=None,
        discovery=None,
        dht_sensors=[],
        ds18b20_sensors=[],
        retries=2,
    ):
        """Sync settings to the Konnected device."""
        url = self.base_url + "/settings"

        payload = {
            "sensors": sensors or [],
            "actuators": actuators or [],
            "dht_sensors": dht_sensors or [],
            "ds18b20_sensors": ds18b20_sensors or [],
            "token": auth_token,
            "apiUrl": endpoint,
        }

        if blink is not None:
            payload["blink"] = blink

        if discovery is not None:
            payload["discovery"] = discovery

        try:
            async with self.throttle:
                async with self.websession.put(url, json=payload, timeout=3) as resp:
                    return resp.status >= 200 and resp.status < 300
        except (aiohttp.ClientError, asyncio.TimeoutError) as err:
            if retries > 0:
                return await self.put_settings(
                    sensors,
                    actuators,
                    auth_token,
                    endpoint,
                    blink,
                    discovery,
                    dht_sensors,
                    ds18b20_sensors,
                    retries - 1,
                )
            else:
                raise Client.ClientError(err)

    class ClientError(Exception):
        """Generic Error."""
