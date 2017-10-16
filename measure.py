#!/usr/bin/env python

import googlemaps
from datetime import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
        "-r", "--reverse", 
        help="check route to home instead of from home", 
        action="store_true"
        )
args = parser.parse_args()

import private
gmaps = googlemaps.Client(key=private.API_KEY)

LOG_FMT="%Y-%m-%d %H:%M:%S"

with open(private.logFileName, "a") as logFile:
    for route, waypoints in private.homeToOfficeWaypoints.iteritems():
        origin = private.homeAddress
        destination = private.officeAddress
        via = ['via:'+w for w in waypoints]
        if args.reverse:
            origin = private.officeAddress
            destination = private.homeAddress
            via = list(reversed(via))

        now = datetime.now()
        directionsResult = gmaps.directions(
                origin,
                destination,
                mode="driving",
                waypoints=via,
                departure_time=now)
        
        #TODO: What if the JSON doesn't contain the entry
        durationWithTraffic = directionsResult[0]['legs'][0]['duration_in_traffic']['value']

        logFile.write("%s\t%s\t%s\t%d\n" % (
            now.strftime(LOG_FMT), 
            "from_home" if not(args.reverse) else "to_home",
            route, 
            durationWithTraffic
            ))

        #TODO: Store the actual route for testing 
        #print directionsResult[0]['overview_polyline']['points']
