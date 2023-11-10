from pwn import *

context.log_level = 'debug'
context.os = 'linux'
context.arch = 'amd64'

payload = asm('mov rax, 0x12345678')

io = process('/challenge/pwntools-tutorials-level2.0')

# No lines, it would append a '\n' after your assembly instructions
# io.sendlineafter("Please give me your assembly in bytes (up to 0x1000 bytes): \n", payload)

io.sendafter("Please give me your assembly in bytes (up to 0x1000 bytes): \n", payload)

while True:
    io.recv()