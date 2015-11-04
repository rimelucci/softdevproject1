import pymongo
import hashlib

#Mongo:

#        You can use dictionaries like python

#        Unlike python you can add and set with .

#        db.<collection>.insert(x) inserts the dictionary x

#        A list of dictionaries can be entered into a collection, which is really good

#        db.<collection>.find() displays all

#        db.<collection>.find({name : "  ", age : 30}) finds all with those aspects

#        db.people.find({$or:[{name:"Dana"}, {age:{$gt:20}}]}) will look for anyone with that name or with age greater than 20

#        db.people.update({name : "thomas"}, {$set:{age:50, last:"thompson"}}) finds anyone with name : "thomas" and sets their age to 50

#        db.people.update({name:"Dana"}, {$inc:{age:5}})

#        adding ,{upsert:true} before the last paren adds the person if they dont exist


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
    
    if (!registerCheck(username)):
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

