import pymysql
import base

connection = pymysql.connect(host='localhost',user='root',database='onlineshopping',
                             port = 3306, autocommit = True)
cursor = connection.cursor()

print("""
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
  """)

base.header()

query = "select * from products"
cursor.execute(query)
data = cursor.fetchall()
rowcount = cursor.rowcount

print("""
<div class="container">
<h2 class='text-center'>Products</h2>
<hr>
    <div class='row'>
""")

for i in range(rowcount):
    print("""
    <div class='col-md-3'>
        <div class="card" style="width:15rem; margin-bottom:50px;">
    <img src="{}" class="card-img-top w-100" alt="..." style='height:300px;'>
    <div class="card-body">
        <h5 class="card-title">{}</h5>
        <p class="card-text">Price : {}</p>
        <a href="#" class="btn btn-primary">View Details</a>
    </div>
    </div></div>
        """.format(data[i][3], data[i][1], data[i][2]))
print("""
</div></div>
""")


print("""
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>
""")
