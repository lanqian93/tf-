import random
import time

import requests


i = 0
while i < 500:
    res = requests.get("http://www.9air.com/aq/GetRandomImage")
    with open("trainImage/{}.jpg".format(i), "wb") as f:
        f.write(res.content)
    time.sleep(random.random())
    i += 1