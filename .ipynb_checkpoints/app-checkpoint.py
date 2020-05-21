#Importing dependences I also needed to add the date time dependences from the climate_starter
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from flask import Flask, jsonify
import datetime as dt 
from datetime import timedelta
from datetime import date
# -------------------------------------------------------------------
# Using the previous information from the climate starter I can use that information to create my api 

# database creation

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# database reflection

base = automap_base()
base.prepare(engine, reflect = True)

# save reference

measurement = base.classes.measurement 
station = base.classes.station

session = Session(engine)

final_date = session.query(measurement.date).order_by(measurement.date.desc()).first()

final_date_df = pd.to_datetime(final_date[0])

previous_year = final_date_df - pd.Timedelta(days=365)

# Flask creation 

app = Flask(__name__)

# route configuration
# -------------------------------------------------------------------
@app.route("/")

def index():
    return(
        f"Here are your routes<br/>"
        f"Here is the route for precipitation: /api/v1.0/precipitation<br/>"
        f"Here is the route for stations:/api/v1.0/stations<br/>"
        f"Here is the route for tobs: /api/v1.0/tobs<br/>"
        f"Data breakdown from start date: /api/v1.0/start<br/>"
        f"Data breakdown from given dates: /api/v1.0/dates<br/>"
    )
# -------------------------------------------------------------------
@app.route("/api/v1.0/precipitation")
def pricipitation():
    session = Session(engine)
    results = session.query(measurement.prcp, measuremnt.date).filter(measurement.date >= final_date).all()
    session.close()
    for date, prcp in results:
        pricipitation_dict = {}
        pricipitation_dict["prcp"] = prcp
        pricipitation_dict["date"] = date
        pricipitation_data.append(prcp_dict)
    return jsonify(pricipitation_data
# -------------------------------------------------------------------
@app.route("/api/v1.0/stations")
def station():
    session = Session(engine)
    results = session.query(station.name, measurement.station).filter(station.station == measurement.station).group_by(station.name).all()
    stations_list =list(np.ravel(stations_search))
    return jsonify(station_list)
    session.close()
# -------------------------------------------------------------------
@app.route("/api/v1.0/tobs")
def tobservations():
    session = Session(engine)
    results = session.query(measurement.date, measurement.tobs).filter(measurement.date).filter(measurement.date > final_fate).filter(Station.name=='WAIHEE 837.5, HI US').all()
    session.close()
    tobs_list = list(np.ravel(tob_search))
# -------------------------------------------------------------------            
@app.route("/api/v1.0/start")
def start():
    first_date = dt.datetime.strptime(start, '%Y-%m-%d')
    session = Session(engine)
    temperature = session.query(func.min(measurement.tobs),func.avg(measurement.tobs),func.max(measurement.tobs).filter(measurement.date >= start_date)).all()
    all_temp = []
    for TMIN, TAVG, TMAX in temp:
        temperature_dict = {}
        temperature_dict["TMIN"] = temp[0][0]
        temperature_dict["TAVG"] = temp[0][1]
        temperature_dict["TMAX"] = temp[0][1]
        temperature_collection.append(temp_dict)
    return jsonify(temperature_collection)
session.close()
# -------------------------------------------------------------------                  
@app.route("/api/v1.0/dates")
def temp_at_dates(start, end):
    session = Session(engine)
    results = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.date = start).filter(measurement <= end).all())
    session.close()
    temp_at_dates_data = []
    for temp in results:
        temp_at_dates_dict = {}
        temp_at_dates_dict["Start Date"] = start
        temp_at_dates_dict["End Date"] = end
        temp_at_dates_dict["Min Temperature"] = temp.min
        temp_at_dates_dict["Avg Temperature"] = temp.avg
        temp_at_dates_dict["Max Temperature"] = temp.max
        temp_at_dates_data.append(temp_at_dates_dict)
    return jsonify(temp_at_dates_data)
# -------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
            
