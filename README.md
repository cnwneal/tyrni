Tyrni
=====

Goal: Read Google Calendar events from a Raspberry Pi, send notifications via an Arduino with attached vibe board, RGB LED and piezo speaker.

Design
======

Grab XML from the Google Calendar "Private Address", parse it out into events that use the Arduino for notification.

libraries
=========
- [Google's api client library](https://developers.google.com/api-client-library/python/start/installation)

prototypes
==========
When developing I write a small program that demonstrates a new features on its own.

- moodclock.py - Setting RGB values over a serial connection

What does the name Tyrni mean?
=============
[Darius Bacon](https://github.com/darius/) said a Raspberry Pi project should be named after a berry.
[Tyrni](http://fi.wikipedia.org/wiki/Tyrni) is the Finnish name for the memorable [Sea Buckthorn berry](http://en.wikipedia.org/wiki/Hippophae_rhamnoides) I tried when I lived in Finland.

TODO
=====
look into using a starfleet insignia as piezo sensor
