from .models import PageView
from django.db.models import F

class PageViewsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        hit, created = PageView.objects.get_or_create(application='cards')
        if request.method == 'GET':
            hit.hits = hit.hits + 1
            hit.save()
        request.hits = hit.hits
        response = self.get_response(request)
        return response