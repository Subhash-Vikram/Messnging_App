"""
Contains all operations related to group_details collection
"""
import json
from pymongo import MongoClient
import configparser
from datetime import datetime

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


# checks if groupname already exists
def if_exists(col_group, group_name: str) -> bool:
    groups = col_group.count_documents({"Name": group_name})
    if groups:
        return True
    return False


# Returns list of groups of the given user
def list_of_groups(username: str) -> list:
    db = connect()
    col_group = db[COLLECTION]
    group_details = col_group.find({'Members': {'$in': [username]}}, {"_id": 0})
    return list(group_details)


# create a new group
def create_group(username: str, json_val: str) -> dict:
    db = connect()
    col_group = db[COLLECTION]
    json_val = json.loads(json_val)
    group_name = json_val['Name']
    if not if_exists(col_group, group_name):
        json_val['CreatedBy'] = username
        json_val['CreatedDate'] = datetime.now()
        col_group.insert_one(json_val)
        return {"Status": "Success", "Message": "Group created successfully."}
    else:
        return {"Status": "Failed", "Message": "Group name already exists."}


def delete_group(username: str, groupname: str) -> dict:
    db = connect()
    col_group = db[COLLECTION]
    if if_exists(col_group, groupname):
        del_group = col_group.delete_one({'Name': groupname, 'CreatedBy': username})
        if del_group.deleted_count:
            return {"Status": "Success", "Message": "Group deleted successfully."}
        else:
            return {"Status": "Failed", "Message": "user cannot delete this group."}
    else:
        return {"Status": "Failed", "Message": "Group name doesn't exists."}


def search_group(groupname: str) -> dict:
    db = connect()
    col_group = db[COLLECTION]
    find_group = col_group.find({'Name': {'$regex': groupname, '$options': "$i"}}, {"_id": 0})
    if find_group.__sizeof__():
        return list(find_group)
    else:
        return {"Status": "Failed", "Message": "Group name doesn't exists."}
