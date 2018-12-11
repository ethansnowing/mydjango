from django.db import connection

cursor = connection.cursor()
cursor.execute('select * from (select * from video order by name desc) where rownum <=20')