import sqlite3
import hashlib

def authenticate(username,password):
    conn = sqlite3.connect("databases/users.db")
    c = conn.cursor()
    
    #the users.db file should contain the username and the hashed password
    #passwords stored as hashlib.sha224(<password>).hexdigest()

    if (username == "admin" and password == "password"):
        return True
    else:
        return False

    #authenicate checks the usernames and if the hash of the password matches with the password already in the database

def register(username,password):
    hpass = hashlib.sha224(password).hexdigest()
    
    conn = sqlite3.connect("databases/users.db")
    c = conn.cursor()
    
    #check if username is in the database already
    #might put this check somewhere else?
    


def makePost(username,title,body):
    conn = sqlite3.connect("databases/myDatabase.db")
    c = conn.cursor()
    ans = c.execute('INSERT INTO posts VALUES("'+username+'","'+title+'","'+body+'");')
    conn.commit()
    return True;
    #adds a post to the database based on parameters

def getAllPosts():
    conn = sqlite3.connect("databases/myDataBase.db")
    c = conn.cursor()
    c.execute('select * from posts;')
    return c.fetchall();
    #2d array 
    #first index = row id
    #second index - 0=name, 1=title, 2=body

