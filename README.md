# playbulb-tools
A bunch of scripts to do interesting things with Playbulb LED lights.

[Playbulbs](http://www.playbulb.com/en/index.html) are colour LED lights sold by a company called Mipow. They come with an iOS and Android app that can set their colour and various patterns using a Bluetooth 4.0 LE connection. There's no security on them whatsoever, so any nearby device can connect and change their colour. The protocol is [somewhat understood](https://pdominique.wordpress.com/2015/01/02/hacking-playbulb-candles/), so they can also be controlled programatically - for example, by the scripts here.

## mailcheck

A script that checks an IMAP mailbox at a defined interval, and will set the playbulb colour to red if there are no unread messages, or green (with a brief flash) when you have unread mail. Inspired by similar "ambient connected" devices like [Nabaztag](https://en.wikipedia.org/wiki/Nabaztag).

[Watch it in action here.](https://vimeo.com/119624218)
