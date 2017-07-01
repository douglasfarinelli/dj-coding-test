# ! coding: utf-8

import contextlib
from django.utils import module_loading


class ApiAppConfigMixin:
    """Mixin to load DRF routes defined in app_name.<API_ROUTES_PATH>"""

    API_ROUTES_PATH = 'api.routes'

    def ready(self):
        super(ApiAppConfigMixin, self).ready()
        with contextlib.suppress(ImportError):
            module_loading.import_module('%s.%s' % (self.name, self.API_ROUTES_PATH))
