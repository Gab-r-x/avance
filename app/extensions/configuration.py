from importlib import import_module
from dynaconf import FlaskDynaconf

def load_extensions(app):
    for extension in app.config.EXTENSIONS:
        # Split data in form `extension.path:factory_function`
        module_name, factory = extension.split(":")
        # Dynamically import extension module.
        extension = import_module(module_name)
        # Invoke factory passing app.
        getattr(extension, factory)(app)


def init_app(app, **config):
    FlaskDynaconf(app, **config)