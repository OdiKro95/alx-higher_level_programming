#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost",
                         user=mysql_user,
                         passwd=mysql_password,
                         db=db_name,
                         port=3306)

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Execute the query to get all states, sorted by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results and print them
    results = cur.fetchall()
    for row in results:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
