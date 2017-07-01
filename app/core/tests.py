# ! coding: utf-8

from django.test import override_settings, SimpleTestCase


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}


@override_settings(DATABASES=DATABASES)
class SQLiteInMemoryMixin(SimpleTestCase):
    """Setting the database to memory."""
