"""
Fizz buzz I: while loop
- ให้ loop ตัวเลข 1-20
- ถ้า input หาร 3 ลงตัว ให้ print fizz 
- ถ้า input หาร 5 ลงตัว ให้ print buzz
- ถ้า input หาร 3 และ 5 ลงตัว ให้ print fizz buzz (___ and ___)
- ถ้า input 3 และ 5 ไม่ลงเลย ให้ print ตัวเลขนั้นออกมา
"""

count = 0
while count < 20:
    count += 1
    if count % 3 == 0 and count % 5 == 0:
        print("fizz buzz")
    elif count % 3 == 0:
        print("fizz")
    elif count % 5 == 0:
        print("buzz")
    else:
        print(count)