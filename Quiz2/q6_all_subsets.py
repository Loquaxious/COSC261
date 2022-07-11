def all_subsets(s):
    """Returns a list of sets of all subsets of a given set"""
    if len(s) == 0:
        return [set()]
    else:
        element = s.pop()
        result = all_subsets(s)
        new_lst =[]
        for sets in result:
            new_lst.append(sets.union({element}))
        return new_lst + result
    

print(sorted(map(sorted, all_subsets({0, 1, 2})))) 
print(sorted(map(sorted, all_subsets({'a', 'b'}))))
print({1} in all_subsets({0, 1, 2}))