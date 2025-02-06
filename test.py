people = {"person3":{"age":3,"height":2},"person2":{"age":8,"height":1},"person4":{"age":7,"height":0}}
print(dict(sorted(people.items(),key=lambda person : person[1]["age"])))

for i in range(2,5):
    print(i)

import random
import math

x = random.random()
print(math.floor(x * 50))
arr = [x for _ in range(10)]
print(arr)