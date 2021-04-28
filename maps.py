from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db
import csv

bp = Blueprint('maps', __name__)

@bp.route('/')
@login_required
def index():

    camera_locations = []
    with open("static/Fixed_Speed_Cameras.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                #print(f'\tfID: {row[2]}, Address: {row[3]}, Direction: {row[4]}')
                camera_locations.append([row[2], row[3], row[4]])
                line_count += 1
        #print(f'Processed {line_count} lines.')
        #print(camera_locations)

    return render_template('maps/googlemaps.html', cameraDB=(camera_locations))

@bp.route('/aboutus', methods=('GET', 'POST'))
@login_required
def aboutus():
    return render_template('maps/aboutus.html')