import redis

r = redis.Redis()
r.set("name", "Diwakar")
name = r.get("name")
print(name)
