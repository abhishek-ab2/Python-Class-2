## Form workflow 
- Receive request in view
- We initiate the form
- Form validates the data received
- finally, submits the data

## Why we dont use sql in django
- SQL is exploitable -> SQL injection


- We run queries through .objects attr, which is a ModelManager

## Query examples
Select * from orders where name=k;
Order.objects.filter(name='k')

## Lookups
- lt lookup - less than
- lte lookup
- gt lookup - greater than
- gte lookup

- startswith - string starts with a value (case sensitive)
- endswith - string ends with a value (case sensitive)
- contains - string contains a value (case sensitive)
- exact - string equals (case sensitive)
- istartswith - string starts with a value (case insensitive)
- iendswith - string ends with a value (case insensitive)
- icontains - string contains a value (case insensitive)
- iexact - string equals (case insensitive)

- isnull - whether a column value is NULL
