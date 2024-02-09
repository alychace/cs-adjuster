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
from gi.repository import Gio, GLib


interface_settings = Gio.Settings.new("org.gnome.desktop.interface")

color_scheme = interface_settings['color-scheme']

if color_scheme == "default" or color_scheme == "prefer-light":
    color_scheme = "prefer-dark"
else:
    color_scheme = "prefer-light"

interface_settings['color-scheme'] = color_scheme