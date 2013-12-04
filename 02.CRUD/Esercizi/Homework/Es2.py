
import sys
import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.students
grades = db.grades

cur = grades.find({ 'type' : 'homework' }).sort([("student_id", 1), ("score", 1)])

tmp_student_id = -1

for row in cur:
	if int(row['student_id']) != tmp_student_id:
		# Nuovo studente - elimino questo record
		tmp_student_id = row['student_id']
		grades.remove( { "_id" : row['_id'] } )
