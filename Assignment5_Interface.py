#!/usr/bin/python2.7
#
# Assignment5 Interface
# Name:
#

from pymongo import MongoClient
import os
import sys
import json
import math

def distance_calculator(lat1, lon1, lat2, lon2):
    pi_1 = math.radians(lat1)
    pi_2 = math.radians(lat2)
    delta_pi = math.radians(lat2-lat1)
    delta_lambda = math.radians(lon2-lon1)
    a = math.sin(delta_pi/2) * math.sin(delta_pi/2) + math.cos(pi_1) * math.cos(pi_2) * math.sin(delta_lambda/2) * math.sin(delta_lambda/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return 3959 * c

def FindBusinessBasedOnCity(cityToSearch, saveLocation1, collection):
    page = collection.find({'city': {'$regex':cityToSearch, '$options':"$i"}})
    output = open(saveLocation1, "w+")
    for line in page:
        output.write(line['name'].upper() + "$" + line['full_address'].replace("\n", ", ").upper() + "$" + line['city'].upper() + "$" + line['state'].upper() + "\n")
    output.close()

def FindBusinessBasedOnLocation(categoriesToSearch, myLocation, maxDistance, saveLocation2, collection):
    page = collection.find({'categories':{'$all': categoriesToSearch}}, {'name': 1, 'latitude': 1, 'longitude': 1, 'categories': 1})
    lat1, lon1 = float(myLocation[0]), float(myLocation[1])
    output = open(saveLocation2, "w+")
    for line in page:
        lat2, lon2 = float(line['latitude']), float(line['longitude'])
        d = distance_calculator(lat1, lon1, lat2, lon2)
        if maxDistance >= d:
            output.write(line['name'].upper() + "\n")
    output.close()


	



