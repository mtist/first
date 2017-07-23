from socket import *

def send_answer(conn, status="200 OK", typ="text/plain; charset=utf-8", data=""):
    data = data.encode("utf-8")
    conn.send(b"HTTP/1.1 " + status.encode("utf-8") + b"\r\n")
    conn.send(b"Server: simplehttp\r\n")
    conn.send(b"Connection: close\r\n")
    conn.send(b"Content-Type: " + typ.encode("utf-8") + b"\r\n")
    conn.send(b"Content-Length: " + bytes(len(data)) + b"\r\n")
    conn.send(b"\r\n")# после пустой строки в HTTP начинаются данные
    conn.send(data)


serverSocket = socket(AF_INET, SOCK_STREAM)
port = 3303
serverSocket.bind(('', port))
serverSocket.listen(10)

while True:
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(2048)
        message = message.decode('utf-8')
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = ''
        for string in f:
            outputdata += f.readline()

        send_answer(connectionSocket, data = outputdata)
    except IOError:
        pass
        #Отправляем ответ об отсутствии файла на сервере
        #Начало вставки
        #Конец вставки
        #Закрываем клиентский сокет
        #Начало вставки
        #Конец вставкиserver
Socket.close()
