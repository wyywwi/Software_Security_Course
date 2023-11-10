from pwn import *

context.log_level = 'debug'
context.os = 'linux'
context.arch = 'amd64'

io = process('/challenge/pwntools-tutorials-level1.1')

payload = b'p' + p8(0x15) + p32(0x075bcd15) + b'Bypass Me:)'

io.sendlineafter("Enter your input> \n", payload)

print(io.recvline())