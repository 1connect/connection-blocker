#!/usr/bin/env python2

import sys
import subprocess

import GeoIP

VALID_COUNTRIES = ('DE', 'PL')
DATABASE = '/usr/share/GeoIP/GeoIP.dat'

if len(sys.argv) != 3:
    print("Usage:\n%s {service name} {ip}" % sys.argv[0])
    sys.exit(1)

SERVICE = sys.argv[1]
IP = sys.argv[2]

db = GeoIP.open(DATABASE, GeoIP.GEOIP_STANDARD)

country = db.country_code_by_addr(IP)

if country in VALID_COUNTRIES or country is None:
    sys.exit(0)
else:
    subprocess.call(
        ['logger', 'deny %s connection from %s (%s [%s])' % (SERVICE, IP, db.country_name_by_addr(IP), country)])
    sys.exit(1)
