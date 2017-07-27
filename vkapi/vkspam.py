from json import loads
from urllib.request import urlopen
from time import sleep
from random import randint 

i = 0
token = "a308545c37710e87dd110565a361f2088825b9387507712d08661f4766b44709a9c7e33b67f1891f3baa9"
nickname = 'Ivan%20Ivanov'
sortrnd = randint(0,1)
request = "https://api.vk.com/method/users.search?q=" + nickname + "&sort=" + str(sortrnd) + "&count=1000&fields=can_write_private_message,online=1&access_token=" + token + "&v=5.67"

response = urlopen(request)
response = response.read().decode('utf-8')
response = loads(response)
response = response['response']

for users_id in response['items']:
    check_messages = urlopen('https://api.vk.com/method/messages.getHistory?user_id=' + str(users_id['id']) + '&access_token=' + token + '&v=5.67')
    check_messages = check_messages.read().decode('utf-8')
    check_messages = loads(check_messages)
    # print(check_messages)
    check_messages = check_messages['response']
    if (users_id["can_write_private_message"] == 1) and (not check_messages['items']):
        send_message = 'https://api.vk.com/method/messages.send?user_id=' + str(users_id['id']) + '&message=Hello,Friend&access_token=' + token + '&v=5.67'
        urlopen(send_message)
        i += 1
        print(i)
        if i % 10 == 0:
            sleep(25)
        else:
            sleep(1)
    else:
        sleep(0.1)
        continue