# Import the dependencies.
from flask import Flask, jsonify # , render_template
import datetime as dt

import sqlalchemy as sql
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import inspect


#################################################
# Database Setup
#################################################
engine = sql.create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
#session = Session(engine) # don't do this---- put this within each routing function-- local variable, each user = own private session

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# HTML Routes (front end)
#################################################
@app.route("/")
def home():
    """List of all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"<a href='/api/v1.0/precipitation'>/api/v1.0/precipitation</a><br/>"
        f"<a href='/api/v1.0/stations'>/api/v1.0/stations</a><br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/tstats/&lt;start&gt;<br/>"
        f"/api/v1.0/tstats/&lt;start&gt/&lt;end&gt;<br/>"

    )


#################################################
# API Routes (back end)
#################################################


#/api/v1.0/0/precipitation : 
# Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary 
#       using date as the key and prcp as the value
# Return the JSON representation of your dictionary.


#/api/v1.0/stations : 
# Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def station_list():
    session = Session(engine)
    fake_station_list = ["station1", "station2"]
    session.close()
    return jsonify(fake_station_list)

#/api/v1.0/tobs : 
#Query the dates and temperature observations of the most-active station for the previous year of data.
#Return a JSON list of temperature observations for the previous year.

#/api/v1.0/<cstart> and /api/v1.0/<cstart>/<end>
# Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
# For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
# For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.


#############################
# prevents from running unless this is named app.py
if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)