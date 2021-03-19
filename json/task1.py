import random
import json


file = open("users.txt", mode='w', encoding='Latin-1')

users = ['Vasiliy', 'Dmitriy', 'Maxim', 'Misha', 'Daniil']
latest_logins = ['12.02.21', '13.02.21', '14.02.21', '15.02.21', '16.02.21']
durations = ['2hours','30minute','1hour','3hours','4hours']


user_1 = {
    'login': users[random.randint(0, 4)],
    'latest_login': latest_logins[random.randint(0,4)],
    'duration': durations[random.randint(0,4)]
}

user_2 = {
    'login': users[random.randint(0, 4)],
    'latest_login': latest_logins[random.randint(0,4)],
    'duration': durations[random.randint(0,4)]
}

user_3 = {
    'login': users[random.randint(0, 4)],
    'latest_login': latest_logins[random.randint(0,4)],
    'duration': durations[random.randint(0,4)]
}


user_4 = {
    'login': users[random.randint(0, 4)],
    'latest_login': latest_logins[random.randint(0,4)],
    'duration': durations[random.randint(0,4)]
}

user_5 = {
    'login': users[random.randint(0, 4)],
    'latest_login': latest_logins[random.randint(0,4)],
    'duration': durations[random.randint(0,4)]
}

allUsers = []
allUsers.append(user_1)
allUsers.append(user_2)
allUsers.append(user_3)
allUsers.append(user_4)
allUsers.append(user_5)
json.dump(allUsers, file)
file.close()