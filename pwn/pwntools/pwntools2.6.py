# rax = the sum from 1 to rcx
'''
    mov rax, 0x0
start:
    add rax, rcx
    loop start
'''

from pwn import *

context.log_level = 'debug'
context.os = 'linux'
context.arch = 'amd64'

payload = asm('mov rax, 0x0\nstart:\nadd rax, rcx\nloop start', arch = 'amd64')

io = process('/challenge/pwntools-tutorials-level2.6')

io.sendafter("Please give me your assembly in bytes (up to 0x1000 bytes): \n", payload)

while True:
    io.recv()