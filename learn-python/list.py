friends = ["Hassan", "Musa", "Esha"]

friends2 = ["Dua", "Ali", "Minha"]

friends.extend(friends2)
print(friends)

# agr ek specific instance ko tag krna hai to slice k start aur end same index dalna hai jese [2:2]

friends.insert(1, "Amina")  # agr ek entry dalni hai khaas index pr
print(friends)

friends[2:2] = ["Lalli", "Meena"]  # agr specifically us index pr series insert krni hai
print(friends)

# agr kuch change krna hai. yaha main ne index 2 pr value change kr di 3 pr finish takay ek change ho. agr zyada range dalta to zyada remove ho k replace ho jati
friends[2:3] = ["Hijab", "Hathi"]
print(friends)

friends.append("Tahawar")  # inserts at end
print(friends)

friends.remove("Meena")
print(friends)

del friends[
    2
]  # to remove multiple or even single at once. adding just a single index will delete at that index and range will delete multiple enteries
print(friends)
