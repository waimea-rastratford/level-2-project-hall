#===========================================================
# PROJECT NAME HERE
# By YOUR NAME HERE
#===========================================================

from flask import Flask, request, session, render_template, flash, redirect, send_file, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from datetime import datetime, timedelta
from os import getenv
from io import BytesIO
import html
from app.helpers import *


# Create the app
app = Flask(__name__)


#===========================================================
# App Routes Handlers
#===========================================================
def get_bookings(date):
    return next((item for item in bookings if item["date"] == date), None)






#-----------------------------------------------------------
# Home page - Show all notes
#-----------------------------------------------------------
def get_dates():
        today = datetime.now()
        weekday = today.weekday()
        monday = today - timedelta(days = weekday)
        weeks_to_show = 5
        days_to_show = weeks_to_show * 7

        first_day_to_show = monday
        last_day_to_show = monday + timedelta(days = days_to_show - 1)

        dates = []
        for i in range(days_to_show):
            day = first_day_to_show + timedelta(days = i)
            date = day.strftime("%Y-%m-%d")
            dates.append(date)

        return dates



#-----------------------------------------------------------
# Home page - Show all notes
#-----------------------------------------------------------
@app.get("/")
def show_home():

    today = datetime.now()
    weekday = today.weekday()
    monday = today - timedelta(days = weekday)
    weeks_to_show = 5
    days_to_show = weeks_to_show * 7

    first_day_to_show = monday
    last_day_to_show = monday + timedelta(days = days_to_show - 1)

    dates = []
    for i in range(days_to_show):
        day = first_day_to_show + timedelta(days = i)
        date = day.strftime("%Y-%m-%d")
        dates.append(date)

    with connect_db() as db:
        sql = """
            SELECT date
            FROM bookings
        """

        bookings = db.execute(sql).fetchall()

        return render_template("pages/home.jinja", bookings=bookings, dates=dates)



#-----------------------------------------------------------
# Page for each booking
#-----------------------------------------------------------
@app.get("/booking/<date>")
def show_booking(date):
    # booking= get_bookings(date)

    with connect_db() as db:
        sql = """
            SELECT
                people.id,
                people.name,
                people.phone_number,
                bookings.id,
                bookings.event,
                bookings.date
                
                FROM people
                JOIN bookings ON bookings.people_id = people.id
                WHERE bookings.date = ?
            
        """
        params = ()
        booking = db.execute(sql, (date,)).fetchone()
    
    return render_template("pages/booking.jinja", booking=booking)


#-----------------------------------------------------------
# Delete Booking
#-----------------------------------------------------------
@app.get("/booking/<date>/delete")
def delete_a_booking(date):
    # Delete the booking using its date
    with connect_db() as db:
        sql = """
            DELETE FROM bookings
            WHERE date = ?
        """
        params = (date,)
        db.execute(sql, params)

    flash("Booking deleted", "success")
    return redirect("/")


#-----------------------------------------------------------
# Page for each booking
#-----------------------------------------------------------
@app.get("/booking/create")

def create_bookings():
    dates = get_dates()

    with connect_db() as db:
        sql = """
            SELECT
                people.id,
                people.name,
                people.phone_number,
                bookings.id,
                bookings.event,
                bookings.date
                
                FROM people
                JOIN bookings ON bookings.people_id = people.id

            
        """
        params = ()
        booking = db.execute(sql).fetchall()
    
    return render_template("pages/create_booking.jinja", booking=booking, dates=dates)



# #-----------------------------------------------------------
# # Home page - Show all notes
# #-----------------------------------------------------------

@app.post("/booking/create")



def post_bookings():
    name = request.form.get("name")
    phone_number = request.form.get("phone_number")
    event = request.form.get("event")
    date = request.form.get("date")


    with connect_db() as db:
        sql = """
            INSERT INTO people (name, phone_number)
            VALUES (?, ?)
        """
        cursor = db.execute(sql, (name, phone_number))
       
        people_id = cursor.lastrowid


        sql = """
            INSERT INTO bookings (event, date, people_id)
            VALUES (?, ?, ?)
        """
        db.execute(sql, (event, date, people_id ))

    flash("Booking created successfully!")
    return redirect("/")



#===========================================================
# Configure the app
#===========================================================
load_dotenv()
app.config.from_prefixed_env()
init_logging(app)
init_text_filters(app)
init_date_filters(app)
init_error_handlers(app)
init_database()
register_commands(app)

