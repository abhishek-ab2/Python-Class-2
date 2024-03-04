## Covered Topics
- File Structure
- Basic Application

- __init__.py - to initialize the dir as a module
- asgi.py - for ASGI
- settings.py - Used for project configuration/settings
- urls.py - Root repository of project urls
- wsgi.py - for WSGI

## For APPS
- admin.py - for customisations for django admin dashboard
- apps.py - for app configuration
- models.py - for creating models for ur app
- tests.py - to write tests for your app
- views.py - to create views
- urls.py - repo for app urls

Add a migration - makemigrations
Run a migration - migrate
To add an app:
- python manage.py startapp <app_name>
- Add it to INSTALLED_APPS
- include its urls to root url conf


## Assignment
- Replicate the project