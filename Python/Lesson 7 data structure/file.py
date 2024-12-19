lst = ['Apple' , 'Guava' , 'Mango' , 'Banana', 'Kiwi']
print("Length of list:",len(lst))
print("First Element:",lst[0])
print("Last Element:",lst[-1])

lst.insert(0,'Papaya')
print("Updated List :",lst)

lst.append('Passion')
print("Appended list:",lst)

lst.remove ('Guava')
print("Updated List :",lst)

lst.sort()
print("Sorted List :",lst)

lst.pop(1)
print("Updated List:",lst)

lst.reverse()
print("Reversed List:",lst)

print("Multiplication on List:",lst*2)

lst=lst[:4]
print ("Sliced list:",lst)

lst.clear()
print ("Updated List:",lst)