class Queue(list):
    put = list.append

    def peek(self):
        return self[0]

    def get(self):
        return self.pop(0)      #인덱스 0인 데이터 추출

q = Queue()
q.put(1)
q.put(5)
q.put(10)

print(q)        #[1, 5, 10]
print(q.get())  #1   삭제됨
print(q)        #[5, 10]
print(q.peek()) #5
print(q)        #[5, 10]


q = []
q.append(1)
q.append(5)
q.append(10)

print(q)        #[1, 5, 10]
print(q.pop(0))  #1   삭제됨
print(q)        #[5, 10]
print(q[0])     #5
print(q)        #[5, 10]

#프린터기 출력시 처음부터. 너비 우선 탐색

