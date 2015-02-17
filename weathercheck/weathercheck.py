# Python script to set a Playbulb LED colour based on the current weather.
# Run me as a cron job for ambient weather information!
# by Ian Renton
# https://github.com/ianrenton/playbulb-tools
# Uses python OpenWeatherMap wrapper from https://github.com/csparpa/pyowm

import pyowm, re, subprocess

#### Config ####

# Your location
LOCATION = 'London'

# Your Playbulb address (obtained with 'sudo hcitool lescan')
PLAYBULB_ADDRESS = '01:23:45:67:89:10'

# Weather to colour dict
COLOUR_MAP = { 'clear': 'FFFF6000',
               'clouds': '80000000',
               'rain': '000000FF',
               'drizzle': '0000FFFF',
               'snow': 'FFFFFFFF',
               'thunderstorm': '80FF0000'}

#### Code below ####

# Show the name of the playbulb
proc = subprocess.Popen(('gatttool -b ' + PLAYBULB_ADDRESS + ' --char-read -a 0x0003').split(), stdout = subprocess.PIPE)
for line in iter(proc.stdout.readline,''):
  name = ''.join(x.strip() for x in re.findall(r'[0-9a-f]{2}\s', line)).decode("hex")
  print 'Playbulb name: ' + name

# Get weather forecast
weather = pyowm.OWM().weather_at_place(LOCATION).get_weather().get_status()
colour = COLOUR_MAP[weather]
print 'Weather for ' + LOCATION + ': ' + weather + ', colour ' + colour

# Set Playbulb colour
subprocess.call(('gatttool -b ' + PLAYBULB_ADDRESS + ' --char-write -a 0x0016 -n ' + colour).split())
