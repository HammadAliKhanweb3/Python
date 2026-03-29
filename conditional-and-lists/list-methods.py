# accessing list items
colors=["red","green","blue","brown","black"]

print(colors)

print(colors[0])
# accessing last item
print(colors[-1])

# deleting list items
numbers=[5,10,15,20,25]
del numbers[0]
print(numbers)
numbers.pop()
print(numbers)
numbers.remove(15)
print(numbers)

# sorting list

numbers=[8,3,12,7,5,10]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers[0:3])
print(numbers[1:])


