## Konnected Python library

This is a simple Python library to talk to a Konnected device. Konnected is an open-source software for ESP8266 devices
that enables simple wired binary sensors and actuators to talk to home automation frameworks such as Home Assistant and
SmartThings. The most popular use case for Konnected is to connected a wired home alarm system to your Smart Home hub.

This library was written to support Home Assistant integration.

For more information see [konnected.io](https://konnected.io)

## Usage

```
>>> import konnected

''' initialize the Konnected client with a host and port '''
>>> k = konnected.Client('192.168.86.10', '17000')


''' sync settings to the device
k.put_settings([{"pin":1}],[],'secureToken','http://example.com')

```