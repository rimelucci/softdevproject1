import hashlib
from pymongo import MongoClient

client = MongoClient()
db = client.test_database

def initializeTables():
    #create the user table in user.db if the table does not already exist
    db.createCollection("users", {})

    #create the posts table in myDatabase.db if the table does not already exist
    db.createCollection("posts", {})


#authenticate checks the usernames and if the hash of the password matches with the password already in the database
#returns true or false
def authenticate(username,password):
#    if (username == "admin" and password == "password"):
#        return True
#    else:
#        return False

    hpass = hashlib.sha224(password).hexdigest()
    ans = db.users.find({uname : username, pword : hpass})
    for r in ans:
        return True
    return False
    #the users.db file should contain the username and the hashed password
    #passwords stored as hashlib.sha224(<password>).hexdigest()

def registerCheck(username):
    ans = db.users.find({uname : username})
    for r in ans:
        return False
    return True
    #if user exists in database, returns False

 
def register(username,password):
    hpass = hashlib.sha224(password).hexdigest()
    
    if (not (registerCheck(username))):
        db.users.insert({uname : username, pword : hpass})
    #check if username is in the database already
    #might put this check somewhere else?
    


def makePost(username,title,body):
    db.posts.insert({uname : username, title : title, body : body})
    #adds a post to the database based on parameters

def getAllPosts():
    return db.posts.find()
    #2d array 
    #first index = row id
    #second index - 0=name, 1=title, 2=body

