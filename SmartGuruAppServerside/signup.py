
import mysql.connector

db_connection = mysql.connector.connect(
                         host="www.remotemysql.com",
                         user="u2oI1tyJuT",
                         passwd="joBxFoudcl",
                         database="u2oI1tyJuT"
                    )


db_cursor = db_connection.cursor()

name="nipun"
email="nipunnadeen@gmail.com"
password="123"
type="s"



sql = "insert into users VALUES(null, '%s', '%s', '%s', '%s')"%(name, email, password, type)

number_of_rows = db_cursor.execute(sql)


db_connection.commit()
print(db_cursor.rowcount, "Record Inserted to the database")