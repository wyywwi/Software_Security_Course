from pwn import *

context.log_level = 'debug'
context.os = 'linux'
context.arch = 'amd64'

payload = asm('div rbx\nadd rdx, rcx\nsub rdx, rsi\nmov rax, rdx')

io = process('/challenge/pwntools-tutorials-level2.2')

io.sendafter("Please give me your assembly in bytes (up to 0x1000 bytes): \n", payload)

while True:
    io.recv()