<!DOCTYPE html>
<html>
<head>Hello World!</head>
<body>
	<p>Welcome {{username}}<p>
	<ul>
		%for thing in things:
		<li>{{thing}}</li>
		%end
	</ul><p>
	<form action="/favorite_fruit" method="POST">
	What is your favourite fruit?
	<input type="text" name="fruit" size="40" value=""><br>
	<input type="submit" value="Submit">
	</form>
</body>
</html>