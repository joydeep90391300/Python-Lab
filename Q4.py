y =(lambda x : x*2)(12)
print(y)

list1 = [1,2,3,4,5,6,7,8,9]
z = filter(lambda x : x%2==0 , list1)
print(z)

z = filter(lambda x : x%2==0 , list1)
print(list(z))

#numbers1 = [1,2,3]
#num2 = [4,5,6]

l = ['sat','bat','cat','mat']
test = list(map(list ,l))
print(test)

string = 'csit'
print(lambda string:string)
x = 'csit'
(lambda x :print(x))(x)

list1 = [1,2,3,4,5,6]
print(list(map(lambda x:pow(x , 3), list1)))


l = ['12345','dog','cat']
print(list(map(list,l)))

table = [lambda j=x : 2*j for x in range(1,11)]
for i in table:
    print(i())

list = [[5,4,3],[1,4,5,6],[6,3,9,12]]
s = lambda x:[sorted(i) for i in x]
print(s(list))

secmax = lambda x : [x[-2] for i in s(x)]
print(secmax(list))

from functools import reduce
li = [5,6,7,8,9,10,11]
sum = reduce (lambda x,y :x+y, li)
print(sum)

from functools import reduce
li = [5,6,7,8,9,10,11]
max = reduce (lambda x,y :x if x>y else y, li)
print(max)

