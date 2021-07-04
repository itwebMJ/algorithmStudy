from Queue import Queue

q = Queue()
q.put(1)
q.put(5)
q.put(10)

print(q)        #[1, 5, 10]
print(q.get())  #1   삭제됨
print(q)        #[5, 10]
print(q.peek()) #5
print(q)        #[5, 10]
