"""
Contains all operations related to group_messages collection
"""
from pymongo import MongoClient
import configparser
from datetime import datetime

# Parsing Config File
PARSER = configparser.ConfigParser()
PARSER.read("Config\\Config.config")
CONNECTION_STRING = PARSER.get('Database', 'conn_string')
DATABASE = PARSER.get('Database', 'database')
CONNECTION_STRING = CONNECTION_STRING.replace('<username>', PARSER.get('Database', 'username'))
CONNECTION_STRING = CONNECTION_STRING.replace('<password>', PARSER.get('Database', 'password'))
CONNECTION_STRING = CONNECTION_STRING.replace('<database>', DATABASE)
MSG_COLLECTION = 'group_messages'
GRP_COLLECTION = 'group_details'


# used to connect to DB
def connect():
    # Used to connect to Database
    database = MongoClient(CONNECTION_STRING)
    return database[DATABASE]


# checks if user belongs to the group
def if_exists(col_group, username: str, groupname: str) -> bool:
    groups = col_group.count_documents({"Name": groupname, 'Members': {'$in': [username]}})
    if groups:
        return True
    return False


# view messages of the given group
def view_messages(username: str, groupname: str) -> dict:
    db = connect()
    col_group = db[GRP_COLLECTION]
    if if_exists(col_group, username, groupname):
        col_msg_group = db[MSG_COLLECTION]
        messages = col_msg_group.find({}, {"_id": 0})
        return list(messages)
    else:
        return {"Status": "Failed", "Message": "User doesn't belong to the given group."}


def send_message(username: str, groupname: str, message: str) -> dict:
    db = connect()
    col_group = db[GRP_COLLECTION]
    if if_exists(col_group, username, groupname):
        doc = {'Username': username, 'Groupname': groupname,
               'DateSent': datetime.now(), 'Likes': [], 'Message': message}
        col_msg_group = db[MSG_COLLECTION]
        sent_msg = col_msg_group.insert_one(doc)
        if sent_msg.acknowledged:
            return {"Status": "Success", "Message": "message sent successfully"}
        else:
            return {"Status": "Failed", "Message": "sending message failed."}
    else:
        return {"Status": "Failed", "Message": "User doesn't belong to the given group."}


def like_message(username: str, msgsentby: str, groupname: str, message: str) -> dict:
    db = connect()
    col_group = db[GRP_COLLECTION]
    if if_exists(col_group, username, groupname):
        col_msg_group = db[MSG_COLLECTION]
        msg_liked = col_msg_group.update_one({'Username': msgsentby, 'Groupname': groupname, 'Message': message},
                                             {'$push': {'Members': {'$each': [username], '$position': -1}}})
        if msg_liked.modified_count:
            return {"Status": "Success", "Message": "message liked successfully"}
        else:
            return {"Status": "Failed", "Message": "liking message failed."}
    else:
        return {"Status": "Failed", "Message": "User doesn't belong to the given group."}
