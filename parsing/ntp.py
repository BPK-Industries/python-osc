import datetime
import struct
import time


# 63 zero bits followed by a one in the least signifigant bit is a special
# case meaning "immediately."
IMMEDIATELY = struct.pack('>q', 1)

# From NTP lib.
_SYSTEM_EPOCH = datetime.date(*time.gmtime(0)[0:3])
_NTP_EPOCH = datetime.date(1900, 1, 1)
_NTP_DELTA = (_SYSTEM_EPOCH - _NTP_EPOCH).days * 24 * 3600


def NtpToSystemTime(date):
    """Convert a NTP time to system time.

    System time is reprensented by seconds since the epoch in UTC.
    """
    return date - _NTP_DELTA


def SystemToNtpTime(date):
    """Convert a system time to a NTP time datagram.

    System time is reprensented by seconds since the epoch in UTC.
    """
    ntp = date + _NTP_DELTA
    num_secs, fraction = str(ntp).split('.')
    return struct.pack('>I', int(num_secs)) + struct.pack('>I', int(fraction))