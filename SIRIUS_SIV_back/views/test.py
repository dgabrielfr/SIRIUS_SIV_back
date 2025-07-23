from pyramid.view import view_config
import requests

@view_config(route_name='test', renderer='string')
def test(request):
    return 'test réalisé avec succès'
