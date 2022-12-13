f = open("helloworld.html", "w")
message = """
<DOCTYPE html>
<html>
<body>
<h1>Hello World</h1>
<p>This is a test</p>
</body>
</html>
"""
f.write(message)
f.close()