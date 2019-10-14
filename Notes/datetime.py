from datetime import datetime
import time
dt1 = datetime(2018,1,1)
dt2 = datetime.now()
dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())
print(f"{dt.year} / {dt.month}")
print(dt.strftime("%Y/%m"))
print(dt2 > dt1)
