

names = ['Amir', 'Bear', 'Charlton', 'Daman']
print(names[-1][-1])

list1=[1, 3, 2]
print(list1*2)

def last(n):
    return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))