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


def connect():
    # Used to connect to Database
    database = MongoClient(CONNECTION_STRING)
    return database[DATABASE]


def username_exists(col_user, username: str) -> bool:
    # check username exists or not
    user = col_user.count_documents({"Username": username})
    if user:
        return True
    else:
        return False


def auth_user(username: str, password: str):
    # checks weather user exists or not
    db = connect()
    col_user = db['users']
    if username_exists(col_user, username):
        user_details = col_user.count_documents({"Username": username, "Password": password})
        if user_details:
            return {"Status": "Success", "Message": "Login Successful"}
        else:
            return {"Status": "Failed", "Message": "Password doesn't match."}
    else:
        return {"Status": "Failed", "Message": "username doesn't exists..."}


if __name__ == '__main__':
    auth_user('subhash', 'subh@sh1031')
