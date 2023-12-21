from flask import Flask

class FlaskAdapter:
    def __init__(self, app: Flask):
        self.app = app

    def route(self, route_str, **options):
        def decorator(func):
            endpoint = options.pop("endpoint", func.__name__)
            self.app.route(route_str, **options)(func)
            return func
        return decorator
