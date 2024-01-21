d = {
    "cat": "แมว",
    "dog": "หมา",
    "rat": "หนู",
    "pig": "หมู",
}

print(d["cat"])
print(d["dog"])
print(d["rat"])
print(d["pig"])
print(d["snake"])

d2 = {
    "name": "Garfield",
    "kind": "cat",
    "age": 3,
    "color": "orange",
}
d2["name"]
d2["age"]
d2["color"]
d2["kind"]
d2["weight"] = 5
print(d2)
d2["weight"] = 6
print(d2)
del d2["weight"]
print(d2)
d2.keys()
d2.values()

for k, v in d2.items():
    print(k, v)

d2.get("weight", 0)
