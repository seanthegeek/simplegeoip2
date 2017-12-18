#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

"""Returns IP address ownership and location information based on MaxMind's GeoLite databases"""

from os import path
from collections import OrderedDict
from argparse import ArgumentParser
import json

import geoip2.database


__version__ = "1.0.0"


class GeoIP:
    """
    A simple interface to the free MaxMind GeoLite2 databases
    """
    def __init__(self, dbdir=None):
        """
        Initializes the interface
        Args:
            dbdir: A path to a directory containing GeoLite2-ASN.mmdb and GeoLite2-ASN.mmdb
        """
        if dbdir:
            self.dbdir = dbdir
        elif path.exists("/usr/local/share/GeoIP"):
            self.dbdir = "/usr/local/share/GeoIP"
        else:
            self.dbdir = "/usr/share/GeoIP"
        self.asndb = path.join(self.dbdir, "GeoLite2-ASN.mmdb")
        self.citydb = path.join(self.dbdir, "GeoLite2-City.mmdb")

    def lookup(self, ip_address):
        """
        Returns ownership and location information for the given IP address

        Notes:
            The latitude and longitude coordinates are for the city, not for the IP address

        Args:
            ip_address (str): The IP address to query for

        Returns:
            OrderedDict: A dictionary with the following keys: ``ip_address``, ``asn``, ``organization``,
            ``location_string``, ``city``, ``subdivision``, ``country`, `subdivision_iso``, ``country_iso``,
            ``latitude``, ``longitude``

        """
        with geoip2.database.Reader(self.asndb) as reader:
            asn_response = reader.asn(ip_address)
        with geoip2.database.Reader(self.citydb) as reader:
            city_response = reader.city(ip_address)

        asn = asn_response.autonomous_system_number
        organization = asn_response.autonomous_system_organization
        city = city_response.city.name
        subdivision = city_response.subdivisions.most_specific.name
        country = city_response.country.name
        subdivision_iso = city_response.subdivisions.most_specific.iso_code
        country_iso = city_response.country.iso_code
        latitude = city_response.location.latitude
        longitude = city_response.location.longitude
        location = []
        if city:
            location.append(city)
        if subdivision:
            location.append(subdivision)
        if country:
            location.append(country)
        location_string = ", ".join(location)

        results = OrderedDict([("ip_address", ip_address), ("asn", asn), ("organization", organization),
                               ("location_string", location_string), ("city", city), ("subdivision", subdivision),
                               ("country", country), ("subdivision_iso", subdivision_iso),
                               ("country_iso", country_iso), ("latitude", latitude), ("longitude", longitude)])

        return results


def _main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("ip_address", nargs="+", help="One or more IP addresses to look up")
    parser.add_argument("-d", "--database-directory", help="Overrides the path to the directory containing MaxMind "
                                                           "databases")
    parser.add_argument("-v", "--version", action="version", version=__version__)
    args = parser.parse_args()
    if len(args.ip_address) == 1:
        results = GeoIP(args.database_directory).lookup(args.ip_address[0])
    else:
        results = []
        for ip_address in args.ip_address:
            results.append(GeoIP(args.database_directory).lookup(ip_address))
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    _main()
