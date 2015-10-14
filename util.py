def authenticate(username,password):
    if (username == "admin" and password == "password"):
        return True
    else:
        return False

def makePost(username,title,body):
    conn = sqlite3.connect("myDatabase.db")
    c = conn.cursor()
    ans = c.execute('insert into posts values("'+username+'","'+title'","'+body'");')
    conn.commit()
    return True;
    #adds a post to the database based on parameters
    
