# https://www.w3schools.com/python/python_ref_string.asp for more string methods
# escaping characters
"this a string"
# 'this is bob's cat'
"this is bob's cat"
'this is bob\'s cat'
"this is \"bob'\" cat"
print('this is "bob"\tcat')
print('this is "bob" cat\\')
# new line
print('this is "bob" cat.\nIt has 4 legs.')
# raw string
print(r'this is "bob" cat.\n\tIt has 4 legs.')
# string is a list like object
my_string = "abcdef"
print(my_string[0])
print(my_string[1])
print(my_string[2])
print(my_string[-1])
for i in my_string:
    print(i)
my_string[1:]
my_string[:-1]
my_string[1:3]
# check if a string is in another string, substring
my_string2 = "Hello world"
"hello" in my_string2
"Hello" in my_string2
# concatenation strings
mystring3 = "Hello" + " " + "world"
print(mystring3)
# useful string methods (methods are functions that belong to an object)
## upper
sentence1 = "hello world, i am a string."
sentence1.upper()
## lower
sentence2 = "HELLO!!!"
sentence2.lower()
## isalnum
sentence3 = "hello123"
sentence3.isalnum()
sentence4 = "hello@123"
sentence4.isalnum()
## isalpha
sentence5 = "hello"
sentence5.isalpha()
sentence6 = "hello123"
sentence6.isalpha()
## isdigit
sentence7 = "123"
sentence7.isdigit()
sentence8 = "h123"
sentence8.isdigit()
## split
sentence9 = "hello world, i am a string."
sentence9.split()  # >>> ['hello', 'world,', 'i', 'am', 'a', 'string.']
sentence9.split(',')  # >>> ['hello world', ' i am a string.']
## join
list_words = ['apple', 'banana', 'orange']
', '.join(list_words)  # >>> 'apple, banana, orange'