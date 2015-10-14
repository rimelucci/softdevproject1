import sqlite3

def authenticate(username,password):
    if (username == "admin" and password == "password"):
        return True
    else:
        return False

def makePost(username,title,body):
    conn = sqlite3.connect("myDatabase.db")
    c = conn.cursor()
    ans = c.execute('INSERT INTO posts VALUES("'+username+'","'+title+'","'+body+'");')
    conn.commit()
    return True;
    #adds a post to the database based on parameters

def getAllPosts():
    conn = sqlite3.connect("myDataBase.db")
    c = conn.cursor()
    c.execute('select * from posts;')
    return c.fetchall();
    #2d array 
    #first index = row id
    #second index - 0=name, 1=title, 2=body

