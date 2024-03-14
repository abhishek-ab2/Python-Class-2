## Covered topics
- Querysets


- filter() -> Returns result based on filters provided (either kwargs or Q objects)
- exclude() -> Results matching the filters are excluded
- all() -> Returns all rows
- order_by() -> Change order of a query (by default ascending order of id)
- distinct() -> Fetch unique rows only (behaviour is subjective to db, for ex: we cant pass column in mysql)
- annotate() -> Annotations are values calculated in queries
- values() -> Get results of a query, return type is list or dict
- values_list() -> Same as values but individual rows are represented as list.
- none() -> Returns\Sets None as your query result
- reverse() -> Reverses the results
- select_related() -> Fetches the fk object in the query rather just the id of fk(default behaviour)
- only() -> Fetches only particulars columns passed
- using() -> Used to set which db to use for the query
- raw() -> Used to run sql queries

Template tags:
Tags are special functions which are used to perform some operation in a template.


Template Inheritance



### Assignment
- Go through the given urls
- Create a django project
- Create a Blog model
- Requirements -> A simplified version of twitter, (you can post, see all the public blogs, delete ur blogs, update ur blogs and basic registration and login)
