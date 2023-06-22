frinds = ["ah", "mo", "ab", "moh", "am", "ame"]
print(frinds[0])
print(frinds[1])
print(frinds[2])
print(frinds[3])
print(frinds[4])
print(frinds[5])
# a = 0
# while a < len(frinds):
#   print(f"#{a +1 } {frinds[a]}")
#  a += 1


tries = 4
realpass = "am30022@gmail"
passw = input("password?")
while passw != realpass:
    tries -= 1
    print(f"wrong pass {tries} lefted")
    passw = input("password?")
    if tries == 0:
        break
else:
    print("good")
