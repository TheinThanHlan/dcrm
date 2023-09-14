import mysql.connector



database = mysql.connector.connect(
            host= 'localhost',
            user = 'tth',
            password='testingtesting'
        )


cursorObject =database.cursor();


cursorObject.execute('create database t');

print("All Done")
