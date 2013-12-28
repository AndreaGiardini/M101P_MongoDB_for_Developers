Es 5.2

```javascript
db.zips.aggregate([ 
	{$match: 
		{$or : [{"state":"NY"},{"state":"CA"}]} 
	},
	{ $group: 
		{ _id : {city:"$city", state:"$state"}, 
		population : { $sum : "$pop"} } 
	},  
	{ $match:
		{"population" : {$gt: 25000}} 
	},
	{ $group: 
		{_id:"total", "average":{$avg:"$population"}} 
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
		{ _id : 
			{ student_id : "$student_id",
			class_id : "$class_id"
			},
		"average" :
			{$avg:"$scores.score"}
		}
	},
	{ $group:
		{_id: "$_id.class_id", "avg": {$avg: "$average"}}
	},
	{ $sort: 
		{avg : 1}
	}
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
	{ $match:
		{ "first_char": 
			{$in: ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] }
		}
	}, 
	{ $group: 
		{_id:null,
		tot_pop:{ $sum: "$pop"}
		}
	}
])
```