class LoaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Before view
        request.show_loader = True   # global flag

        response = self.get_response(request)

        # After view
        return response