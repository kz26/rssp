from pyramid.config import Configurator


__version__ = "1.0.0"

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    #config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('index', '/')
    config.add_route('feed', '/feed/{url:.+}')
    config.scan()
    return config.make_wsgi_app()
