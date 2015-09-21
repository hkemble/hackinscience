import datetime
d = datetime.datetime.today()
iso = d.isoformat()
print("Today is", iso[0:10], "and it is", iso[11:19])
