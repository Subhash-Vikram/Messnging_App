import json


# check weather a json body is valid
def isValidJson(jsonInput):
    try:
        json.loads(jsonInput.decode("utf-8").replace("\\", r"\\"))
    except ValueError:
        return False
    return True
