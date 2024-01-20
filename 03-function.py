# Functions
## built in functions
### print(), send output to the console
print(5)

### type(), return the type of the variable
print(type(5))

### Function definition syntax pattern
# def function_name(arg1):
#     ...
#     return

def add_one(num: int) -> int:
    """Return the number plus one
    """
    ret = num + 1
    return ret

def sum_nums(num1: int, num2: int) -> int:
    """Returns the sume of two input numbers
    """
    ret = num1 + num2
    return ret

def hello() -> None:
    """Prints Hello World
    """
    print("Hello World")

print("add_one(5):")
print(add_one(5))
print("sum_nums(5, 6):")
print(sum_nums(5, 6))
print("hello():")
hello()

### Combining functions
def add_one_then_sum_itself_then_hello(num: int) -> int:
    """
    - add one to the input num
    - sum the result with num
    - print hello world
    - return the final result
    """
    ret = add_one(num)
    ret = sum_nums(ret, num)
    hello()
    return ret
print("add_one_then_sum_itself_then_hello(5):")
my_result = add_one_then_sum_itself_then_hello(5)
print(my_result)