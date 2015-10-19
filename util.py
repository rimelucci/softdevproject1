import sqlite3
import hashlib

def initializeTables():
    #create the user table in user.db if the table does not already exist
    conn = sqlite3.connect("databases/users.db")
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS users
    (username text, password text)
    ''')
    conn.commit()
    conn.close()

    #create the posts table in myDatabase.db if the table does not already exist
    conn = sqlite3.connect("databases/myDatabase.db")
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS posts 
    (username text, title text, body text)
    ''')
    conn.commit()
    conn.close()


#authenticate checks the usernames and if the hash of the password matches with the password already in the database
#returns true or false
def authenticate(username,password):
#    if (username == "admin" and password == "password"):
#        return True
#    else:
#        return False

    hpass = hashlib.sha224(password).hexdigest()
    conn = sqlite3.connect("databases/users.db")
    c = conn.cursor()
    ans = c.execute('SELECT * FROM users WHERE username = "'+username+'" and password = "'+hpass+'";')
    for r in ans:
        return True
    return False
    #the users.db file should contain the username and the hashed password
    #passwords stored as hashlib.sha224(<password>).hexdigest()

 
def register(username,password):
    hpass = hashlib.sha224(password).hexdigest()
    
    conn = sqlite3.connect("databases/users.db")
    c = conn.cursor()
    c.execute('INSERT INTO users VALUES("'+username+'","'+hpass+'");')
    conn.commit()
    conn.close()
    #check if username is in the database already
    #might put this check somewhere else?
    


def makePost(username,title,body):
    conn = sqlite3.connect("databases/myDatabase.db")
    c = conn.cursor()
    ans = c.execute('INSERT INTO posts VALUES("'+username+'","'+title+'","'+body+'");')
    conn.commit()
    #adds a post to the database based on parameters

def getAllPosts():
    conn = sqlite3.connect("databases/myDatabase.db")
    c = conn.cursor()
    c.execute('select * from posts;')
    return c.fetchall();
    #2d array 
    #first index = row id
    #second index - 0=name, 1=title, 2=body

