from time import sleep


class PauseRequest:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        sleep(3)
        print(request)
        response = self.get_response(request)
        return response

