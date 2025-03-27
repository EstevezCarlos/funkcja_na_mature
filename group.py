def group(data:list, key):
    """
    Group data in list by key.
    If neighbour elements modified by key return the same value, they are grouped together.
    >>> group([0,1,1,1], lambda x:x)
    [[0], [1, 1, 1]]
    >>> group([0,0,0,1], lambda x:x)
    [[0, 0, 0], [1]]
    >>> group([1,1,1], lambda x:x)
    [[1, 1, 1]]
    """
    result = [[data[0]]]
    for i in range(0,len(data)-1):
        if key(data[i]) != key(data[i+1]):
            result.append([])
        result[-1].append(data[i+1])
    
    return result

def is_odd(num):
    return num % 2 == 1

data = [1,2,1,3,2,4,6,3,2,3]
print(group(data, is_odd))