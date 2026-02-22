import mysql.connector 
sp=mysql.connector.connect(
    host="localhost",user="root",password="root5646",database="mysql_database")
mycursor=sp.cursor()


mycursor.execute("CREATE TABLE users(id int auto_increment primary key,name varchar(255),email varchar(255))")
insert="insert into users(name,email) values(%s,%s)"
values=("lasiya","lasi@gamil.com")
mycursor.execute(insert,values)
sp.commit() 
print("user added")
print("userslist:")
mycursor.execute("select* from users")
for sl in mycursor.fetchall():
    print(sl) 
up = "UPDATE users SET name = %s where id = %s"
val =("latha",105)
mycursor.execute(up,val)  
sp.commit()
print("user updated")
dl = "DELETE FROM users WHERE id =103" 
mycursor.execute(dl)
sp.commit()
print("user deleted")
 
mycursor.execute("select* from users")
for s in mycursor.fetchall():
    print(s) 
