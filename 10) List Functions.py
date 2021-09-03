lucky_number = [4, 52, 30, 104, 98, 456, 968]

Friends = ["Abdullah", "Abdul Wahid", "Muhammad", "Sallahudin"]


print(Friends)

Friends.extend(lucky_number)
print(Friends)

Friends = ["Abdullah", "Abdul Wahid", "Muhammad", "Sallahudin", "Zulfaris"]
print(Friends)

Friends = ["Abdullah", "Abdul Wahid", "Muhammad", "Sallahudin"]
Friends.insert(2, "Daniel Aziz")
print(Friends)

Friends = ["Abdullah", "Abdul Wahid", "Muhammad", "Sallahudin"]
Friends.remove("Abdullah")
print(Friends)

Friends = ["Abdullah", "Abdul Wahid", "Muhammad", "Sallahudin"]
Friends.clear()
print(Friends)

Friends = ["Abdullah", "Abdul Wahid", "Muhammad", "Sallahudin"]
Friends.pop()
print(Friends)

Friends = ["Abdullah", "Abdul Wahid", "Muhammad", "Sallahudin"]
print(Friends.index("Muhammad"))

Friends = ["Abdullah", "Abdul Wahid", "Muhammad", "Sallahudin"]
print(Friends.count("Sallahudin"))

Friends = ["Abdullah", "Abdul Wahid", "Muhammad", "Sallahudin"]
Friends.sort()
print(Friends)

lucky_number.sort()
print(lucky_number)

lucky_number.reverse()
print(lucky_number)

friend2 = Friends.copy()
print(friend2)