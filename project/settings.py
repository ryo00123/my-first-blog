DEBUG = False

下の方に記述します
""" django-herokuの設定 """
try:
    from .local_settings import *
except ImportError:
    pass
if not DEBUG:
    import django_heroku
    django_heroku.settings(locals())
