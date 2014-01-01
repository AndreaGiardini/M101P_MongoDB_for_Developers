Es 5.1
```javascript
db.posts.aggregate([
	{ $unwind: "$comments" },
	{ $group: 
		{"_id": "$comments.author", 
		sum: {"$sum": 1}
	}},
	{ $sort: {"sum": -1} },
	{ $limit:1 }
])
```

Es 5.2

```javascript
db.zips.aggregate([ 
	{ $group: 
		{ _id : {state:"$state", city:"$city"}, 
		population: { $sum : "$pop"} } 
	},  
	{ $match:
		{ population : {$gt: 25000}, 
		"_id.state": {"$in":["CA","NY"]} }
	},
	{ $group: 
		{ _id:"answer", 
		average: {$avg:"$population"}} 
	}
])
```

Es 5.3

```javascript
db.grades.aggregate([
	{ $unwind : "$scores" },
	{ $match : 
		{ "scores.type" : {$ne: "quiz"}}
	},
	{ $group: 
		{ _id : { student_id : "$student_id", class_id : "$class_id"},
		average : {$avg:"$scores.score"}
		}
	},
	{ $group:
		{ _id: "$_id.class_id", "avg": {$avg: "$average"}}
	},
	{ $sort: {avg : -1}},
	{ $limit:1 }
])
```

Es 5.4

```javascript
db.zips.aggregate([
	{ $project: 
		{ first_char: 
			{$substr : ["$city",0,1]}, 
			pop : "$pop"
		}
	}, 
	{ $match: {"first_char": {$regex: "[0-9]"}} },
	{ $group: 
		{ _id:"answer", 
		total: { $sum: "$pop"}
		}
	}
])
```
