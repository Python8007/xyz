# l = 1,[2,3,4,4]
# # l.remove(5)
# # a,b=[int(i) for i in (input('entertwo numbers').split(','))]
# # print(a,b)
# c,d=l
# # print(c,d)
#
# for i in 2,:
#     print(i)

# n = int(input('Enter numbers:'))
# for i in range(1,n+1):
#     print(''*(n-1),end='')
#     print('* '*i)

import sys
class Test:
    pass
t1 = Test()
t2=t1
# print(sys.getrefcount(Test))
'''
for i in range(5):
    print(i,end=',')
    if i>3:
        break
else:
    print('For complted successfully..')
'''
a = range(10)
# print(list(a))

class Employee:
    def __init__(self,sal,name):
        self.salary=sal
        self.name=name

    def __str__(self):
        return f'{self.__dict__}'

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name==other.name

    def __repr__(self):
        return str(self)

    def __mul__(self, other):
        return self.salary+other.salary

e1 = Employee(1000,'xxx')
e2 = Employee(1000,'xxx')

# print(id(e1))
# print(id(e2))
s={e1,e2}
# print(len(s))

# print(e1+e2)

# z=  eval(input('Enter value:'))
# print(z)
import copy
l1 = [1,2,3,4,[777,888]]
# l2=l1
l2 = copy.deepcopy(l1)
l1[4].append('rakesh')
# print(id(l1))
# print(id(l2))
# print(l1)
# n = int(input("Enter number of rows: "))
# for i in range(n+1):
#     print('* '*i)
s = '       rakesh           '
s1 = 'rakesh'
# print(s is not s1)
# print(s.find('x'))
# print(s.index('z'))
# print(s)
# print(s.lstrip())
# print(s[2])
# del s
# print(s)
del l1[2]
# print(l1)
# print(list(s))

# print(dict(enumerate(s)))
# print(sorted(s))
# print(s1.count('ab'))

print(s.split())

name='Rakesh R Sawant'
name1 = name.split(' ')
# print('_'.join(name1))
# print(name.startswith('Raks'))
# print(''.join(reversed(s)))

S2='abcd'
S1='ABCD'
l1 = (list(zip(S1,S2)))
result=''
for i in range(len(l1)):
    result = result+l1[i][0]+l1[i][1]

# print(result)
ip='B4A1D3'
o='ABD134'
l1=[i for i in ip if i.isalpha()]
l2=[(j) for j in ip if j.isdigit()]
result=''.join(sorted(l1))+''.join(sorted(l2))
# print(result)

ip='a4b3c2'
op='aaaabbbcc'
# print(ip.index('b'))
result=''
for i in range(len(ip)):
    if ip[i].isdigit():
        continue
    else:
        result=result+ip[i]*int(ip[i+1])
# print(result)

ip = 'aaabbaaabbcccdd'
l=[i for i in ip]
result=[j for j in set([(f'{i}',ip.count(i)) for i in l ])]
print(result)
d={}
for i in ip:
    count = ip.count(i)
    if i not in l:
        l.append((i,count))
# print(list(set(l)))
l=[1,2,3,4]
l2=[1,2,3,4,5555]
l.insert(1,'rakesh')
# print(l)
# print(l.pop(5))
# print(l+l2)
# l.extend()
# print(l)
a='abcd'
l=list(a)
l1=[]
res=''
for i in a:
    l1.append(l.pop())
# print(''.join(l1))

for j in range(len(a)):
    res=res+a[len(a)-(len(a)+1+j)]
# print(res)
a=(1,2,3)
b=(1,2,3)
# print(id(a))
# print(id(b))
l=sorted((1,5,2,4,9))
# print(l)

l=[10,15,4,23,0]
def buuble_sort(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l

print(buuble_sort(l))
print(buuble_sort(l)[-1])
max()