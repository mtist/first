from json import loads
from urllib.request import urlopen
from time import sleep

ids = []
token = "39af7e3d04c185af50f6aa07febd5d26592dd82e69eca3f9f295c4674c7364e0756813e47e452ca038a50"
nickname = 'Ivan%20Ivanov'

request = "https://api.vk.com/method/users.search?q=" + nickname + "&count=1000&fields=can_write_private_message&access_token=" + token + "&v=5.67"
# print (request)
# request = 'https://api.vk.com/method/users.search?q=Ivan Ivanov&count=1000&fields=can_write_private_message&access_token=39af7e3d04c185af50f6aa07febd5d26592dd82e69eca3f9f295c4674c7364e0756813e47e452ca038a50&v=5.67'
data = urlopen(request)
data = data.read().decode('utf-8')
data = loads(data)
# print(data)
items = data["response"]["items"]
for user_id in items:
    if user_id["can_write_private_message"] == 1:
        ids.append(user_id["id"])

for msg in ids:
    data = urlopen('https://api.vk.com/method/messages.send?user_id=' + str(msg) + '&message=Hello, Friend&v=5.67')
    i += 1 
    print(i)
    sleep(0.1)