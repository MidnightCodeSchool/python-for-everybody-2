"""
Fizz buzz II: for loop
- ให้ loop ตัวเลข 1-20
- ถ้า input หาร 3 ลงตัว ให้ print fizz 
- ถ้า input หาร 5 ลงตัว ให้ print buzz
- ถ้า input หาร 3 และ 5 ลงตัว ให้ print fizz buzz (___ and ___)
- ถ้า input 3 และ 5 ไม่ลงเลย ให้ print ตัวเลขนั้นออกมา
"""

nums = [
    1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,
    19,20
        ]
for num in nums:
    print(num)
    if num % 3 == 0 and num % 5 == 0:
        print("fizz buzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
