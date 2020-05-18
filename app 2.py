{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Importing dependences I also needed to add the date time dependences from the climate_starter\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func\n",
    "import datetime as dt\n",
    "from flask import Flask, jsonify\n",
    "import datetime as dt \n",
    "from datetime import timedelta\n",
    "from datetime import date"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Using the previous information from the climate starter I can use that information to create my api \n",
    "\n",
    "# database creation\n",
    "\n",
    "engine = create_engine(\"sqlite:///Resources/hawaii.sqlite\")\n",
    "\n",
    "# database reflection\n",
    "\n",
    "base = automap_base()\n",
    "base.prepare(engine, reflect = True)\n",
    "\n",
    "# save reference\n",
    "\n",
    "measurement = base.classes.measurement \n",
    "station = base.classes.station\n",
    "\n",
    "session = Session(engine)\n",
    "\n",
    "final_date = session.query(measurement.date).order_by(measurement.date.desc()).first()\n",
    "\n",
    "final_date_df = pd.to_datetime(final_date[0])\n",
    "\n",
    "previous_year = final_date_df - pd.Timedelta(days=365)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Flask creation \n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# route configuration\n",
    "\n",
    "@app.route(\"/\")\n",
    "\n",
    "def index():\n",
    "    return(\n",
    "        f\"Here are your routes<br/>\"\n",
    "        f\"Here is the route for precipitation: /api/v1.0/precipitation<br/>\"\n",
    "        f\"Here is the route for stations:/api/v1.0/stations<br/>\"\n",
    "        f\"Here is the route for tobs: /api/v1.0/tobs<br/>\"\n",
    "        f\"Data breakdown from start date: /api/v1.0/start<br/>\"\n",
    "        f\"Data breakdown from given dates: /api/v1.0/dates<br/>\"\"\n",
    "    )\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unexpected EOF while parsing (<ipython-input-4-bb4f83f6698e>, line 11)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-4-bb4f83f6698e>\"\u001b[0;36m, line \u001b[0;32m11\u001b[0m\n\u001b[0;31m    return jsonify(pricipitation_data\u001b[0m\n\u001b[0m                                     ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m unexpected EOF while parsing\n"
     ]
    }
   ],
   "source": [
    "@app.route(\"/api/v1.0/precipitation\")\n",
    "def pricipitation():\n",
    "    session = Sessions(engine)\n",
    "    results = session.query(measurement.prcp, measuremnt.date).filter(measurement.date >= final_date).all()\n",
    "    session.close()\n",
    "    for date, prcp in results:\n",
    "        pricipitation_dict = {}\n",
    "        pricipitation_dict[\"prcp\"] = prcp\n",
    "        pricipitation_dict[\"date\"] = date\n",
    "        pricipitation_data.append(prcp_dict)\n",
    "    return jsonify(pricipitation_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/api/v1.0/stations\")\n",
    "\n",
    "def stations():\n",
    "    results = session.query(station.name, measurement.station).filter(station.station == measurement.station).group_by(station.name).all()\n",
    "    stations_list =list(np.ravel(stations_search))\n",
    "    return jsonify(station_list)\n",
    "    session.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/api/v1.0/tobs\")\n",
    "\n",
    "def tobservations():\n",
    "    results = session.query(measurement.date, measurement.tobs).filter(measurement.date).filter(measurement.date > final_fate).filter(Station.name=='WAIHEE 837.5, HI US').all()\n",
    "    session.close()\n",
    "    tobs_list = list(np.ravel(tob_search))\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/api/v1.0/start\")\n",
    "\n",
    "def start():\n",
    "    first_date = dt.datetime.strptime(start, '%Y-%m-%d')\n",
    "    session = Session(engine)\n",
    "    temperature = session.query(func.min(measurement.tobs),func.avg(measurement.tobs),func.max(measurement.tobs).filter(measurement.date >= start_date)).all()\n",
    "    all_temp = []\n",
    "    for TMIN, TAVG, TMAX in temp:\n",
    "        temperature_dict = {}\n",
    "        temperature_dict[\"TMIN\"] = temp[0][0]\n",
    "        temperature_dict[\"TAVG\"] = temp[0][1]\n",
    "        temperature_dict[\"TMAX\"] = temp[0][1]\n",
    "        temperature_collection.append(temp_dict)\n",
    "    return jsonify(temperature_collection)\n",
    "session.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "keyword can't be an expression (<ipython-input-14-b616bea648f3>, line 4)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-14-b616bea648f3>\"\u001b[0;36m, line \u001b[0;32m4\u001b[0m\n\u001b[0;31m    results = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.date = start).filter(measurement <= end).all())\u001b[0m\n\u001b[0m                                                                                            ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m keyword can't be an expression\n"
     ]
    }
   ],
   "source": [
    "@app.route(\"/api/v1.0/dates\")\n",
    "\n",
    "def temp_at_dates(start, end):\n",
    "#     results = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.date = start).filter(measurement <= end).all())\n",
    "#     session.close()\n",
    "#     temp_at_dates_data = []\n",
    "#     for temp in results:\n",
    "#         temp_at_dates_dict = {}\n",
    "#         temp_at_dates_dict[\"Start Date\"] = start\n",
    "#         temp_at_dates_dict[\"End Date\"] = end\n",
    "#         temp_at_dates_dict[\"Min Temperature\"] = temp.min\n",
    "#         temp_at_dates_dict[\"Avg Temperature\"] = temp.avg\n",
    "#         temp_at_dates_dict[\"Max Temperature\"] = temp.max\n",
    "#         temp_at_dates_data.append(temp_at_dates_dict)\n",
    "#     return jsonify(temp_at_dates_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
