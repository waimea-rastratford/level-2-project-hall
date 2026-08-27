#============================================================================
# Database schema and seed data configuration
#============================================================================


#----------------------------------------------------------------------------
# Table definitions
#----------------------------------------------------------------------------
# Define your tables with a name, a schema and optional seed/sample data,
# using this format, and then add the tables to the Table Registry below:
#
# class TableName:
#     NAME      = "name"
#     SCHEMA    = "CREATE TABLE name (...)"
#     SEED_DATA = "INSERT INTO name (...)" or None
#----------------------------------------------------------------------------

class BookingTable:   

    NAME = "bookings"

    SCHEMA = """
        CREATE TABLE booking (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            event   TEXT,
            booking_name  TEXT,
            date_id  INTEGER FOREIGN KEY ,
            personal_id INTEGER FOREIGN KEY
        )
    """

    SEED_DATA = """
        INSERT INTO booking (event, booking_name, date_id, personal_id )
        VALUES
            ("Birthday", "Jeff", "1", "1")
    """


# Add more table classes here...

class InfoTable:

    NAME = "information"

    SCHEMA = """
        CREATE TABLE info (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            ph_number   TEXT,
            full_name  TEXT
        )
    """

    SEED_DATA = """
        INSERT INTO info (ph_number, full_name)
        VALUES
            ("0270599348", "Jeff Ceaser the 3rd")
    """    


class DateTable:

    NAME = "dates"

    SCHEMA = """
        CREATE TABLE date (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            day   TEXT,
            month  TEXT,
            year  TEXT
        )
    """

    SEED_DATA = """
        INSERT INTO date (day, month, year)
        VALUES
            ("01", "01",91 )
    """    


#----------------------------------------------------------------------------
# Table registry
#----------------------------------------------------------------------------
# Register all of your tables by adding them to the TABLES list here:
#
# TABLES = [
#     Table1Name,
#     Table2Name,
#     etc.
# ]
#
# Note: The table order is important - Create the tables that have
# foreign keys *after* the tables they link to have been created
#----------------------------------------------------------------------------

TABLES = [
    BookingTable,
    InfoTable,
    DateTable
    # Add more tables here...
]

