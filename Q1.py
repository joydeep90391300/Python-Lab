list1 = [1,2,3]
list1 = ['c','s','i','t',[2,4,8]]
print(list1[1:5])

list=[]
list1 = [1,2,3]
list1 = [1,"hello",3.4]
list1 = [1,[1,2,3],3.4]
list1 = ['c','s','i','t',[2,4,8]]
#print(list1[-1][-1])
#print(list1[2:5])
#print(list1[:])

#list1.append([7])
list1 = [1,2,4]
list1.extend([7,8,9])
#print(list1)
#print(["repeat"]*3)
#print([1] *3)

list1.insert(3 , 16)
#print(list1)

odd=[1,9,10,9,11]
odd[1:2] = [5,7,8]
#print(odd)

odd.remove(8)
#print(odd)

odd.pop()
#print(odd)
odd=[1,23,3,4,55,5,5,5,6,7,8]
#print(odd)

pow = [x**2 for x in range(10)]
#print(pow)

pow = [2**x for x in range(10) if x>5]
#print(pow)

even = [x for x in range(51) if x%2==0]
print(even)
odd = [x for x in range(51) if x%2!=0]
print(odd)

number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)

num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)