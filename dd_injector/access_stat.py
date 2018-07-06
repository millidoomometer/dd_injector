import os
import time

class Stats:
    def __init__(self, location):
        self.location = location

    def size(self):
        access_log_size = os.path.getsize(self.location)
        return access_log_size

    def age(self):
        access_log_mtime = int(os.path.getmtime(self.location))
        mtime_diff = (int(time.time()) - access_log_mtime)/60/60
        return mtime_diff

    def age_minutes(self):
        access_log_mtime = int(os.path.getmtime(self.location))
        mtime_diff = (int(time.time()) - access_log_mtime)/60
        return mtime_diff
