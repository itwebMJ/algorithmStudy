class Stack(list):
    push = list.append

    def peek(self):
        return self[-1]

    #pop은 내장함수

s = Stack()

s.push(1)
s.push(5)
s.push(10)
'''
print(s)    #[1, 5, 10]
print(s.pop())  #10     석제됨
print(s.peek()) #5
'''


s_l = []

s_l.append(1)
s_l.append(5)
s_l.append(10)

print(s_l)          #[1, 5, 10]
print(s_l.pop())    #10
print(s_l)          #[1, 5]
print(s_l[-1])      #5
print(s_l)          #[1, 5]

#인터넷의 되돌아가기, 앞으로가기, 깊이 우선 탐색