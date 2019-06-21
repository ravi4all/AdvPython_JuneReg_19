import cgi
import pymysql

connection = pymysql.connect(host='localhost',user='root',database='db_demo',
                             port = 3306, autocommit = True)
cursor = connection.cursor()

form = cgi.FieldStorage()

email = form.getvalue('email')
pwd = form.getvalue('pwd')

query = "select * from users where email = %s and pwd = %s"
cursor.execute(query, (email, pwd))
data = cursor.fetchall()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
""")

if len(data) < 1:
    print("<h2>Invalid User</h2>")
else:
    print("""
    <h1>Welcome {}</h1>
    <h3>EmailId : {}</h3>
    <h3>City : {}</h3>
    """.format(data[0][0],data[0][1],data[0][3]))

print("""
</body>
</html>""")