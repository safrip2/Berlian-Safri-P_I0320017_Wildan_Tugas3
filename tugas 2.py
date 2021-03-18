my_profile = {
    'name': 'Berlian Safri Prakoso',
    'age': 19,
    'interest': ['book', 'gadget', 'game'],
    'social': ['ig = safri_p2', 'twitter = @berlian_safri', 'line = safri_p2'],
    'music': ['Faint', 'American Idiot', 'Starlight', 'Hymn for the Weekend'],
    'food': ['nasi padang', 'sate gule', 'tengkleng']
}
my_profile['interest'].append('pc enthusiast') #menambahkan hobi
my_profile['interest'][2] = "gaming" #mengganti hobi
my_profile['social'][2] = 'safri_p' #mengganti social media
my_profile['food'].pop(2) #menghapus makanan favorit
my_profile['food'].pop(1) #menghapus makanan favorit
print("my hobby is", my_profile['interest'])
print('the correct of my Line ID is', my_profile['social'][2])
print("my favourite food right now is", my_profile['food'])
