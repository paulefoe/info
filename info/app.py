from aiohttp import web

import aiopg.sa

from info.routes import init_routes
from info.utils import get_config


def init_config(app: web.Application, argv=None) -> None:
    app['config'] = get_config(argv)


async def init_database(app: web.Application) -> None:
    """
    This is signal for success creating connection with database
    """
    config = app['config']['postgres']

    engine = await aiopg.sa.create_engine(**config)
    app['db'] = engine


async def close_database(app: web.Application) -> None:
    """
    This is signal for success closing connection with database before shutdown
    """
    app['db'].close()
    await app['db'].wait_closed()


def init_app(argv=None) -> web.Application:
    app = web.Application()
    init_config(app, argv)
    init_routes(app)
    app.on_startup.extend([init_database])
    app.on_cleanup.extend([close_database])
    return app


app = init_app()
