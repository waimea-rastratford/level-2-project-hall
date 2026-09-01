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



# Add more table classes here...

class PeopleTable:

    NAME = "people"

    SCHEMA = """
        CREATE TABLE people (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            name            TEXT NOT NULL,
            phone_number    TEXT NOT NULL

        )
    """

    SEED_DATA = """
        INSERT INTO people (name, phone_number)
        VALUES
            ("Jeff Ceaser", "021 024 2345"),
            ("Derek Man", "021 042 2555"),
            ("Lisa Lisbon", "021 054 4562"),
            ("Ronald Mcdonald", "021 087 6953"),
            ("Mrs Lincoln", "021 065 0995")
    """    



class BookingTable:   

    NAME = "bookings"

    SCHEMA = """
        CREATE TABLE bookings (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            event       TEXT NOT NULL,
            date        TEXT NOT NULL,
            people_id   INTEGER NOT NULL,

            FOREIGN KEY (people_id) REFERENCES people(id)
        )
    """

    SEED_DATA = """
        INSERT INTO bookings (people_id, date, event)
        VALUES
            ("1", "2026-05-03", "Birthday"),
            ("2", "2026-07-07", "Wedding" ),
            ("3", "2026-03-11", "Birthday"),
            ("4", "2026-06-14", "Get Together"),
            ("5", "2026-09-21", "Funeral" )
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
    PeopleTable,
    BookingTable,
    # Add more tables here...
]

