# Import the dependencies.
from flask import Flask, jsonify, render_template
import datetime as dt
from datetime import datetime, timedelta
import pandas as pd
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
        f"<a href='/api/v1.0/tobs'>/api/v1.0/tobs</a><br/>"
        f"<a href='/api/v1.0/tstats/&lt;start&gt;'>/api/v1.0/tstats/&lt;start&gt;</a><br/>"
        f"<a href='/api/v1.0/tstats/&lt;start&gt/&lt;end&gt;'>/api/v1.0/tstats/&lt;start&gt/&lt;end&gt;</a><br/>"
    )

#################################################
# API Routes (back end)
#################################################


#/api/v1.0/0/precipitation : 
# Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value
# Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation")
def precipitation_dictionary():
    session = Session(engine)
    
    #logic from Jupyter notebook queries
    most_recent_date_str = session.query(func.max(Measurement.date)).scalar()
    most_recent_date = datetime.strptime(most_recent_date_str, '%Y-%m-%d').date()
    one_year_prior_date = most_recent_date - timedelta(days=365)
    
    date_and_precip_scores = session.query(
        Measurement.date, 
        Measurement.prcp
        ).filter(
            Measurement.date >= one_year_prior_date
            ).all()
    
    #for loop to create precipitation dictionary
    precipitation_dict = {}
    for date, prcp in date_and_precip_scores:
        date_format = datetime.strptime(date, '%Y-%m-%d').date().strftime('%Y-%m-%d') #have to reconvert datetime to different type of datetime
        precipitation_dict[date_format] =prcp
    
    session.close()
    # Return JSON representation of the dictionary
    return jsonify(precipitation_dict)

#/api/v1.0/stations : 
# Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def station_list():
    session = Session(engine)
    stations = session.query(Station.station).all()
    station_list = [station[0] for station in stations] #list comprehension to take all stations and pull the first one as the station list name
    session.close()
    return jsonify(station_list)

#/api/v1.0/tobs : 
#Query the dates and temperature observations of the most-active station for the previous year of data.
#Return a JSON list of temperature observations for the previous year.
@app.route("/api/v1.0/tobs")
def tobs_list():
    session = Session(engine)
 # Logic from the Jupyter file
    most_recent_date_str = session.query(func.max(Measurement.date)).scalar()
    most_recent_date = datetime.strptime(most_recent_date_str, '%Y-%m-%d').date()
    one_year_prior_date = most_recent_date - timedelta(days=365)
    
    # Query for the most active station
    activity_of_stations = session.query(Measurement.station, func.count(Measurement.station)) \
                                 .filter(Measurement.date >= one_year_prior_date) \
                                 .group_by(Measurement.station) \
                                 .order_by(func.count(Measurement.station).desc()) \
                                 .all()

    # Most active station
    max_station = activity_of_stations[0][0]

    # Query temperature data for the most active station
    temperature_data = session.query(Measurement.date, Measurement.tobs) \
                              .filter(Measurement.station == max_station) \
                              .filter(Measurement.date >= one_year_prior_date) \
                              .all()

    # Prepare JSON response
    tobs_data = []
    for date, tobs in temperature_data:
        tobs_data.append({
            "date": date,
            "tobs": tobs
        })

    session.close()
    return jsonify(tobs_data)

    # Return JSON representation of the dictionary
    return jsonify(tobs_data)

#/a pi/v1.0/<cstart> and /api/v1.0/<cstart>/<end>
# Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
# For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
# For a specified start dateand end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

#PT1- start only 
@app.route("/api/v1.0/tstats/<start_date>")
@app.route("/api/v1.0/tstats/<start_date>/<end_date>")
def tstats(start_date, end_date=dt.date(dt.MAXYEAR,12,31)):
    session = Session(engine)
    result = session.query(
                    func.min(Measurement.tobs), 
                    func.avg(Measurement.tobs), 
                    func.max(Measurement.tobs))\
        .filter(Measurement.date >= start_date)\
        .filter(Measurement.date <= end_date)\
        .first()
    session.close()
    return jsonify(list(result))

#############################
# prevents from running unless this is named app.py
if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)