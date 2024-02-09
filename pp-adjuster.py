#!/usr/bin/env python3

import os
import gi.repository
gi.require_version('Notify', '0.7')
from gi.repository import Notify

Notify.init("Power Profile Adjuster")

if os.popen('powerprofilesctl get').read().strip() == "power-saver":
    os.system("powerprofilesctl set balanced")
elif os.popen('powerprofilesctl get').read().strip() == "balanced":
    os.system("powerprofilesctl set performance")
elif os.popen('powerprofilesctl get').read().strip() == "performance":
    os.system("powerprofilesctl set power-saver")


new_profile = os.popen('powerprofilesctl get').read().strip()

Notify.Notification.new("Power profile set to " + new_profile).show()
