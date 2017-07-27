from json import loads
from urllib.request import urlopen
from time import sleep

ids = []
i = 0
token = "6697777fcadb3bf83b76c889ed237b81a799cbce279b792b477dacde8d467d6e15097b1533dedcec40eec"
nickname = 'Ivan%20Ivanov'

request = "https://api.vk.com/method/users.search?q=" + nickname + "&count=1000&fields=can_write_private_message,online=1&access_token=" + token + "&v=5.67"
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
    print("msg", msg)
    send_message = 'https://api.vk.com/method/messages.send?user_id=' + str(msg) + '&message=Hello,Friend&access_token=' + token + '&v=5.67'
    trying = urlopen('https://api.vk.com/method/messages.getHistory?user_id=' + str(msg) + '&access_token=' + token + '&v=5.67')
    trying = trying.read().decode('utf-8')
    trying = loads(trying)
    # print(trying)
    if not trying['response']['items']:
        print('Send message to ' + str(msg))
        data_message = urlopen(send_message)
        i += 1
        print(i)
        if i % 20 == 0:
            sleep(30)
            continue
        sleep(1)
    else:
        sleep(0.3)
        continue