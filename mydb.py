import mysql.connector
import json

FILEPATH = ''

# Read the configuration from the JSON file
with open(FILEPATH, 'r') as config_file:
    config = json.load(config_file)

user = config.get('user')
password = config.get('password')

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = user,
    passwd = password
)

# prepare a cursor object

cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute('CREATE DATABASE crmdb')

print('All done')
