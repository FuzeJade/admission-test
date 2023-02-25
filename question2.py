def count(input):
    # your code here
    counts = {}
    for i in input:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts


input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1))  # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}


def group_by_key(input):
    # your code here
    groups = {}
    for i in input:
        key = i['key']
        value = i['value']
        if key in groups:
            groups[key] += value
        else:
            groups[key] = value
    return groups


input2 = [
    {'key': 'a', 'value': 3},
    {'key': 'b', 'value': 1},
    {'key': 'c', 'value': 2},
    {'key': 'a', 'value': 3},
    {'key': 'c', 'value': 5}
]

print(group_by_key(input2))  # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}
