# Ticket price based on age
# Conditionals (flow control)
# if condition1(bool):
#     # if condition one is met, do this
#     ...
# elif condition2(bool):
#     # if condition two is met, do this
#     ...
# else:
#     # if none of the above conditions are met, do this
#     # optional
#     ...


ADULT_AGE = 18
SENIOR_AGE = 65

age = input("How old are you? ")
age = int(age)
if age < 0:
    print("Invalid age")
    exit()

if age >= SENIOR_AGE:
    print("Baht 200")
elif age >= ADULT_AGE:
    print("Baht 250")
elif age < ADULT_AGE:
    print("Baht 150")