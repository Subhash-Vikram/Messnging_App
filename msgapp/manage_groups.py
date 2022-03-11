"""
Contains all operations related to group_details collection
"""
# import json
from pymongo import MongoClient
import configparser

# Parsing Config File
PARSER = configparser.ConfigParser()
PARSER.read("E:\\Messnging_App\\Config\\Config.config")
CONNECTION_STRING = PARSER.get('Database', 'conn_string')
DATABASE = PARSER.get('Database', 'database')
CONNECTION_STRING = CONNECTION_STRING.replace('<username>', PARSER.get('Database', 'username'))
CONNECTION_STRING = CONNECTION_STRING.replace('<password>', PARSER.get('Database', 'password'))
CONNECTION_STRING = CONNECTION_STRING.replace('<database>', DATABASE)
COLLECTION = 'group_details'


# used to connect to DB
def connect():
    # Used to connect to Database
    database = MongoClient(CONNECTION_STRING)
    return database[DATABASE]


# Returns list of groups of the given user
def list_of_groups(username: str) -> list:
    db = connect()
    col_user = db[COLLECTION]
    group_details = col_user.find({'Members': {'$in': [username]}}, {"_id": 0})
    return list(group_details)
