{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
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
   "cell_type": "raw",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 25,
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
   "execution_count": 28,
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
    "        f\"Data breakdown from end date: /api/v1.0/end<br/>\"\n",
    "    )\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/api/v1.0/precipitation<br/>\")\n",
    "def prcp():\n",
    "    session = Sessions(engine)"
   ]
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
