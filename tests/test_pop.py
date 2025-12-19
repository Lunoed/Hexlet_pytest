def fill(coll: list, value, begin=0, end=None):
    if end is None:
        end = len(coll)

    length = len(coll)

    if begin < 0:
        begin = max(0, (begin + length))
    if end < 0:
        end = max(0, (end + length))

    begin = max(0, min(begin, length))
    end = max(0, min(end, length))
    if begin >= end:
        return coll
    
    for i in range(begin, end):
        coll[i] = value

    return coll


collect = [1, 2, 3, 4]
fill(collect, 'i', 1, 1000)
print(collect)
