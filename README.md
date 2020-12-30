# DataRepresentation-and-Querying
Datarepresentation and Querying module - Project A Web Application Project 2020


Action	Method	URL	Sample Params	Sample Return
Get All	GET	/coffeeconsumers	none	[{...},{...},{...}]
Find by id	GET	/coffeeconsumers/id	none	[{"id":"1","type":"xxx"},{"name":"xxx","quantity":"xxx"}]
Create	POST	/coffeeconsumers	{"type":"xxx"},{"name":"xxx","quantity:"xxx"}	[{"id":"1","type":"xxx"},{"name":"xxx","quantity":"xxx"}]
Update	PUT	/coffeeconsumers/id	{"quantity:"xxx"}	[{"id":"1","type":"xxx"},{"name":"xxx","quantity:"xxx"}]
Delete	DELETE	/coffeeconsumers/id	none	{"done:"true}
