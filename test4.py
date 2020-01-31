from datetime import datetime
from pytz import timezone

fmt = "%Y-%m-%d %H:%M:%S"


now_utc = datetime.now(timezone('UTC'))
now_pacific = now_utc.astimezone(timezone('Singapore'))
print(now_pacific.strftime(fmt))

