import os
import requests_cache
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfiguration(object):
    requests_cache.install_cache(cache_name='poke_cache', backend='sqlite', expire_after=180)
