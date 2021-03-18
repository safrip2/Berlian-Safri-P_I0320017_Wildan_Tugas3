profile = {
    'name': "zara",
    'age': 27,
    'class': 'First'
}
del profile['name']


print("profile age:", profile['age'])
print(profile.get('school'))
profile.clear()
