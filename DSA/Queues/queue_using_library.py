from collections import deque


# using collections module
custqueue = deque((9,1,2,3,4,), maxlen = 8)

custqueue.append(1)
custqueue.append(2)
custqueue.append(3)

# print(custqueue)
# print(custqueue.popleft())
# print(custqueue)
# custqueue.clear()
# print(custqueue)


# using queue module for creating quue
import queue as q

customQueue = q.Queue(maxsize= 4)
# print(customQueue.empty())
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)
# print(customQueue.qsize())
# print(customQueue.get())
# print(customQueue.qsize())


# using multiprocessing module
from multiprocessing import Queue

customqueue = Queue(maxsize = 4)

customqueue.put(1)
customqueue.put(4)

print(customqueue)
print(customqueue.get())