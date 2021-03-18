friends = ["Habib", "Fahri", "Jimly", "Andi", "Amel", "Amanda", "Diondi", "Andrew", "Samuel", "Nanang"]
friends[2] = "Diki"
friends[4] = "Ameng"
friends[8] = "Kristiono"
print("index 4,6,7 is", friends[4], friends[6], friends[7]) #menampilkan index 4, 6, 7
print("Jimly a.k.a", friends[2], ", Amel a.k.a", friends[4], ", Samuel a.k.a", friends[8]) #mengganti list 3, 5, 9. pakai 2, 4, 8 karena di soal disuruh pakai "List" bukan index
friends = friends + ["Dini", "Savira"] #menambahkan 2 teman
print("now my friens is", friends)
for friend in friends: #show in loop
    print(friend)
print(f"My close friends are {len(friends)} people" )