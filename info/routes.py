from info.views import index


def init_routes(app):
    app.router.add_get('/', index)
