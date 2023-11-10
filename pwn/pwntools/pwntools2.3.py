from pwn import *

context.log_level = 'debug'
context.os = 'linux'
context.arch = 'amd64'

payload = asm('mov rax, [0x404000]\nmov [0x405000], rax\nmov rax, [0x404004]\nmov [0x405004], rax', arch = 'amd64')

io = process('/challenge/pwntools-tutorials-level2.3')

io.sendafter("Please give me your assembly in bytes (up to 0x1000 bytes): \n", payload)

while True:
    io.recv()