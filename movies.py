import sqlite3 as sql

connection = sql.connect("dabaseMovies.db")

pointer = connection.cursor()
pointer.execute("CREATE TABLE IF NOT EXISTS MOVIES( NAME TEXT, ACTOR TEXT, ACTRESS TEXT,DIRECTOR_NAME TEXT, YEAR INTEGER )")
pointer.execute("INSERT INTO MOVIES VALUES('Beast','Vijay','Pooja','Nelson',2022)")
pointer.execute("INSERT INTO MOVIES VALUES('Doctor','Sivakarthikeyan','Priyanka mohan','Nelson',2021)")
pointer.execute("INSERT INTO MOVIES VALUES('Vikram','Kamalhassan','Swathishta','LogeshKangaraj',2022)")
pointer.execute("INSERT INTO MOVIES VALUES('Master','Vijay','Malavika mohanan','LogeshKangaraj',2021)")
pointer.execute("INSERT INTO MOVIES VALUES('Asuran','Dhanush','Manju warrier','Vetrimaaran',2019)")

# Printing all the elements of the database 
print("*********Everything in the database*********")
allMovies = pointer.execute("SELECT * FROM MOVIES").fetchall()
for i in allMovies:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
  print("============================================================================================")

# In this query, we are printing only the details from the db where Vijay is the lead actor
print("*********Actor Query*********")
actorQuery = pointer.execute("SELECT * FROM MOVIES WHERE ACTOR = 'Vijay'").fetchall()
for i in actorQuery:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
  print("============================================================================================")
