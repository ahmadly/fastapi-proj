import importlib
import os

_SETTINGS_FILE = os.getenv('SETTINGS', 'core.settings.dev')


def load_settings():
    return importlib.import_module(_SETTINGS_FILE)


SETTINGS = load_settings()
