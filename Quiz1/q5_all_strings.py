def all_strings(alpha, length):
    """Given a language this function will generate a list 
    of all strings of a given length"""
    if length > 0:
        result = all_strings(alpha, length-1)
        new_lst = []
        for string in result:
            for symbol in alpha:
                new_lst.append(str(string) + str(symbol))
        if len(result) == 0:
            for symbol in alpha:
                new_lst.append(str(symbol))
        return new_lst
    else:
        return ['']
    
            
            
print(sorted(all_strings({0, 1}, 3)))  
print(sorted(all_strings({'a', 'b'}, 2)))
print(len(all_strings({'a', 'b', 'c'}, 2)))