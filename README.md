# playbulb-tools
A bunch of scripts to do interesting things with Playbulb LED lights.

[Playbulbs](http://www.playbulb.com/) are colour LED lights sold by a company called Mipow. They come with an iOS and Android app that can set their colour and various patterns using a Bluetooth 4.0 LE connection. There's no security on them whatsoever, so any nearby device can connect and change their colour. The protocol is [somewhat understood](https://pdominique.wordpress.com/2015/01/02/hacking-playbulb-candles/), so they can also be controlled programatically - for example, by the scripts here.

These scripts were inspired by protocol information found at [https://pdominique.wordpress.com/2015/01/02/hacking-playbulb-candles/](https://pdominique.wordpress.com/2015/01/02/hacking-playbulb-candles/) and [https://github.com/Phhere/Playbulb/](https://github.com/Phhere/Playbulb/).

They require a computer with a Bluetooth 4.0 Low Energy compatible device and the `hcitool`/`gattool` utilities installed. (Install the `bluez` package.) It also seems that only certain versions of gattool work properly ( see issue #1 ) &mdash; it's confirmed working in 4.101 but not in 5.28.

I found information on the 'undocumented' gattool non-interactive mode (which does seem to be somewhat documented in later versions) from http://www.humbug.in/2014/using-gatttool-manualnon-interactive-mode-read-ble-devices/

These scripts are tested on Ubuntu Linux (armhf) 14.04, but YMMV on Mac, Windows, other Linuxes etc.

## mailcheck

A script that checks an IMAP mailbox at a defined interval, and will set the playbulb colour to red if there are no unread messages, or green (with a brief flash) when you have unread mail. Inspired by similar "ambient connected" devices like [Nabaztag](https://en.wikipedia.org/wiki/Nabaztag).

[Watch it in action here.](https://vimeo.com/119624218)

## weathercheck

A script that polls OpenWeatherMap for weather data, and sets the colour of the bulb as an ambient weather indicator. This script has some other improvements, such as displaying the name of the Playbulb it connects to. It does not run forever but is a one-off designed to be run by a cron job.

Lesson learned today: the Playbulb candle sucks at yellow. Even with the official app the yellow is really unconvincing.
