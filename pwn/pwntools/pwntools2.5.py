from pwn import *

context.log_level = 'debug'
context.os = 'linux'
context.arch = 'amd64'

payload = asm('pop rax\nmov rbx, rax\nneg rax\ncmovl rax, rbx\npush rax', arch = 'amd64')

io = process('/challenge/pwntools-tutorials-level2.5')

io.sendafter("Please give me your assembly in bytes (up to 0x1000 bytes): \n", payload)

while True:
    io.recv()