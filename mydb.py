import mysql.connector as mysql_connector_python

dataBase = mysql_connector_python.connect(
    host='localhost',
    user='root',
    password='johnson070',
    auth_plugin='caching_sha2_password'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

# Commit the changes to the database
dataBase.commit()

print('all done!')