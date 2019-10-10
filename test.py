with open("users9.txt", "r") as file:
    userdata9 = file.read()
with open("users8.txt", "r") as file:
    userdata8 = file.read()
with open("users7.txt", "r") as file:
    userdata7 = file.read()


def datalength(parameter):
    with open("users9.txt", "r") as file:
        userdata9 = file.read()
    with open("users8.txt", "r") as file:
        userdata8 = file.read()
    with open("users7.txt", "r") as file:
        userdata7 = file.read()
    if parameter == userdata9:
        with open("users9.txt", "r") as file:
            userdata9 = file.readlines()
        return str(userdata9.__len__() - 1)
    elif parameter == userdata8:
        with open("users8.txt", "r") as file:
            userdata8 = file.readlines()
        return str(userdata8.__len__() - 1)
    elif parameter == userdata7:
        with open("users7.txt", "r") as file:
            userdata7 = file.readlines()
        return str(userdata7.__len__() - 1)
    with open("users9.txt", "r") as file:
        userdata9 = file.read()
    with open("users8.txt", "r") as file:
        userdata8 = file.read()
    with open("users7.txt", "r") as file:
        userdata7 = file.read()

print("  |  Grade 9 user ids (" + datalength(userdata9) + " entries)\n" + userdata9)