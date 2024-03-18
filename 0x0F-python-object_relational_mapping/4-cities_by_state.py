#!/usr/bin/env python3
"""Script to list all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to MySQL server
        conn = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)

        # Create a cursor object
        cursor = conn.cursor()

        # Execute the query
        query = "SELECT * FROM cities ORDER BY id ASC"
        cursor.execute(query)

        # Fetch all rows and print them
        for row in cursor.fetchall():
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Close database connection
        if 'conn' in locals() and conn.open:
            conn.close()

