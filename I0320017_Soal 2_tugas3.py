my_profile = {
    'name': 'Berlian Safri Prakoso',
    'age': 19,
    'interest': ['book, ', 'gadget, ', 'game, '],
    'social': ['ig = safri_p2 ', 'twitter = @berlian_safri ', 'line = safri_p2 '],
    'music': ['Faint', 'American Idiot', 'Starlight', 'Hymn for the Weekend'],
    'food': ['nasi padang ', 'sate gule ', 'tengkleng ']
}
my_profile['interest'].append('and PC enthusiast') #menambahkan hobi
my_profile['interest'][2] = "PC gaming, " #mengganti hobi
my_profile['social'][2] = 'safri_p' #mengganti social media
del my_profile['food'][1:]
print("my hobby is", ''.join(my_profile['interest']))
print("the correct of my Line ID's is", my_profile['social'][2])
print("my favourite food right now is", ''.join(my_profile['food']))


