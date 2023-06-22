user = {
    "name": "eman",
    "age": 19,
    "country": "egypt",
    "love": "me",
    "name": "emy"  # اتعدل عشان اللس فوقهه مبقاش ليه لازمه
}
print(user)
print(user['love'])
print("@"*20)
print(user.get('name'))
print(user.keys())
print(user.values())

lan = {
    1: {
        'name': "c",
        "progrss": "1"
    },
    2: {
        "name": "css",
        "pro": 0
    },
    3: {
        'name': 'c#',
        'pro': 2
    }
}
print(lan)
print(lan[1])
print(lan[2])
print(lan[3]['name'])
# clear
# update
# copy
