# basic list manipulation
number = [1, 2, 3]
new_list = []
for n in number:
    add_1 = n + 1
    new_list.append(add_1)
# above code converted to list comprehension
new_list = [n+1 for n in number]

# dictionary comprehension
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split(" ")}
print(result)


