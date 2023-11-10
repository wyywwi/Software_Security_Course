from pwn import *

context.log_level = 'debug'
context.os = 'linux'
context.arch = 'amd64'

io = process('/challenge/pwntools-tutorials-level1.0')

payload = p32(0xdeadbeef)

io.sendlineafter("Enter your input> \n", payload)

print(io.recvline())