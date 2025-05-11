def dupl_with_given_key(iterable, key= lambda x: x):
    seen = [] 
    for item in iterable:
        if key(item) in seen:
            yield item  
        else:
            seen.append(key(item))  
            

print(tuple(dupl_with_given_key([[1], [2, 3], [4], [5, 6, 7], [8, 9]], key=len)))
# Výstup: ([4], [8, 9])

print(tuple(dupl_with_given_key([[2, 3], [4], [1], [4], [2, 3]])))
# Výstup: ([4], [2, 3])


lss = [1,2,3,4,5]

def add_one(iterable, key = lambda x: x):
    new_list =[]
    
    for item in iterable:
        key_item = key(item)
        key_item += 1
        new_list.append(key_item)
    
    print(new_list)
    


def add_three(x):
    return x+3

lst = [1,2,3,4,5]
add_one(lst, add_three)







