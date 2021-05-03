from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db
import csv
import googlemaps
import json
import time

bp = Blueprint('maps', __name__)

@bp.route('/')
@login_required
def index():

    camera_locations = []
    with open("static/geocodedCameraLocations.json") as json_file:
        json_reader = json.load(json_file)
        item_count = 0
        for item in json_reader:
            #print(f'\tfID: {row[2]}, Address: {row[3]}, Direction: {row[4]}')
            camera_locations.append(item)
            item_count += 1
        #print(f'Processed {item_count} lines.')
        #print(camera_locations)
        json_file.close()

    return render_template('maps/googlemaps.html', cameraDB=(camera_locations))

# this only needs to be done once each time the database is updated.
# this method will overwrite "static/geocodedCameraLocations.json"
def geocode_addresses():
    gmaps = googlemaps.Client(key='AIzaSyDva4m0Xpx3yLGnBHUzzSm2IgTPKuhmMiM')

    camera_locations = []
    with open("static/Fixed_Speed_Cameras.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                #if ((line_count % 10) == 0): # google geocode has a cooldown on the amount of calls in 1 second.
                #        time.sleep(1)
                #print(f'\tfID: {row[2]}, Address: {row[3]}, Direction: {row[4]}')
                geocode_result = gmaps.geocode(row[3])
                lat = geocode_result[0]["geometry"]["location"]["lat"]
                lon = geocode_result[0]["geometry"]["location"]["lng"]
                camera_locations.append([row[2], lat, lon, row[4]])
                line_count += 1
        csv_file.close()

    with open("static/geocodedCameraLocations.json", 'w') as geoJson:
        json.dump(camera_locations, geoJson)
    print("DONE UPDATING CAMERA LOCATION DATABASE")

@bp.route('/aboutus', methods=('GET', 'POST'))
@login_required
def aboutus():
    return render_template('maps/aboutus.html')

@bp.route('/roadopinion', methods=('GET', 'POST'))
@login_required
def roadopinion():
    return render_template('maps/roadopinion.html')