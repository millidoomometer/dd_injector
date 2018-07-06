import socket
import mon_config
import urllib
from datadog import initialize, api

hostname = socket.gethostname()

class DD:
    def __init__(self):
        dd_keys = mon_config.Conf()
        self.options = {
            'api_key': dd_keys._read('datadog')['api_key'],
            'app_key': dd_keys._read('datadog')['app_key']
        }
        initialize(**self.options)

    def inject(self, k, v):
        api.Metric.send(
            metric=k,
            points=v,
            host=hostname
        )
