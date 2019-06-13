# pip install pymysql
import pymysql

connection = pymysql.connect(host='localhost',user='root',database='lms',
                             port = 3306, autocommit = True)
cursor = connection.cursor()

# query = "create table books (b_id int, b_name varchar(100), b_course varchar(100))"

# query = "insert into books values (101,'Let us C', 'BCA')"

b_id = 103
b_name = 'Java Head First'
b_course = 'Mtech'

query = "insert into books values (%s, %s, %s)"
cursor.execute(query, (b_id, b_name, b_course))

cursor.close()
connection.close()