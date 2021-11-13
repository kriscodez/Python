

d = {
    'k1': 123,
    'k2': 345,
    'k3': 678,
    'k4': {
        'token': "hi Im the token"
    }
}

print(d['k2'])
print(d['k4']['token']) # "hi im the token"

d1 = {
   'key1': ['basketball', 'writing', 'creating', 'salivating']
}

hobby_list = d1['key1']
first_hobby = hobby_list[0]
print(first_hobby)