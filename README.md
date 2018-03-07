## Konnected Python library

This is a simple Python library to talk to a Konnected device. Konnected is an open-source software for ESP8266 devices
that enables simple wired binary sensors and actuators to talk to home automation frameworks such as Home Assistant and
SmartThings. The most popular use case for Konnected is to connected a wired home alarm system to your Smart Home hub.

This library was written to support Home Assistant integration.

For more information see [konnected.io](https://konnected.io)

## Usage

```
>>> import konnected

# Initialize the Konnected client with a host and port.
# Every Konnected module uses a different HTTP port

>>> k = konnected.Client('192.168.86.10', '17000')

# Sync settings to the device

>>> k.put_settings([{"pin":1}],[],'secureToken','http://example.com')
True

# Get status of each input pin
>>> k.get_device()
[{'state': 0, 'pin': 1}, {'state': 1, 'pin': 2}]

# Get status of a single input pin

>>> k.get_device(2)
[{'state': 1, 'pin': 2}]

# Actuate an output pin

>>> k.put_device(pin=8, state=1)
{'state': 1, 'pin': 8}

# Get device status

>>> k.get_status()
{'mac': '2c:3a:e8:43:8a:38', 'gw': '192.168.86.1', 'hwVersion': '2.0.5', 'rssi': -31, 'nm': '255.255.255.0', 'ip': '192.168.86.10', 'actuators': [{'trigger': 1, 'pin': 8}], 'port': 12426, 'uptime': 2349, 'heap': 23904, 'swVersion': '2.1.3', 'sensors': [{'state': 0, 'pin': 1}]}

''' 
```

## Python version

This library was designed to work with Python 3. Parts may work with Python 2.7, but if it does it's totally accidental.