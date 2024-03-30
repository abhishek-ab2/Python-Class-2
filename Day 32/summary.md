# Covered Topics
- Advanced Queries

# Lookups:
- Some complex also have their own lookups:
- Datetime -> __date, __year, __month
- Relations -> You have columns of the table as their lookups
For ex:
class Blog:
    user = FK()
    created_on = DT()

blog.created_on = datetime(year, month, date, hour, minute, seconds, microseconds)

Blog.objects.filter(created_on__date=date(2022, 8, 1))
Blog.objects.filter(created_on__date='2022-08-01')
Blog.objects.filter(created_on__year__gt=2023)


# Blogs with user's first_name and last_name equal to val
Blog.objects.filter(user__first_name=val, user__last_name=val)
Blog.objects.filter(user__last_name__iendswith=val)

# Blogs with user's country's name endswith val
Blog.objects.filter(user__country__name__iendswith=val) # traverse within relations through lookups


# Q Objects - represents a query condition
# F Objects - represents a column value
# Q Objects - rep
Queryset methods:
- order_by - You pass multiple columns to have primary and secondary columns to sort by

- filter - By default filter uses kwargs, but for complex queries you can use Q objects

- annotate - Used to generate runtime columns 

# Annotations you can test
- Blog.objects.annotate(max_user_id=Max('user_id'))
- Blog.objects.annotate(user_count=Count('user'))


# Advanced Queries:
- Case - For implementing if elif else for an annotation
- FilteredRelation
- aggregate

# For Project:
- User Profile - Show user's data along with some statistics like avg post count on a day, total likes
- Private and public blogs


# For future ref
- js and jquery
- REST Api (django-rest-framework)
- SQL
