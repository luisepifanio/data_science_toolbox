#!/usr/bin/env python
from datetime import datetime

import logging
import tzlocal


def posix2local(timestamp, tz=tzlocal.get_localzone()):
    """Seconds since the epoch -> local time as an aware datetime object."""
    return datetime.fromtimestamp(timestamp, tz)


class ISO8601Formatter(logging.Formatter):
    def converter(self, timestamp):
        return posix2local(timestamp)

    def formatTime(self, record, datefmt=None):
        dt = self.converter(record.created)
        if datefmt:
            s = dt.strftime(datefmt)
        else:
            t = dt.strftime(self.default_time_format)
            s = self.default_msec_format % (t, record.msecs)
        return s
