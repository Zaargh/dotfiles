#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from tools import *

from pythonwifi.iwlibs import Wireless
import re

interface = 'wlp3s0'
wifi = Wireless(interface)

ic = icon('') # TODO: scanning icon?
text = wifi.getEssid()

print("%s %s" % (ic, pango(text)))
