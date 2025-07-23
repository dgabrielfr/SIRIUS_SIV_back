from pyramid.view import view_config
import requests

@view_config(route_name='hello', renderer='string')
def hello(request):
    return 'Hello from backend'
