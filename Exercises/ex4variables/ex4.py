home = 3
rooms_in_homes = 5
livers = 7
house_in_use = 1
pets = 4
house_not_in_use = house_in_use - home
not_animal_users = livers - pets
total_rooms = rooms_in_homes * home

print("I have: ", home, "homes.")
print("Each of my homes has: ", rooms_in_homes, "rooms.")
print("We love pets, that's why we have: ", pets, "pets.")
print("So actually we are: ", not_animal_users, "peoples living togheter.\nWe don't use ", abs(house_not_in_use), "houses, but we have a total of ", total_rooms, "rooms." )