import pymysql
import base
import cgi

connection = pymysql.connect(host='localhost',user='root',database='onlineshopping',
                             port = 3306, autocommit = True)
cursor = connection.cursor()

form = cgi.FieldStorage()
p_id = form.getvalue('p_id')

print("""
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="../styles.css">
    <title>Hello, world!</title>
  </head>
  <body>
  """)

base.header()
query_1 = "select * from productdetails where p_id = %s"
cursor.execute(query_1, (p_id))
productsdetails = cursor.fetchall()

query_2 = "select * from products where p_id = %s"
cursor.execute(query_2, (p_id))
products = cursor.fetchall()

# print(productsdetails)

print("""
<div class="container">
<h2 class='text-center'> Product Detail </h2>
<hr>
        <div class="row">
            <div class="col-md-6">
                <img class='w-100' src="{}" alt="">
            </div>
            <div class="col-md-6">
                <h3>Title</h3>
                <p>{}</p>
                <h4>Price</h4>
                <p>{}</p>
                <h4>Rating : {}</h4>
                <h4>Description</h4>
                <p>{}</p>
                <p>Offers : {}</p>
                <h4>Highlights</h4>
                <p>{}</p>
            </div>
        </div>
    </div>
""".format(products[0][3], products[0][1], products[0][2],
productsdetails[0][2],productsdetails[0][1],productsdetails[0][3],
productsdetails[0][4]))

print("""
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>
""")
