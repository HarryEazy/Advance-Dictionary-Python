# Import mysql-connector package to connect to mysql database
import mysql.connector

# Create connection variable "con" with the specific parameters
con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
# IP Address
host = "108.167.140.122",
database = "ardit700_pm1database"
)

# Create cursor for mysql
cursor = con.cursor()

# Get user input for the word they want to search
word = input("Enter a word: ")

# Queries database to get matches with user inputted "word"
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)

# Gets and stores using fetchall() and store in a variable "results"
results = cursor.fetchall()

# If results has a value
if results:
    for result in results:
        # Print the first line - the definition of the word
        print(result[1])
# No word found ad results is False
else:
    print("No word found")