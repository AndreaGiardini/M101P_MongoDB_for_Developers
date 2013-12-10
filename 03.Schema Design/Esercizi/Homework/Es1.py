import sys
import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.school
students = db.students

for student in students.find():
	tmp = 100;
	for score in student['scores']:
		if(score['type'] == "homework" and score['score'] < tmp ):
			tmp = score['score']
	students.update( { '_id' : student['_id'] }, { '$pull' : { "scores" : { "score" : tmp } } } )
