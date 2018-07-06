import os
from configparser import ConfigParser

class Conf:

    def __init__(self):
        self.parser = ConfigParser()
        real_dir = os.path.dirname(os.path.realpath(__file__))
        config_path = os.path.join(real_dir, "../mon_config.ini")
        self.parser.read(config_path)

    def _read(self, section):
        conf = {}
        if self.parser.has_section(section):
            items = self.parser.items(section)
            for item in items:
                conf[item[0]] = item[1]
        else:
            raise Exception('{0} not found in the {1} file'.format(section, conf))

        return conf
