import os, json, socket, sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = "./temp/udp_socket_file"
address = "./temp/udp_client_socket_file"

try:
    os.unlink(address)
except FileNotFoundError:
    pass

message = bytes(sys.argv[1], encoding="utf-8")
sock.bind(address)
try:
    print('sending{!r}'.format(message))
    sent = sock.sendto(message, server_address)
    print(f'waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data))
finally:
    print(f'closing socket')
    sock.close()