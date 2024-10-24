import mysql.connector

# Establish a connection to the database
db_connection = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="mykull",
    password="password",
    database="flight_game",
    collation="utf8mb4_general_ci",
)

# Create a cursor object
cursor = db_connection.cursor()

# teht 8.1

# Ask for ICAO code from the user
icao_code = input("Please enter the ICAO code: ")

# Execute the SQL query
cursor.execute(
    f"SELECT airport.name, country.name FROM airport JOIN country ON airport.iso_country = country.iso_country WHERE airport.ident = '{icao_code}'"
)

# Fetch the result
result = cursor.fetchone()

# Check if result is not None
if result is not None:
    # Print the airport name and country name
    print(f"Airport Name: {result[0]}, Country: {result[1]}")
else:
    print("No results found for the given ICAO code.")

# teht 8.2


# teht 8.3

# Close the connection
db_connection.close()
