#!/usr/bin/env python

import sys
import os
import math
from time import sleep

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/pygarmin")
from pygarmin import garmin, link

phys = link.SerialLink("/dev/sensors/garmin_gps")
gps = garmin.Garmin(phys)

gps.pvt_on()

while True:
    try:
        data = gps.get_pvt()

        alt = getattr(data, 'alt', 'N/A')
        posn = getattr(data, 'posn', [None, None])
        lat = posn[0]
        lon = posn[1]

        if lat is not None and lon is not None:
            lat_deg = lat * 180 / math.pi
            lon_deg = lon * 180 / math.pi
            print(f"Lat: {lat_deg}\nLon: {lon_deg}\nAlt: {alt}\n")
        else:
            print(f"Lat: N/A\nLon: N/A\nAlt: {alt}\n")

        gps.get_pvt()

    except Exception as e:
        print(f"Unexpected error: {e}")

    sleep(1.0)
