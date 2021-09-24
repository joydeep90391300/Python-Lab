
name = input("Enter your name: ")
print("Hello, " + name)
print(type(name))

num = int(input("Enter a number: "))
add = num + 1
print(add)

print("{}, for everybody"
	.format("Python"))

str = "This article is written in {}"
print(str.format("Python"))

print("Hello, I am {} years old !".format(20))

text = 'Python for everybody'

print(text.split())

word = 'Python, for, everybody'

print(word.split(','))

word = 'Python:for:everybody'

print(word.split(':'))
