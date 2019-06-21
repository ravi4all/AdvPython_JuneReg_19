import cgi
import pymysql

connection = pymysql.connect(host='localhost',user='root',database='db_demo',
                             port = 3306, autocommit = True)
cursor = connection.cursor()

form = cgi.FieldStorage()

name = form.getvalue('u_name')
email = form.getvalue('u_email')
pwd = form.getvalue('u_pwd')
city = form.getvalue('u_city')
gender = form.getvalue('gender')

query = "insert into users values (%s,%s,%s,%s)"
cursor.execute(query,(name,email,pwd,city))

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h1>Welcome {}</h1>
<h3>EmailId : {}</h3>
<h3>City : {}</h3>
<h3>Gender : {}</h3>

</body>
</html>
""".format(name,email,city,gender))