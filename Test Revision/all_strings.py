def all_strings(alpha, length):
    """ """
    results = []
    strings('', alpha, length, results)
    return results


def strings(string, alpha, length, results):
    """Helper method"""
    if len(string) == length:
        results.append(string)
    else:
        for symbol in alpha:
            strings(string + str(symbol), alpha, length, results)
            
print(sorted(all_strings({0, 1}, 3)))