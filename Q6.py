
def evenOdd(x):
	if (x % 2 == 0):
		print("even")
	else:
		print("odd")



evenOdd(2)
evenOdd(3)

def my_function(name):
  for x in name:
    print(x)

names = ["ravi", "John", "Michael"]

my_function(names)

def recursive_fibonacci(n):
     if n <= 1:
        return n
     else:
        return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

n_terms = 10

if n_terms <= 0:
    print("Invalid input ! Please input a positive value")
else:
    print("Fibonacci series:")
for i in range(n_terms):
	print(recursive_fibonacci(i))


def f():
	print(s)

s = "Global"
f()

def foo():
    y = "local"
    print(y)

foo()