'''
add_gst = lambda price: price > 0
print(add_gst(20))
'''

'''
is_passing = lambda marks: marks > 40
print(is_passing(50))  # True
print(is_passing(30))  # False
print(is_passing(40))  # False
'''

'''
items  = [("Zuchini",40),("Banana",100),("Apple",25)]
SortedItems = sorted(items,key=lambda item:item[0])
print(SortedItems)
'''


'''
items  = [("Zuchini",40),("Banana",100),("Apple",25)]
print(items)
'''



furts = ["Banana", "Apple", "watermelon", "graps"]

longest_word = max(furts, key=lambda word: len(word))

print(longest_word)
