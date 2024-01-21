# Math operations
a = 5
b = 2
c = 5
print(a + b)  # addition
print(a - b)  # subtraction
print(a * b)  # multiplication
print(a / b)  # division
print(a % b)  # modulus -> หารเอาเศษ
print(a ** b)  # exponent
print(a // b)  # floor division -> หารเอาส่วน (หารได้กี่ครั้ง?)
print(a * b - c)  # >>> 5
print(a * (b - c))  # >>> -15
# Type
## 1. int
print(type(5))
## 2. float
print(type(5.0))
## 3. str
print(type('Hello'))
print(type("Hello"))
print(type('''Hello
           world
           '''))
print(type("""Hello
           world
           """))
## 4. bool
print(type(True))
print(type(False))
print(type(a == b))
print(type(a != b))
print(type(a > b))
print(type(a < b))
## 5. None
print(type(None))
# Variable
this_is_a_variable = 5
print(this_is_a_variable)
this_is_a_variable = 6
print(this_is_a_variable)
## 6. List
list_a = [1, 2, 3, 4, 5]
list_b = ['a', 'b', 'c', 5]
print(type(list_a))
print(type(list_b))
print(list_a[0])
print(list_a[1])
print(list_a[2])
print(list_a[-1])
# Function
# def function_name(arg1: type, arg2: type):
#     ...
#     return ...
def add(a: int, b: int) -> int:
    return a + b
print(add(5, 2))
# Built-in function: input
def get_name() -> None:
    name = input('What is your name? ')
    print('Hello, ' + name)
# get_name()
# Type casting
g = "5"
print(type(g))
g = int(g)
print(type(g))
# int("five")  # doesn't work
print(int(5.6)) # >>> 5
# Flow control: if if-else else
# if expression1: 
#     do this
# elif expression2:
#     do this
# else:
#     do this
if a > b:
    print('a > b')
elif a < b:
    print('a < b')
else:
    print('a == b')
# For loop
my_items = ['apple', 'banana', 'orange']
for item in my_items:
    print("I have: ", item, "in my bag")