import redis
import datetime


r = redis.Redis()

today = datetime.date.today()
stoday = today.isoformat()  # Python 3.7+
visitors = {"dan", "jon", "alex"}
print(stoday)
r.sadd(stoday, *visitors)
values = r.smembers(stoday)
print(values)

card = r.scard(today.isoformat())
print(card)
