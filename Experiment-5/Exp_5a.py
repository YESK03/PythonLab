my_tuple = (20,40,60,80,100)

print("Tuple",my_tuple)

print("First Element:",my_tuple[0])
print("Last Element:",my_tuple[-1])
print("Length:",len(my_tuple))
print("Count of 20:",my_tuple.count(20))
print("Index of 60:",my_tuple.index(60))

print("Maximum:",max(my_tuple))
print("Minimum:",min(my_tuple))
print("Sum:",sum(my_tuple))

print("Is 40 present?",40 in my_tuple)

#Convert tuple into list
my_list = list(my_tuple)
print("Converted list into tuple:",my_list)

#Converted list into tuple
my_tuple1 = tuple(my_list)
print("Coverted list to tuple:",my_tuple1)
