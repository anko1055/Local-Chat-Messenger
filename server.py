import socket
import os
from faker import Faker
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = '/tmp/socket_file'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('Starting up on {}'.format(server_address))

sock.bind(server_address)

sock.listen(1)

while True:
    print('Waiting for a connection...')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        while True:
            data = connection.recv(1024)

            data_str =  data.decode('utf-8')
            print('Received ' + data_str)

            if data:
                faker = Faker()
                response = faker.text()
                print("Sending")
                connection.sendall(response.encode())
            else:
                print('no data from', client_address)
                break
    finally:
        print("Closing current connection")
        connection.close()