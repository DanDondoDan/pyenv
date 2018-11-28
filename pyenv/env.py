
import re
import os

__all__ = ['ENV']


class Singleton:
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not class_._instance:
            class_._instance = super(Singleton, class_).__new__(class_, *args, **kwargs)
        return class_._instance


class _Env(Singleton):
    _BOOL = {'True': True,  'False': False}

    _regex = re.compile("^[-+]?\d+\.\d+$")

    def __getattr__(self, item: str):
        value = os.environ.get(item, '')

        if value.isdigit():
            return int(value)

        if _Env._regex.match(value):
            return float(value)

        if value in _Env._BOOL:
            return _Env._BOOL[value]

        return value

    def __setattr__(self, item, value):
        os.environ.__setattr__(item, value)

    def __repr__(self):
        return repr(os.environ)

    def __str__(self):
        return str(os.environ)


ENV = _Env()
