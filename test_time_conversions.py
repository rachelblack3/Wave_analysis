import time_conversions
import datetime

def test_h5():
    """
    Test for h5 bytes time to Python datetime object conversion
    """
    assert time_conversions.h5_time_conversion(b'2015-01-01T00:00:00Z') == datetime.datetime(2015, 1, 1, 0, 0, 0)
