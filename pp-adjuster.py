#!/usr/bin/env python3
# 
# Copyright (c) 2024 Aly Raffauf.
# 
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License 
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import os

def send_notification(summary, body, icon="dialog-information"):
    os.system(f'notify-send "{summary}" "{body}" -i {icon}')

if os.popen('powerprofilesctl get').read().strip() == "power-saver":
    os.system("powerprofilesctl set balanced")
elif os.popen('powerprofilesctl get').read().strip() == "balanced":
    os.system("powerprofilesctl set performance")
elif os.popen('powerprofilesctl get').read().strip() == "performance":
    os.system("powerprofilesctl set power-saver")

new_profile = os.popen('powerprofilesctl get').read().strip()

send_notification("Power Mode Changed", f"Power profile set to {new_profile}.", "dialog-information")
