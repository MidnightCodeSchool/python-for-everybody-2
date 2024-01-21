"""
Fizz buzz III: for loop, range
- ให้ loop ตัวเลข 1-20
- ถ้า input หาร 3 ลงตัว ให้ print fizz 
- ถ้า input หาร 5 ลงตัว ให้ print buzz
- ถ้า input หาร 3 และ 5 ลงตัว ให้ print fizz buzz (___ and ___)
- ถ้า input 3 และ 5 ไม่ลงเลย ให้ print ตัวเลขนั้นออกมา
"""

for num in range(1, 20 + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("fizz buzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
