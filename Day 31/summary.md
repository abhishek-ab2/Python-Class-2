## Covered Topics
- Object Update in Django
- Session Storage

## Session
- Session is a storage where the data is stored in the backend, hence is secure and reliable


## Update/Set data in session:
request.session['key'] = value


## Delete data from session:
del request.session['key']
 OR 
request.session.clear()


## Scenarios-
Data is needed on only one page - query params (request.GET) or request body (request.POST)
else if needed on more than one pages and forwarding is a hassle - session


## Assignment:
- Implement blog and its functionalities, list blogs (provide filters and sort by must), create blogs, update blogs, delete blogs
- Add proper navigation for all the pages
