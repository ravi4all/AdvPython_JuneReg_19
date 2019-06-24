import cgi
import os

form = cgi.FieldStorage()
image = form['file']

print("Content-type:text/html\r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
""")
# print("Image is",form['file'])
if image.filename:
    # print("Image is",image)
    # print("Filename is",image.filename)
    fn = os.path.basename(image.filename)
    open("images/"+fn, 'wb').write(image.file.read())
    print("Image Saved Successfully...")

print("<img src=../{}>".format('images/'+fn))
print("""
</body>
</html>
""")