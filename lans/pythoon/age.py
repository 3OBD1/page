age = int(input("how old r u?"))
print(type(age))
months = age*12
weeks = months*4
days = age * 365.25
hours = days*24
minutes = hours*60
seconds = minutes*60
print(f"your age is {age%.2} years,\
{days}day,{hours}hour,{minutes}minute,{seconds}second")
print("{months}months")
print("{weeks}week")
