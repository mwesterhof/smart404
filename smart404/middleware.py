from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect

from .models import NotFoundEntry


class Smart404Middleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
            entry, created = NotFoundEntry.objects.get_or_create(
                site=request.site,
                url=request.path
            )
            if not created:
                if entry.permanent:
                    response_class = HttpResponsePermanentRedirect
                else:
                    response_class = HttpResponseRedirect

                return response_class(entry.redirect_to)
        return response
