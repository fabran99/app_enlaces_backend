from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "links_app.settings")
django.setup()
app = Celery('links_app')
app.conf.broker_transport_options = {'visibility_timeout': 36000}

app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()

app.conf["result_backend_transport_options"] = {'visibility_timeout': 18000}
