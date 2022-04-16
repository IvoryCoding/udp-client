#   Date:        2022/04/16
#   Author:      Emma Gillespie
#   Description: A basic tcp client
#   Resources:

#!/usr/bin/python3

import socket
import argparse

def udpConnection(host, port, bytes):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto(b"AAAABBBBBCCCC",(host,port))
    data, addr = client.recvfrom(bytes)

    print(data.decode())
    client.close()

if __name__ == "__main__":
    # Set the arguments
    parse = argparse.ArgumentParser(description="Python udp client")
    parse.add_argument("host", help="Host name or IP address to udp client")
    parse.add_argument("-p", "--port", help="The port to udp client to")
    parse.add_argument("-b", "--bytes", help="Pass how many bytes of response to get")

    args = parse.parse_args()
    host = args.host
    port = args.port
    bytes = args.bytes

    udpConnection(host, int(port), int(bytes))
