## Official doc on db configuration
https://docs.djangoproject.com/en/5.0/ref/databases/#id13

## Form
Forms have two methods:
- GET -> When you want the data as query parameters, usually used for filters and is unsafe
- POST -> When you want sensitive data

Form attributes:
1. All the fields - renders as their corresponding input tags
2. as_p (method) - Renders the form with p tags
3. errors - Contains the errors raised during validation

Form Declaration:
class <FormName>(ModelForm):
    class Meta:
        model = <Model>
        fields = 'field1', 'field2' or '__all__'
        exclude = 'field1' # Optional

## Queries
- Model.objects.all() - Returns all rows of the model
- Model.objects.filter() - Returns all rows based on filters, takes filters as keyword arguments

Note: Django queries are lazy in nature, hence are not a list or list like object.

## Assignment:
- Replicate the project
- Go through django templating and querysets (optional)
- https://docs.djangoproject.com/en/5.0/ref/models/querysets/
- https://docs.djangoproject.com/en/5.0/topics/templates/#syntax