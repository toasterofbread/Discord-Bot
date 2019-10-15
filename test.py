variable = "users9.txt"

id = "402344993391640578"

club_filename = "test.txt"

with open(club_filename, "r") as file:
    tempdata = file.readlines()
with open(club_filename, "w") as file:
    file.write("\n")
for value in tempdata:
    if str(id) not in str(value):
        with open(club_filename, "a") as file:
            file.write(str(value))