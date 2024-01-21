# while condition:
#     do...
count = 0
while count < 5:
    print(count)
    count = count + 1

count = 5
while count > 0:
    print(count)
    count = count - 1

# Use break to exit loop
count = 0
while count < 100:
    print(count)
    count = count + 1
    if count == 5:
        break
# Use continue to skip some loops
count = 0
while count < 10:
    count = count + 1
    if count == 5:
        continue
    if count == 6:
        continue
    print(count)