from django.urls import Resolver404, resolve


class AddSlashMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path_info
        try:
            resolve(path)
        except Resolver404:
            if not path.endswith('/'):
                try:
                    resolve(path + '/')
                    request.path_info = request.path = path + '/'
                except Resolver404:
                    pass
        return self.get_response(request)
