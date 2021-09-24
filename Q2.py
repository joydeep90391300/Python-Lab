Tuple1 = ()
print(Tuple1)
Tuple1 = ('Python', 'For')
print(Tuple1)

list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))

Tuple1 = tuple('Python')
print("\nTuple with the use of function: ")
print(Tuple1)

Tuple1 = (5, 'Welcome', 7, 'Home')
print("\nTuple with Mixed Datatypes: ")
print(Tuple1)

Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'for')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)

Tuple1 = ('Python',) * 3
print("\nTuple with repetition: ")
print(Tuple1)

Tuple1 = ('Python')
n = 5
print("\nTuple with a loop")
for i in range(int(n)):
    Tuple1 = (Tuple1)
    print(Tuple1)