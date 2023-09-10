import random
naturalNum = set(random.sample(range(1, 100), 10))
realNum = set(random.sample([random.uniform(1, 100) for i in range(10)], 10))
commonNum = naturalNum.intersection(realNum)
if commonNum:
    print("Common Numbers:", commonNum)
else:
    print("No common numbers found.")