"""
Contains all operations related to user collection
"""
import json
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


# used to connect to DB
def connect():
    # Used to connect to Database
    database = MongoClient(CONNECTION_STRING)
    return database[DATABASE]


# Checks username exists or not
def username_exists(col_user, username: str) -> bool:
    # check username exists or not
    user = col_user.count_documents({"Username": username})
    if user:
        return True
    return False


# Checks weather user is admin or not
def is_Admin(username: str) -> bool:
    db = connect()
    col_user = db['users']
    user_details = col_user.find_one({"Username": username})
    if user_details['Admin']:
        return True
    return False


# checks weather user exist or not
def auth_user(username: str, password: str) -> dict:
    # checks weather user exists or not
    db = connect()
    col_user = db['users']
    if username_exists(col_user, username):
        user_details = col_user.find_one({"Username": username, "Password": password})
        if user_details:
            return {"Status": "Success", "Message": f"{user_details['Name']} logged in successfully."}
        else:
            return {"Status": "Failed", "Message": "Password doesn't match."}
    else:
        return {"Status": "Failed", "Message": "username doesn't exists..."}


# Returns list of all users of the application
def list_of_users() -> list:
    db = connect()
    col_user = db['users']
    user_details = col_user.find({}, {"_id": 0})
    return list(user_details)


# used to create a new user
def add_user(json_val: str) -> dict:
    json_val = json.loads(json_val)
    username = json_val['Username']
    db = connect()
    col_user = db['users']
    if username_exists(col_user, username):
        return {"Status": "Failed", "Message": "Username already exists."}
    else:
        col_user.insert_one(json_val)
        return {"Status": "Success", "Message": "User added successfully."}


# used to update an existing user
def update_user(json_val: str) -> dict:
    json_val = json.loads(json_val)
    username = json_val['Username']
    db = connect()
    col_user = db['users']
    if username_exists(col_user, username):
        col_user.update_one({'Username': username}, {'$set': json_val})
        return {"Status": "Success", "Message": "User updated successfully."}
    else:
        return {"Status": "Failed", "Message": "Username doesn't exists."}


# used to delete an existing user
def delete_user(json_val: str) -> dict:
    json_val = json.loads(json_val)
    username = json_val['Username']
    db = connect()
    col_user = db['users']
    if username_exists(col_user, username):
        col_user.delete_one({'Username': username})
        return {"Status": "Success", "Message": "User deleted successfully."}
    else:
        return {"Status": "Failed", "Message": "Username doesn't exists."}
