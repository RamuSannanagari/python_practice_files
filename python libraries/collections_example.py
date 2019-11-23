# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 07:55:29 2018

@author: abhi
"""

from collections import OrderedDict,defaultdict

roll_no = OrderedDict([
    (11, 'Shubham'),
    (9, 'Pankaj'),
    (17, 'JournalDev'),
])

for key, value in roll_no.items():
    print(key, value)

marks = [
    ('Shubham', 89),
    ('Pankaj', 92),
    ('JournalDev', 99),
    ('JournalDev', 98)
]

dict_marks = defaultdict(list)

for key, value in marks:
    dict_marks[key].append(value)

print(list(dict_marks.items()))


from collections import Counter

marks_list = [
    ('Shubham', 89),
    ('Pankaj', 92),
    ('JournalDev', 99),
    ('JournalDev', 98)
]

count = Counter(name for name, marks in marks_list)
print(count)


import collections

User = collections.namedtuple('User', 'name age gender')
shubham = User(name='Shubham', age=23, gender='M')
print(shubham)

print('Name of User: {0}'.format(shubham.name))



name = collections.deque('Shubham')
print('Deque       :', name)
print('Queue Length:', len(name))
print('Left part   :', name[0])
print('Right part  :', name[-1])

name.remove('b')
print('remove(b):', name)


import collections

name = collections.deque('Shubham')
print('Deque       :', name)

name.extendleft('...')
name.append('-')
print('Deque       :', name)
