import pymysql

connection = pymysql.connect(host='localhost',user='root',database='lms',
                             port = 3306, autocommit = True)
cursor = connection.cursor()

# query = "select * from books"

query = "select * from books where b_course = 'MCA'"
cursor.execute(query)
data = cursor.fetchall()
print(data)

cursor.close()
connection.close()