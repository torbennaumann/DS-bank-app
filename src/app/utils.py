import datetime
import random


def random_timestamp():
    days = random.randint(1, 365)
    now = datetime.datetime.utcnow()
    delta = datetime.timedelta(days=days)
    return now - delta
