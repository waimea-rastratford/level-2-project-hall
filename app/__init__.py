#===========================================================
# PROJECT NAME HERE
# By YOUR NAME HERE
#===========================================================

from flask import Flask, request, session, render_template, flash, redirect, send_file, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from os import getenv
from io import BytesIO
import html
from app.helpers import *


# Create the app
app = Flask(__name__)


#===========================================================
# App Routes Handlers
#===========================================================
def get_booking(date):
    return next((item for item in bookings if item["date"] == date), None)
#-----------------------------------------------------------
# Home page - Show all notes
#-----------------------------------------------------------
@app.get("/")
def show_home():
    with connect_db() as db:
        sql = """
            SELECT event, date, id
            FROM bookings
        """
        params = ()
        bookings = db.execute(sql, params).fetchall()
        return render_template("pages/home.jinja", bookings=bookings)



#-----------------------------------------------------------
# Home page - Show all notes
#-----------------------------------------------------------
@app.get("/booking/<date>")
def show_booking(date):
    booking = get_booking(date)
    
    return render_template("pages/booking.jinja", booking=booking)

 # with connect_db() as db:
    #     sql = """
    #         SELECT event, date, id
    #         FROM bookings
    #     """
    #     params = ()
    #     bookings = db.execute(sql, params).fetchall()
#====================



with connect_db() as db:
        sql = """
            SELECT event, date, id
            FROM bookings
        """
        params = ()
        bookings = db.execute(sql, params).fetchall()
# #-----------------------------------------------------------
# # Home page - Show all notes
# #-----------------------------------------------------------
# @app.get("/")
# def show_home():
#     with connect_db() as db:
#         sql = """
#             SELECT event, date, id
#             FROM bookings
#         """
#         params = ()
#         bookings = db.execute(sql, params).fetchall()
#         return render_template("pages/home.jinja", bookings=bookings)

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

