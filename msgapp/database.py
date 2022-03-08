from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://Subhash3111:subhash1031@msgapp.gyttk.mongodb.net/msgpp?retryWrites=true&w=majority"


def connect():
    # Used to connect to Database
    database = MongoClient(CONNECTION_STRING)
    return database['msgapp']


def auth_user(username: str, password: str):
    # checks weather user exists or not
    db = connect()
    col_user = db['users']
    user_details = col_user.find({"username": username, "password": password})
    if user_details:
        for item in user_details:
            print(item)
    else:
        print("user doesn't exists...")



if __name__ == '__main__':
    auth_user('Subhash', 'subh@sh1031')

