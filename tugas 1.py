friends = ["Habib", "Fahri", "Jimly", "Andi", "Amel", "Amanda", "Diondi", "Andrew", "Samuel", "Nanang"]
friends[2] = "Diki"
friends[4] = "Ameng"
friends[8] = "Kristiono"
print("index 4,6,7 is", friends[4], friends[6], friends[7])
print("Jimly a.k.a", friends[2], ", Amel a.k.a", friends[4], ", Samuel a.k.a", friends[8])
friends = friends + ["Dini", "Savira"]
print("now my friens is", friends)
for friend in friends:
    print(friend)
print("total item in this list:", len(friends))