from collections import deque

a = deque(maxlen=10)
a.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# for i in range(100):
#     a.append(i)
print(a)