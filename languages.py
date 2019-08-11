languages={
    'Somnath': 'Java',
    'Jhinuk': 'Python',
    'Sarah': 'C',
    'Namtata': 'PHP'
}

print(languages)
print(languages['Somnath'])
languages['Sarah']='Cython'
print(languages)

lang = languages.get('Raj', 'No Such user exists');
print(lang)

print(languages.keys())

for key in languages.keys():
    print(key)

for value in languages.values():
    print(value)

for item in languages.items():
    print(item)

for key, value in languages.items():
    print(f"{key}, {value}")