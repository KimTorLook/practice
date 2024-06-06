

import datetime as dt
from datetime import timedelta

def timeschudule():
    start_day = dt.datetime(2024,1,1)

    for x in range(366):
        print(start_day.strftime("%Y-%m-%d"), start_day.strftime("%A"))
        start_day += timedelta(days=1)


ts = timeschudule()